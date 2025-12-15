---
tags: [statistics, estimation, bias, variance, inference]
aliases: [불편 추정, Unbiased Estimator]
---

# 불편 추정량 (Unbiased Estimator)

## 정의

통계적 추정에서 **불편 추정량(unbiased estimator)** 이란,  
**표본으로부터 구한 추정치의 기대값이 해당 모수(parameter)와 정확히 일치하는 경우**를 말합니다.

수식으로는 다음과 같이 정의됩니다:

$$
\text{추정량 } \hat{\theta} \text{ 가 모수 } \theta \text{의 불편 추정량} \iff E[\hat{\theta}] = \theta
$$

---

## 예시

### 1. 평균의 불편 추정량

- 표본 평균 $\bar{X} = \frac{1}{n}\sum X_i$는 모평균 $\mu$의 불편 추정량:
  $$
  E[\bar{X}] = \mu
  $$

### 2. 분산의 불편 추정량

- **표본 분산**은 다음처럼 $n - 1$로 나눠야 **불편 추정**이 된다:

$$
s^2 = \frac{1}{n - 1} \sum_{i=1}^n (x_i - \bar{x})^2
\quad \Rightarrow \quad E[s^2] = \sigma^2
$$

- 반면 $n$으로 나누면:
  $$
  \tilde{s}^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 \Rightarrow E[\tilde{s}^2] = \frac{n - 1}{n} \sigma^2
  $$

→ 기대값이 실제 분산보다 작음 → **편향(bias) 존재**

---

## 편향(Bias)란?

추정량 $\hat{\theta}$의 **기대값과 실제 모수 $\theta$의 차이**:

$$
\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta
$$

- 불편 추정량은 $\text{Bias} = 0$
- 편향이 있더라도 분산이 낮으면 유용할 수 있음 → **편향-분산 트레이드오프** 이슈로 이어짐

---

## 불편 vs. 일치성 (Consistency)

- 불편 추정량은 항상 좋은가? → 꼭 그렇지는 않음
- **일치 추정량**은 $n \to \infty$일 때 모수에 수렴하는 추정량
- 많은 경우 불편성보다 **일치성**이 더 중요

---

## 요약

| 용어 | 정의 |
|------|------|
| 불편 추정량 | 기대값이 정확히 모수와 같은 추정량 |
| 편향 (bias) | $E[\hat{\theta}] - \theta$ |
| 표본 평균 | 평균 $\mu$의 불편 추정량 |
| 표본 분산 ($n-1$ 분모) | 분산 $\sigma^2$의 불편 추정량 |
| $n$ 분모 사용 | 편향된 분산 추정량 → 기대값이 작음 |

---

## 관련

- [표본 분산과 $n - 1$의 이유](why_divide_by_n_minus_1_covariance)
- [표본 공분산](covariance_and_correlation)
- [편향-분산 트레이드오프](bias_variance_tradeoff)
