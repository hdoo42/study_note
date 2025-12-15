---
tags: [statistics, covariance, variance, unbiased-estimator, sample]
aliases: [표본 공분산, 분산 추정, 자유도, n-1 이유]
---

# 왜 공분산은 $n$이 아니라 $n - 1$로 나눌까?

## 개요

표본 공분산이나 표본 분산을 계산할 때, 분모로 **$n$이 아니라 $n - 1$을 사용하는 이유**는 **불편 추정([[unbiased estimation]])** 때문입니다.

---

## 1. 표본 공분산 정의

$$
s_{XY}
= \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})\,(y_i - \bar{y})
$$

이 값은 모집단 공분산 $\mathrm{Cov}(X, Y)$를 추정하기 위한 **불편 추정량**입니다.

---

## 2. 왜 $n$이 아닌가?

표본 평균 $\bar{x}, \bar{y}$는 모평균 $\mu_X, \mu_Y$를 모르는 상황에서 **대신 사용하는 추정치**입니다.  
이 평균 계산 자체가 데이터의 **자유도(degree of freedom)**를 1씩 소모하게 되므로, 전체 $n$개의 독립 정보가 아닌 **$n - 1$개의 자유도**만 남습니다.

→ 그대로 $n$으로 나누면 추정치가 **기대값보다 작아져서 편향(bias)**이 생깁니다.

---

## 3. 수식적 비교

### 분산 예시 (단일 변수)

- **불편 추정량**:  
  $$
  s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2,\quad \text{→ } E[s^2] = \mathrm{Var}(X)
  $$

- **편향된 추정량**:  
  $$
  \tilde{s}^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2,\quad \text{→ } E[\tilde{s}^2] = \left(\frac{n - 1}{n}\right)\mathrm{Var}(X)
  $$

> $E[\tilde{s}^2]$는 모집단 분산보다 항상 작기 때문에 **편향 있음**.

---

## 4. 요약

- $n$으로 나누면 **편향된 공분산/분산**이 됨
- $n - 1$은 **평균을 추정하면서 잃어버린 자유도**를 보정
- 결과적으로 $s_{XY}$는 **모집단 공분산의 기대값과 정확히 일치**

---

## 5. 관련 개념

- **불편 추정량 (Unbiased Estimator)**: 기대값이 실제 모수와 같은 추정량
- **자유도 (Degrees of Freedom)**: 독립적으로 변화할 수 있는 데이터 수
- **분산 vs 공분산**: $\mathrm{Var}(X) = \mathrm{Cov}(X, X)$

