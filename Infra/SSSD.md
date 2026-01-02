---
id: SSSD
aliases: []
tags:
  - sssd
  - auth
---

SSSD(System Security Services Daemon)는 리눅스 시스템이 원격 인증 서버(LDAP, Kerberos 등)와 직접 통신할 때 발생하는 지연, 오프라인 접속 불가, 설정 복잡성 문제를 해결하기 위해 **로컬 시스템과 원격 서버 사이에 위치하여 캐싱(Caching)과 연결 중계(Broker)** 역할을 수행하는 데몬입니다.

---

### 1. SSSD가 존재하는 이유: "중개자(Broker)"

과거에는 리눅스에서 중앙 계정 관리(LDAP/Kerberos)를 연동하려면 `nss_ldap`, `pam_krb5` 등을 직접 설정했습니다. 하지만 이 방식은 네트워크가 끊기면 로그인이 불가능하고, 매번 서버에 요청을 보내느라 느렸습니다.

SSSD는 이 문제를 해결하기 위해 **로컬 운영체제(PAM/NSS)** 와 **백엔드 서버(LDAP/Kerberos)** 사이에서 **중개 및 캐싱**을 담당합니다.

#### 핵심 역할 3가지
1. **통합 인터페이스:** OS 입장에서는 그냥 SSSD하고만 대화하면 됩니다. (백엔드가 AD인지, FreeIPA인지, LDAP+Kerberos 조합인지 몰라도 됨)
2. **오프라인 로그인 지원 (Caching):** 한 번 로그인한 사용자의 정보를 로컬(`LDB` 데이터베이스)에 저장해두어, 네트워크가 끊겨도 로그인할 수 있게 합니다.
3. **부하 감소:** 매번 요청하는 대신 캐시된 정보를 주거나, 하나의 연결을 재사용하여 서버 부하를 줄입니다.
---
### 2. LDAP와 Kerberos의 역할 분담 (Data Flow)
SSSD 설정에서 이 둘은 명확히 다른 역할을 수행합니다. SSSD는 이 둘을 조합하여 완전한 인증 프로세스를 만듭니다.
* **LDAP (Identity Provider):** "이 사용자가 누구인가?" (신원 정보)
  * 사용자 이름(uid), 그룹 정보(gid), 홈 디렉토리 경로, 쉘 정보 등을 가져옵니다.
* **Kerberos (Authentication Provider):** "이 사용자가 진짜 그 사람이 맞는가?" (인증)
  * 비밀번호 검증 및 티켓(TGT) 발급을 담당합니다.

---

### 3. 데이터 변환 과정 시각화 (State Transformation)

사용자가 터미널에서 `ssh user1@server`를 입력했을 때, SSSD 내부에서 데이터가 어떻게 변환되고 흐르는지 단계별로 확인합니다.

**상태 0: 사용자 입력**

* Input: `ID: user1`, `PW: secret123`

**상태 1: NSS 요청 (사용자 정보 확인)**

1. OS(SSH 데몬)는 `user1`이 존재하는지 확인하기 위해 NSS(Name Service Switch)를 호출합니다.
2. `nss_sss` 모듈이 **SSSD 데몬**에 쿼리를 던집니다.
3. **SSSD:** 로컬 캐시(LDB) 확인  없으면 **LDAP 서버**에 쿼리 (`(&(objectClass=posixAccount)(uid=user1))`).
4. **LDAP 서버:** `uid=1001, gid=1001, shell=/bin/bash` 등의 속성(Attribute) 반환.
5. **SSSD:** 정보를 로컬 캐시에 저장하고 OS에 반환.

* **결과:** OS는 `user1`의 존재를 인지함.

**상태 2: PAM 요청 (비밀번호 검증)**

1. OS는 비밀번호 검증을 위해 PAM(Pluggable Authentication Modules)을 호출합니다.
2. `pam_sss` 모듈이 **SSSD 데몬**에 인증 요청을 보냅니다.
3. **SSSD:** 입력받은 `secret123`을 가지고 **Kerberos KDC(Key Distribution Center)**에 `AS-REQ`(인증 요청)을 보냅니다.
4. **Kerberos:** 비밀번호가 맞으면 `TGT`(Ticket Granting Ticket)를 발급하여 SSSD에 반환.
5. **SSSD:** TGT를 받았으므로 인증 성공으로 간주 (`PAM_SUCCESS` 반환).

* **결과:** 로그인 성공.

**상태 3: 최종 세션 생성**

* SSSD는 발급받은 Kerberos 티켓을 `/tmp/krb5cc_xxx`와 같은 파일로 로컬에 저장(캐싱)하여, 이후 사용자가 SSO(Single Sign-On)로 다른 서비스에 접근할 때 재사용할 수 있게 만듭니다.

---

### 4. 구조 요약 (Architecture)

```text
[ Application (SSH, Sudo, etc.) ]
       |             |
    (Identity)    (Auth)
   NSS Library    PAM Library
       |             |
-------------------------------------------
| [ Client Libraries (nss_sss, pam_sss) ] |  <-- OS 영역
-------------------------------------------
             | (Socket 통신)
             v
----------------------------------
|      [ SSSD Daemon ]           | <-- SSSD 영역
|  1. Monitor (프로세스 관리)    |
|  2. Responders (NSS, PAM 응답) |
|  3. Data Provider (백엔드 통신)|
|  4. LDB Cache (로컬 캐시 DB)   |
----------------------------------
             |
    --------------------
    |                  |
[ LDAP Server ]   [ Kerberos KDC ]  <-- 원격 서버 영역
 (사용자 정보)       (비밀번호 인증)

```

---

### 5. 핵심 질문 (Reverse Teaching)

이 개념을 제대로 이해했는지 확인하기 위해 다음 퀴즈에 답해보세요.

1. 네트워크 케이블을 뽑았는데도 리눅스 서버에 어제 로그인했던 AD(Active Directory) 계정으로 로그인이 되었습니다. SSSD의 어떤 기능 때문이며, 이때 인증은 Kerberos 서버를 통해 이루어진 것입니까? (O/X 로 대답하고 이유 설명)
> [!ANSWER]-
> SSSD의 캐시 기능 때문. 인증은 서버를 통해 이루어진게 아니라 SSSD의 LDB의 인증에 의해 이루어짐.  
2. SSSD 설정 파일(`sssd.conf`)에서 `id_provider = ldap`, `auth_provider = krb5`로 설정했습니다. 만약 LDAP 서버는 살아있는데 Kerberos 서버만 다운되었다면, `id user1` 명령어와 `ssh user1@localhost` 명령어의 결과는 각각 어떻게 됩니까?
> [!ANSWER]-
> id는 뜨고, ssh는 실패
