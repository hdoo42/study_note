---
id: 1767332881-VGUM
aliases:
  - XDP
tags: []
---

# XDP (eXpress Data Path) - 근본 이해

## Why (근본 원리)
**XDP는 네트워크 패킷이 커널의 복잡한 네트워크 스택을 거치기 전에 NIC 드라이버 레벨에서 직접 처리함으로써, 패킷 처리 오버헤드를 최소화하고 최대 성능을 달성하기 위한 리눅스 커널 기술입니다.**

---

## How (구체적 작동 메커니즘)

### 1. 패킷 처리 경로의 물리적 위치
```
[NIC Hardware] 
    ↓ DMA (메모리에 패킷 복사)
[Driver RX Ring Buffer] ← **XDP가 여기서 실행됨**
    ↓ (XDP가 PASS를 반환한 경우에만)
[sk_buff 할당 및 네트워크 스택]
    ↓
[iptables/netfilter]
    ↓
[Socket/Application]
```

**핵심**: XDP는 `sk_buff` (커널의 패킷 메타데이터 구조체) 할당 **이전**에 실행됩니다. 이것이 성능의 핵심입니다.

### 2. XDP 프로그램의 정확한 실행 시점
- NIC가 패킷을 메모리에 DMA로 쓴 직후
- 드라이버의 NAPI poll 함수 내부
- `sk_buff` 할당 **전**
- 단 하나의 선형 메모리 버퍼만 접근 가능 (fragmented packets 처리 제한)

### 3. XDP 프로그램이 반환할 수 있는 Verdict (정확히 5가지)

```c
enum xdp_action {
    XDP_ABORTED = 0,  // 에러 - 패킷 드롭 + trace
    XDP_DROP,         // 패킷 즉시 폐기 (DDoS 방어)
    XDP_PASS,         // 일반 네트워크 스택으로 전달
    XDP_TX,           // 같은 NIC로 패킷 재전송 (reflection)
    XDP_REDIRECT,     // 다른 NIC 또는 CPU로 전송
};
```

### 4. 메모리 구조 (극도로 구체적)
```
XDP 프로그램이 받는 컨텍스트:
struct xdp_md {
    __u32 data;          // 패킷 데이터 시작 포인터 (실제로는 offset)
    __u32 data_end;      // 패킷 데이터 끝 포인터
    __u32 data_meta;     // 메타데이터 영역 (커스텀)
    __u32 ingress_ifindex; // 들어온 인터페이스 ID
    __u32 rx_queue_index;  // RX 큐 번호
};
```

**중요**: `data`와 `data_end`는 실제 포인터가 아니라 offset입니다. 커널이 eBPF 프로그램 로드 시 실제 주소로 변환합니다.

### 5. XDP 모드 3가지 (성능 차이 명확히)

| 모드 | 위치 | 성능 | 제약 |
|------|------|------|------|
| **Native** | NIC 드라이버 내부 | 최고 (14M pps+) | 드라이버 지원 필요 |
| **Offloaded** | NIC 하드웨어 | 이론상 최고 | Netronome 등 특수 NIC만 |
| **Generic** | 네트워크 스택 내부 | 낮음 (테스트용) | 모든 NIC 지원 |

---
