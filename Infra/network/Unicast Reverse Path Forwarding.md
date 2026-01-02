---
id: 1767331617-SHHM
aliases:
  - uRPF
tags:
  - network
---

**Fundamental Rationale**
uRPF(Unicast Reverse Path Forwarding)는 라우터가 수신한 패킷의 **출발지 IP 주소(Source IP)**를 검증하여, 해당 패킷이 위조(Spoofing)되지 않았는지 확인하고 네트워크 유입을 차단하는 보안 메커니즘입니다.

---

### **Core Protocols: 동작 원리와 데이터 상태 변화**

일반적인 라우팅은 **Destination IP(목적지)**만 보고 "어디로 보낼지"를 결정하지만, uRPF는 **Source IP(출발지)**를 보고 "어디서 왔어야 정상인지"를 역으로 검증합니다.

#### **1. 데이터 처리 흐름 (Data State Transformation)**

패킷이 라우터 인터페이스로 들어올 때(Ingress), 라우터 내부의 FIB(Forwarding Information Base)와 비교하는 과정입니다.

* **Input State:**
* 수신 인터페이스: `Eth0`
* 패킷 헤더: `Src: 10.1.1.5`, `Dst: 200.2.2.2`


* **Transformation (Verification Logic):**
1. 라우터는 `Src: 10.1.1.5`를 라우팅 테이블(FIB)에서 조회합니다.
2. **"만약 내가 10.1.1.5로 패킷을 보낸다면, 어느 인터페이스로 내보내야 하는가?"**를 묻습니다 (Reverse Path Check).
3. FIB 조회 결과: `10.1.1.0/24` 네트워크는 `Eth0`을 통해 도달 가능함.


* **Comparison:**
* 실제 수신 인터페이스(`Eth0`) == FIB 상의 예상 인터페이스(`Eth0`)?


* **Output State:**
* **일치 (Match):** 정상 패킷으로 간주  **Forwarding**.
* **불일치 (Mismatch):** IP 스푸핑으로 간주  **Drop**.



#### **2. 동작 모드 (Modes of Operation)**

네트워크 환경(대칭/비대칭 경로)에 따라 두 가지 모드로 나뉩니다.

* **Strict Mode (엄격한 모드):**
* **조건:** `Src IP`가 라우팅 테이블에 존재해야 하며, **반드시 들어온 인터페이스와 나가는 인터페이스가 일치**해야 함.
* **논리:** 

* **용도:** 경로가 대칭적인(들어온 곳으로 나가는) Edge Network, ISP 가입자 구간.
* **한계:** 비대칭 라우팅(Asymmetric Routing) 환경에서는 정상 패킷도 드롭됨.


* **Loose Mode (느슨한 모드):**
* **조건:** `Src IP`로 가는 경로가 라우팅 테이블에 **존재하기만 하면** 통과 (인터페이스 불일치 허용).
* **논리:** 

* **용도:** 경로가 비대칭일 수 있는 ISP 간 연동 구간, 백본망.
* **한계:** 라우팅 테이블에 있는 IP로 위조해서 들어오면 막을 수 없음 (DDoS 방어력 약함).



---

### **Strict Interaction: 개념 검증 (Reverse Teaching)**

단순히 정의를 외우는 것은 의미 없습니다. 실제 네트워크 설계 관점에서 이해했는지 확인합니다.

**당신이 해결해야 할 퀴즈입니다:**

> **시나리오:**
> 당신은 기업 망 관리자입니다. 인터넷 연결을 이중화하기 위해 ISP A와 ISP B 두 회선을 사용하고 있습니다.
> * 나가는 트래픽(Outbound): 항상 ISP A 회선(`Eth0`)을 사용합니다.
> * 들어오는 트래픽(Inbound): ISP A(`Eth0`) 또는 ISP B(`Eth1`) 중 부하가 적은 쪽으로 들어옵니다.
> 
> 
> **문제:**
> 이 상황에서 ISP A에 연결된 라우터 인터페이스(`Eth0`)에 **uRPF Strict Mode**를 적용했습니다.
> 외부에서 ISP B 회선(`Eth1`)을 타고 들어와야 할 응답 패킷이, 라우팅 경로 변경으로 인해 갑자기 ISP A 회선(`Eth0`)으로 들어왔습니다.
> 1. 이 패킷은 처리됩니까, 드롭됩니까?
> 2. 그 이유는 무엇이며, 이를 해결하기 위해 모드를 변경하지 않고 라우팅 테이블 조작만으로 해결하려면 어떻게 해야 합니까? (힌트: Strict Mode의 조건 `Ingress == FIB Interface`를 만족시키려면?)
> 
> 

생각한 답을 정리해서 말해 주십시오.
