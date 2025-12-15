---
id: pairwise_covariance
aliases:
  - 2차원 공분산
  - pairwise covariance
tags:
  - probability
  - statistics
  - covariance
  - pairwise
---

# 2차원 데이터의 공분산 (Pairwise Covariance)

## 데이터 구조

각 관측치는 2차원 점 $(x_i, y_i)$로 표현됩니다.  
데이터 집합:  
$$
\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}
$$

## 평균 및 중심화

각 변수의 평균:  
$$
\bar x = \frac{1}{n}\sum_{i=1}^n x_i,\quad
\bar y = \frac{1}{n}\sum_{i=1}^n y_i
$$  
중심화된 값:  
$$
x_i' = x_i - \bar x,\quad
y_i' = y_i - \bar y
$$

## 표본 공분산

두 변수 $X,Y$의 표본 공분산은 다음과 같습니다:  
$$
s_{XY}
= \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)
= \frac{1}{n-1}\sum_{i=1}^n x_i'\,y_i'
$$

- $s_{XY} > 0$: $X,Y$가 함께 증가하는 경향  
- $s_{XY} < 0$: $X,Y$가 반대 방향으로 변하는 경향  
- $s_{XY} = 0$: 선형 상관관계가 없음

## 공분산 행렬

2차원 데이터의 공분산 행렬은  
$$
\mathbf{S}
= \begin{pmatrix}
s_{XX} & s_{XY} \\[6pt]
s_{XY} & s_{YY}
\end{pmatrix}
$$  
여기서  
- $s_{XX} = \frac{1}{n-1}\sum (x_i - \bar x)^2$  
- $s_{YY} = \frac{1}{n-1}\sum (y_i - \bar y)^2$

## 시각적 해석

- 2D 평면에 점을 그렸을 때, 공분산 크기와 부호가 점들의 **분포 방향**과 **퍼짐 정도**를 나타냄  
- 공분산 행렬의 고유벡터는 데이터가 가장 크게 퍼진 방향(PCA 주성분)을 알려줌

## 예시 (Python)

```python
import numpy as np

# 예시 데이터: n x 2 배열
data = np.array([[x1, y1],
                 [x2, y2],
                 …,
                 [xn, yn]])

# 공분산 행렬 계산 (열이 변수)
cov_matrix = np.cov(data, rowvar=False)
print(cov_matrix)
```
