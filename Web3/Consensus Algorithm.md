---
id: consensus-algorithm
aliases:
  - Consensus Algorithm
tags:
  - blockchain
  - distributed ledger
---

# 합의 알고리즘 (Consensus Algorithm)

## 개요
합의 알고리즘은 분산 네트워크에서 각 노드가 동일한 데이터 기록을 유지하도록 하는 메커니즘입니다. 주로 블록체인에서 거래의 유효성을 검증하고 블록 생성을 조율하는 역할을 합니다.

## 주요 목표
- 안전성: 네트워크 공격에 대한 내성을 제공
- 탈중앙화: 중앙 집중식 권한 없이 모든 노드가 참여
- 확장성: 네트워크 규모 확대에도 안정적 운영 보장

## 대표적인 합의 알고리즘

### Proof of Work (PoW)
- 노드들이 복잡한 수학 문제를 풀어 경쟁적으로 블록 생성
- 높은 에너지 소모와 연산 비용이 필요하지만 보안성이 우수함
- 대표적 사례: 비트코인

### Proof of Stake (PoS)
- 노드가 보유한 암호화폐의 양(스테이크)에 따라 블록 생성 권한 부여
- 에너지 효율성이 높으며, 경제적 인센티브 제공
- 대표적 사례: 이더리움 (전환 이후)

### 기타 방식
- Delegated Proof of Stake (DPoS): 대표 노드를 선출하여 합의를 이끌어내는 방식
- Practical Byzantine Fault Tolerance (PBFT): 신뢰할 수 있는 소수의 노드 간 협의를 통해 합의 달성
- Proof of Authority (PoA): 인증된 노드가 블록을 생성하는 방식

## 작동 원리
1. 노드들이 거래를 수집하고, 유효성을 검증합니다.
2. 거래들을 하나의 블록으로 묶어 네트워크에 전파합니다.
3. 합의 알고리즘에 따라 블록의 최종 승인이 이루어지며, 블록체인에 추가됩니다.
4. 추가된 블록은 모든 노드가 동일하게 유지하여 데이터의 위·변조를 방지합니다.

## 응용 분야
- 금융 서비스: 거래 기록, 송금, 결제 시스템
- 공급망 관리: 제품의 생산 및 유통 경로 추적
- 디지털 신원: 사용자 인증 및 자산 관리

## 참고 자료
- [Proof of Work - 비트코인 위키](https://en.bitcoin.it/wiki/Proof_of_work)
- [Proof of Stake - 이더리움 문서](https://ethereum.org/ko/developers/docs/consensus-mechanisms/pos/)
- [분산 원장 기술 개요 - 위키피디아](https://ko.wikipedia.org/wiki/%EB%B6%84%EC%82%B0_%EC%9B%90%EC%9E%A5)
id: Consensus Algorithm
aliases:
  - Consensus Algorithm
tags: []
---

# Consensus Algorithm
