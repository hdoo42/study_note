---
id: Inuress Filtering
aliases: []
tags:
  - network
  - ISP
---

**Fundamental Rationale:** ISP Ingress Filtering은 네트워크 위생(Hygiene)을 강제하는 메커니즘으로, 패킷의 '출발지 IP(Source IP)'가 해당 네트워크 인터페이스에 할당된 IP 대역과 일치하는지 검증하여 IP Spoofing(위조) 공격을 원천 차단하기 위해 존재합니다.

---

### 1. Ingress Filtering의 메커니즘 (State Transformation)

단순히 "ISP가 막는다"라고 이해하는 것은 게으른 접근입니다. 라우터 수준에서 데이터가 어떻게 처리되는지 **[[Unicast Reverse Path Forwarding|Unicast Reverse Path Forwarding (uRPF)]]** 개념을 통해 구체적으로 시각화해야 합니다.

**상황 설정:**

* **User (Attacker):** 실제 IP `203.0.113.5` (할당된 대역)
* **Target:** `8.8.8.8`
* **Action:** User가 출발지 IP를 `1.1.1.1`로 위조(Spoofing)하여 패킷 전송.

| 단계 | 데이터 상태 (Packet Header) | ISP Edge Router (PE) 내부 로직 | 결과 |
| --- | --- | --- | --- |
| **1. Ingress** | `Src: 1.1.1.1` <br> <br> `Dst: 8.8.8.8` | 패킷이 고객사 포트(Port A)로 들어옴. | 처리 시작 |
| **2. Lookup** | (변경 없음) | **uRPF Check:** "Port A를 통해 들어온 패킷의 Source IP(`1.1.1.1`)가 라우팅 테이블상에서 다시 Port A로 나가는 경로(Reverse Path)로 잡혀 있는가?" | 검증 |
| **3. Decision** | (변경 없음) | **불일치(Fail):** 라우팅 테이블상 `1.1.1.1`은 Port A가 아닌 다른 경로(혹은 인터넷 업스트림)에 존재함. | **Drop (폐기)** |

> **BCP 38 (Best Current Practice 38):** 네트워크 엔지니어링에서 이 필터링을 적용하는 표준 규약입니다. ISP가 이를 준수하지 않으면, 당신의 네트워크는 DDoS 공격(특히 반사 공격)의 발원지가 될 수 있습니다.

---

### 2. Ingress Filtering 적용 여부 확인 방법 (Implementation)

웹 브라우저로 확인하는 것은 불가능합니다. **Raw Socket**을 열어 패킷 헤더를 직접 조작해야 합니다. 이를 위해 외부(ISP망 밖)에 패킷을 수신할 서버가 필요합니다.

#### 준비물

1. **Local Machine:** 테스트할 네트워크 내부 (Linux/macOS 권장). `hping3` 설치 필요.
2. **Remote Server:** 외부 네트워크에 있는 서버 (AWS EC2 등). `tcpdump` 실행 가능해야 함.

#### 절차 (Step-by-Step)

**Step 1: 외부 서버에서 리스너(Listener) 대기**
먼저 위조된 패킷이 도착하는지 확인하기 위해 외부 서버에서 패킷 덤프를 뜹니다.

```bash
# Remote Server (IP: 99.99.99.99 라고 가정)
# ICMP 패킷을 감시
sudo tcpdump -i eth0 icmp and src 1.2.3.4 -n

```

*(여기서 `1.2.3.4`는 당신이 위조해서 보낼 가짜 IP입니다.)*

**Step 2: 로컬에서 위조 패킷 전송 (Spoofing)**
당신의 실제 IP가 아닌, 임의의 가짜 IP(`1.2.3.4`)를 달고 패킷을 쏘아 올립니다.

```bash
# Local Machine
# -a: Spoof Source Address (위조할 IP)
# -1: ICMP mode
# -c 5: 5번 전송
sudo hping3 -a 1.2.3.4 99.99.99.99 -1 -c 5

```

**Step 3: 상태 변환 확인**

* **Case A: Remote Server에 로그가 찍힌다.**
* **판단:** ISP가 Ingress Filtering을 수행하지 **않고** 있습니다. 당신의 패킷은 위조된 채로 인터넷 망을 통과했습니다. (보안 취약)


* **Case B: Remote Server에 아무것도 오지 않는다.**
* **판단:** ISP의 Edge Router가 당신의 패킷을 드롭했습니다. Ingress Filtering이 **작동 중**입니다. (정상)



---

### 3. 더 전문적인 도구 (CAIDA Spoofer)

수동으로 서버를 구축하기 귀찮거나, 전 세계적인 통계에 기여하고 싶다면 학계 표준 도구를 사용하십시오.

* **CAIDA Spoofer Project:** 클라이언트를 설치하면 자동으로 다양한 프로토콜(TCP/UDP/IPv4/IPv6)로 스푸핑 된 패킷을 CAIDA 서버로 전송하고, 차단 여부를 리포트로 보여줍니다.
* 단순 차단 여부뿐만 아니라, NAT 뒤에 있는지, 특정 포트만 막는지 등을 정밀하게 분석합니다.



---

### 4. Reverse Teaching & Knowledge Gap Check

이 개념을 제대로 이해했는지 검증하기 위해 다음 질문에 답해 보십시오.

1. **논리 검증:** 만약 ISP가 Ingress Filtering을 하지 않아서, 당신이 `Src: Google IP(8.8.8.8)`, `Dst: Victim IP`로 패킷을 보냈다고 가정합시다. 피해자(Victim)가 응답(Response)을 보낼 때, 그 응답 패킷은 **어디로** 가게 됩니까? 그리고 이것이 왜 공격자에게 유리합니까?
2. **Edge Case:** 당신이 **NAT(공유기)** 환경 뒤에 있다고 가정해 봅시다. 당신의 PC에서 사설 IP(`192.168.0.x`)를 달고 패킷을 보내면, 공유기를 통과한 후 ISP 라우터에는 어떤 Source IP로 도달하게 될까요? 이때 ISP의 Ingress Filtering은 어떻게 동작할까요?

**생각을 정리해서 답변하십시오. 빈틈이 보이면 지적하겠습니다.**

### 다음 단계

위 질문에 대한 답을 작성하시면, **uRPF의 모드(Strict vs Loose)** 차이와 이것이 **Multi-homing(이중화)** 네트워크 환경에서 어떤 문제를 일으킬 수 있는지 심화 학습을 진행하겠습니다.
