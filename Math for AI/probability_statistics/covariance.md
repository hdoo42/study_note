---
id: covariance
aliases:
  - 공분산
  - 共分散
tags:
  - probability
  - statistics
  - covariance
  - correlation
---

# 공분산 (Covariance)

## 정의

**공분산** 은 두 확률 변수 $X$ 와 $Y$ 가 함께 어떻게 변하는지를 나타내는 척도입니다.  
- 두 변수의 편차(평균으로부터의 차이)를 곱한 값의 기댓값으로 정의됩니다.  
- 양수이면 두 변수가 같은 방향으로, 음수이면 반대 방향으로 변하는 경향이 있음을 의미합니다.

---

## 수식

두 확률 변수 $X, Y$ 의 공분산은 다음과 같이 정의됩니다:

$$
\mathrm{Cov}(X, Y)
= E\bigl[(X - E[X])\,(Y - E[Y])\bigr]
= E[X\,Y] - E[X]\,E[Y]
$$

- $E[\cdot]$ 는 기댓값 연산자  
- $E[X\,Y]$ 는 두 변수의 곱에 대한 기댓값  
- $E[X]\,E[Y]$ 는 각 변수 기댓값의 곱

---

## 성질

1. **대칭성**:  
   $$\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y, X)$$

2. **스케일링**:  
   임의 상수 $a, b$ 에 대해  
   $$\mathrm{Cov}(aX, bY) = a\,b\;\mathrm{Cov}(X, Y)$$

3. **상관관계와의 관계**:  
   분산 $\sigma_X^2 = \mathrm{Cov}(X,X)$ 이며, 공분산을 표준화하면 상관계수(correlation coefficient)가 됩니다:  
   $$
   \rho_{X,Y}
   = \frac{\mathrm{Cov}(X, Y)}{\sigma_X\,\sigma_Y}, 
   \quad -1 \le \rho_{X,Y} \le 1
   $$

4. **독립성**:  
   만약 $X$ 와 $Y$ 가 독립이라면  
   $$\mathrm{Cov}(X, Y) = 0$$  
   그러나 역은 항상 성립하지 않습니다 (공분산 0 이 독립을 보장하지 않음).

---

## 예시

- 두 확률 변수 $X, Y$ 가 다음 분포를 가질 때:  
  $$P(X=0)=P(X=1)=0.5,\quad Y = 2X$$  
  - $E[X] = 0.5,\;E[Y] = 1$  
  - $E[XY] = E[2X^2] = 2E[X] = 1$  
  - 공분산:  
    $$
    \mathrm{Cov}(X, Y)
    = E[XY] - E[X]E[Y]
    = 1 - (0.5)(1) = 0.5
    $$

- 실험 데이터 $(x_i, y_i)$ 에 대해 표본 공분산(sample covariance)으로 추정할 때:  
  $$
  s_{XY}
  = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)
  $$  
  여기서 $\bar x, \bar y$ 는 표본 평균.

---

## 활용

- **다변량 분석**: 변수 간 선형 관계 탐색  
- **포트폴리오 이론**: 자산 수익률 간의 공분산을 이용해 리스크 평가  
- **회귀분석**: 공분산을 통해 회귀계수 계산

---

## 관련 개념

- **분산 (Variance)**: $\mathrm{Var}(X)=\mathrm{Cov}(X,X)$  
- **상관계수 (Correlation Coefficient)**: $\rho_{X,Y}$  
- **공분산 행렬 (Covariance Matrix)**: 다변량 확률 변수들의 공분산을 행렬 형태로 표현  

