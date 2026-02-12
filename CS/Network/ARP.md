# ARP (Address Resolution Protocol)

## 1. 개요 (Overview)

**ARP (Address Resolution Protocol, 주소 결정 프로토콜)**는 네트워크 계층(Layer 3)의 **IP 주소**를 데이터 링크 계층(Layer 2)의 **MAC 주소**로 변환하는 프로토콜이다.

*   **RFC 문서**: RFC 826
*   **주요 역할**: 논리적 주소(IP) → 물리적 주소(MAC) 매핑

### 왜 필요한가? (The "Why")
우리가 인터넷 통신을 할 때 상대방의 IP 주소는 알고 있지만, 실제 데이터 패킷이 로컬 네트워크(LAN) 상의 장비(스위치, 허브 등)를 통과하여 목적지 기기의 네트워크 인터페이스 카드(NIC)에 도달하기 위해서는 **MAC 주소**가 필요하다. 이더넷 프레임은 MAC 주소를 기반으로 전송되기 때문이다.

---

## 2. 동작 원리 (How it works)

ARP의 동작은 기본적으로 **Request(요청)**와 **Reply(응답)** 과정으로 이루어진다.

### 시나리오
호스트 A (`192.168.0.10`)가 같은 네트워크에 있는 호스트 B (`192.168.0.20`)와 통신하려고 한다. A는 B의 IP는 알지만 MAC 주소는 모른다.

### 단계별 과정

1.  **ARP Cache 확인**:
    *   호스트 A는 먼저 자신의 **ARP Cache Table** (메모리)에 `192.168.0.20`에 해당하는 MAC 주소가 있는지 확인한다.
    *   있으면 바로 통신 시작 (Hit). 없으면 다음 단계로 진행 (Miss).

2.  **ARP Request (Broadcast)**:
    *   호스트 A는 네트워크 상의 **모든 기기**에게 "누가 IP `192.168.0.20`을 가지고 있니? 너의 MAC 주소를 알려줘"라는 메시지를 보낸다.
    *   이때 목적지 MAC 주소는 `FF:FF:FF:FF:FF:FF` (브로드캐스트)로 설정된다.
    *   이 패킷은 같은 LAN 대역의 모든 호스트에게 전달된다.

3.  **ARP Reply (Unicast)**:
    *   네트워크의 모든 호스트가 이 요청을 받지만, 자신의 IP가 아닌 호스트들은 무시한다.
    *   호스트 B (`192.168.0.20`)는 자신의 IP를 찾는 요청임을 확인하고, 자신의 MAC 주소를 담아 호스트 A에게 응답한다.
    *   이 응답은 호스트 A에게만 직접 보내는 **유니캐스트** 방식이다.

4.  **Caching (저장)**:
    *   호스트 A는 응답받은 B의 MAC 주소를 자신의 **ARP Cache Table**에 저장한다. (일정 시간 동안 유지)
    *   이후 통신에서는 테이블을 참조하여 바로 패킷을 전송한다.

---

## 3. ARP 패킷 구조 (Packet Structure)

ARP 패킷은 이더넷 프레임의 데이터 부분(Payload)에 캡슐화되어 전송된다.

| 필드 | 설명 |
| :--- | :--- |
| **Hardware Type** | 하드웨어 유형 (예: Ethernet = 1) |
| **Protocol Type** | 프로토콜 유형 (예: IPv4 = 0x0800) |
| **Hardware Address Length** | MAC 주소 길이 (6 bytes) |
| **Protocol Address Length** | IP 주소 길이 (4 bytes) |
| **Opcode** | 명령 코드 (1: Request, 2: Reply) |
| **Sender Hardware Address** | 보내는 호스트의 MAC 주소 |
| **Sender Protocol Address** | 보내는 호스트의 IP 주소 |
| **Target Hardware Address** | 목적지 호스트의 MAC 주소 (Request 시 0으로 채움) |
| **Target Protocol Address** | 목적지 호스트의 IP 주소 |

---

## 4. 관련 명령어 (Commands)

운영체제별로 ARP 테이블을 확인하고 관리하는 명령어가 있다.

### Windows / Linux / macOS 공통
```bash
# ARP 테이블 확인
arp -a

# 특정 IP의 ARP 엔트리 삭제 (관리자 권한 필요)
arp -d <IP_Address>
```

---

## 5. RARP와 GARP

### RARP (Reverse ARP)
*   ARP의 반대 개념.
*   **MAC 주소 → IP 주소** 변환.
*   디스크가 없는 씬 클라이언트(Thin Client) 등이 부팅 시 자신의 IP 주소를 서버로부터 할당받기 위해 사용했으나, 현재는 **DHCP**가 이 역할을 대신하므로 거의 사용되지 않음.

### GARP (Gratuitous ARP)
*   자신의 IP와 MAC 주소를 알리기 위해 **스스로** 보내는 ARP 요청.
*   **용도**:
    1.  **IP 충돌 감지**: 같은 네트워크에 내가 쓰려는 IP를 누가 이미 쓰고 있는지 확인.
    2.  **ARP 테이블 갱신**: 장비 교체(MAC 변경)나 이중화(HA) 구성에서 Master 변경 시 주변 장비들의 ARP 테이블을 갱신시키기 위함.

---

## 6. 보안 이슈: ARP Spoofing (ARP Poisoning)

ARP는 "인증" 절차가 없는 신뢰 기반 프로토콜이다. 즉, 누군가 거짓으로 "내가 그 IP 주인이야"라고 응답해도 이를 검증하지 않고 받아들인다.

*   **공격 방식**: 공격자가 자신의 MAC 주소를 게이트웨이(공유기)의 MAC 주소인 것처럼 속여서(Spoofing) 피해자에게 ARP Reply를 보낸다.
*   **결과**: 피해자의 트래픽이 공격자를 거쳐서 나가게 되며, 공격자는 패킷을 도청하거나 변조할 수 있다. (중간자 공격, MITM)
*   **대응**:
    *   중요한 서버나 게이트웨이의 ARP 엔트리를 **정적(Static)**으로 설정.
    *   ARP Spoofing 탐지/방어 솔루션 사용.