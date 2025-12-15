# Discrete Random Variables and Natural Numbers

## Introduction to Discrete Random Variables

이산 확률 변수는 가산할 수 있는(countable) 값들을 취하는 확률 변수입니다. 보통 자연수나 정수와 같은 분리된 값들의 집합에서 값을 가집니다.

## Discrete vs Continuous Random Variables

### 이산 확률 변수 (Discrete Random Variables)
- 유한하거나 가산 무한한 값들을 취합니다.
- 점 질량 함수(Probability Mass Function, PMF)로 표현됩니다.
- 예: 주사위 눈금, 동전 던지기 결과, 특정 시간 동안 도착하는 고객 수

### 연속 확률 변수 (Continuous Random Variables)
- 연속적인 범위 내의 값을 가질 수 있습니다.
- 확률 밀도 함수(Probability Density Function, PDF)로 표현됩니다.
- 예: 키, 무게, 시간, 온도

## Discrete Random Variables and Natural Numbers

자연수는 이산 확률 변수를 표현하는 데 매우 중요한 역할을 합니다.

### 자연수를 값으로 갖는 이산 확률 변수

1. **계수 데이터(Count Data)**
   - 일정 시간 내 발생하는 이벤트의 수
   - 예: 하루 동안 웹사이트 방문자 수, 한 시간 동안 통화 횟수

2. **순위 데이터(Rank Data)**
   - 항목들의 순위나 순서를 나타내는 데이터
   - 예: 경주에서의 등수, 선호도 순위

3. **사이즈 데이터(Size Data)**
   - 이산적인 크기를 나타내는 데이터
   - 예: 가족 구성원 수, 아파트 방의 개수

## 주요 이산 확률 분포와 자연수

### 베르누이 분포 (Bernoulli Distribution)
- 값: 0 또는 1 (이진 결과)
- PMF: $P(X=1) = p$, $P(X=0) = 1-p$
- 응용: 동전 던지기, 합격/불합격, 성공/실패

### 이항 분포 (Binomial Distribution)
- 값: 0, 1, 2, ..., n (n번의 시행에서 성공 횟수)
- PMF: $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$
- 응용: n번의 독립적인 시행에서 성공 횟수

### 포아송 분포 (Poisson Distribution)
- 값: 0, 1, 2, ... (무한 가산)
- PMF: $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$
- 응용: 단위 시간/공간 당 발생하는 이벤트 수
- 예: 시간당 웹사이트 방문 수, 공간당 세포 수

### 기하 분포 (Geometric Distribution)
- 값: 1, 2, 3, ... (첫 성공까지의 시행 횟수)
- PMF: $P(X=k) = (1-p)^{k-1}p$
- 응용: 첫 성공까지 필요한 시도 횟수

### 음이항 분포 (Negative Binomial Distribution)
- 값: r, r+1, r+2, ... (r번째 성공까지의 시행 횟수)
- PMF: $P(X=k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}$
- 응용: r번째 성공까지 필요한 시도 횟수

## 자연수 기반 이산 확률 변수의 특성

### 가산성(Countability)
자연수는 가산 무한집합이므로, 이산 확률 변수의 값 공간을 명확하게 표현할 수 있습니다.

### 이산적 점프(Discrete Jumps)
이산 확률 변수의 누적 분포 함수(CDF)는 계단 함수 형태를 가지며, 각 자연수 값에서 불연속적인 점프가 발생합니다.

### 엔트로피(Entropy)
자연수 기반 이산 확률 변수의 엔트로피는 정보 이론에서 중요한 개념입니다:
$H(X) = -\sum_{x} P(X=x) \log P(X=x)$

## 머신러닝에서의 응용

### 분류 문제
클래스 레이블은 보통 0, 1, 2, ... 등의 자연수로 인코딩됩니다.

### 카운트 기반 모델
텍스트 분석에서의 단어 빈도, 희소 이벤트 분석 등에서 자연수 기반 이산 확률 변수가 사용됩니다.

### 강화 학습
상태 공간이 이산적일 때, 상태와 행동은 종종 자연수로 인덱싱됩니다.

## 결론

이산 확률 변수, 특히 자연수를 취하는 확률 변수는 많은 실제 현상을 모델링하는 데 필수적입니다. 데이터가 본질적으로 이산적인 경우, 적절한 이산 확률 분포를 선택하여 모델링하는 것이 중요합니다.
