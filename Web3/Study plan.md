---
id: Study plan
aliases: []
tags: []
---

# Solana 스마트 컨트랙트 개발자 1년 로드맵

사용자의 목표는 **1년 이내에 Solana 스마트 컨트랙트 개발자로 취업**하는 것입니다. 이에 맞춰, **Solana 및 Web3 기본 개념**에서 시작해 **Rust 기반 Solana 프로그램(스마트 컨트랙트)** 개발 실력을 쌓고, 마지막 몇 달은 **포트폴리오 프로젝트** 완성과 **구직 준비**에 집중하는 로드맵을 제시합니다. 하루 10분(주말 포함)을 꾸준히 투자할 수 있도록 **월별**, **주차별**로 학습 주제와 분량을 점진적으로 설계했습니다. 각 주차별로 학습 목표와 추천 자료(튜토리얼, 문서 등) 또는 실습 과제를 포함하며, 주어진 시간 내에 꾸준히 소화할 수 있도록 조절했습니다.

## 1개월차: 블록체인과 Solana 이해 기초 다지기

이달은 **블록체인 일반 원리**와 **Web3 개념**을 익히고, Solana를 공부할 기반을 만듭니다. Rust에는 이미 익숙하시므로, 블록체인의 작동 방식과 Solana 네트워크의 철학적 배경을 파악하는 데 집중합니다.

### 1주차: Web3와 블록체인 개념 이해

- **학습 주제:** Web3의 개념과 블록체인의 기본 원리 학습. 탈중앙화(Decentralization)의 의미, 분산원장 기술이 해결하는 문제를 알아봅니다. 또한 **스마트 컨트랙트**(Smart Contract)의 개념과 기존 웹 개발과의 차이를 이해합니다.

