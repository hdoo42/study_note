---
id: Softmax
aliases:
  - Softmax
tags: []
---

# Softmax
**Softmax** 함수(softmax function)는 **로짓(logit)** 벡터(실수 벡터)를 **확률 분포**로 변환하기 위해 사용되는 함수이다. 주로 **분류(classification)** 문제에서 마지막 단계에 적용되어, 각 클래스에 해당하는 확률값을 출력한다.

---

## 1. **정의**  

길이가 $n$인 벡터 $\mathbf{z} = (z_1, z_2, \dots, z_n)$가 주어졌을 때, **Softmax** 함수**는** 아래와 같이 각 원소를 **지수 함수**(exponential)로 변환한 뒤, 그 합으로 정규화(normalize)한다.

$$
\text{Softmax}(\mathbf{z})_i 
= \frac{ e^{z_i} }{ \sum_{k=1}^{n} e^{z_k} }
,\quad i=1,\dots,n
$$

이때,  
- 분자 $[[Natural_logarithm|e]]^{z_i}$는 해당 원소의 **지수 형태**  
- 분모 $\sum_{k=1}^{n} e^{z_k}$는 모든 원소의 **지수 값 합**  
- 결과적으로 $\text{Softmax}(\mathbf{z})_i$는 $0$과 $1$ 사이의 실수가 되고, 모든 $i$에 대해 합이 1이 된다.

---

## 2. **특징 및 역할**

1. **확률 분포로 해석 가능**  
   - 모든 차원의 출력이 0 이상이며, 전체 합이 1이므로, “이 벡터는 확률분포”라고 볼 수 있다.  
   - 예: 분류 문제에서 $i$-번째 요소가 “$i$-번째 클래스일 확률”로 해석됨.

2. **지수적 강조**  
   - 원소 $z_i$가 클수록 $e^{z_i}$는 급격히 커지므로, **큰 로짓이 더 큰 확률값**을 갖는다.  
   - 미세한 차이도 지수함수로 인해 크게 확장되므로, **명확한 우세**를 갖는 클래스에 확률이 집중되는 효과가 있다.

3. **Shift Invariance**  
   - $\mathbf{z}$에 어떤 상수 $c$를 더한 벡터 $\mathbf{z}+c$에 대해 **Softmax** 값은 동일하다.  
     $$
       \text{Softmax}( \mathbf{z}+c ) 
       = \text{Softmax}( \mathbf{z} ).
     $$  
   - 즉, 로짓 벡터의 **절대값**이 아니라 **서로 간 상대적 차이**가 확률 분포에 영향을 준다.

---

## 3. **사용 예시**

1. **분류 문제(Classification)**  
   - 신경망(예: CNN, RNN, Transformer 등)의 마지막 레이어에서 각 클래스별 로짓을 만든 뒤, **Softmax**를 통해 “각 클래스가 정답일 확률”을 출력한다.

2. **Attention 기법(Scaled Dot-Product Attention 등)**  
   - Attention에서 Query-Key의 유사도를 구한 뒤, **Softmax**를 적용하여 “어느 토큰(단어)에 집중할 것인지”에 대한 **가중치**(확률)를 만든다.

3. **Reinforcement Learning**  
   - 정책(Policy)을 파라미터화할 때 행동에 대한 확률 분포를 구하기 위해 **Softmax** 함수를 쓴다.

---

## 4. **추가 수식: Logits & Temperature**

- **Logits**: $\mathbf{z}$ 자체를 “로짓”이라 부르며, 모델이 예측하는 **결정적 점수**나 **에너지**로 간주한다.  
- **Temperature($\tau$)** 파라미터:  
  $$
  \text{Softmax}_\tau(\mathbf{z})_i 
  = \frac{ e^{z_i / \tau} }{ \sum_{k=1}^{n} e^{z_k / \tau} }
  $$  
  - $\tau$가 **1보다 작으면** 확률 분포가 더 극단적으로 치우치게 되고(“sharp”해짐),  
  - $\tau$가 **크면** 분포가 고르게 퍼지게 된다.

---

## 5. **단점 및 주의사항**

1. **Overflow 문제**  
   - $\mathbf{z}$의 원소가 매우 클 경우 $e^{z_i}$ 계산에서 **수치적 overflow**가 발생할 수 있다.  
   - 실무에서는 로짓 벡터의 최댓값($\max(z)$) 등을 빼서 $\mathbf{z}$의 범위를 조정한 뒤 지수를 취하는 방식으로 해결한다.  
     $$
     \text{Softmax}(\mathbf{z})_i 
     = \frac{ e^{z_i - \max(\mathbf{z})} }{\sum_{k} e^{z_k - \max(\mathbf{z})}}
     $$
     이는 Shift Invariance 성질로 인해 값이 동일하다.

2. **Overconfidence**  
   - 네트워크가 특정 클래스의 로짓을 매우 크게 예측하면, Softmax가 **한 클래스에 확률이 몰리는** 결과를 낳을 수 있다.  
   - 이는 Uncertainty 추정 시 주의가 필요하다. (Calibration 기법 등)

---

## 정리

- **Softmax** 함수는 실수 벡터를 확률 분포로 변환해주는 핵심 도구이며,  
- 분류, Attention, 강화학습 정책 등 다양한 영역에서 활용된다.  
- 지수 함수의 특성 덕분에 **가장 높은 점수를 받은 요소**에 **확률 집중**이 일어나는 한편,  
- 수치적 안정성(Overflow)이나 **Overconfidence** 문제는 별도로 관리해야 한다.

이상으로 **Softmax** 함수에 대한 핵심 개념과 활용 방법을 살펴보았다.
