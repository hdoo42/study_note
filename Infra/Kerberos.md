---
id: Kerberos
aliases: []
tags:
  - auth
---
**1. 근본적 원리 (Rationale)**
Kerberos는 신뢰할 수 없는 네트워크(Unsecured Network) 상에서 신뢰할 수 있는 제3자(KDC)를 통해 **대칭키 암호화 방식**만을 사용하여 비밀번호 전송 없이 사용자와 서비스 간의 상호 신원을 검증하기 위해 존재합니다.

---

**3. 핵심 메커니즘: 3단계 티켓팅 시스템 (The How)**

Kerberos는 그리스 신화의 머리 셋 달린 개(케르베로스)처럼 3가지 주체가 상호 작용합니다. 모든 과정은 **'나만 열 수 있는 상자 안에 상대방을 위한 열쇠를 넣어 보내는 과정'**의 연속입니다.

**주요 변수 정의 (LaTeX 사용):**

* : Client (사용자)
* : Authentication Server (인증 서버)
* : Ticket Granting Server (티켓 발급 서버)
* : Service Server (접속하려는 실제 서비스)
* : 사용자의 비밀번호 해시값 (대칭키)
* : TGS만 아는 비밀키
* : 서비스 서버만 아는 비밀키

#### **Phase 1: 신원 증명 및 TGT 발급 (Login)**

* **상황:** 가 로그인을 시도합니다.
* **Input:** 가 ID를 에 평문으로 전송 (비밀번호는 전송하지 않음).
* **Logic:** 는 DB에서 의 비밀번호 해시()를 찾습니다.
* **Output (AS  C):** 메시지를 두 개의 암호화된 파트로 보냅니다.
1. **Session Key 1 ():** $K_{c}$로 암호화됨. (만 풀 수 있음)
2. **TGT (Ticket Granting Ticket):** $K_{tgs}$로 암호화됨. (**는 절대 풀 수 없음**)


* **검증:** 는 자신의 비밀번호를 입력해 $K_{c}$를 생성하고 1번을 풉니다. 풀리면 로그인 성공입니다. 는 이제 를 가지고 있지만, 내용은 볼 수 없습니다.

#### **Phase 2: 서비스 티켓 요청 (Client  TGS)**

* **상황:** 가 특정 서비스(파일 서버 등)를 이용하려 합니다.
* **Input:** 에게 받은 **TGT** + **Authenticator** (현재 시간 를 $S_{c-tgs}$로 암호화한 값).
* **Logic:** 는 자신의 키 $K_{tgs}$로 **TGT**를 해독하여 세션키 $S_{c-tgs}$를 꺼냅니다. 그 키로 **Authenticator**를 해독해 시간 를 확인합니다.
* *NTP 필수 이유:* 여기서 시간 차이가 허용 범위(보통 5분)를 넘거나, 이미 사용된 시간값이면 Replay Attack으로 간주하고 거부합니다.


* **Output (TGS  C):**
1. **Session Key 2 ():** $S_{c-tgs}$로 암호화됨.
2. **Service Ticket:** $K_{ss}$로 암호화됨. (역시 는 못 품)



#### **Phase 3: 서비스 접속 (Client  SS)**

* **상황:** 가 최종적으로 에 접근합니다.
* **Input:** **Service Ticket** + **New Authenticator** (새로운 시간 $T'$를 $S_{c-ss}$로 암호화).
* **Logic:** 는 자신의 키 $K_{ss}$로 티켓을 해독해 세션키 $S_{c-ss}$를 얻고, 그것으로 Authenticator를 검증합니다.
* **Result:** 인증 완료. 이후 통신은 선택적으로 $S_{c-ss}$를 이용해 암호화할 수 있습니다.

---

**4. 시각화 (State Transformation)**

데이터가 어떻게 변환되는지 머릿속으로 그리십시오.

1. **Client 초기 상태:** `ID`, `Password`
2. **AS 응답 수신 후:** `SessionKey(AS-C)`, `Encrypted_TGT` (내용 모름)
3. **TGS 요청 시:** `Encrypted_TGT`를 그대로 전달, `Authenticator` 생성하여 첨부.
4. **TGS 응답 수신 후:** `SessionKey(C-SS)`, `Encrypted_ServiceTicket` (내용 모름)
5. **최종:** 서비스는 `Encrypted_ServiceTicket`을 받아 내부의 `User_ID`와 `SessionKey`를 확인하여 문을 열어줌.

---

**5. 지식 검증 퀴즈 (Anti-Laziness)**

위 내용을 완벽히 이해했는지 확인하기 위해 다음 질문에 답하십시오. "모르겠다"는 허용되지 않습니다. 논리를 세워 답을 도출하십시오.

1. 사용자(Client)가 TGS로부터 받은 `Service Ticket`을 로컬에서 해독하려고 시도하면 어떤 일이 발생하는가? 그리고 그 이유는 무엇인가? (암호화 키의 관점에서 설명하라)
2. 왜 AS는 사용자에게 곧바로 `Service Ticket`을 주지 않고, 중간에 `TGT`라는 번거로운 단계를 거치는가? (보안성과 효율성 측면에서 추론하라)
3. 해커가 네트워크 패킷을 스니핑하여 `Authenticator`를 가로챘다. 이를 이용해 나중에 재전송(Replay) 공격을 시도할 때, Kerberos는 이를 어떻게 차단하는가? (구체적인 변수를 들어 설명하라)
