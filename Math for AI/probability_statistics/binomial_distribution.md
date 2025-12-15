---
id: binomial_distribution
aliases:
  - 이항분포
  - Binomial 분포
tags:
  - probability
  - statistics
  - binomial
  - distribution
  - bernoulli
---

# Binomial Distribution

## 정의

**이항분포(Binomial distribution)** 는 **성공/실패로 나뉘는 베르누이 시행을 $n$번 독립적으로 반복했을 때**, 그 중 성공한 횟수를 나타내는 이산 확률 분포입니다.

- 시행 횟수: $n$
- 성공 확률: $p$
- 확률 변수 $X$: $n$번 시행 중 성공한 횟수
- 가능한 값: $X \in \{0, 1, 2, \dots, n\}$

---

## 수식적 표기

$$
X \sim \mathrm{Binomial}(n, p)
$$

또는:

$$
X \sim \mathrm{Bin}(n, p)
$$

---

## 확률 질량 함수 (PMF)

$$
P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad \text{where } k = 0, 1, \dots, n
$$

여기서:
- $\binom{n}{k}$는 조합 (nCk), 즉 $n$번 중 $k$번 성공할 경우의 수
- $p^k$: $k$번 성공할 확률
- $(1 - p)^{n-k}$: $n-k$번 실패할 확률

---

## 기대값과 분산

- 기대값: $E[X] = np$
- 분산: $Var(X) = np(1 - p)$

---

## 조건

- 각 시행은 **서로 독립**이다.
- 각 시행은 **동일한 성공 확률 $p$를 가진다.**

---

## 예시

- 공정한 동전을 10번 던져 앞면이 나올 횟수 $X$는 $X \sim \mathrm{Bin}(10, 0.5)$
- 어떤 제품의 불량률이 3%일 때, 100개 제품을 검사했을 때의 불량 개수 $X \sim \mathrm{Bin}(100, 0.03)$

---

## 베르누이 분포와의 관계

- 베르누이 분포는 이항분포의 특수한 경우로, $n = 1$일 때 $\mathrm{Bin}(1, p) = \mathrm{Bernoulli}(p)$

---

## 관련 분포

- $\mathrm{Bernoulli}(p)$: 단일 시행
- $\mathrm{Geometric}(p)$: 첫 성공까지 걸리는 시행 수
- $\mathrm{Poisson}(\lambda)$: $n$이 크고 $p$가 작을 때 근사

