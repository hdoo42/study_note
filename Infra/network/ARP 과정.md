---
id: ARP 과정
aliases:
  - ARP
tags:
  - network
---

**기본 원칙(Rationale):**
ARP(Address Resolution Protocol)는 운영체제 커널의 네트워크 스택 내부에서 일어나는 '인터럽트 처리'와 '패킷 버퍼링' 과정을 포함하며, 단순한 "요청-응답"이 아닌 **상태 머신(State Machine)의 전이 과정**으로 이해해야 정확합니다.

---

### ARP 프로세스: 원자적 단계 (Atomic Steps)

**상황:** `Host A(192.168.1.10)`가 같은 서브넷의 `Host B(192.168.1.20)`에게 [[ICMP Echo Request(ping)]]를 보내려 하지만, ARP 테이블에 정보가 없는 상태(`Cold Start`)입니다.

#### Phase 1: 커널 내부의 판단 및 버퍼링 (Pre-transmission)

1. **L3 라우팅 조회 (Lookup):**
* `Host A`의 IP 계층은 목적지 `192.168.1.20`이 서브넷 마스크 연산 결과 **로컬 네트워크(Directly Connected)** 임을 확인합니다.
* 전송할 인터페이스(예: `eth0`)를 결정합니다.


2. **ARP 캐시 조회 (Cache Check):**
* 커널은 ARP 테이블(Neighbor Table)을 조회합니다.
* **결과:** `Miss` (정보 없음).


3. **패킷 보류 (Packet Queueing):**
* 원래 보내려던 ICMP 패킷(IP 패킷)은 전송되지 못하고 커널 메모리 내의 **대기 큐(Pending Queue / sk_buff)**에 저장됩니다. (상태: `INCOMPLETE`)
* *이 패킷은 ARP 해결 전까지 나갈 수 없습니다.*



#### Phase 2: ARP 요청 생성 및 브로드캐스트 (The Request)

4. **ARP 프레임 생성 (Construction):**
* ARP 드라이버가 28바이트의 ARP 페이로드를 생성합니다.
* **중요 필드 값:**
* `Opcode`:  (Request)
* `Sender MAC`: `A_MAC` / `Sender IP`: `192.168.1.10`
* `Target MAC`: **`00:00:00:00:00:00`** (모름, 비워둠)
* `Target IP`: `192.168.1.20`




5. **L2 캡슐화 (Encapsulation):**
* 이더넷 헤더가 붙습니다.
* `EtherType`:  (이 패킷은 ARP임을 명시)
* `Destination MAC`: **`FF:FF:FF:FF:FF:FF`** (L2 브로드캐스트)


6. **물리적 전송 (Transmission):**
* NIC(랜카드)가 전기 신호로 변환하여 케이블로 송출합니다. 같은 L2 도메인(스위치)에 있는 모든 포트로 퍼집니다.



#### Phase 3: 수신 및 처리 (Processing & Reply)

7. **타인(Host C)의 필터링:**
* 패킷을 수신하고 L2 헤더(`FF:FF...`)를 통과시킵니다.
* ARP 페이로드를 열어 `Target IP`를 확인합니다.
* `192.168.1.20` != `Host C IP`  **즉시 폐기(Silent Drop).**


8. **당사자(Host B)의 수신 및 학습:**
* `Target IP`가 자신의 IP와 일치함을 확인합니다.
* **학습(Side Effect):** `Host B`는 `Opcode 1`을 받았지만, 나중에 어차피 통신해야 하므로 **`Sender(Host A)`의 MAC과 IP 정보를 자신의 ARP 테이블에 먼저 등록**합니다.


9. **ARP 응답 생성 (Reply Construction):**
* `Host B`가 응답 패킷을 만듭니다.
* **중요 필드 값:**
* `Opcode`:  (Reply)
* `Sender MAC`: `B_MAC` (자신의 정보 채움)
* `Target MAC`: `A_MAC` (요청 패킷에서 추출한 정보)




10. **유니캐스트 전송 (Unicast):**
* L2 헤더의 `Destination MAC`을 `A_MAC`으로 설정하여 **정확히 A에게만** 보냅니다.



#### Phase 4: 완료 및 큐 해제 (Completion)

11. **Host A의 수신:**
* `Host A`는 ARP Reply(`Opcode 2`)를 받습니다.
* 자신의 ARP 테이블 상태를 `INCOMPLETE`  `REACHABLE`로 변경하고 `B_MAC`을 기록합니다.


12. **지연 패킷 방출 (Dequeuing):**
* **Step 3**에서 대기하고 있던 ICMP 패킷(IP 패킷)의 큐가 풀립니다.
* 이제야 비로소 IP 패킷에 `Destination MAC: B_MAC`을 붙여서 실제로 전송합니다.



---

### 5. 핵심 요약 (Reverse Teaching)

이 과정에서 ARP 요청(`Request`) 패킷 내부의 **'Target MAC'** 필드와, 이더넷 헤더의 **'Destination MAC'** 주소는 서로 다른 값을 가집니다.

**Q. Step 4와 Step 5를 참고하여, ARP 요청 시 이 두 필드의 값이 각각 무엇인지(Hex 값), 그리고 왜 그렇게 설정되는지 설명하십시오.**