- **학습 목표:** 블록체인이 어떻게 **신뢰를 코드로 대체**하는지 큰 그림을 그립니다. 비트코인과 이더리움 등 주요 블록체인에서 거래가 처리되는 방식, 네트워크 참여자(노드)의 역할 등을 익혀둡니다. 스마트 컨트랙트란 무엇이며, 왜 Web3에서 중요 요소인지 개념을 파악하세요.
 - **추천 자료:**
    - (개념 정리) _쉽게 이해하는 블록체인 개요_ 등의 자료를 찾아 읽어보세요 (예: [AWS 블록체인 설명서](https://aws.amazon.com/what-is/blockchain/?aws-products-all.sort-by=item.additionalFields.productNameLowercase&aws-products-all.sort-order=asc) 등).
    - (동영상) 유튜브에서 "블록체인 기초"를 검색해 5~10분 분량의 설명 영상을 시청해도 좋습니다.
- **실습(선택):** 이더리움의 **Remix** 같은 온라인 IDE를 이용해 간단한 스마트 컨트랙트 예제를 배포해보는 것도 도움이 됩니다 (예: Remix에서 제공하는 예제 코드 실행해보기).

### 2주차: Solana 블록체인 소개 및 아키텍처 개요

- **학습 주제:** **Solana** 블록체인의 철학과 설계 원리 학습. Solana가 다른 블록체인과 어떻게 다른지, 특히 **고속 처리**를 가능케 한 핵심 개념(예: **Proof of History** 개념, **병렬 처리(Sealevel)** 모델 등)을 알아봅니다. Solana 네트워크 구조, 클러스터(메인넷, 테스트넷, 로컬)을 소개합니다.
- **학습 목표:** Solana가 **초당 수만 건의 거래**를 처리할 수 있는 이유와 기술적 배경(예: PoH 기반 시간 증명)을 이해합니다. 또한 Solana의 **계정 모델**과 **프로그램(스마트 컨트랙트)** 개념을 다른 체인(Ethereum 등)과 비교합니다. 특히 Solana의 **프로그램은 상태를 자체적으로 저장하지 않는(stateless)** 특성이 있다는 점을 기억하세요 ([What is the difference between ethereum smart contracts and solana programs? - Solana Stack Exchange](https://solana.stackexchange.com/questions/10236/what-is-the-difference-between-ethereum-smart-contracts-and-solana-programs#:~:text=In%20calls%20to%20EVM%20contracts%2C,function%20that%20updates%20contract%20state)). 이로 인해 Ethereum과 달리 **프로그램 코드와 상태 데이터 계정이 분리**되어 있으며, 프로그램 호출 시에 필요한 상태 계정들을 모두 인자로 제공해야 함을 이해합니다 ([What is the difference between ethereum smart contracts and solana programs? - Solana Stack Exchange](https://solana.stackexchange.com/questions/10236/what-is-the-difference-between-ethereum-smart-contracts-and-solana-programs#:~:text=In%20calls%20to%20EVM%20contracts%2C,function%20that%20updates%20contract%20state)).
- **추천 자료:**
    - (공식 문서) Solana 공식 문서의 _“Solana란 무엇인가”_ 섹션을 읽으며 네트워크 개요와 설계 철학을 파악합니다.
    - (비교 글) _Solana vs Ethereum_ 비교 블로그를 찾아 읽어보세요 (Solana가 stateless 프로그래밍 모델을 택한 이유와 차이점 설명) ([What is the difference between ethereum smart contracts and solana programs? - Solana Stack Exchange](https://solana.stackexchange.com/questions/10236/what-is-the-difference-between-ethereum-smart-contracts-and-solana-programs#:~:text=In%20calls%20to%20EVM%20contracts%2C,function%20that%20updates%20contract%20state)).
- **참고 개념:** Solana에서 스마트 컨트랙트를 특별히 **“프로그램(Program)”**이라고 부르므로, 이후 용어를 혼용해서 사용합니다. 프로그램은 블록체인에 업로드된 **실행 코드**이며, **상태는 따로 계정(Account)**에 저장합니다.

### 3주차: 개발 환경 설정 (Rust Toolchain, Solana CLI)

- **학습 주제:** Solana 개발을 위한 **로컬 환경 구성**. 이미 Rust 환경은 갖춰져 있을 가능성이 높지만, Solana 전용 개발 도구들을 설치합니다. **Solana CLI 툴(Solana Tool Suite)** 설치 및 **클러스터 연결** 설정을 진행합니다. 또한 간단한 Solana CLI 사용법을 익혀봅니다.
- **학습 목표:** 로컬에 Solana 개발에 필요한 툴체인을 갖추고, Solana 네트워크에 연결할 수 있는 상태를 만듭니다. `solana --version` 등 명령어를 실행해보고, Solana CLI로 키페어를 생성하고(`solana-keygen new`) 네트워크를 Devnet으로 설정(`solana config set --url devnet`)하는 등의 기본 동작을 수행해 봅니다.
- **추천 자료:**
    - (설치 가이드) Solana 공식 튜토리얼 _“Install the Solana CLI and Anchor”_ 가이드 참고 – Rust 설치, Solana CLI 설치 방법, 클러스터 설정 등이 단계별로 나와 있습니다.
    - (블로그 글) _Solana/Rust Set Up Guide_와 같은 블로그 글을 참고하여 Windows/MacOS에 Solana CLI 세팅을 완료합니다.
- **실습:**
    1. **키페어 생성** – `solana-keygen new` 명령으로 지갑 키를 하나 생성하고, 공개키와 비밀키 위치를 확인해보세요.
    2. **에어드롭** – Devnet에 연결한 뒤 `solana airdrop 1` 명령으로 테스트용 SOL을 받아보고, `solana balance`로 잔액을 확인합니다.
    3. **로컬 테스트validator** (선택) – `solana-test-validator` 명령으로 로컬 테스트넷을 구동하여 콘솔 로그를 구경합니다.

### 4주차: Solana 계정 및 트랜잭션 기초 개념 탐구

- **학습 주제:** Solana의 **계정(Account) 모델**과 **트랜잭션 구성**에 대한 기초 개념을 학습합니다. Solana에서 **모든 데이터는 계정에 저장**되고, 프로그램 자체는 상태를 저장하지 않는다는 점을 다시 확인합니다. 또한 **트랜잭션**이 어떻게 구성되어 프로그램을 호출하는지, 트랜잭션 내 **명령(Instruction)**의 개념을 알아봅니다.
- **학습 목표:** Solana 계정의 구조와 속성(예: 공개키 주소, Lamports(토큰) 보유량, 소유자 프로그램, 데이터 길이, 임대료 등)을 이해합니다. **계정은 Solana의 1급 객체**로, 계정이 실행 가능(executable) 플래그를 갖고 있으면 프로그램 코드가 들어있는 **프로그램 계정**임도 이해하세요 ([Solana teardown: Walkthrough of the example helloworld program - DEV Community](https://dev.to/cogoo/solana-teardown-walkthrough-of-the-example-helloworld-program-18m4#:~:text=Programs%20are%20stateless,we%20need%20is%20that%3B%20our)). 트랜잭션은 다수의 명령을 포함할 수 있고, 각 명령은 호출할 프로그램과 관련 계정 리스트 및 데이터를 가지고 있습니다. Solana에서는 어떤 프로그램을 호출하든 **해당 프로그램이 사용하게 될 모든 계정 정보를 트랜잭션에 명시적으로 제공**해야 함을 기억합니다.
- **추천 자료:**
    - (공식 문서) Solana 개발자 문서의 _계정(Account)_ 설명 섹션 – 계정 구조와 권한에 대해 상세히 나와 있습니다 (예: **계정의 소유자 필드**는 해당 계정을 수정할 수 있는 프로그램을 가리키며, 소유자 프로그램만 그 계정 데이터를 변경 가능 ([The Solana Programming Model: An Introduction to Developing on Solana](https://www.helius.dev/blog/the-solana-programming-model-an-introduction-to-developing-on-solana#:~:text=The%20,few%20rules%20on%20account%20ownership))).
    - (블로그) _Solana Programming Model_ 소개 블로그 – Solana의 **프로그램과 계정의 분리**에 대해 잘 설명한 글입니다. “Solana programs are stateless... all data they need is in separate accounts” 등의 부분을 참고하세요 ([The Solana Programming Model: An Introduction to Developing on Solana](https://www.helius.dev/blog/the-solana-programming-model-an-introduction-to-developing-on-solana#:~:text=of%20code%20and%20data,a%20program%20to%20interact%20with)).
- **실습:**
    - Solana CLI로 새로운 임시 계정을 하나 만들어보고 (`solana-keygen new -o temp.json`), `solana account <새 계정 주소>` 명령으로 계정 정보를 조회해보세요. 데이터 길이, 소유자(owner)가 어떤 프로그램으로 설정되어 있는지 등을 확인합니다 (새 계정은 기본적으로 System Program이 소유자로 설정됨).

## 2개월차: Solana 프로그램 개발 준비 및 기본 예제

이달은 **Solana 프로그램(스마트 컨트랙트) 개발**의 기초를 다집니다. 간단한 예제를 통해 Solana에서 프로그램을 작성하고 배포하는 전체 사이클을 경험해보고, **Rust로 Solana 프로그램을 작성하는 방법**을 익힙니다. 처음에는 Anchor 프레임워크 없이 **네이티브 Solana 프로그램**을 직접 다뤄보면서 기본을 이해하고, 이후 Anchor 사용을 위한 대비를 합니다.

### 1주차: Rust로 Solana 프로그램 구조 이해 (네이티브 방식)

- **학습 주제:** **네이티브 Solana 프로그램**의 구조와 작성 방법을 배웁니다 (Anchor 없이). Solana 프로그램은 Rust로 작성되며 Solana의 런타임 규칙에 따라 컴파일됩니다. 프로그램의 진입점(`entrypoint`)과 프로그램 내 **프로세서(processor) 함수**의 구현 패턴을 살펴봅니다.
- **학습 목표:** Solana 프로그램이 Rust 코드로 어떻게 구성되는지 큰 그림을 그립니다. 예를 들어 Solana 프로그램에는 `#[program]` 어트리뷰트 (Anchor 사용시)나 또는 직접 `entrypoint!(process_instruction)` 매크로를 사용하여 진입점을 정의한다는 것을 이해합니다. 또한 **borsh** 또는 **serde**를 이용한 데이터 직렬화, **계정 구조체 정의**, **프로그램 에러 처리** 등에 대한 감을 잡습니다. 이 모든 것을 저수준에서 Anchor 없이 구현하면 boilerplate 코드가 많다는 점을 체감하는 것이 목표입니다.
- **추천 자료:**
    - (예제 코드) Solana Labs의 공식 GitHub 예제 [`example-helloworld` 레포](https://github.com/solana-labs/example-helloworld) – “Hello World” 프로그램의 Rust 코드를 살펴보세요. `program/src/lib.rs` 파일의 코드를 읽으며 각 부분이 무엇을 하는지 주석과 함께 이해해봅니다.
    - (블로그) _Solana teardown: example helloworld program_ (DEV Community) – Solana Hello World 예제 코드를 한 줄씩 해설한 블로그입니다 ([Solana teardown: Walkthrough of the example helloworld program - DEV Community](https://dev.to/cogoo/solana-teardown-walkthrough-of-the-example-helloworld-program-18m4#:~:text=In%20this%20article%2C%20we%27ll%20walk,how%20programs%20on%20Solana%20work)) ([Solana teardown: Walkthrough of the example helloworld program - DEV Community](https://dev.to/cogoo/solana-teardown-walkthrough-of-the-example-helloworld-program-18m4#:~:text=Programs%20are%20stateless,we%20need%20is%20that%3B%20our)). 이 글을 통해 Solana 네이티브 프로그램의 구조를 설명과 함께 따라가보세요. 특히 “Programs are stateless... If you need to store state between transactions, you can do so using Accounts”라는 설명을 확인해보세요 ([Solana teardown: Walkthrough of the example helloworld program - DEV Community](https://dev.to/cogoo/solana-teardown-walkthrough-of-the-example-helloworld-program-18m4#:~:text=Programs%20are%20stateless,we%20need%20is%20that%3B%20our)).
- **실습:** 코드를 직접 작성하지 않더라도, 위 예제를 **로컬에서 빌드 및 배포**해볼 것을 권장합니다. Solana CLI로 로컬 테스트넷(`solana-test-validator`)을 가동한 후, 예제 프로그램 코드를 `cargo build-bpf`로 빌드하고 `solana program deploy` 명령으로 로컬에 배포해봅니다. 배포 후 `solana logs`를 통해 프로그램이 `msg!` 매크로로 찍는 로그("Hello World!")가 출력되는지 확인해보세요.

### 2주차: Solana 프로그램 배포와 실행 흐름 이해

- **학습 주제:** 지난 주 작성한 네이티브 프로그램을 **Devnet에 배포 및 호출**해보며, Solana 프로그램의 실행 흐름을 익힙니다. 클라이언트(Off-chain)에서 프로그램을 호출하는 방법, 트랜잭션 생성 방법 등을 간략히 학습합니다.
- **학습 목표:** Solana에서 프로그램을 배포(deploy)한다는 것이 무엇인지 이해하고, **프로그램ID(Public Key)**의 역할을 파악합니다. 프로그램 배포 후에는 클라이언트 측에서 해당 프로그램ID에 대해 트랜잭션을 만들어 호출해야 합니다. 이때 **프론트엔드나 스크립트가 Solana Web3 SDK** (예: JavaScript Solana web3.js나 Rust solana-client 라이브러리)를 통해 트랜잭션을 구성하고, 필요한 계정들을 포함하여 전송하는 흐름을 이해하세요. 간단한 클라이언트 예제를 통해 “Hello World” 프로그램을 실제로 호출해 로그를 남기는 작업을 수행해봅니다.
- **추천 자료:**
    - (공식 튜토리얼) Solana Docs의 _Local Deployment Quickstart_ 가이드 – 로컬 및 Devnet에 프로그램을 배포하고 호출하는 과정을 단계별로 설명합니다.
    - (예제 코드) 위 GitHub 예제의 `/src/client` 디렉토리에 클라이언트 코드가 있다면 참고하거나, Solana 웹3.js를 이용한 간단한 호출 예제를 찾아보세요.
    - (도구) **Solana Explorer** 사이트에서 Devnet을 선택해, 배포된 프로그램 계정을 조회하고 트랜잭션 로그를 확인하는 방법도 익혀둡니다.
- **실습:**
    1. Devnet에 **에어드롭**을 충분히 받은 자신의 지갑을 통해 `solana program deploy` 명령으로 Hello World 프로그램을 Devnet에 배포합니다 (배포 시 프로그램ID(pubkey) 출력 확인).
    2. 간단한 Rust or Node.js 스크립트를 작성하여 해당 프로그램의 `process_instruction`을 호출하는 트랜잭션을 만들어 Devnet에 보내봅니다. (힌트: Solana web3.js의 `sendAndConfirmTransaction` 함수나 solana-client Rust crate의 `send_transaction` 등을 사용해볼 수 있습니다.)
    3. Solana Explorer 또는 `solana logs -u devnet`로 해당 트랜잭션의 로그를 확인해 프로그램이 제대로 호출되었는지 검증합니다.

### 3주차: Anchor 프레임워크 소개 및 설치

- **학습 주제:** **Anchor 프레임워크**를 본격적으로 도입합니다. Anchor는 Solana 프로그램 개발을 생산적으로 만들어주는 인기 프레임워크입니다. 이번 주에는 Anchor의 철학과 기능을 개략적으로 이해하고, 개발 환경에 Anchor를 설치합니다.
- **학습 목표:** Anchor가 **어떤 문제를 해결해주는지** 이해합니다. Anchor를 사용하면 계정의 (디)시리얼라이즈, 계정 검증, 보일러플레이트 코드 생성을 자동화하여 개발자가 비즈니스 로직에 집중할 수 있습니다 ([Anchor By Example - Introduction](https://examples.anchor-lang.com/#:~:text=Anchor%20is%20a%20framework%20for,quickly%20building%20secure%20Solana%20programs)). 또한 Anchor 프로젝트의 구조(예: _programs_ 폴더와 _tests_ 폴더, Anchor.toml 파일 등)를 살펴보고, 기본 명령어 (`anchor build`, `anchor test`, `anchor deploy`)의 역할을 파악하세요. 이번 주 학습으로 “왜 Anchor를 쓰는가?”에 대한 답을 얻고 넘어가는 것이 중요합니다.
- **추천 자료:**
    - (공식 문서) Anchor 공식 사이트의 _Introduction_ 문서를 읽어 Anchor의 주요 개념을 이해합니다. Anchor가 어떻게 보일러플레이트를 줄이고 보안을 강화하는지 설명되어 있습니다 ([Anchor By Example - Introduction](https://examples.anchor-lang.com/#:~:text=Anchor%20is%20a%20framework%20for,quickly%20building%20secure%20Solana%20programs)).
    - (커뮤니티 자료) _Anchor by Example_ 저장소의 소개글 – Anchor로 작성된 여러 예제들을 보여주는 오픈소스 자료 ([Anchor By Example - Introduction](https://examples.anchor-lang.com/#:~:text=Anchor)). 여기서 Anchor가 지원하는 기능들과 예제 목록을 훑어보면 앞으로 만들 프로젝트의 아이디어를 얻을 수도 있습니다.
    - (설치 가이드) Anchor 설치: 터미널에서 `cargo install --git https://github.com/coral-xyz/anchor avm --locked` 등의 명령으로 Anchor CLI를 설치합니다. Anchor 책(Anchor Book)에 나와있는 [설치 가이드](https://www.anchor-lang.com/docs/installation)를 따라 하시면 됩니다.
- **실습:**
    - Anchor CLI 설치 후 `anchor --version`으로 정상 설치 여부를 확인합니다.
    - Anchor가 잘 설치되었으면, `anchor init hello_anchor` 명령으로 첫 Anchor 프로젝트를 초기화해봅니다. 생성된 디렉토리 구조를 살펴보고, `programs/hello_anchor/src/lib.rs` 파일에 기본 템플릿 코드가 생성되었는지 확인하세요.

### 4주차: 첫 Anchor 프로그램 개발 – “Hello World”

- **학습 주제:** Anchor를 사용하여 Solana 프로그램 “Hello World”를 만들어봅니다. Anchor 프로젝트를 빌드하고, 프로그램이 클라이언트 요청을 받아 **간단한 동작(콘솔에 메시지 출력 등)**을 수행하도록 구현합니다. Anchor의 편의성(예: `#[derive(Accounts)]` 구조체, `msg!` 매크로 사용 등)을 직접 체험해봅니다.
- **학습 목표:** Anchor로 프로그램을 작성하고 배포하는 한 사이클을 경험합니다. Anchor에서는 **프로그램 모듈에 `#[program]` 어트리뷰트를 붙여 함수들을 정의**하고, **계정 구조체를 `#[account]` 어트리뷰트로 데코레이션**하여 검증하는 방법 등을 사용합니다. 이러한 Anchor 코드가 내부적으로 어떻게 Solana 런타임에 맞게 동작하는지 큰 그림을 이해하세요. 이번 주 목표는 Anchor로 “Hello World” 로그를 출력하는 프로그램을 Devnet에 배포하고, Anchor가 자동 생성한 IDL(Interface Description Language) 및 클라이언트 코드로 프로그램을 호출해보는 것입니다.
- **추천 자료:**
    - (튜토리얼) QuickNode 가이드 **“How to Write Your First Anchor Program in Solana – Part 1”** ([How to Write Your First Anchor Program in Solana - Part 1 | QuickNode Guides](https://www.quicknode.com/guides/solana-development/anchor/how-to-write-your-first-anchor-program-in-solana-part-1#:~:text=Programs%20are%20what%20Solana%20calls,first%20Solana%20Program%20with%20Anchor)) – Anchor로 Hello World 프로그램을 작성하고 Solana Playground 혹은 로컬에서 실행하는 방법을 단계별로 안내합니다. 해당 자료를 참고하여 차근차근 따라해보세요.
    - (공식 예제) Anchor 예제 중 _Hello World_ 파트를 참고해도 좋습니다. 예제 코드에는 `msg!("Hello, {}!", user.key());` 같이 메시지를 출력하는 간단한 프로그램이 포함되어 있을 것입니다.
- **실습:**
    1. **프로그램 구현:** Anchor 프로젝트의 lib.rs에 간단한 헬로 함수(`hello(ctx: Context<...>)`)를 만들어 `msg!` 매크로로 `"Hello Solana!"` 같은 메시지를 출력하게 작성합니다. (QuickNode 튜토리얼 참고)
    2. **테스트:** `anchor build && anchor deploy`로 Devnet에 배포한 후, `anchor test`로 자동 생성된 TypeScript 클라이언트 테스트를 실행해 봅니다. 테스트 스크립트가 프로그램을 호출하여 로그가 잘 출력되는지 확인하세요.
    3. **Solana Explorer 확인:** Devnet Explorer에서 프로그램ID로 검색하여 프로그램 계정이 생성되었는지, 로그에 "Hello Solana!"가 찍혔는지 확인해봅니다.

## 3개월차: Anchor를 통한 기본 DApp 개발 연습

Anchor 기반 개발에 익숙해지는 달입니다. **Anchor로 상태를 저장하고 조작**하는 방법을 학습하고, 이를 이용해 간단한 상태ful 스마트 컨트랙트를 만들어봅니다. 이번 달을 마치면 Anchor로 임의의 데이터 구조를 계정에 저장하고, 프로그램에서 읽고 쓰는 전 과정을 이해하게 될 것입니다.

### 1주차: Anchor로 상태 저장 - Counter 프로그램 설계

- **학습 주제:** **상태가 있는 프로그램** 구현하기 – 간단한 **카운터(counter)** 애플리케이션을 설계합니다. 사용자가 프로그램을 호출할 때마다 계정에 숫자를 1씩 증가시키는 로직을 만들 것입니다. 이를 통해 Anchor에서 **계정 초기화 (`init`), Program Derived Address(PDA) 사용, 계정 구조체 정의** 등을 연습합니다.
- **학습 목표:** Anchor로 **데이터 계정(Data Account)**을 생성하고 관리하는 방법을 익힙니다. `#[account(init, payer = user, space = ...)]` 등의 구문을 사용해 새로운 계정을 생성하고 초기화하는 방법, `#[account(mut)]`로 계정을 mutable하게 받아와서 데이터를 수정하는 방법을 학습하세요. 또한 Anchor의 `#[derive(Accounts)]` 구조체 내에서 **프로그램 파생 주소(PDA)**를 활용하여 **프로그램이 임의의 주소에 계정을 생성**하는 패턴도 이해합니다 (예: 특정 `seeds`와 `bump`를 이용한 PDA 생성).
- **추천 자료:**
    - (튜토리얼) QuickNode 가이드 **“How to Write Your First Anchor Program – Part 2”** ([How to Write Your First Anchor Program in Solana - Part 2 | QuickNode Guides](https://www.quicknode.com/guides/solana-development/anchor/how-to-write-your-first-anchor-program-in-solana-part-2#:~:text=This%20is%20the%202nd%20guide,your%20program%20has%20been%20used)) – 지난주 작성한 Hello 프로그램에 상태를 추가하여, 호출 횟수를 계정에 저장/증가시키는 방법을 단계별로 설명합니다. 계정 초기화와 데이터 저장 코드를 집중해서 따라해보세요.
    - (공식 문서) Anchor 문서의 _Accounts_ 챕터 – `#[account]` 데코레이터의 다양한 옵션 (init, mut, seeds, bump 등)과 그 의미를 정리해둡니다. Anchor를 통해 PDA를 생성하고 사용하는 방법도 이 문서에서 확인할 수 있습니다.
    - (예시 코드) Anchor 예제 _Counter_ 혹은 _Increment_ 유사 사례를 GitHub에서 찾아 참고하면 구조를 이해하기 쉽습니다.
- **실습:**
    1. **카운터 프로그램 구현:** `counter` 라는 u32 필드 하나를 갖는 계정 구조체 `CounterAccount`를 정의하고, `Initialize` 및 `Increment` 두 가지 instruction을 Anchor 프로그램에 구현합니다. `Initialize`는 새로운 PDA 계정을 `init`하여 counter=0으로 세팅, `Increment`는 해당 계정을 받아와 counter 값을 +1 증가시킵니다.
    2. **테스트:** Anchor 테스트(Typescript) 코드를 작성 또는 수정하여, `Initialize`를 한 번 호출하고 이어서 `Increment`를 여러 번 호출해본 뒤, 최종 counter 값이 기대대로 증가했는지 assert합니다.
    3. **개념 확인:** 프로그램에서 **PDA**를 생성할 때 어떤 seeds를 사용할 지 결정하고 (`[user.key().as_ref(), b"counter"]` 등), 같은 seeds로 다시 호출하면 동일 PDA에 접속한다는 것을 확인하세요. PDAs의 **결정적(deterministic)** 특성과 **off-curve 주소** 개념도 함께 복습합니다 ([What are Solana PDAs? Explanation & Examples (2025)](https://www.helius.dev/blog/solana-pda#:~:text=Solana%20programs%20,PDAs)) ([What are Solana PDAs? Explanation & Examples (2025)](https://www.helius.dev/blog/solana-pda#:~:text=The%20key%20for%20each%20piece,seeds%20determined%20by%20the%20programmer)).

### 2주차: Anchor에서 PDA(Program Derived Address) 활용 심화

- **학습 주제:** **PDA**에 대한 이해를 더욱 심화합니다. PDA는 Solana 프로그램이 서명권자 없이도 특정 계정을 **프로그램 제어 하에 생성**할 수 있게 해주는 강력한 기능입니다. 이번 주에는 PDA의 이론과 실제를 더 공부하고, Anchor로 PDA를 다루는 연습을 합니다 (예: Associated Token Account 생성 등).
- **학습 목표:** PDA가 **어떻게 생성**되고 **왜 필요한지** 이해합니다. Solana의 계정들은 기본적으로 사용자의 서명이 없으면 생성/변경이 불가능하지만, **PDA를 이용하면 프로그램이 정해진 규칙(seed)에 따라 생성한 계정에 대해 권한을 가집니다** ([What are Solana PDAs? Explanation & Examples (2025)](https://www.helius.dev/blog/solana-pda#:~:text=Solana%20programs%20,PDAs)). 예를 들어, SPL 토큰의 Associated Token Account도 PDA의 한 예입니다. Anchor에서 `#[account(init, seeds = [...], bump)]`를 사용해 PDA를 생성하고, `#[account(address = ...)]` 등의 제약으로 올바른 PDA가 들어왔는지 검증하는 패턴을 연습하세요.
- **추천 자료:**
    - (블로그) _What are Solana PDAs?_ (Helius) – PDA의 개념과 사용 사례를 알기 쉽게 설명한 글입니다 ([What are Solana PDAs? Explanation & Examples (2025)](https://www.helius.dev/blog/solana-pda#:~:text=Solana%20programs%20,PDAs)) ([What are Solana PDAs? Explanation & Examples (2025)](https://www.helius.dev/blog/solana-pda#:~:text=The%20key%20for%20each%20piece,seeds%20determined%20by%20the%20programmer)). PDAs를 키-값 저장소로 보는 관점 등 새로운 시각을 얻을 수 있습니다.
    - (튜토리얼) QuickNode 가이드 **“How to Use Program Derived Addresses”** – 간단한 Anchor 예제를 통해 PDA 생성과 사용을 보여주는 자료입니다. 직접 따라하면서 PDA 관련 Anchor 코드를 작성해보세요.
    - (공식 문서) Solana 공식 _Program Derived Address_ 문서 – PDA 생성 규칙(Ed25519 curve 상 off-curve 생성)과 `find_program_address` 함수 동작 등을 알고 싶다면 참고합니다.
- **실습:**
    - **PDA 실습:** 지난주 만든 Counter 프로그램에서 PDA를 사용했다면 잘 적용되었는지 검증합니다. 혹은 새로 간단한 실습으로, 프로그램에서 `Pubkey::find_program_address` 함수를 호출해 PDA를 구하고, 그 PDA에 데이터를 써보는 짤막한 코드를 작성합니다. (Anchor에서는 `#[account(init, seeds, bump)]`가 내부적으로 이 과정을 처리합니다.)
    - **Associated Token Account 예제:** SPL 토큰의 ATA 생성도 PDA 개념 응용입니다. Anchor에서 특정 지갑과 Mint 주소를 seeds로 하여 PDA를 구하면 해당 ATA 주소가 나옵니다. Anchor로 ATA를 생성/조회하는 코드를 한 번 참고하거나 작성해보세요 (예: `anchor_spl::token::create_associated_token_account` 함수 활용).

### 3주차: Cross-Program Invocation (CPI) 이해 및 활용

- **학습 주제:** Solana의 **CPI(Cross-Program Invocation)** 개념을 학습합니다. 하나의 Solana 프로그램이 **다른 프로그램을 호출**할 수 있는 메커니즘으로, 예를 들어 우리의 프로그램이 **토큰 프로그램**을 호출해 토큰 전송이나 계정 생성 등을 수행할 수 있습니다. 이번 주에는 Anchor에서 CPI를 사용하는 방법과 보안 고려사항을 익힙니다.
- **학습 목표:** Solana 프로그램 내에서 외부 프로그램을 호출하는 **CPI 흐름**을 이해합니다. CPI를 하기 위해서는 호출 대상 프로그램의 ID와 필요한 계정들을 인자로 제공하고, 대상 프로그램의 명령 데이터를 구성하여 Solana 런타임에 요청해야 합니다. Anchor에서는 CPI 호출을 위해 **`ctx.accounts`로부터 CPI Context를 생성**하고, Anchor가 제공하는 헬퍼 (예: `anchor_spl` crate) 등을 활용할 수 있습니다. 또한 **CPI 시 발생할 수 있는 보안 이슈** (예: 재진입 공격은 Solana에서는 없지만, CPI 남용 시 계정 검증 문제가 생길 수 있음) 에 대해서도 간략히 학습합니다.
- **추천 자료:**
    - (튜토리얼) QuickNode 가이드 **“Transfer SOL and SPL Tokens using Anchor”** – Anchor로 시스템 프로그램을 호출해 SOL 전송, 토큰 프로그램을 CPI 호출해 SPL 토큰 전송을 구현하는 예제를 제공합니다. 이를 따라 하면서 CPI의 사용법을 익히세요.
    - (공식 문서) Solana 개발 문서의 _Cross-Program Invocation_ 섹션 – CPI의 원리와 실행 과정, 그리고 중첩 CPI(call depth) 한계 등에 대해 설명합니다.
    - (Anchor 문서) Anchor에서 CPI를 할 때 `CpiContext::new`를 사용하고 `invoke` 매크로를 호출하는 방법, 또는 `anchor_spl` 등의 이용 방법을 문서나 예제 코드에서 찾아보세요.
- **실습:**
    - **시스템 프로그램 CPI:** Anchor 프로그램 내에서 Solana **시스템 프로그램**을 CPI 호출해 rent-exempt 계정을 생성하거나, lamports를 다른 계정으로 송금해보는 코드를 작성해 봅니다. (힌트: 시스템 프로그램의 `create_account` 호출에 해당하는 CPI는 Anchor에서 `system_program::CreateAccount` 구조체를 정의하고 `invoke`로 호출할 수 있습니다).
    - **토큰 프로그램 CPI:** Anchor의 `anchor_spl::token` 라이브러리를 활용하여, 내 프로그램에서 토큰 Mint를 생성하고, 임의의 사용자의 ATA로 일정 토큰을 발행(mint)하는 기능을 구현해보세요. 이는 곧 토큰 프로그램의 `MintTo` CPI 호출을 의미합니다.
    - **검증:** 위 CPI 동작들이 성공했다면, Solana Explorer나 Spl-Token-CLI 등을 통해 실제 토큰 계정에 변화가 생겼는지 확인해 봅니다.

### 4주차: Anchor 중급 기능 탐구 (에러 처리, 컨스트레인트, 이벤트 등)

- **학습 주제:** Anchor가 제공하는 기타 **편의 기능**들을 살펴봅니다. 예를 들어 **어카운트 컨스트레인트(#[account(...)] 내부 조건)**의 다양하고 강력한 사용법, **커스텀 에러 정의** 및 에러 처리 (`error_code!` 매크로), **이벤트(Event)** 시스템 (프로그램에서 이벤트를 에mitter 가능) 등을 가볍게 훑습니다. 또한 Anchor 테스트에서의 편의 기능 (예: `#[tokio::test]`와 함께 사용하는 방법)도 살펴봅니다.
- **학습 목표:** 지금까지 작성한 프로그램들을 리팩토링하거나 보완하면서 Anchor의 추가 기능들을 적용해 봅니다. 계정 컨스트레인트를 통해 **유효성 검증**을 강화하고, 잘못된 입력을 사전에 차단하는 방법을 익히세요 (예: 토큰 프로그램의 owner 검증, 데이터 길이 검증 등). 또한 프로그램에서 사용자에게 유용한 정보를 로그 외에 **이벤트**로 내보내고, 클라이언트에서 이를 수신할 수 있다는 것도 개념적으로 알아둡니다. Anchor의 에러 코드를 정의하여 가독성을 높이고, 테스트에서 해당 에러가 잘 발생하는지 검증해봅니다.
- **추천 자료:**
    - (공식 문서) Anchor _Error Handling_ 섹션 – `#[error_code]` 매크로로 에러 정의하기, `require!` 매크로로 조건 체크하기 등의 방법을 확인합니다.
    - (예제) Anchor by Example의 _Error_ 관련 예제가 있다면 참고하거나, GitHub의 Solana 프로그램 코드에서 에러 처리를 어떻게 하는지 찾아보세요.
    - (블로그) _Solana Program common errors_ 관련 정리된 글이 있다면 읽어보고, 우리가 만들었던 프로그램들에 적용할 수 있는 에러 케이스가 무엇이 있을지 생각해보세요.
- **실습:**
    - 지난주까지 작성한 카운터 또는 토큰 관련 간단한 프로그램에 **추가 컨스트레인트**를 넣어보세요. 예를 들어, Increment 함수에 잘못된 계정이 전달되었을 때 `#[account(constraint = counter_account.owner == program_id)]` 같은 체크를 추가해 본다든지, authority로 넘겨받는 계정에 `signer` 컨스트레인트를 붙여본다든지 해보세요.
    - **에러 정의:** 임의로 에러 하나를 정의하고 (`InvalidAuthority` 등), 특정 잘못된 상황에 `return err!(ErrorCode::InvalidAuthority);`를 호출해봅니다. 테스트를 통해 해당 에러가 발생하면 `.try_next_instruction_error()`로 캐치하여 제대로 처리되는지 검증해보세요.
    - **이벤트 발생:** 고급 도전과제로, Anchor 이벤트 (`#[event]` 구조체) 하나를 정의하고 `emit!()`으로 발생시켜본 후, 테스트 코드에서 이벤트를 읽어보는 것을 시도해볼 수 있습니다.

## 4개월차: Solana DApp 미니 프로젝트 #1 (예: 토큰 및 간단한 응용)

이달부터는 지금까지 배운 것을 활용하여 **작은 프로젝트**들을 진행합니다. 첫 번째 미니 프로젝트로 **토큰 및 간단 응용**을 주제로 선택합니다. 예를 들어, **커스텀 SPL 토큰 발행 및 분배 DApp**이나 **간단한 토큰 에어드롭 프로그램** 등을 만들면서, 실전 감각을 키웁니다. 이 과정을 통해 Anchor로 비교적 완결된 DApp 하나를 만드는 경험을 합니다.

### 1주차: 미니 프로젝트 #1 기획 – 토큰 프로젝트

- **학습 주제:** 만들 프로젝트의 기능을 설계하고 필요한 지식을 정리합니다. 예를 들어 “특정 조건을 만족하는 사용자에게 토큰을 보상으로 지급하는 프로그램”을 구상했다고 칩시다. 그러면 필요한 구성 요소는 커스텀 토큰(Mint), 보상 상태를 기록할 계정, 관리자를 위한 권한 계정 등이 있을 것입니다.
- **학습 목표:** 프로젝트의 **스펙을 간단히 문서화**해보세요. 어떤 계정들이 필요하고, 어떤 인스트럭션이 필요한지 목록을 만듭니다. 예) 계정: Token Mint, Vault Account(PDA, 토큰 보관용), Authority Account(보상 지급 승인자). 인스트럭션: Initialize (Mint 생성), RewardUser (특정 사용자 ATA로 일정 토큰 전송) 등. 이렇게 설계를 하면 구현이 수월해집니다. 또한 이 과정에서 혹시 모르는 개념(예: Mint 생성 방법, 메타데이터 추가여부 등)을 체크해보고 학습 계획에 반영하세요.
- **추천 자료:**
    - Solana Cookbook의 _Token_ 챕터 – SPL 토큰 관련 개념과 예시들을 정리한 자료로, 토큰 발행에 필요한 계정과 CPI 호출 내용이 잘 나와 있습니다.
    - 과거 Anchor로 만든 간단한 에어드롭/토큰 분배 프로젝트가 있는지 검색해보고 레퍼런스를 모읍니다. 비슷한 프로젝트를 참고하면 구조를 잡는 데 도움이 될 것입니다.
    - (디스커션) Solana Discord 또는 포럼에서 “token reward program”에 대해 검색하면 유사한 질문과 답변이 있을 수 있으니 참고하세요.
- **실습:** 프로젝트 설계 문서를 짧게라도 작성해 보세요 (README 등에 정리). 자신의 말로 어떤 기능을 어떤 순서로 구현할지 적어보는 것은 개발 시간을 줄여줍니다. 이 문서를 GitHub 리포지토리에 미리 만들어두고 커밋해도 좋습니다.

### 2주차: 미니 프로젝트 #1 개발 – 토큰 프로그램 구현 (Mint, 초기화)

- **학습 주제:** 프로젝트 핵심 기능 개발 시작. 먼저 **토큰 Mint 생성 및 초기화 로직**을 구현합니다. Anchor에서 `anchor_spl::token::initialize_mint` 또는 CPI를 통해 토큰 프로그램의 `InitializeMint`를 호출하여 새로운 토큰 종류를 발행합니다. 그 후 초기 공급량을 특정 계정에 발행하거나, 보상 풀 계정(PDA)에 저장해둘 수 있습니다.
- **학습 목표:** **SPL 토큰 프로그램과의 연동**을 확실하게 익히는 것이 목표입니다. 토큰 Mint를 생성하려면 몇 가지 중요한 파라미터(Decimails, authority 등)를 지정해야 하고, CPI 호출에 여러 계정 (Token Program id, Rent sysvar, System program, Mint account 등)이 필요합니다. 이러한 작업을 Anchor에서 할 때 편의를 제공하는가, 아니면 수동으로 CPI를 구성해야 하는가를 경험하면서 익히세요. 이번 주차를 마치면 “내 프로그램이 새로운 토큰을 만들어낼 수 있다”는 것을 검증하는 것이 목표입니다.
- **추천 자료:**
    - (튜토리얼) QuickNode 가이드 **“Create and Mint Fungible SPL Tokens using Anchor”** ([How to Create and Mint Fungible SPL Tokens Using Anchor | QuickNode Guides](https://www.quicknode.com/guides/solana-development/anchor/create-tokens#:~:text=Have%20you%20ever%20wanted%20to,transfer%20of%20tokens%20between%20accounts)) ([How to Create and Mint Fungible SPL Tokens Using Anchor | QuickNode Guides](https://www.quicknode.com/guides/solana-development/anchor/create-tokens#:~:text=)) – Anchor로 토큰을 생성하고, 계정 간 전송 테스트까지 수행하는 예제입니다. 거의 유사한 기능을 다루므로 큰 도움이 될 것입니다.
    - (참고 코드) Metaplex나 Spl-Token-CLI의 소스 코드를 참고하면 토큰 생성 CPI에 필요한 계정 목록을 정확히 파악할 수 있습니다 (Mint 계정 생성 -> InitializeMint CPI 순서).
    - (Anchor SPL) `anchor_spl` 크레이트 문서를 참고하여 `MintTo`, `InitializeMint` 등 래퍼 함수를 활용할 수 있는지 살펴봅니다.
- **실습:**
    1. **Mint 계정 생성:** Anchor `init`를 사용해 PDA가 아닌 새로운 계정을 생성할 수도 있습니다. 프로젝트에서 토큰 Mint 계정을 `#[account(init, payer=payer, space=82, owner=spl_token::id())]` 식으로 생성하고, 이후 CPI로 초기화하십시오.
    2. **InitializeMint CPI:** `spl_token::instruction::initialize_mint` 함수를 호출하는 CPI를 작성하거나, `token::initialize_mint` (anchor_spl) 함수를 사용해 보십시오. Decimals나 authority(pubkey) 값은 프로젝트 요구사항에 맞게 설정합니다.
    3. **검증:** `solana account <MintAddress>` CLI 명령으로 새로 생성한 Mint 계정을 조회하여, Decimals 설정과 Supply 등이 예상대로인지 확인합니다. 또는 `spl-token balance` 명령 등을 통해 토큰이 발행되었는지 확인할 수도 있습니다.

### 3주차: 미니 프로젝트 #1 개발 – 토큰 보상 로직 구현

- **학습 주제:** 프로젝트의 나머지 기능인 **보상 지급 로직**을 구현합니다. 예를 들어, 특정 트랜잭션(또는 오프체인 이벤트)에 반응해 `RewardUser` 인스트럭션이 호출되면, 우리의 프로그램이 **해당 사용자에게 일정량의 토큰을 전송**하는 기능입니다. 이를 위해 **토큰 프로그램의 Transfer 또는 MintTo CPI**를 활용합니다.
- **학습 목표:** **조건부 토큰 전송** 로직을 작성하며, 권한 제어와 안전장치를 고민해봅니다. 보상 지급은 아무나 호출할 수 없도록, `RewardUser` 인스트럭션에 적절한 **권한 계정(예: 관리자 Signer)** 검증을 넣습니다. 또한 한 번 보상한 유저에게 중복으로 주지 않도록 상태를 관리할 필요가 있다면, 보상 여부를 기록하는 계정이나 비트마스크 등을 활용해보세요. 이런 식으로 좀 더 현실적인 시나리오를 다루며 상태 관리와 비즈니스 로직 구현 능력을 향상합니다.
- **추천 자료:**
    - (예시) 기존의 에어드롭 프로그램이나 포인트 적립 프로그램 코드를 참고하면 유용합니다. 예를 들어 Solana 글로벌 해커톤에 출품된 간단한 리워드 프로그램이 GitHub에 공개돼 있다면 이를 분석해보세요.
    - (Solana Cookbook) 트랜잭션 매크로나 시스템 시간 검증 같은 고급 주제가 필요하다면 Solana Cookbook에서 관련 부분을 찾아 참고합니다 (예: **Clock Sysvar**를 이용해 일정 시간 이후에만 보상 지급 등).
    - (StackExchange) "Solana token reward once per user" 같은 키워드로 검색하면, 한 계정당 한 번만 보상 주는 로직을 어떻게 관리할지에 대한 Q&A가 있을 수 있으니 찾아봅니다.
- **실습:**
    - **RewardUser 구현:** `RewardUser(ctx, amount)` 인스트럭션을 Anchor에 추가하고, 로직에서 `anchor_spl::token::transfer` 또는 `mint_to` CPI를 사용하여 `amount` 만큼의 토큰을 보상 지급합니다. 이때 `ctx.accounts`에 필요한 계정(보상 풀 토큰 Account, 대상 유저의 ATA, 토큰 Mint, 토큰 Program 등)을 모두 포함시켜야 합니다.
    - **권한 검증:** `ctx.accounts.authority` 등을 받아와 이 계정이 미리 정한 관리자(pubkey)와 일치하는지 컨스트레인트로 확인하거나, 서명자 체크를 합니다. 의도대로 외부인이 함부로 호출 못하도록 방어합니다.
    - **중복 방지 상태:** 간단히 구현하려면, 보상시 **사용자의 ATA에 메모**를 남기는 방법(예: Memo Program CPI 호출)으로도 검증 가능하지만, 더 나아가 별도 계정에 보상 기록을 남기는 것을 고려해봅니다. (이 부분은 복잡하면 생략 가능합니다.)

### 4주차: 미니 프로젝트 #1 테스트 및 문서화

- **학습 주제:** 완성된 토큰 보상 DApp을 **테스트**하고 **문서화**합니다. 통합 테스트를 여러 케이스로 수행하여 버그를 잡고, 프로젝트의 README에 사용법과 주요 코드를 설명합니다. 또 가능하다면 간단한 **프론트엔드**나 CLI를 만들어 사용자 관점에서 DApp을 동작시켜 봅니다.
- **학습 목표:** 실전 프로젝트 마무리 단계를 경험해봅니다. 단순히 코드가 돌아가는 것에 그치지 않고, **다양한 상황에서 문제가 없는지 검증**하는 것이 중요합니다. Edge case (예: 보상 이미 받은 유저가 다시 요청, 권한 없는 유저가 호출 등)를 테스트하면서 컨트랙트가 안전하게 실패하는지 확인합니다. 문서화를 통해 스스로 프로젝트를 정리하고, 남에게 보여줄 준비를 합니다.
- **추천 자료:**
    - (테스트) Anchor 공식 문서의 _Testing_ 부분 – Rust로 Anchor 프로그램을 직접 테스트하는 법, 또는 JavaScript로 통합테스트하는 방법 등이 나와 있습니다. 이를 참고하여 우리가 만든 프로그램의 통합 테스트를 작성합니다.
    - (예제) 다른 오픈소스 Anchor 프로젝트의 README를 참고하여, 어떻게 프로젝트 개요와 사용 방법,部署 방법 등을 정리하고 있는지 벤치마킹합니다.
    - (도구) Solana Playground나 Solfare 등 UI 툴을 사용하면, 트랜잭션을 손쉽게 구성해 테스트할 수도 있습니다. 혹시 프론트엔드를 직접 개발하지 않더라도 이러한 툴로 DApp 동작을 확인해보세요.
- **실습:**
    - **테스트 코드 작성:** Anchor의 Mocha (Typescript) 테스트를 추가로 작성하거나 Rust로 `#[tokio::test]` 테스트를 작성합니다. 다양한 시나리오 (정상 시나리오, 실패 시나리오)를 모두 커버하도록 노력합니다.
    - **README 작성:** 프로젝트 소개, 사용법, 주요 개념 설명, 실행 방법(예: Devnet 배포 방법, 테스트 방법) 등을 README.md에 상세히 적습니다. 가능하면 영어와 한국어로 작성하면 좋지만, 시간상 한국어로만 작성해도 괜찮습니다.
    - **UI/CLI 시도:** 간단히 `solana program invoke` 명령어나 `solana transfer` 명령 등을 활용해 직접 트랜잭션을 보내보거나, 혹은 간단한 Node.js 스크립트를 만들어 RPC로 `RewardUser`를 호출해보세요. 실제 사용자 입장에서 제대로 동작하는지 최종 검증합니다.

## 5개월차: Solana DApp 미니 프로젝트 #2 (예: 탈중앙화 투표 애플리케이션)

두 번째 미니 프로젝트로 **탈중앙화 투표 DApp**을 개발해봅니다. 이번에는 **프로토콜 설계** 측면을 조금 다르게 해서, 여러 사용자가 참여하는 **상호작용**이 있는 프로그램을 만들어보겠습니다. 예를 들어, “좋아요(Like) 투표를 온체인에 기록하는 DApp”이나 간단한 **DAO 투표 시스템** 등을 구현할 수 있습니다. 이 프로젝트를 통해 **다중 계정 및 관계**를 다루는 능력을 향상하고, 앞서 배우지 않은 Solana의 다른 개념(예: **Sysvar**나 **렌트**)도 접해봅니다.

### 1주차: 미니 프로젝트 #2 기획 – 투표/DAO 주제

- **학습 주제:** 새로운 프로젝트의 주제를 구체화합니다. 예시 시나리오: “사용자들이 특정 게시물에 대해 ‘좋아요’를 투표하면, 스마트 컨트랙트가 투표 결과를 집계하고, 결과를 조회할 수 있게 한다”. 또는 “간단한 DAO 제안 투표 시스템: 제안을 만들고, 찬반 투표를 기록, 마감 후 결과 확정”. 이러한 시나리오를 선택하고, 필요한 기능들을 나열합니다.
- **학습 목표:** 프로젝트 #1보다 조금 더 **복잡한 상태와 상호작용**을 설계하는 것이 목표입니다. 예를 들어 투표 DApp이라면: 투표 **주제(Proposal)**를 나타내는 계정, 각 **사용자별 투표**를 추적할 계정 or 비트플래그, 투표 종료 시간 제어 등 여러 요소가 있습니다. 이러한 요소들을 어떻게 온체인에 표현할지 구상합니다. Solana의 **Sysvar_clock** 계정으로 현재 블록 타임을 가져와 투표 마감 구현하는 등의 아이디어도 고려해봅니다. 이번 프로젝트 설계 단계에서 중요한 것은 **데이터 구조**를 명확히 하는 것입니다.
- **추천 자료:**
    - (예제) Anchor by Example의 _On-chain Voting_ 예제 ([Anchor By Example - Introduction](https://examples.anchor-lang.com/#:~:text=On)) – 이미 투표 시스템 예제가 있습니다. 그것을 참고해 전체 구조(계정: Proposal, Voter 등)를 파악해보세요. 우리 프로젝트에 맞게 변형할 수 있을 것입니다.
    - (DAO 사례) 유명한 Solana DAO 프로젝트(예: Serum DAO, Realms etc.)의 간략한 소개글을 읽어보세요. 너무 복잡한 건 구현하지 않겠지만, 실제 DAO에서는 어떤 식으로 투표를 관리하는지 개념을 얻을 수 있습니다.
    - (StackExchange) “Solana voting program design” 등의 Q&A를 검색해보면, 다른 개발자들의 설계 질문과 답변을 참고할 수 있습니다.
- **실습:**
    - **DB 스키마 설계:** 투표 프로그램에서 사용할 계정들의 구조체를 설계해보고 써보세요. 예: `ProposalAccount { id, description, yes_count, no_count, ... }`, `VoteAccount { proposal_id, voter, choice }` 등. 그리고 각 인스트럭션: `CreateProposal`, `Vote`, `Finalize` 등이 필요할 것으로 정리합니다.
    - **타임라인 정하기:** 투표에 시간 제한이 있다면 Sysvar_clock를 쓸지, 아니면 입력으로 종료시각을 받을지 결정하세요. 이 부분을 어떻게 구현할지도 메모해둡니다.

### 2주차: 미니 프로젝트 #2 개발 – 투표 생성 및 투표 기능 구현

- **학습 주제:** 투표 DApp의 주요 인스트럭션인 **투표 주제 생성(CreateProposal)**과 **투표 참여(Vote)**를 구현합니다. 투표 주제를 만들 때 새로운 계정을 생성하여 Proposal 정보를 저장하고, 투표 참여시에는 각 투표자의 투표를 기록합니다. 중복 투표를 막고, 권한에 따라 투표 생성이 제한되어야 한다면 그런 로직도 구현합니다.
- **학습 목표:** 이번 프로젝트에서는 **여러 사용자의 상호작용**을 다루므로, **1인 1투표 제한** 같은 로직을 온체인으로 관리하는 법을 배우게 됩니다. 예를 들어, 이미 투표한 사용자를 추적하기 위해 ProposalAccount 안에 bitmap을 두거나 별도 VoteAccount를 둘 수 있습니다. Anchor에서 이러한 검증은 컨스트레인트나 조건문으로 구현해야 하며, 정확히 의도대로 동작하는지 테스트가 중요합니다. 또한 Proposal을 생성하거나 투표시 **수수료**(rent 등)를 누가 부담하는지도 고려합니다 (일반적으로 해당 트랜잭션 signer가 rent를 부담).
- **추천 자료:**
    - (예제) 앞서 참고한 Anchor _On-chain Voting_ 예제를 자세히 들여다보세요. Proposal과 Vote를 어떻게 관리하는지 구현을 이해하고, 필요하면 해당 코드 일부를 참고하여 작성합니다.
    - (Sysvar) Solana Sysvar Clock, Rent 등을 사용하는 방법을 공식 문서나 Solana Cookbook에서 찾아봅니다. 투표 마감 시간 비교 등에 Clock 데이터를 쓰려면 `Clock::get().unwrap().unix_timestamp`를 가져오는 식으로 사용할 수 있습니다.
    - (컨스트레인트) Anchor에서 **동적인 컨스트레인트**는 지원이 제한적일 수 있으므로, 복잡한 검증은 Rust 코드 내 조건으로 처리해야 함을 명심하세요. 이런 부분에 대한 Anchor 이슈/토론이 있는지 찾아봐도 좋습니다.
- **실습:**
    - **CreateProposal 구현:** `CreateProposal(ctx, title, description, end_time)` 등을 인자로 받아, 새로운 ProposalAccount를 `init`로 생성하고, 제안ID (PDA 사용 가능) 부여, 제목/설명 저장, 종료시각 저장 등을 합니다. 제안을 생성하는 사람을 `msg.sender` 개념으로 `ctx.accounts.proposer`로 받아두고 필요하면 저장합니다.
    - **Vote 구현:** `Vote(ctx, proposal_id, choice)`를 구현합니다. `choice`는 예를 들어 1바이트 (0=no, 1=yes)로 받고, 해당 ProposalAccount를 `mut`로 불러와 choice에 따라 yes_count/no_count를 += 1 합니다. 이때 **중복투표 체크**가 핵심인데, 간단하게는 ProposalAccount에 `Vec<Pubkey> voters` 리스트를 두고 contains 체크후 push 하는 방법을 쓸 수 있습니다. (물론 온체인에 벡터를 유지하는 건 비용 문제 있지만, 소량 데이터 가정하고 진행). 더 나은 방법은 투표별 PDA (voter별 VoteAccount)를 만들어 exists 여부로 중복 체크하는 것입니다.
    - **검증:** Anchor 테스트로 동일 유저가 두 번 Vote 호출시 에러를 리턴하는지 확인하고, 다른 두 유저가 각각 투표하면 count가 2가 되는지 등을 검증합니다.

### 3주차: 미니 프로젝트 #2 개발 – 투표 종료 및 결과 활용

- **학습 주제:** 투표의 **종료 처리(Finalize or Close)**와 **결과 조회** 기능을 구현/정리합니다. 만약 투표에 종료 시한이 있다면 그 이후에 결과를 확정짓는 `Finalize` 인스트럭션을 만들 수 있습니다. 혹은 투표 때마다 종료 여부를 체크하여 자동으로 막을 수도 있습니다. 또한 최종 투표 결과에 따라 어떤 액션을 트리거하는 시나리오(예: 과반수 이상 찬성 시 토큰 보상 지급 등)를 넣어도 좋습니다.
- **학습 목표:** **스마트 컨트랙트의 흐름 제어**를 다룹니다. 시간 조건이나 득표수 조건에 따라 분기 처리를 구현하면서, Solana 환경에서 시간은 **블록 타임**으로 확인한다는 것(SysvarClock)과, 프로그램은 외부 호출 없이는 자동실행되지 않으므로 별도의 finalize 호출이 필요할 수 있다는 것을 이해합니다. 또한 최종적으로 ProposalAccount를 **정리(close)**하여 임대비용을 반환하는 것도 고려해봅니다 (`#[account(mut, close = recipient)]`). 이 과정을 통해 Solana 프로그램에서도 **자원 해제** 개념이 있다는 것을 배우는 것이 목표입니다.
- **추천 자료:**
    - (SysvarClock 예제) StackExchange 등에 "How to use Clock in Solana program" 등의 간단한 Q&A가 있으니 참고하여 현재 시간 비교 구현을 명확히 합니다.
    - (Close 계정) Anchor 문서의 계정 관리 부분에서 `close = ...` 옵션의 효과를 복습하세요 (계정의 lamports를 돌려주고 계정 제거).
    - (비즈니스 로직) 우리 투표 DApp에서 결과를 활용한 추가 액션이 있다면, 해당 액션 (예: 토큰 지급)을 구현하기 위해 앞서 프로젝트#1의 경험을 적용합니다.
- **실습:**
    - **Finalize 구현:** `Finalize(ctx, proposal_id)`를 구현합니다. 호출 시 현재 Clock.unix_timestamp를 가져와 ProposalAccount.end_time과 비교, 아직 종료 전이면 에러를 반환합니다. 종료 후라면 ProposalAccount 상태를 `finalized = true` 같은 필드를 세팅하거나, 필요시 yes/no 결과에 따라 다른 처리를 수행합니다. 그 후 원하면 `close = proposer` 등으로 ProposalAccount를 close하여 임대비 반환 처리합니다.
    - **결과 액션:** (선택사항) 재미를 위해, 찬성이 이긴 경우 제안 올린 사람에게 토큰 보상을 지급한다든지, 반대가 이긴 경우 어떠한 기록을 남긴다든지 하는 추가 기능을 넣어봅니다. 이로써 복합적인 CPI와 로직을 한 프로그램 내에서 orchestration 해볼 수 있습니다.
    - **검증:** Anchor 테스트로 투표 종료 전 Finalize 호출 시 실패하는지, 종료 후 호출 시 통과되는지 확인합니다. 또한 이미 Finalize된 Proposal에 다시 Vote가 불가한지도 테스트하세요.

### 4주차: 미니 프로젝트 #2 검증 및 개선

- **학습 주제:** 두 번째 프로젝트를 마무리합니다. 전반적인 코드 검토와 **리팩토링/개선** 작업을 진행합니다. Solana 프로그램의 **보안 취약점 점검**도 간략히 실시합니다. 예컨대, 계정 종속 관계가 제대로 검사되고 있는지, 권한 없는 호출을 막았는지, Overflow 가능성은 없는지 등을 살핍니다.
- **학습 목표:** 작성한 코드를 **실무 수준으로 다듬는 연습**을 합니다. 의미 없는 클론이나 벡터 복사는 없는지, 계산을 off-chain으로 할 수 있는데 on-chain으로 한 부분은 없는지 생각해봅니다. 또한 **Common security pitfalls** (예: 필요한 signer 체크 빠짐, **AccountInfo 직접 사용 지양** ([anchor - What are the best practices I can do to secure my Solana smart contracts if I can't afford an audit? - Solana Stack Exchange](https://solana.stackexchange.com/questions/289/what-are-the-best-practices-i-can-do-to-secure-my-solana-smart-contracts-if-i-ca#:~:text=1.%20Try%20to%20avoid%20,it%20is%20not%20needed%20anymore)) 등)을 점검하여 수정합니다. 더불어 프로그램을 Devnet에 배포하여 실제 환경에서 여러 사용자 지갑으로 시나리오 테스트를 해보고, 발견되는 문제를 개선합니다.
- **추천 자료:**
    - (보안 체크리스트) Solana StackExchange 질문 **“Solana 스마트 계약 보안 베스트프랙틱스”**에 대한 답변을 참고합니다 ([anchor - What are the best practices I can do to secure my Solana smart contracts if I can't afford an audit? - Solana Stack Exchange](https://solana.stackexchange.com/questions/289/what-are-the-best-practices-i-can-do-to-secure-my-solana-smart-contracts-if-i-ca#:~:text=1.%20Try%20to%20avoid%20,it%20is%20not%20needed%20anymore)). 여기에는 Anchor 개발 시 유의해야 할 사항들이 정리되어 있습니다 (예: AccountInfo 대신 Account 구조체 사용, Signer 체크, Owner 체크, Rent 반환 등). 우리 코드에 해당 사항들이 적용되었는지 하나씩 점검하세요.
    - (리팩토링) Rust 클린코드 관련 자료나 블로그 (특히 Anchor context 구조 활용 팁 등)를 참고하여, 코드 가독성과 효율을 개선할 수 있는 부분을 찾아봅니다.
    - (테스트) 추가로 생각나는 edge case를 테스트해보고, 혹시 실패한다면 그 부분을 보완합니다.
- **실습:**
    - **코드 리뷰:** 스스로 각 인스트럭션 handler 함수를 검토하며, 잘못된 가정이나 취약점이 없는지 점검 체크리스트를 만들어 확인합니다. 예: 모든 #[account]에 필요한 constraint가 있는가? 데이터 길이 초과 쓰기는 없는가? 사용자의 서명이 꼭 필요한 곳에 `#[account(signer)]`를 썼는가? 등.
    - **Devnet 시나리오 테스트:** 실제 지갑 둘 이상을 동원하여 Devnet에서 하나의 Proposal에 대해 투표를 진행해봅니다. CLI 명령이나 간단한 script를 작성해 여러 트랜잭션을 순서대로 보내 보세요. 실제 환경에서 예상대로 작동하는지, state가 잘 유지되는지 확인합니다.
    - **문서화 업데이트:** README에 프로젝트#2의 내용도 추가하거나 별도의 문서로 작성합니다. 프로젝트 소개, 사용 방법 (CLI 명령 예시 등), 그리고 잠재적 개선점이나 알고리즘 설명 등을 정리해두면 좋습니다.

## 6개월차: 고급 주제 학습 (보안, 최적화, NFT 등) 및 이전 학습 복습

이달은 그동안 배운 것을 **정리하고 부족한 부분을 채우는 기간**입니다. 또한 Solana의 **NFT나 DeFi 간략한 개념**, 그리고 **보안 베스트 프랙티스** 등을 학습하여 견문을 넓힙니다. 마지막으로 중요한 건, 앞서 만든 프로젝트들을 한 번 더 돌아보며 코드 품질을 개선하고자 합니다.

### 1주차: Solana 스마트 컨트랙트 보안 모범사례 학습

- **학습 주제:** Solana 프로그램 개발 시 지켜야 할 **보안 모범사례(Best Practices)**를 정리해서 학습합니다. 이미 일부는 앞에서 다루었지만, 한 번 체계적으로 검토합니다. 예를 들어 **검증 우선 순위** (계정 공개키 검증 -> 권한 검증 -> 데이터 검증 등)나, **계정종료 시 자금 처리**, **Overflow 방지** 등의 일반적 이슈들을 점검합니다.
- **학습 목표:** 보안 사고 사례를 통해 어떤 실수가 취약점을 만드는지 인지합니다. 특히 Anchor 개발 시 자주 하는 실수와 그 예방책을 숙지하세요. 예를 들면, **AccountInfo를 직접 쓰지 않고** 가능하면 타입이 있는 Account 구조를 쓰는 것, `msg!`로 민감정보 출력하지 않기, **Signer와 Owner 체크** 철저히 하기, 불필요한 계정은 받지 않기 등입니다 ([anchor - What are the best practices I can do to secure my Solana smart contracts if I can't afford an audit? - Solana Stack Exchange](https://solana.stackexchange.com/questions/289/what-are-the-best-practices-i-can-do-to-secure-my-solana-smart-contracts-if-i-ca#:~:text=1.%20Try%20to%20avoid%20,it%20is%20not%20needed%20anymore)). 이러한 사항들을 머릿속 체크리스트로 가지고 이후 개발에 임하는 것이 목표입니다.
- **추천 자료:**
    - (블로그) Helius의 _Hitchhiker’s Guide to Solana Program Security_ – Rust/Anchor에서 발생할 수 있는 보안 이슈와 mitigations를 정리한 글입니다.
    - (정리 글) _Solana Security Best Practices_ 블로그 ([Best Solana Security Practices: A Comprehensive Guide ... - ScaleBit](https://www.scalebit.xyz/blog/post/best-solana-security-practices-guide.html#:~:text=Best%20Solana%20Security%20Practices%3A%20A,By%20following%20these)) ([anchor - What are the best practices I can do to secure my Solana smart contracts if I can't afford an audit? - Solana Stack Exchange](https://solana.stackexchange.com/questions/289/what-are-the-best-practices-i-can-do-to-secure-my-solana-smart-contracts-if-i-ca#:~:text=1.%20Try%20to%20avoid%20,it%20is%20not%20needed%20anymore)) – 개발자가 읽기 좋게 베스트프랙티스를 나열한 글을 찾아 읽습니다. 핵심 포인트들을 노트해두세요.
    - (GitHub Repo) Armani(Anchor 창시자)가 올린 보안 관련 레포지토리가 있다고 언급되니 한 번 찾아 봅니다 (예: common exploits 모음 레포) ([anchor - What are the best practices I can do to secure my Solana smart contracts if I can't afford an audit? - Solana Stack Exchange](https://solana.stackexchange.com/questions/289/what-are-the-best-practices-i-can-do-to-secure-my-solana-smart-contracts-if-i-ca#:~:text=You%20can%20check%20out%20this,recommended%20safety%20checks%20are%20given)).
- **실습:**
    - **자기 프로젝트 보안 감사:** 지난달 완성한 두 개의 미니 프로젝트의 코드를 다시 열어, 위에서 정리한 체크리스트를 적용해 봅니다. 예를 들어 AccountInfo를 쓴 곳이 있나? 필요한 signer/owner 검증이 누락된 곳은 없나? 발견되면 즉시 수정하고 테스트하세요.
    - **유닛 테스트 추가:** 보안 관련 테스트도 작성합니다. 예: 잘못된 소유자 계정을 넣었을 때 실패하는지, overflow가 일어날 만한 값을 넣어보는 테스트 등. 이를 통해 우리가 넣은 검증 로직이 잘 작동하는지 확인합니다.
    - **Audit 보고서 읽기 (선택):** 공개된 Solana 프로그램 **감사 보고서(audit report)**를 한두 개 찾아 읽어봅니다. 예: 어떤 취약점이 발견되었고 어떻게 고쳤는지 읽어보면 많은 교훈을 얻습니다.

### 2주차: Solana NFT 생태계와 메타프로그램 간략 탐색

- **학습 주제:** Solana의 **NFT**와 **메타프로그램(Metaplex)**에 대해 가볍게 공부합니다. 직접 NFT 관련 코딩을 깊게 하지는 않겠지만, Solana 개발자로서 NFT가 어떻게 구현되는지 기본은 알아두는 것이 좋습니다. Metaplex의 **Token Metadata Program**과 **Candy Machine** 개념도 알아봅니다.
- **학습 목표:** Solana에서 **NFT = 1개 발행 토큰 + 메타데이터**라는 구조를 이해합니다. Metaplex가 제공하는 표준 프로그램(예: NFT metadata 저장용 on-chain program)이 있다는 것을 알고, 필요시 우리 프로그램에서 이를 CPI 호출할 수도 있겠다는 아이디어를 가져갑니다. 또한 Candy Machine v2(대량 민팅 시스템) 작동 방식도 개략적으로 파악합니다. 이 모든 내용을 깊게 파지 않아도 되지만, **용어와 개념**을 알아두는 것이 목표입니다.
- **추천 자료:**
    - (공식 문서) Metaplex Docs – Metaplex가 정의한 NFT 표준, 토큰 메타데이터 구조, Master Edition 개념 등을 읽어봅니다.
    - (블로그/튜토리얼) _“Solana NFT 발행 튜토리얼”_ 같은 제목의 블로그나 유튜브가 많으니 10분 내외짜리를 참고합니다. NFT 생성과정을 개략적으로 파악하는 데 도움이 됩니다.
    - (Cookbook) Solana Cookbook의 NFT 섹션 – NFT 관련 계정 구성도나 코드 스니펫을 제공할 수 있으니 한 번 훑어봅니다.
- **실습:**
    - **Candy Machine 사용 체험(선택):** Metaplex의 Candy Machine CLI를 사용해서 Devnet에 1~2개의 NFT를 직접 발행해봅니다. (이건 10분 * 7일로는 부족할 수도 있으므로 가벼운 마음으로 하세요.) 이를 통해 NFT 발행자 입장의 경험을 해볼 수 있습니다.
    - **프로그램 연동 상상:** 우리가 만든 프로젝트에 NFT를 연동한다면 무얼 할 수 있을지 상상해보고, 메모해둡니다. 예를 들어 투표권을 NFT로 부여한다든지, 보상으로 NFT를 주도록 프로그램을 확장한다든지, 이런 아이디어를 적어보세요. (반드시 구현하지는 않더라도 사고실험 해보는 겁니다.)

### 3주차: Solana DeFi 프로토콜 개요 학습 (예: DEX, Lending)

- **학습 주제:** Solana에서 돌아가는 주요 **DeFi 프로토콜**들의 개념을 익힙니다. 예를 들어 Serum(Dex)의 주문서 시스템, Orca 같은 AMM, Solend 등의 Lending 프로토콜이 어떻게 동작하는지 표면적으로 공부합니다. 역시 직접 개발은 아니지만, **남들이 만든 고급 Solana 프로그램 구조**를 접해보는 것이 목적입니다.
- **학습 목표:** DeFi 프로토콜을 접함으로써 Solana 프로그램의 **확장성 있는 설계**를 배웁니다. Order Book 방식의 Serum은 계정에 주문 정보를 저장하고 중앙 한계주문서를 구현합니다. AMM은 풀 계정 두 개 토큰 잔고를 가지고 수학적 공식을 구현합니다. Lending은 담보 계정, 채무 계정 등 복잡한 구조를 가집니다. 이런 것을 큰 그림으로 이해하여, 향후 면접이나 실전에서 Solana 전문성을 보여줄 때 활용할 지식을 얻는 것이 목표입니다.
- **추천 자료:**
    - (화이트페이퍼) Serum Docs – Serum Dex의 구조 (Market, Bids, Asks, Event Queue 계정 등) 설명 읽기. 너무 자세한 수치는 몰라도 됩니다.
    - (블로그) _Solana AMM implementation_ 관련 블로그 – 간단한 Constant Product AMM을 Solana에 구현하는 예제를 다룬 글이 있다면 참고하세요.
    - (프로토콜 코드) 시간 될 때 Solend나 Mango Markets의 코드 리포지토리를 둘러보세요. 이해는 다 못해도, 프로젝트 구조와 계정 모델링을 어떻게 했는지 느껴보는 것이 중요합니다.
- **실습:**
    - **Order Book 이해도 점검:** 간단한 Q&A 형태로 스스로 정리합니다. “중앙화 거래소의 Order Book을 Solana 온체인에서 관리하려면 어떤 계정들이 필요할까?” 라고 자문해보고, Serum 사례를 떠올리며 답해봅니다.
    - **AMM 간단 계산**: 종이에 Solana상의 간단한 Swap 과정을 써보세요. 예: A/B 토큰 풀에서 A 입금, B 출금이 어떻게 계산되고 계정에 기록되는지. 이런 사고 훈련이 DeFi 이해에 도움됩니다.
    - **여담 정리:** 학습한 DeFi 개념들을 노트에 요약해둡니다 (면접 대비용으로도 활용 가능). Solana에서 이더리움과 다른 DeFi 디자인 포인트(예: Solana는 계정 수수료, 한 트랜잭션 당 여러 호출 가능 등)도 메모합니다.

### 4주차: 첫 6개월 복습 및 정리

- **학습 주제:** 지난 6개월간 배운 내용을 **전반적으로 복습**합니다. 특히 중요 개념 (**계정 모델, PDA, CPI, Anchor 기본**)은 다시 한 번 개념을 글로 정리하거나, 동료나 가상의 청중에게 설명한다는 느낌으로 정돈합니다. 또한 아직 완전히 이해가 안 된 부분이 있다면 추가 자료를 찾아 채워넣습니다.
- **학습 목표:** 처음 시작할 때에 비해 지금 얼마나 성장했는지 스스로 평가해봅니다. 그리고 남은 6개월 동안 **어떤 부분을 강화할지 계획 조정**을 합니다. 예를 들어 아직도 PDAs가 헷갈리면 다시 집중학습하거나, 특정 프로젝트의 코드가 어려웠다면 더 단순화해서 연습하거나 하는 식입니다. 복습을 통해 지식을 공고히 하고, 다음 단계(포트폴리오 프로젝트)로 넘어갈 준비를 갖추는 것이 목표입니다.
- **추천 자료:**
    - (정리 노트) 지금까지 만든 모든 노트나 코드를 한 곳에 모아보세요. 그리고 목차를 만들어 봅니다. “Solana Basics, Anchor, Project1, Project2, Advanced Topics...” 등. 이걸 기반으로 스스로 작은 위키나 블로그 글을 작성해도 좋습니다. 정리하면서 빠뜨린 부분을 발견할 수 있습니다.
    - (동영상) 유튜브에 Solana 개발 관련 정리된 영상이 있다면 시청해봅니다. 지금 보면 6개월 전에는 이해 못했던 내용도 귀에 들어올 것입니다.
    - (질문) 혹시 주변에 Solana 개발자 커뮤니티가 있다면, 질문을 하나 쯤 해보세요. 예를 들어 “Anchor로 PDA 만들 때 bump를 저장하는 이유는?” 같은 비교적 심화 질문을 던져보고 토론해보면 지식이 입체적으로 바뀝니다.
- **실습:**
    - **자기 설명 연습:** 빈 문서나 종이에 Solana의 핵심 개념들을 요약해보세요. 예: Solana 계정 vs Ethereum 계약, Anchor가 하는 일, 내가 만든 프로젝트 설명 등. 이렇게 쓰거나 말로 설명해보면 면접 대비도 되고 지식도 명확해집니다.
    - **퀴즈 풀기:** 스스로 또는 온라인에서 Solana 퀴즈를 만들어 풀어봅니다. 예를 들어 “트랜잭션에 계정을 몇 개까지 넣을 수 있는가?” 같은 세부사항까지 체크해보세요. 모르는 건 찾아서 채우면 됩니다.
    - **계획 조정:** 남은 기간에 더 투자하고 싶은 분야를 생각합니다. 예를 들어 NFT쪽 프로젝트를 하나 더 해보고 싶다거나, 아니면 DeFi 프로토콜 코드를 한 번 기여해보고 싶다거나. 후반 로드맵에 이를 반영할지 고민해봅니다.

## 7개월차: 포트폴리오 대형 프로젝트 기획 및 준비

남은 기간 중 **약 3달은 포트폴리오용 최종 프로젝트 개발**, **마지막 2~3달은 구직 준비**에 집중할 예정입니다. 이제 7개월차부터는 최종 프로젝트를 구상하고 착수합니다. 이 프로젝트는 앞선 미니 프로젝트보다 크고 복잡하며, **완성도 높게 구현**해서 실제 구직 시 어필할 주력 포트폴리오가 될 것입니다. 이번 달에는 어떤 프로젝트를 만들지 결정하고, 필요한 사전 준비를 진행합니다.

### 1주차: 포트폴리오 프로젝트 아이디어 브레인스토밍

- **학습 주제:** 어떤 주제의 프로젝트를 포트폴리오로 만들지 결정합니다. 이상적으로는 **본인이 흥미를 느끼고**, **시장에서도 의미있게 봐줄 만한** 분야가 좋습니다. 예컨대 DeFi, NFT, 게임, 인프라, 툴링 등. 앞서 두 개의 미니 프로젝트를 했으니, 포트폴리오 프로젝트는 새로운 도전을 포함하는 것이 좋습니다.
- **학습 목표:** **구체적이고 명확한 프로젝트 목표**를 수립하는 것입니다. 예를 들어 “간단한 DEX를 만들겠다”는 너무 크면, 범위를 좁혀 “두 개의 SPL 토큰 간 스왑을 지원하는 미니 AMM 구현” 정도로 구체화합니다. 또는 “NFT 경매 시장” 등. 이때 현실적으로 2~~3개월 내 구현 가능한지 판단해야 합니다 (너무 거대하면 취소해야 하므로). 아이디어를 2~~3개 정도 후보로 놓고, 실현 가능성과 흥미를 저울질하여 하나를 선정합니다.
- **추천 자료:**
    - (트렌드 파악) Solana 생태계에서 인기 있는 앱/프로토콜을 조사합니다. Solana 뉴스나 커뮤니티를 살펴보며 현재 무엇이 화두인지, 어떤 종류의 프로젝트들이 주목받는지 감을 잡습니다.
    - (해커톤 수상작) Solana 혹은 다른 L1들의 해커톤 우승작 아이디어들을 찾아보세요. 거기에 흥미로운 아이디어가 많습니다. 그런 것을 참고하여 자신만의 변형된 프로젝트로 기획할 수도 있습니다.
    - (멘토 조언) 가능하다면 Solana 개발자 커뮤니티 (디스코드 등)에 들어가 “포트폴리오로 어떤 걸 만들면 좋을까요?”라고 조언을 구해볼 수도 있습니다. 실무자들이 선호하는 난이도의 과제를 알 수도 있습니다.
- **실습:**
    - **아이디어 리스트 작성:** 하고 싶은 프로젝트 아이디어를 3개 정도 적고, 각각에 대해 개발 난이도, 필요한 기술, 차별화 포인트 등을 간략히 분석해보세요. (예: “미니 Uniswap AMM – 필요기술: PDA, 수학계산, 풀 가격 공식; 난이도: 중상; 차별화: 간단 UI도 제작” 등)
    - **결정 및 기획서 작성:** 최종 아이디어 하나를 골랐다면, 하나의 문서에 기획서를 작성합니다. 목표, 주요 기능, 필요한 스마트 컨트랙트 모듈, 필요한 프론트엔드 여부 등을 명시합니다. 이 기획서는 추후 프로젝트 진행 중 방향을 잡는 나침반이 될 것입니다.
    - **기술 조사:** 선택한 아이디어와 관련하여 추가로 공부해야 할 기술이 있다면 조사합니다. 예를 들어 “AMM을 하려면 안전한 산술 라이브러리가 필요하겠다” -> Solana safe math crate 찾기, “NFT 경매를 하려면 시간 연장 기능” -> 다른 경매 구현 사례 조사 등.

### 2주차: 프로젝트 핵심 구성요소 연구 및 프로토타이핑

- **학습 주제:** 선택한 프로젝트의 **핵심 기술적인 구성요소**를 파악하고, 가능하다면 간단한 **프로토타입**을 만들어봅니다. 예를 들어 AMM이면 **유동성 풀 계정 구조**와 **교환 로직**이 핵심이므로, 그것만 떼어서 간단히 실험해볼 수 있습니다. NFT 경매면 **입찰 로직**과 **타이머**가 핵심이겠지요. 이런 핵심 부분을 먼저 검증해보는 단계입니다.
- **학습 목표:** 프로젝트의 가장 어려운 부분을 초기에 파악하여 위험을 줄입니다. 미리 작은 프로토타입으로 테스트해보면 본 구현에서 막힐 확률을 줄일 수 있습니다. 또한 필요한 외부 라이브러리나 기존 프로토콜과의 연동 여부도 이때 결정합니다. (예: “기존 Serum 프로그램을 CPI로 호출해야 하나? 아니면 처음부터 쓸건가?” 등의 전략 결정) 이번 주 목표는 “내가 만들려는 프로젝트의 기술적 난제가 무엇인지 알고, 그것의 해결 방향을 일부 확인했다”는 상태가 되는 것입니다.
- **추천 자료:**
    - (유사 프로젝트) GitHub에서 유사한 프로젝트가 오픈소스로 공개된 게 있다면 큰 도움이 됩니다. 코드를 보며 우리의 접근법을 구체화할 수 있습니다. 없더라도 Ethereum 등의 구현을 참고할 수 있습니다 (Solidity 코드를 Rust로 포팅하는 식으로).
    - (Solana Labs/reference) Solana Labs나 Fondation에서 제공하는 참고 구현이 있는지 찾습니다. 예: AMM의 참고 구현이 Solana Labs GitHub에 있을 수 있고, 경매 컨트랙트 예시가 과거에 Solana 블로그에 올라온 적 있을 수 있습니다.
    - (수학/알고리즘) 특정 알고리즘에 자신이 없다면 (예: AMM 곡선, 경매 가격 계산 등), 이번 주에 집중 공부합니다. 관련 논문 요약이나 블로그 글을 읽어 개념을 확실히 합니다.
- **실습:**
    - **프로토타입 코드 작성:** 프로젝트 핵심 부분만 모킹하여 Anchor 프로젝트를 하나 만듭니다. 예를 들어 AMM이면 두 토큰 주고받는 최소한의 함수 하나를 만들어 시뮬레이션해보고, 슬리피지 계산 등을 검증합니다. UI나 전체 흐름은 없지만, 로우레벨로 잘 동작하는지 보는 것입니다.
    - **성능 측정(선택):** 혹시 트랜잭션 당 연산이 많아 **BPF 연산 예산**이 걱정된다면, 이 프로토타입을 `cargo build-bpf --release`로 빌드해보세요. Solana CLI로 `solana program deploy` 하지 않아도 `solana program dump` 명령 등으로 BPF 코드 사이즈나 연산량을 볼 수 있습니다. (고급 내용이므로 필요하면 시도)
    - **외부 연동 테스트:** 외부 CPI가 필요한 경우, 간단히 CPI 호출이 되는지 테스트합니다. 예: Serum DEX CPI를 써야 한다면, Serum의 program id를 불러와 dummy call (예: open orders account 생성) 해보기 등. 에러 없이 잘 호출되면 연동 가능성이 높다는 뜻입니다.

### 3주차: 프로젝트 개발 시작 – 스마트 컨트랙트 구현

- **학습 주제:** 포트폴리오 프로젝트의 본격적인 **스마트 컨트랙트 구현 단계**에 돌입합니다. Anchor 프로젝트를 세팅하고, 계정 구조, 인스트럭션을 차례로 구현합니다. 우선 **핵심 기능 위주로 우선 개발**하고 부가 기능은 이후에 추가하는 방식으로 진행합니다(즉, MVP – 최소기능제품을 먼저 만든다는 개념으로).
- **학습 목표:** 프로젝트 개발을 관리하는 능력을 기릅니다. 코드를 작성하면서 Git을 활용해 버전 관리를 하고, 커밋 메시지도 의미 있게 작성해봅니다. (면접 시 Git 커밋 히스토리도 볼 수 있으니, 깔끔하게 관리하는 습관을 들입니다.) 이번 주는 주된 기능 1~2개를 완성하는 것이 목표입니다. 또한 적절히 **단위 테스트**도 병행하여, 개발 진행 중 버그를 조기에 잡도록 합니다.
- **추천 자료:**
    - (Git 워크플로우) 효율적인 개발을 위해 GitHub 프로젝트 보드나 이슈 트래커를 사용할 수도 있습니다. 간단히 할 일 목록을 만들고 진행 상황을 가시화하면 체계적으로 진행할 수 있습니다.
    - (코드 리뷰) 작성 중인 코드를 주기적으로 스스로 리뷰하거나, 가능한 경우 다른 개발자에게 피드백을 받아보세요. Solana Discord의 개발자들에게 코드 조언을 구하는 것도 방법입니다.
    - (디버깅) Solana 프로그램 디버깅 기법 관련 자료 (예: solana-test-validator를 --detach로 돌리고 로그 확인, 또는 Anchor.toml에서 [scripts] 활용 등)을 익혀두면 개발 속도를 높일 수 있습니다.
- **실습:**
    - **코딩 & 커밋:** 예를 들어 DEX AMM 프로젝트라면, 유동성 풀 생성 및 유동성 공급 인스트럭션을 이 주에 구현하는 식으로 범위를 정하세요. 구현하면서 의미 있는 단계마다 commit & push를 합니다. (예: "Impl pool init", "Add liquidity deposit feature" 등)
    - **테스트 작성:** 주요 기능마다 Anchor 통합테스트를 작성/갱신합니다. TDD(테스트 주도 개발)까지는 아니어도, 최소한 수동으로 CLI 테스트하는 것보다 자동 테스트가 안전합니다. CI 세팅이 가능하다면 GitHub Actions로 `anchor test`를 돌려보는 것도 도전해보세요.
    - **문서 갱신:** 프로젝트 README나 설계 문서를 그때그때 업데이트합니다. 개발하면서 계획이 바뀔 수도 있으니 문서도 현실에 맞게 수정하고, 중요한 결정(예: "X 대신 Y 방식으로 구현하기로 함")들을 기록해둡니다.

### 4주차: 프로젝트 개발 – 스마트 컨트랙트 완성 및 클라이언트 연동 시작

- **학습 주제:** 스마트 컨트랙트의 남은 부분을 모두 구현하여 **기능을 완성**합니다. 그리고 **클라이언트 연동**을 준비합니다. 클라이언트는 웹 DApp이 될 수도 있고, 터미널 CLI 툴이 될 수도 있습니다. 여기서는 주로 스마트 컨트랙트 관점에서, 클라이언트가 필요한 계정과 데이터를 올바르게 전달할 수 있도록 IDL 확인, API 설계 등을 합니다.
- **학습 목표:** 스마트 컨트랙트 코드를 기능적으로 완성하고, 이전 단계까지 작성한 테스트가 모두 통과하는 상태를 이룹니다. 또한 Anchor IDL (Interface Description Language)이 자동 생성되는데, 이를 활용해 프론트엔드에서 호출할 것이므로 **IDL 구조를 이해**합니다. 클라이언트 개발은 다음 달 본격화하겠지만, 이 주에 **간단한 스크립트로 실제 컨트랙트 호출을 몇 번 해보는 것**이 목표입니다.
- **추천 자료:**
    - (Anchor IDL) Anchor IDL과 코드 생성에 관한 Anchor 문서 – 프론트엔드에서 Anchor provider와 IDL JSON을 통해 함수를 호출하는 방식을 미리 알아둡니다.
    - (Frontend 프레임워크) 만약 React + Anchor 인 경우, Solana Labs의 **@solana/web3.js**와 **@project-serum/anchor** NPM 패키지 사용법을 찾아봅니다. 예제를 따라 작은 페이지에서 우리 프로그램을 호출해볼 수 있을 것입니다.
    - (CLI) 프론트엔드 대신 Rust 기반 CLI 툴을 만들 생각이라면, Solana CLI나 solana-client crate 사용 예시를 복습합니다. Rust로 직접 RPC 호출하여 트랜잭션 만들어 보내는 방법을 익혀야 합니다.
- **실습:**
    - **모든 기능 구현 및 테스트:** 스마트 컨트랙트의 잔여 인스트럭션과 계정 구조를 모두 완성코딩합니다. 그리고 준비된 테스트 케이스를 모두 돌려 통과시키고, 추가로 엣지 케이스가 생각나면 테스트를 보강합니다. 모든 기능이 기대대로 동작하면 on-chain 부분은 일단 완성입니다. 수고했습니다!
    - **간이 클라이언트 호출:** Anchor가 생성한 IDL JSON 파일을 확인해봅니다 (`target/idl/` 경로). 그리고 JavaScript 환경에서 `@project-serum/anchor`를 써서 이 IDL을 불러와 Provider설정 후 함수 호출을 한 번 해보세요. 예를 들어 Node.js 스크립트에서 `const program = new anchor.Program(idl, programID, provider); program.rpc.myFunction(...);` 이런 식으로 호출 테스트를 합니다. 이때 wallet 키페어도 세팅해야 하니 Anchor docs의 "Using JavaScript" 부분을 참고합니다.
    - **UI 설계(준비):** 다음 달 클라이언트 개발을 염두에 두고, 어떤 화면이나 CLI 명령어 구조가 될지 구상합니다. 종이에 화면 와이어프레임을 그리거나, CLI라면 명령어 예시 (`myapp swap --amount 100 --tokenA ...`) 등을 적어봅니다. 스마트 컨트랙트가 완성되었으니 이를 가장 잘 사용할 수 있는 UX를 고민해보세요.

## 8개월차: 포트폴리오 프로젝트 완성 (클라이언트 개발 및 통합)

이달은 **프로젝트의 프론트엔드 또는 사용자 인터페이스 부분**을 개발하고, 전체 DApp을 완성하는 기간입니다. 또한 프로젝트 전체를 여러 번 통합테스트하여 **버그를 잡고 성능을 개선**합니다. 완료된 결과물은 포트폴리오로서 외부에 보일 것이므로, **UI/UX**에도 신경 써서 다듬습니다.

### 1주차: 프로젝트 클라이언트 (웹 또는 CLI) 개발

- **학습 주제:** 스마트 컨트랙트와 상호작용할 **클라이언트 어플리케이션**을 개발합니다. 웹이라면 React 등의 프레임워크를 사용해 지갑 연결(Wallet Adapter), 트랜잭션 전송 등을 구현합니다. CLI툴이라면 Rust나 Node.js로 커맨드라인 인터페이스를 구축합니다. 이 과정에서 Solana RPC와 Anchor client usage를 실제로 다루게 됩니다.
- **학습 목표:** 사용자가 우리의 프로그램을 쉽게 활용할 수 있는 인터페이스를 제공하는 것이 목표입니다. 개발자로서, 블록체인 상의 raw data를 받아와 화면에 표시하고, 사용자의 액션을 트랜잭션으로 변환해 보내는 흐름을 구현해봅니다. 이를 통해 **풀스택 블록체인 개발 경험**을 얻게 됩니다. 이번 주에는 클라이언트에서 핵심 기능 한두 개 (예: 조회 및 간단한 트랜잭션 전송)가 동작하는 상태를 만드는 것이 목표입니다.
- **추천 자료:**
    - (React + Anchor 예제) Solana 제공 DApp 예제나, Anchor 튜토리얼 중 프론트엔드 연동 부분을 참고하세요. 예를 들어 Solana Foundation의 Full-Stack 예제 ([Recommended Resource for learning Anchor - Solana Stack Exchange](https://solana.stackexchange.com/questions/3376/recommended-resource-for-learning-anchor#:~:text=,Anchor%20by%20the%20Solana%20Foundation)) ([Recommended Resource for learning Anchor - Solana Stack Exchange](https://solana.stackexchange.com/questions/3376/recommended-resource-for-learning-anchor#:~:text=,Solana%20Advance%20Development%20Course))나 Anchor 공식 튜토리얼에 React 연동 코드가 있을 수 있습니다.
    - (솔라나 월렛 어댑터) Solana Wallet Adapter GitHub – Phantom 등 지갑을 웹에서 연동하는 공식 패키지. 사용법 문서를 보고, React에 적용합니다.
    - (CLI) Rust의 `solana-client` crate 문서 – RPC 요청 (getAccountInfo, sendTransaction 등) 함수들을 복습합니다. 또한 Clap crate 등을 이용해 CLI 파싱하는 방법도 참고합니다.
- **실습:**
    - **환경 셋업:** 웹 개발의 경우 React 앱 초기 설정, Material UI나 Chakra UI 같은 컴포넌트 라이브러리 적용 등을 진행합니다. 지갑 연결 컴포넌트를 만들어 Phantom, Solflare 등으로 로그인할 수 있게 합니다. CLI 개발의 경우 `structopt` or `clap` 이용해 명령어 구조 뼈대를 만듭니다.
    - **데이터 표시:** 프로그램의 중요한 데이터 (예: AMM의 Pool 상태, 사용자 보유 토큰 잔액 등)을 클라이언트를 통해 조회하여 화면에 표시합니다. RPC의 `getProgramAccounts`나 Anchor `program.account.myAccount.fetch()` 등을 활용합니다. 이 단계에서 JSON 문자열을 파싱하고, 우리 Rust 구조체와 매칭하는 작업이 필요할 수 있습니다.
    - **트랜잭션 전송:** 클라이언트에서 버튼 클릭이나 CLI 명령으로 프로그램의 인스트럭션 하나를 호출해 봅니다. Anchor client에서는 `program.rpc.methodName(arguments, ctx)` 형태로, 또는 web3.js에서는 `new TransactionInstruction({keys, programId, data})`로 직접 만들어 전송 가능합니다. 처음엔 간단한 기능 (예: "Initialize Pool")을 실행해보고, 성공 여부를 확인합니다.

### 2주차: 클라이언트 기능 구현 및 DApp 개선

- **학습 주제:** 클라이언트의 **나머지 기능들을 모두 구현**합니다. 사용자 입력을 받아 여러 유형의 트랜잭션을 만들고, 직관적으로 사용할 수 있도록 UI/UX를 개선합니다. 또한 오류 처리와 로딩 상태 관리 등 사용자 경험을 고려한 요소를 추가합니다.
- **학습 목표:** 실제 사용하는 데 **불편함이 없는 수준의 완성도**를 갖춘 클라이언트를 만드는 것이 목표입니다. 주요 기능 (스마트 컨트랙트의 모든 기능)들을 UI에서 실행할 수 있어야 하고, 잘못된 사용에 대한 메시지나 안내가 나와야 합니다. 개발자로서는, **프론트엔드와 블록체인 백엔드의 경계**에서 발생하는 문제(예: 트랜잭션 사이즈, 지갑 승인, 네트워크 지연 등)에 대응하는 능력을 기르게 됩니다.
- **추천 자료:**
    - (UX 조언) Solana DApp 사용자로서 불편했던 점들 (예: “트랜잭션 진행중 스피너가 없어서 헷갈렸다”)을 떠올려 봅니다. 우리 앱에 그런 일이 없게 처리합니다. 혹은 다른 잘 만든 DApp (Phantom stake 페이지 등)을 사용해보고 UX를 벤치마킹합니다.
    - (최적화) 웹의 경우 React Query나 SWR을 사용해 RPC 호출 캐싱/갱신을 하면 성능이 좋아질 수 있습니다. 또는 WebSocket으로 실시간 업데이트. 이러한 고급 기법도 시간되면 적용해봅니다.
    - (테스트) 가능하면 클라이언트 측 코드도 간단한 단위 테스트를 작성해봅니다. 복잡한 로직은 아니지만, 데이터 파싱 부분 등은 테스트 가능할 수 있습니다.
- **실습:**
    - **풀기능 구현:** 남은 모든 인스트럭션들을 클라이언트에서 호출할 수 있는 버튼/폼 등을 만듭니다. 예를 들어 "Swap" 기능 구현, "Vote" 기능 구현 등. 각각에 대해 사용자가 입력해야 할 값들을 폼으로 제공하고, 제출 시 트랜잭션 생성 -> 지갑 승인 -> 전송 -> 결과 대기 -> 완료 등의 흐름을 처리합니다.
    - **에러 처리:** 트랜잭션이 실패하거나 사용자 입력 오류가 있을 경우 UI에 피드백을 줍니다. Anchor의 `ProgramError`가 프론트에 전달되면 메시지를 해석해 (“Insufficient funds” 등) 적절한 안내를 합니다. 사용자 입장에서 이해하기 쉽게 메시지를 표현하는 것이 포인트입니다.
    - **UI 다듬기:** 레이아웃이나 스타일을 개선하고, 로딩 인디케이터, 성공 알림 등을 추가합니다. 또한 앱 이름, 로고 등을 간단히 만들어 브랜드화(?)합니다. (세련된 디자인까지는 아니어도, 깔끔하고 일관된 스타일이면 충분합니다.)
    - **통합 테스트:** 실제 DApp을 자신이 사용해보며 시나리오 테스트를 합니다. 예를 들어 풀 생성 -> 유동성 공급 -> 스왑 -> 유동성 제거 -> 종료 이런 전체 흐름을 UI로 수행하고, 중간에 이상 없었는지 확인합니다.

### 3주차: 프로젝트 통합 및 최종 디버깅, 성능 개선

- **학습 주제:** 완성된 DApp을 여러 번 시나리오별로 실행해보며 **버그를 잡고 안정화**합니다. 또한 **성능이나 비용(수수료)** 측면에서 개선할 점이 없는지 점검합니다. 예를 들어 트랜잭션에서 불필요한 계정을 참조하고 있진 않은지, 계정 임대비 최적화는 잘 됐는지 등.
- **학습 목표:** 실제 배포 가능한 수준의 프로젝트를 얻는 것입니다. 이 단계에서는 새로운 기능 추가보다는 **폴리싱(polishing)** 작업에 집중합니다. 코드 주석도 정리하고, 변수명 등도 컨벤션에 맞게 수정합니다. 필요하면 간단한 **스마트 컨트랙트 최적화**도 시도합니다 (BPF 한도에는 안 걸렸는지 확인).
- **추천 자료:**
    - (최적화 가이드) Solana 공식 문서나 블로그에 _프로그램 최적화_ 관련 팁이 있다면 읽어봅니다. 예: 계정 크기 최소화, 반복문 최소화, computational budget 요청 방법 등.
    - (측정 툴) `solana program show <PROGRAM_ID>` 명령을 Devnet에서 실행하면 해당 프로그램의 데이터 사이즈와 지금까지 소비한 총 CU 등이 나옵니다. 이런걸 보면서 성능 힌트를 얻습니다. 또 `solana transaction simulate` 명령으로 특정 트랜잭션의 CU 사용량을 확인할 수도 있습니다.
    - (피드백) 프로젝트를 Solana 개발자 커뮤니티에 미리 공개하여 피드백을 받아도 좋습니다. 다른 사람들이 코드나 사용법을 보고 의견을 줄 수 있다면 반영해봅니다.
- **실습:**
    - **버그 사냥:** 남아있는 버그나 UI 글리치를 모두 잡습니다. 여러 지갑, 여러 상황에서 테스트합니다 (예: 둘 이상의 사용자로 DApp 상호작용, 네트워크를 Devnet/Mainnet 변경 테스트 등).
    - **수수료 점검:** 우리의 트랜잭션이 지나치게 많은 계정을 요구한다면 줄일 방법을 생각해봅니다. 혹은 한 트랜잭션에 너무 많은 인스트럭션을 넣어 두 번째 서명이 필요하다면 분할합니다. 계정 rent도 혹시 낭비되는 곳 없는지 확인합니다 (쓰지 않는 계정을 길게 잡았다면 space 줄이기 등).
    - **코드 정리:** 모든 스마트 컨트랙트 코드에 주석을 달아둡니다 (면접관이 코드를 볼 수도 있으므로 친절하게). README에 known issues나 한계점이 있으면 명시합니다. 클라이언트 코드도 refactor 해서 가독성을 높이고 Dead code 제거 등 청소를 합니다.

### 4주차: 프로젝트 배포 및 포트폴리오화

- **학습 주제:** 프로젝트를 **배포 및 공개**합니다. 스마트 컨트랙트를 Mainnet-beta나 공개 테스트넷에 배포할지 결정하고, 클라이언트 (웹이라면 호스팅, CLI라면 공개 리포지토리) 등을 배포합니다. 그리고 프로젝트를 포트폴리오로 포장하기 위한 작업 – 예를 들어 **시연 영상** 제작이나, **프로젝트 설명 블로그 작성** 등을 진행합니다.
- **학습 목표:** 취업 준비에 바로 활용할 수 있도록 프로젝트를 잘 포장하는 것이 목표입니다. 완성된 결과물을 **다른 사람이 쉽게 볼 수 있는 형태**로 만들어야 합니다. GitHub 리포지토리는 오픈소스로 정리하고, README에 데모 이미지나 GIF, 링크 등을 추가합니다. Mainnet에 배포하는 경우 보안에 특히 신경 써야 하므로, 가능하면 Devnet 상태로 두고 시연 영상으로 대체해도 무방합니다. 핵심은 **내가 이걸 만들었다**는 것을 증명하고 쉽게 전달하는 것입니다.
- **추천 자료:**
    - (배포 방법) Vercel이나 Netlify로 React 앱을 쉽게 호스팅할 수 있습니다. 또는 GitHub Pages 활용. CLI라면 사용법과 릴리즈 방법을 README에 쓰고, `cargo install`로 쉽게 설치 가능하게 안내합니다.
    - (프로젝트 발표) Hackathon 프로젝트 발표 영상을 몇 개 찾아보세요. 2~3분 동안 핵심을 어필하는 방법을 참고합니다. 우리도 면접 시 비슷하게 설명할 수 있도록 준비합니다.
    - (포트폴리오 정리) 온라인 포트폴리오 (개인 블로그, Devpost, LinkedIn 포트폴리오 등)에 프로젝트를 등재합니다. 가능하면 **프로젝트 소개글**을 블로그에 작성하여, 개발 동기, 기술 스택, 어려웠던 점, 캡처 화면, 결과 등을 정리합니다. 이는 면접 시 훌륭한 어필 자료가 됩니다.
- **실습:**
    - **Mainnet-beta 배포(선택):** 자신 있다면 프로그램을 Mainnet에 deploy 합니다. 단, 비용(솔라나 수수료)이 들 수 있으므로 Devnet에 유지해도 됩니다. Mainnet에 올린다면 소스코드를 immutability (upgrade authority 제거)하거나 필요한 절차를 따라 안전하게 올리세요.
    - **웹사이트/리포 오픈:** React 앱을 Vercel에 배포하고 URL을 확보합니다. GitHub 리포지토리를 public으로 전환하고, README 최상단에 배포 링크와 스크린샷 이미지를 포함합니다. 사용법도 단계별로 적어둡니다.
    - **데모 영상 녹화:** 화면 녹화 프로그램으로 DApp을 사용하는 1~2분짜리 영상을 만듭니다. 주요 기능을 빠르게 보여주고, 이를 YouTube 등 링크로 공유 가능하게 합니다. (면접 전에 면접관에게 보내면 좋습니다.)
    - **소개 자료 작성:** 블로그 포스팅이나 PDF 등으로 프로젝트 소개서를 만듭니다. **문제점->해결책->성과** 구조로 쓰면 좋습니다. 이 자료를 나중에 이력서와 함께 제출하거나, 면접 때 활용할 수 있습니다.

## 9개월차: 취업 준비 – 이력서 및 온라인 프로필 정비

이제 기술 학습과 프로젝트 개발은 완료되었습니다. 남은 기간은 **취업 활동에 집중**해야 합니다. 9개월차에는 **이력서 작성 및 온라인 프로필 정리**를 진행합니다. GitHub을 비롯해 본인의 기술 브랜딩을 강화하고, 지원할 회사 리스트업도 시작합니다.

### 1주차: 이력서 작성 (Solana 개발자 버전)

- **학습 주제:** 본인의 **기술 이력서**를 작성하거나 업데이트합니다. 기존에 Rust 개발자로서 경험이 있다면 그에 Solana 관련 역량을 추가합니다. 없다면 이번에 새로 작성합니다. **영문 이력서**도 가능한 준비하여 글로벌 포지션도 노릴 수 있게 합니다.
- **학습 목표:** 이력서 상에서 **Solana 및 스마트 컨트랙트 관련 기술 스킬셋과 프로젝트 경험이 잘 드러나도록** 하는 것이 목표입니다. 1년 경력은 짧을 수 있으나, 개인 프로젝트와 학습 내용을 강조하면 신입/주니어 Solana 엔지니어 포지션에 어필할 수 있습니다. 또한 Rust 및 백엔드 경험도 부각해서, Rust 개발자로서도 고려될 수 있게 합니다.
- **추천 자료:**
    - (이력서 예시) 인터넷에 공개된 **블록체인 개발자 이력서 샘플** ([Solana Developer Resume Sample - DevsData](https://devsdata.com/resumes/solana/solana-developer-resume-sample/#:~:text=Solana%20Developer%20Resume%20Sample%20,solutions%20and%20enhancing%20system%20performance))를 참고합니다. 솔라나 경력이 1년 미만이라도, 프로젝트 중심으로 잘 쓴 예시를 보면 도움이 됩니다.
    - (포맷) 일반적인 기술이력서 템플릿을 사용하되, Web3/블록체인 분야에 맞게 **프로젝트/해커톤 경험** 섹션을 강조하는 것이 좋습니다. 학력이나 기존 경력도 쓰되, 비중을 조절합니다.
    - (키워드) 이력서에 포함하면 좋은 **키워드**를 정리합니다. 예: "Rust", "Solana", "Anchor Framework", "Smart Contract", "Web3", "Distributed Systems", "DeFi/NFT", etc. 이러한 단어들이 어딘가 녹아있도록 합니다 (단, 의미없이 나열하지 말고 실제 경험과 연결).
- **실습:**
    - **초안 작성:** A4 1-2페이지 분량으로 이력서를 써봅니다. 중요한 섹션: 요약(한줄 자기소개), 기술스택(언어: Rust, Solidity는 부차적, 프레임워크: Anchor, etc.), 프로젝트 경험 (여기서 포트폴리오 프로젝트를 맨 위에 상세히 기술), 그리고 기타 경력/교육.
    - **다듬기:** 초안을 작성했으면, 불필요한 내용 줄이고 임팩트 있는 내용으로 교체합니다. 예를 들어 "Solana 스마트 컨트랙트 2건 개발 및 Devnet 배포, Anchor 프레임워크 사용 경험" 등의 한 줄로 핵심을 드러내고 자세한 것은 아래 프로젝트 상세에 적습니다.
    - **영문 버전:** 가능하면 영문으로도 번역해둡니다. 글로벌 크립토 회사 지원 시 바로 활용 가능합니다. 영어로 작성 시에도 명확하고 간결하게 씁니다. (필요하면 친구나 커뮤니티에 교정받기)

### 2주차: GitHub 정리 및 오픈소스 기여 정리

- **학습 주제:** 본인의 GitHub를 채워나갑니다. 이미 포트폴리오 프로젝트 코드를 올렸겠지만, README를 좀 더 보강하거나 pinned repository로 설정하는 등 **관리가 잘 된 인상**을 줍니다. 또한 그동안 공부하며 혹시라도 오픈소스에 작은 기여(PR)을 했다면 정리합니다.
- **학습 목표:** 채용 담당자가 지원자의 GitHub 프로필을 봤을 때 **활동적이고 능숙한 개발자**라는 느낌을 받도록 하는 것이 목표입니다. 이를 위해 pin할 2~3개의 대표 리포지토리를 선정하고, 각 리포에 충분한 정보(설명, 사용법)를 제공하세요. 또한 issue나 PR 기록이 있다면 볼 수 있게 공개프로필 설정합니다.
- **추천 자료:**
    - (GitHub 프로필 꾸미기) GitHub 프로필 README 기능이 있습니다. 이를 활용해 **자기소개 및 기술 스택, 프로젝트 링크** 등을 프로필에 추가하면 좋습니다. 다른 개발자들의 프로필 README를 참고해 멋지게 꾸며봅니다.
    - (Awesome Solana) 앞서 참고했던 **Awesome Solana 목록** ([Recommended Resource for learning Anchor - Solana Stack Exchange](https://solana.stackexchange.com/questions/3376/recommended-resource-for-learning-anchor#:~:text=,%E2%80%94%20a%20comprehensive%20resource%20hub))에 자신의 프로젝트를 추가 기여해볼 수도 있습니다. 그렇게 하면 커뮤니티 노출도 되고, 작은 오픈소스 컨트리뷰션으로 인정받을 수 있습니다.
    - (Git 활동) 지난 1년간의 커밋 히스토리가 그래프로 보이는데, 꾸준히 녹색 칸이 찍혀있다면 좋은 인상을 줍니다. 이미 우리는 매주 공부했으니 커밋도 했을테지만, 놓쳤다면 이제라도 주요 학습 결과물을 커밋으로 남겨 그래프를 채우세요.
- **실습:**
    - **리포지토리 정리:** 포트폴리오 프로젝트 리포지토리는 완전 공개하고, 라이센스도 적절히 명시합니다 (MIT 혹은 Apache 2.0 등). README에 데모 링크, 기능 설명, 스크린샷/GIF, 설치/사용 방법 등을 잘 정리합니다. 다른 미니 프로젝트들도 정리가 되어 있다면 pin 해둡니다.
    - **프로필 README 작성:** GitHub 아이디와 동일한 이름의 repo를 만들어 프로필 README를 작성합니다. 여기에 짧은 자기소개, 기술태그 (뱃지 아이콘 등 활용), 프로젝트 링크 모음을 넣습니다. 또한 Solana와 Rust에 관련된 키워드를 언급해 두면 좋습니다.
    - **오픈소스 PR 정리:** 혹 지난 기간 Solana 관련 오픈소스에 PR을 올렸다면 (예: Solana Cookbook에 오타 수정 PR 등 사소한 것이라도) 이를 이력서나 프로필에 언급합니다. 아직 없다면, 지금 하나 만들어봐도 좋습니다. 작은 수정이라도 Solana 생태계 리포에 컨트리뷰션 하면 눈에 띌 수 있습니다.

### 3주차: 구직 시장 연구 및 지원할 포지션 목록화

- **학습 주제:** Solana 개발자 포지션을 찾고 분석합니다. 글로벌 및 국내 채용 공고를 수집하고, 요구 역량을 파악하며, 자신이 어느 정도 부합하는지 평가합니다. 또한 회사를 리서치하여 관심도 순으로 리스트를 만듭니다.
- **학습 목표:** 지원할 곳의 **우선순위 리스트**(타겟 회사/포지션)를 작성하는 것이 목표입니다. 이를 통해 향후 지원 일정과 면접 대비 계획도 세울 수 있습니다. 또한 공고의 요구사항에 자신이 부족한 부분이 있으면 면접 전에 더 공부하거나 프로젝트에 보완할 수 있습니다.
- **추천 자료:**
    - (구직 사이트) LinkedIn Jobs, 솔라나 재단 채용 게시판, Cryptocurrency Jobs, Wanted 등 플랫폼에서 "Solana", "Rust" 키워드로 검색합니다.
    - (네트워킹) 가능하면 Solana 한국 커뮤니티, 해커톤 디스코드, 트위터 등에서 구인 글을 찾아봅니다. 스타트업의 경우 비공식적으로 채용 정보를 올리는 경우도 있습니다.
    - (직무분석) 각 공고의 자격요건을 살펴 공통 요구를 추출해봅니다. 예: Rust 경험 X년, Anchor 경험, Web3 전반 지식, 영문 커뮤니케이션, etc. 우리 이력서에 그것들을 커버했는지 검토하고, 부족하다면 면접에서 설명할 대비책을 생각합니다 (예: "X년 요구는 안 되지만 제가 Y 프로젝트에서 비슷한 역할을 했습니다" 등).
- **실습:**
    - **공고 수집:** 온라인에서 Solana/Rust 포지션 10여 개를 찾아, 스프레드시트 등에 정리합니다. 회사 이름, 직무, 요구기술, 링크 등을 기록합니다. 그리고 선호도(가고 싶은 정도)와 자신과의 매칭 정도(가능성)를 A, B, C 등급으로 분류합니다.
    - **1차 지원 대상 선정:** A등급 중 상위 3-5개를 먼저 지원 대상으로 정합니다. B, C 등급은 차후 보충. A 등급은 정말 관심있는 곳이니, 지원서/이력서를 그 회사 맞춤으로 약간 조정할 가치도 있습니다. (예: 특정 회사가 DeFi 프로젝트이면, 이력서에 DeFi 관련 학습을 강조하는 등)
    - **지원 준비:** 각 지원처마다 혹시 필요 요구사항이 있는지 확인합니다. 예: 포트폴리오 링크 요구, 커버레터 요구 등. 미리 준비 가능한 건 작성해둡니다. 또한 가능하면 지인 소개나 커뮤니티 레퍼런스를 통해 지원하면 가산점이 있을 수 있으니, 연결고리가 있는지 찾아봅니다 (예: Solana 디스코드에서 알게 된 사람이 그 회사에 있다면 살짝 조언/추천을 구해본다).

### 4주차: 모의 면접 및 기술 인터뷰 대비

- **학습 주제:** **면접 준비**를 집중적으로 합니다. 특히 기술 면접에서 받을 만한 질문들을 예상하여 연습합니다. Rust 언어에 대한 깊이 있는 질문, Solana의 작동원리, 우리가 한 프로젝트에 대한 상세 질문 등이 나올 수 있습니다. 또한 코딩 테스트가 있을 경우를 대비해 Rust로 간단한 알고리즘 문제도 풀어봅니다.
- **학습 목표:** 실제 면접에서 당황하지 않고 자신 있게 답할 수 있도록 하는 것이 목표입니다. **나만의 경험에 기반한 이야기**를 준비하세요. 예를 들어 "이 프로젝트에서 가장 어려웠던 점은 무엇이었나?" 같은 질문에 대비해 에피소드를 정리합니다. 또한 Solana의 내부 개념(예: PoH, 계정구조, rent 등)을 설명해보는 연습을 합니다. 부족한 부분이 드러나면 마지막으로 공부해서 채웁니다.
- **추천 자료:**
    - (면접 질문 리스트) Web3 및 Rust 개발 직군에서 흔히 나오는 질문들을 인터넷에서 찾아보세요. 이를 토대로 Q&A 리스트를 만들어 답변을 준비합니다.
    - (모의 면접) 지인이 있다면 부탁해서 모의 인터뷰를 진행하거나, 없으면 혼자서라도 목소리 내어 답해봅니다. 녹음하거나 녹화해서 어색한 부분이 없는지 체크합니다.
    - (시스템 디자인) 혹시 시스템 디자인 수준의 질문 (예: "NFT 마켓플레이스를 설계해본다면?")이 나올 수도 있으니, Solana 기반 시스템 아키텍처를 그려 설명하는 연습도 해봅니다. (우리 프로젝트 아키텍처 설명으로 충분할 수도 있습니다)
- **실습:**
    - **기술 Q&A 연습:** 예상 질문을 뽑아보죠. 예: "Solana 프로그램이 Ethereum 스마트 컨트랙트와 다른 점은?" – 여기에 대해 stateless 특성을 언급하며 답해봅니다 ([What is the difference between ethereum smart contracts and solana programs? - Solana Stack Exchange](https://solana.stackexchange.com/questions/10236/what-is-the-difference-between-ethereum-smart-contracts-and-solana-programs#:~:text=In%20calls%20to%20EVM%20contracts%2C,function%20that%20updates%20contract%20state)). "Anchor의 장점은?" – 우리가 느낀 바로 답하되 ([Anchor By Example - Introduction](https://examples.anchor-lang.com/#:~:text=Anchor%20is%20a%20framework%20for,quickly%20building%20secure%20Solana%20programs)), 공식 문구도 참고하면 좋습니다. "프로젝트 X에서 왜 PDA를 사용했나?" – PDA의 장점을 설명하며 ([What are Solana PDAs? Explanation & Examples (2025)](https://www.helius.dev/blog/solana-pda#:~:text=Solana%20programs%20,PDAs)) 구체 사례를 들어 말합니다. 이러한 Q&A를 10~20개 연습합니다.
    - **코딩 테스트 연습:** HackerRank나 LeetCode의 Easy/Medium 난도 문제를 2-3개 골라 Rust로 풀어보세요 (시간 제한 30분 내). 일부 회사는 일반 알고리즘 테스트를 보기도 하니, 오랜만이라면 손을 풀어두는 게 좋습니다. 특히 Rust로 풀이 시 borrow 체크 등으로 시간을 잡아먹지 않도록 미리 연습합니다.
    - **행동 면접 대비:** 기술 외에 동기나 협업 등에 대한 질문도 대비합니다. "왜 Solana를 선택했나요?", "1년간 독학하며 어떻게 어려움을 극복했나요?" 등의 질문에 자신의 진솔한 동기를 어필할 수 있게 답변을 구조화하세요. STAR 기법(상황,태스크,액션,결과)으로 답하면 좋습니다.
    - **마무리:** 면접 하루 전에는 가볍게 준비 내용을 훑고 컨디션 조절을 합니다. 블록체인 최신 이슈 (Solana 최근 업그레이드나 가격 동향 등)도 한 번 확인해, 가벼운 대화에도 대비합니다.

이렇게 1년간의 로드맵을 모두 마치게 됩니다. 매일 10분씩의 작은 노력이 모여 큰 성장을 이룬 만큼, 자신감을 가지고 취업 활동에 임하세요. **포트폴리오 프로젝트와 깊이 있는 Rust/Solana 지식**은 이미 갖추었으니, 꾸준한 학습 자세를 어필하면 좋은 결과가 있을 것입니다. 행운을 빕니다!
