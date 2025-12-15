---
id: normal_distribution_two_parameters
aliases:
  - Two-Parameter Normal
  - Normal-μσ²
tags:
  - statistics
  - probability
  - normal-distribution
  - parameters
---

# Parameterization of the Normal Distribution

## Overview

정규분포는 **평균 $μ$와 분산 $σ²$ 두 값만으로 완전히 규정**됩니다.  
이 간결성 덕분에 최소한의 정보로도 실제 데이터를 효과적으로 모델링하고 해석할 수 있습니다.

---

## Why Only Two Parameters?

### Probability Density Function Revisited

정규분포 PDF는  
$f(x)=\frac{1}{\sqrt{2πσ²}}\exp\!\left(-\frac{(x-μ)²}{2σ²}\right)$  
형태입니다.  

- 위치 매개변수 $μ$는 곡선을 좌우로 이동시킵니다.  
- 스케일 매개변수 $σ$는 곡선을 늘이거나 압축합니다.  

$x$가 등장하는 모든 곳이 $(x-μ)$ 또는 $σ$로 나뉘어 있어 **추가 매개변수가 개입할 여지가 없습니다**.

### Uniqueness Proof Sketch

두 정규분포 $N_{1}(μ_1,σ_1²)$, $N_{2}(μ_2,σ_2²)$의 PDF가 동일하다면, 로그를 취해 항을 비교하면 $μ_1=μ_2$, $σ_1²=σ_2²$임이 드러납니다. **따라서 다른 두 쌍의 $(μ,σ²)$가 같은 곡선을 만들 수 없습니다.**

---

## Geometric Interpretation

- **Translation**: $X+k ∼ N(μ+k,σ²)$  
- **Scaling**: $cX ∼ N(cμ,c²σ²)$  

즉, 임의의 정규곡선은 $Z∼N(0,1)$에 위치·스케일 변환만으로 도달할 수 있습니다.

---

## Statistical Consequences

| Aspect | Implication |
|--------|-------------|
| Estimation | 표본평균 $\bar X$와 불편분산 $S²$만으로 충분통계량 성립 |
| Inference | 신뢰구간·가설검정식이 $(\bar X,S²)$에만 의존 |
| Simulation | $Z∼N(0,1)$ 생성 후 $X=μ+σZ$ 변환으로 모든 정규 샘플 생성 |
| Machine Learning | 가우시안 우도·사전분포 업데이트가 $μ,σ²$ 최적화로 단순화 |

---

## Relation to the Central Limit Theorem

중심극한정리에 의해, $n$개의 독립 변수가 있으면 그 평균의 분포가 $N(μ,σ²/n)$에 수렴합니다.  
즉, **두 매개변수**만으로도 대규모 표본 행동을 설명할 수 있습니다.

---

## Practical Example

센서 오차가 $N(0,0.01)$라면 $5\text{cm}$ 초과 오차 확률은  
$P(|X|>0.05)=2\bigl[1-Φ(0.05/0.1)\bigr]$ 입니다.  
또한 $±3σ=±0.3\text{m}$ 범위에 **99.7 %**가 포함되므로 안전 여유를 설계할 수 있습니다.

---

## Key Takeaways

- **Sufficiency**: $μ$와 $σ²$면 충분하다.  
- **Flexibility**: 어떤 벨 모양 데이터도 Affine 변환으로 $N(0,1)$과 연결된다.  
- **Efficiency**: 두 매개변수 추정만으로 계산·데이터 요구량이 최소화된다.

