---
id: bernoulli_distribution
aliases:
  - 베르누이 분포
  - Bernoulli 분포
tags:
  - probability
  - statistics
  - bernoulli
  - distribution
  - pmf
  - notation
---

# Bernoulli Distribution

## 정의

**베르누이 분포(Bernoulli distribution)** 는 결과가 **성공(1)** 또는 **실패(0)** 두 가지 중 하나인 단일 시행에서, 확률 변수 $X$가 취하는 분포입니다.

- $X \in \{0, 1\}$
- $P(X = 1) = p$
- $P(X = 0) = 1 - p$
- 단일 시행일 때만 해당하며, 여러 번 시행하면 이항분포(Binomial distribution)로 확장됩니다.

---

## 수식적 표기

$$
X \sim \mathrm{Bernoulli}(p) \quad \text{또는} \quad X \sim \mathrm{Ber}(p)
$$

여기서:
- $\sim$: "~을 따른다"는 의미
- $\mathrm{Bernoulli}(p)$: 성공 확률 $p$를 갖는 베르누이 분포

---

## 확률 질량 함수 (PMF)

$$
P(X = x) = 
\begin{cases}
p & \text{if } x = 1 \\\\
1 - p & \text{if } x = 0
\end{cases}
$$

또는 간단히:

$$
P(X = x) = p^x (1 - p)^{1 - x}, \quad x \in \{0, 1\}
$$

---

## 기대값과 분산

- 기대값: $E[X] = p$
- 분산: $Var(X) = p(1 - p)$

---

## 베르누이 시행 (Bernoulli Trial)

**베르누이 시행**이란 다음 조건을 만족하는 단일 실험입니다:

1. **결과는 두 가지 중 하나**이다 (성공/실패).
2. **성공 확률 $p$는 고정**되어 있다.
3. **서로 독립적인 반복이 가능**하다 (→ 이항분포로 확장 가능).

---

## 예시

- 동전을 한 번 던졌을 때 앞면(1)이 나올 확률 $p = 0.5$
- 정답률이 $0.8$인 문제를 한 번 푼 경우, 정답일 확률은 $p = 0.8$

---

## 관련 분포

- **Binomial Distribution**: $n$번 반복한 베르누이 시행
- **Geometric Distribution**: 첫 성공까지의 시행 횟수

