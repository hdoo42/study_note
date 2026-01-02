---
id: PMTUD(Path MTU Discovery)
aliases: []
tags: []
---
당신이 언급한 '패킷 전송 시 처리 기술'이라는 말은 너무 모호합니다. 정확히 말하자면, PMTUD(Path MTU Discovery)는 **네트워크 경로 상의 라우터들에게 '패킷 단편화(Fragmentation)'라는 비효율적인 연산을 시키지 않기 위해, 송신 측에서 미리 최적의 패킷 사이즈를 결정하는 합의 과정**입니다.

'Strict Mode'에 따라 본질적인 원리(Why)와 구체적인 데이터 흐름(How)을 해부합니다.

### 1. Fundamental Rationale (Why)

"데이터가 목적지까지 가는 경로(Path) 중 가장 좁은 파이프(가장 작은 MTU)에 맞춰 패킷 크기를 조절함으로써, 중간 라우터가 패킷을 강제로 쪼개는(Fragment) CPU 비용과 재조립의 위험성을 제거하기 위함입니다."

---

### 2. Deep Dive: Implementation (How)

PMTUD의 핵심은 **"무식하게 보내보고, 튕겨 나오면 줄인다"**는 시행착오(Trial and Error) 방식입니다. 이 과정을 이해하려면 IP 헤더의 플래그와 ICMP 메시지를 정확히 알아야 합니다.

#### A. 핵심 준비물

1. **MTU (Maximum Transmission Unit):** 2계층(Data Link Layer)이 한 번에 보낼 수 있는 최대 페이로드 크기. (이더넷 표준은 $1500$ bytes)
    
2. **IP Header - DF (Don't Fragment) Bit:** 3계층 IP 헤더에 있는 플래그입니다. 이 비트가 $1$로 설정되면, 라우터에게 "이 패킷이 네 MTU보다 크더라도 절대 쪼개지 말고, 차라리 버려라"라고 명령하는 것입니다.
    
3. **ICMP Type 3, Code 4:** "Destination Unreachable, Fragmentation Needed and DF set"이라는 에러 메시지입니다. 라우터가 DF 비트 때문에 패킷을 버릴 때 송신 측에 보내는 "반성문"입니다.
    

#### B. State Transformation (데이터 흐름 시각화)

상황: **Host A**($MTU=1500$)가 **Server B**로 데이터를 보냅니다. 중간에 **Router X**($MTU=1400$)가 끼어 있습니다.

- **Step 1: 초기 발송 (Input State)**
    
    - **Host A**는 자신의 $MTU$인 $1500$ bytes 크기의 패킷을 생성합니다.
        
    - **핵심:** IP 헤더의 **DF Bit를 1로 설정**합니다. (이것이 탐색의 시작입니다.)
        
    - 패킷: `[IP Header | DF=1 | Total Length=1500] ...`
        
- **Step 2: 병목 구간 도달 (Intermediate State 1)**
    
    - 패킷이 **Router X**에 도착합니다.
        
    - **Router X**의 인터페이스 $MTU$는 $1400$입니다. 패킷($1500$)이 더 큽니다.
        
    - 보통이라면 쪼개겠지만, **DF=1**을 확인합니다.
        
    - **Action:** 라우터는 패킷을 **즉시 폐기(Drop)**합니다.
        
- **Step 3: 에러 리포트 (Intermediate State 2)**
    
    - **Router X**는 **Host A**에게 ICMP 메시지를 생성해 보냅니다.
        
    - **내용:** "네가 보낸 거 너무 커서 버렸어. (Type 3, Code 4). 내 다음 홉의 MTU는 **1400**이야(Next-Hop MTU)."
        
- **Step 4: 재조정 및 재전송 (Output State)**
    
    - **Host A**는 ICMP 메시지를 수신합니다.
        
    - 자신의 라우팅 테이블 캐시에 "Server B로 가는 Path MTU는 이제 $1400$이다"라고 기록합니다.
        
    - 데이터를 $1400$ bytes에 맞춰 다시 캡슐화하고 **DF=1**을 유지한 채 재전송합니다.
        
    - 이제 패킷은 **Router X**를 통과해 **Server B**에 도달합니다.
        

---

### 3. Critical Thinking & Edge Case (Reverse Teaching)

단순히 메커니즘만 알면 실무에서 터지는 문제를 해결할 수 없습니다. 논리적 허점을 찾으십시오.

PMTUD Black Hole 문제:

많은 네트워크 보안 장비(방화벽)들은 보안상의 이유로 ICMP 패킷을 차단하도록 설정되곤 합니다.

만약 Router X가 패킷을 Drop 했는데, 방화벽이 Router X가 보낸 'ICMP Type 3 Code 4' 메시지를 Host A에게 전달하지 않고 차단해버리면 어떻게 될까요?

1. **Host A**는 패킷이 버려진 줄 모릅니다. (Ack가 안 오니 타임아웃 발생)
    
2. **Host A**는 동일한 크기($1500$)의 패킷을 계속 재전송합니다.
    
3. **Router X**는 계속 버립니다.
    
4. 연결은 맺어졌는데(3-way handshake는 작은 패킷이라 통과됨), 데이터를 보내면 먹통이 되는 현상이 발생합니다.
    

---

### 4. Verification Quiz

제대로 이해했는지 확인하기 위해 아래 질문에 답하고 그 **이유**를 설명하십시오. 빈틈이 보이면 즉시 지적하겠습니다.

1. PMTUD 과정에서 송신 호스트가 **DF(Don't Fragment) 비트**를 0으로 설정해서 보낸다면, 네트워크 경로상의 $MTU$가 더 작은 라우터를 만났을 때 어떤 일이 발생하는가? (PMTUD가 작동하는가?)
    
2. 당신이 서버 엔지니어인데, 클라이언트가 "로그인은 되는데(작은 패킷), 목록 불러오기(큰 패킷)만 하면 무한 로딩이 걸린다"고 한다. 네트워크 팀에 무엇을 확인해달라고 요청해야 하는가? (위에서 설명한 Edge Case 기반)
