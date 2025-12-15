---
id: independence_correlation_causation
aliases: []
tags:
  - probability
  - statistics
  - correlation
  - causation
  - independence
  - machine-learning
  - AI
---

# Independence, Covariance and Correlation

## Independence of Random Variables

### Definition of Probabilistic Independence

두 확률 변수 $X$와 $Y$가 독립적이라는 것은 한 변수의 결과가 다른 변수의 확률 분포에 영향을 주지 않는다는 것을 의미합니다.

수학적으로 다음과 같이 표현됩니다:
- $P(X=x, Y=y) = P(X=x) \cdot P(Y=y)$ (모든 $x, y$에 대해)
- 또는 $P(X|Y) = P(X)$ 그리고 $P(Y|X) = P(Y)$

### Properties of Independence

- 독립적인 확률 변수들의 기대값 곱은 기대값의 곱과 같습니다: $E[XY] = E[X] \cdot E[Y]$
- 독립적인 확률 변수들의 분산 합은 분산의 합과 같습니다: $Var(X + Y) = Var(X) + Var(Y)$
- 독립적인 확률 변수들의 합의 확률 분포는 각 확률 변수 분포의 합성곱입니다.

### Conditional Independence

$X$와 $Y$가 $Z$가 주어졌을 때 조건부 독립이라는 것은 다음과 같이 표현됩니다:  
$P(X=x, Y=y | Z=z) = P(X=x | Z=z) \cdot P(Y=y | Z=z)$

## Covariance

### Definition of Covariance

두 확률 변수 $X$와 $Y$ 사이의 공분산은 두 변수가 함께 어떻게 변하는지 측정합니다:

$Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$

### Properties of Covariance

- $Cov(X, X) = Var(X)$
- $Cov(X, Y) = Cov(Y, X)$
- $Cov(aX, bY) = ab \cdot Cov(X, Y)$
- $Cov(X+Z, Y) = Cov(X, Y) + Cov(Z, Y)$
- 독립적인 변수들의 공분산은 0입니다. 하지만 역은 성립하지 않습니다 (공분산이 0이라고 반드시 독립적인 것은 아님).

### Limitations of Covariance

- 공분산의 크기는 변수들의 스케일에 의존합니다.
- 공분산만으로는 관계의 강도를 비교하기 어렵습니다.
- 공분산은 비선형 관계를 포착하지 못합니다.

## Correlation Coefficient

### Pearson Correlation Coefficient

피어슨 상관계수는 공분산을 표준화하여 -1에서 1 사이의 값을 갖도록 합니다:

$\rho(X, Y) = \frac{Cov(X, Y)}{\sigma_X \sigma_Y} = \frac{Cov(X, Y)}{\sqrt{Var(X)Var(Y)}}$

### Properties of Correlation

- $-1 \leq \rho(X, Y) \leq 1$
- $\rho(X, Y) = 1$: 완벽한 양의 선형 관계
- $\rho(X, Y) = -1$: 완벽한 음의 선형 관계
- $\rho(X, Y) = 0$: 선형 관계 없음 (비선형 관계는 있을 수 있음)
- 상관계수는 선형 변환에 불변입니다: $\rho(aX+b, cY+d) = \rho(X, Y)$ (단, $a, c > 0$)

### Other Types of Correlation

- **Spearman’s Rank Correlation**: 순위 기반 비모수적 상관계수로, 비선형 관계에 민감함
- **Kendall’s Tau**: 순위 일치도를 기반으로 한 상관계수
- **Point-biserial Correlation**: 이분 변수와 연속 변수 사이의 상관관계 측정

## Correlation vs Causation

### Difference Between Correlation and Causation

- **상관관계**: 두 변수가 함께 변하는 경향이 있음을 나타냅니다.
- **인과관계**: 한 변수의 변화가 다른 변수의 변화를 직접적으로 일으킴을 의미합니다.

### Why Correlation Does Not Imply Causation

1. **Hidden Common Cause**: 제3의 변수가 두 변수 모두에 영향을 줄 수 있습니다.
2. **Coincidental Correlation**: 전혀 관련 없는 두 변수가 우연히 비슷한 패턴을 보일 수 있습니다.
3. **Reverse Causation**: 인과 방향이 실제와 반대일 수 있습니다.
4. **Non-linear Relationships**: 두 변수 간의 관계가 선형이 아닐 수 있습니다.

### Methods for Causal Inference

- **Randomized Controlled Trials (RCT)**: 인과성을 입증하는 가장 강력한 방법
- **Natural Experiments**: 외부 요인에 의해 발생한 자연적 조건을 이용한 준실험적 방법
- **Causal Inference Models**: 구조적 인과 모델, 도구 변수 등
- **Graphical Models**: 방향성이 있는 그래프로 인과관계를 표현

## Correlation in Artificial Intelligence

### AI Models Learn Correlations

대부분의 머신러닝 및 딥러닝 모델은 데이터 내의 상관관계를 학습하는 데 초점을 둡니다:

- **회귀 모델**: 입력과 출력 변수 간의 상관관계 학습
- **분류 모델**: 입력 특징과 클래스 간 관계 파악
- **비지도 학습**: 변수 간 유사성 기반 구조 학습

### Limitations in Causal Reasoning

- AI 모델은 관찰된 데이터의 상관성 기반으로 예측합니다.
- “A가 관측되면 B가 관측될 가능성이 높다”는 형태의 예측은 가능하지만,  
  “A를 바꾸면 B도 바뀐다”는 인과 질문에는 직접 답하지 못합니다.

### Causal Approaches in AI

- **Causal Graph Learning**: 데이터로부터 인과 그래프 구조 학습
- **Counterfactual Reasoning**: "만약 X가 달랐다면 Y는?"에 대한 추론
- **Domain Adaptation**: 분포가 다른 환경으로의 일반화
- **Causal Representation Learning**: 인과성을 반영한 특성 학습

## Conclusion

변수 간 관계를 이해하는 것은 통계와 AI 모두에서 핵심입니다.  
독립성, 공분산, 상관계수는 유용한 정량적 도구이지만, **상관관계와 인과관계를 혼동하지 않는 것**이 중요합니다.  
AI는 상관관계에 기반하나, 인과 추론을 통합하려는 연구는 **보다 신뢰할 수 있는 AI 시스템 개발**을 위한 중요한 단계입니다.

