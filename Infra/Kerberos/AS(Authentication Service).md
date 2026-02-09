사용자가 서비스를 이용할 때마다 매번 비밀번호를 입력하거나 네트워크에 노출하지 않도록, **"이 사람은 우리 회원이 맞다"는 1차 검증을 수행하고, 이후 통행증(TGT)을 발급해주기 위해** 존재합니다.

---

### 🛠️ AS의 동작 과정 (The How: 단계별 시각화)

사용자가 컴퓨터에 로그인하는 상황을 가정해 봅시다.

1. **전송 (Client → AS):** 사용자는 ID(예: `duhj`)를 평문으로 AS에 보냅니다. **비밀번호는 보내지 않습니다.**
    
2. **조회 (Inside AS):** AS는 자신의 데이터베이스에서 `duhj`라는 사용자가 있는지 확인하고, 해당 사용자의 **마스터 키(Kuser​)**를 꺼냅니다. (이 키는 사용자 비밀번호의 해시값입니다.)
    
3. **생성 (Inside AS):** AS는 두 가지를 만듭니다.
    
    - **로그인 세션 키(SAS−Client​):** 사용자와 KDC가 당분간 통신할 때 쓸 일회용 대칭키.
        
    - **TGT (Ticket Granting Ticket):** "이 사용자는 인증됨"이라는 문구와 세션 키를 담은 상자. 이 상자는 오직 **TGS만 열 수 있도록 TGS의 비밀키(KTGS​)**로 암호화합니다.
        
4. **응답 (AS → Client):** AS는 위에서 만든 것들을 사용자에게 보냅니다. 이때 **사용자만 열어볼 수 있도록 사용자의 마스터 키(Kuser​)**로 전체를 암호화해서 보냅니다.
    

---

### 🔍 논리 점검 및 비판 (Strict Interaction)

방금 설명에서 아주 중요한 지점이 있습니다. AS는 사용자가 진짜인지 확인하기 위해 비밀번호를 받지 않았습니다. 대신 **"사용자의 마스터 키(Kuser​)"**로 암호화된 뭉치를 던져줬을 뿐입니다.

**만약 해커가 네트워크 중간에서 AS가 보낸 이 응답 뭉치를 가로챘다면, 해커는 사용자의 세션 키나 TGT를 알아낼 수 있을까요? 없다면 왜 없을까요?**
-> 없음. 왜냐면 사용자의 마스터키를 해커는 가지고 있지 않고, 그 상태에서는 암호화된 알 수없는 패킷일 뿐이기 때문. 
이 질문은 커버로스가 어떻게 네트워크상에서 비밀번호를 직접 전송하지 않고도 신원을 증명하는지 이해하는 핵심입니다.

### 💡 핵심 원리 (The Why)

네트워크상에 **패스워드를 직접 전송하지 않으면서도**, 사용자가 가진 비밀번호(비밀 키)를 통해 서버가 발행한 암호문을 풀 수 있는지 확인하여 **사용자의 신원을 증명하고 향후 통신에 쓸 임시 열쇠(세션 키)를 안전하게 전달**하기 위함입니다.

---

### 🛠️ AS(Authentication Service) 교환의 원자적 단계

AS 과정은 크게 **요청(AS_REQ)**과 **응답(AS_REP)**으로 나뉩니다. 각 패킷 내부에 무엇이 들어있고, 어떤 키로 잠기는지 "Low-level"에서 시각화하겠습니다.

#### 1. AS_REQ (Client → AS): "저 로그인하고 싶어요"

사용자가 ID를 입력하면 클라이언트 PC는 다음 정보를 담아 AS로 보냅니다.

- **평문 데이터:** 사용자 ID (`duhj`), 접근하려는 서비스 ID (`TGS`), 타임스탬프.
    
- **특이점:** 비밀번호는 절대로 보내지 않습니다. 오직 '나 누구요'라는 정보만 보냅니다.
    

#### 2. AS의 내부 처리 (Atomic Operation)

AS는 요청을 받자마자 데이터베이스를 뒤져 다음 두 가지 키를 준비합니다.

- **$K_{user}$** 사용자의 비밀번호로부터 유도된 대칭키.
    
- **$K_{TGS}$**: TGS 서버와 KDC만 알고 있는 마스터 키.
    

그 후, AS는 **로그인 세션 키($SK_C-TGS$)** 를 무작위로 생성합니다. 이것이 앞으로 사용자와 TGS가 대화할 때 쓸 '임시 열쇠'입니다.

#### 3. AS_REP (AS → Client): "이 암호문을 풀 수 있다면 당신을 믿겠소"

AS는 클라이언트에게 두 개의 '상자'를 묶어서 보냅니다. 이 구조가 커버로스의 핵심입니다.

| **구분**               | **내용물**                                    | **암호화에 사용된 키**    | **누가 열 수 있는가?**         |
| -------------------- | ------------------------------------------ | ----------------- | ----------------------- |
| **상자 A (Client 전용)** | 세션 키($SK_C-TGS$), 만료 시간                    | $K_{user}$(사용자 키) | **사용자** (비밀번호를 아는 경우만)  |
| **상자 B (TGT)**       | 사용자 ID, 네트워크 주소, 만료 시간, **세션 키$SK_C-TGS$** | $K_{TGS}$         | **TGS 서버** (사용자는 못 열어봄) |

---

### ⚠️ 엄격한 논리 점검 (Brutally Honest Critique)

당신이 앞서 답변한 "클라이언트당 키 1개"는 맞지만, **TGT의 내부 구조**를 간과하면 안 됩니다.

- **지식 간극 식별:** 사용자는 AS로부터 받은 TGT를 가지고 있지만, 그 안을 들여다볼 수 없습니다. TGT는 $K_{TGS}$로 잠겨 있기 때문입니다.
    
- **결론:** 사용자는 $K_{user}$를 이용해 '상자 A'를 열어 **세션 키**만 꺼냅니다. 그리고 '상자 B(TGT)'는 내용도 모른 채 통째로 들고 있다가, 나중에 TGS에게 "자, AS가 준 티켓 여기 있소"라며 그대로 전달만 하는 역할입니다.
    

---

### 🔄 역전 학습 (Reverse Teaching)

위의 '상자 B(TGT)' 안에는 **세션 키(![](data:image/png;base64,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))**가 들어있고, '상자 A' 안에도 동일한 **세션 키**가 들어있습니다.

**왜 AS는 똑같은 세션 키를 굳이 두 군데(사용자용 상자, TGS용 상자)에 나누어 담아서 사용자에게 보낼까요?** 나중에 사용자가 TGS에게 접근할 때 이 두 세션 키가 각각 어떻게 사용될지 추측하여 설명해 보세요.

---

### 🥊 최종 확인 퀴즈 (Challenging Quiz)

**상황:** 해커가 네트워크를 가로채서 AS가 클라이언트에게 보내는 **AS_REP(상자 A + 상자 B)** 전체를 획득했습니다.

1. 해커는 상자 B(TGT)를 복호화해서 그 안의 세션 키를 알아낼 수 있습니까? (이유 포함)
    
2. 만약 사용자가 비밀번호를 틀리게 입력했다면, 클라이언트 프로그램은 AS로부터 받은 응답 중 어떤 부분에서 에러를 발생시키게 될까요? (어떤 키를 사용하려다 실패하는지 설명하세요.)
    

이 질문에 답할 수 있다면 커버로스의 1단계인 AS 과정을 완전히 정복한 것입니다. 다음 단계로 넘어갈까요?