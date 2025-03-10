---
id: Vanishing_Gradient
aliases:
  - Vanishing Gradient
tags:
  - dl
  - traning_dynamics
---

# Q. What is Vanishing Gradient?
### **기울기 소실(Vanishing Gradient) 문제란?**
기울기 소실(Vanishing Gradient) 문제는 딥러닝에서 신경망의 깊이가 깊어질수록 **오차 역전파(Backpropagation)** 과정에서 **기울기(Gradient)** 가 점점 작아져서 **학습이 제대로 이루어지지 않는 문제**야.

이 문제는 **시그모이드(Sigmoid), Tanh 같은 활성화 함수**를 사용할 때 특히 많이 발생해.

---

## **1. 기울기 소실 문제의 원인**
신경망의 가중치는 **역전파(Backpropagation)** 를 통해 업데이트돼. 역전파 과정은 **연쇄 법칙(Chain Rule)** 을 사용해서 오차를 **출력층에서 입력층 방향으로 거꾸로 전파**하는 방식이야.

역전파를 수식으로 보면:
$$
\frac{\partial L}{\partial W_i} = \frac{\partial L}{\partial a_n} \cdot \frac{\partial a_n}{\partial a_{n-1}} \cdot \dots \cdot \frac{\partial a_2}{\partial a_1} \cdot \frac{\partial a_1}{\partial W_i}
$$

* [[partial|Partial]](편미분)
- 여기서 **각 층의 활성화 함수의 도함수(기울기)가 곱해지면서 전파**됨.
- 만약 활성화 함수의 **도함수가 1보다 작으면** 계속 곱해질수록 **점점 작아짐**.
- 깊은 신경망에서는 결국 **기울기가 0에 가까워져서 가중치 업데이트가 거의 일어나지 않음**.

이게 **기울기 소실 문제(Vanishing Gradient Problem)** 야.

---

## **2. 기울기 소실이 발생하는 활성화 함수**
특히 **시그모이드(Sigmoid), Tanh 같은 활성화 함수**를 사용할 때 기울기 소실이 심해져.

### (1) **Sigmoid 함수**
$$
f(x) = \frac{1}{1 + e^{-x}}
$$
도함수:
$$
f'(x) = f(x)(1 - f(x))
$$
- **출력이 0 또는 1에 가까우면 기울기가 0에 가까워짐** → 기울기 소실 문제 발생.
- 깊은 신경망에서는 초기 층까지 오차가 거의 전달되지 않음.

### (2) **Tanh 함수**
$$
f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$
도함수:
$$
f'(x) = 1 - f(x)^2
$$
- **출력이 -1 또는 1에 가까우면 기울기가 0에 가까워짐**.
- 시그모이드보다는 나은 편이지만, 깊은 층에서는 여전히 기울기 소실 문제 발생.

---

## **3. 기울기 소실 문제를 해결하는 방법**
기울기 소실 문제를 해결하기 위해 **비선형 활성화 함수와 네트워크 구조를 개선**하는 여러 방법이 있어.

### ✅ **(1) ReLU (Rectified Linear Unit) 함수 사용**
$$
\text{ReLU}(x) = \max(0, x)
$$
- 도함수:
  $$
  f'(x) =
  \begin{cases} 
  1, & x > 0 \\ 
  0, & x \leq 0 
  \end{cases}
  $$
- **기울기가 0 또는 1만 되므로 기울기 소실 문제를 완화**할 수 있음.
- 다만 **x ≤ 0에서는 기울기가 0이 되어 뉴런이 죽는 문제(Dying ReLU)**가 발생할 수 있음.

### ✅ **(2) Leaky ReLU 사용**
$$
\text{Leaky ReLU}(x) =
\begin{cases} 
x, & x > 0 \\ 
\alpha x, & x \leq 0
\end{cases}
$$
- **x ≤ 0에서도 작은 기울기(보통 $\alpha = 0.01$)를 유지**하여 뉴런이 죽는 문제 해결.

### ✅ **(3) 배치 정규화(Batch Normalization) 사용**
- 입력값을 정규화(normalization)하여 **기울기가 너무 작아지지 않도록 방지**.
- 신경망이 깊어도 학습이 원활하게 진행됨.

### ✅ **(4) 가중치 초기화 방법 개선**
- `Xavier Initialization` (시그모이드, Tanh에 적합)
- `He Initialization` (ReLU, Leaky ReLU에 적합)
- 초깃값을 적절히 조정하면 깊은 층에서도 기울기가 잘 전달될 수 있음.

---

## **4. 기울기 소실과 폭발의 차이**
- **기울기 소실(Vanishing Gradient)** → 기울기가 너무 작아져서 학습이 느려지거나 안 됨.
- **기울기 폭발(Exploding Gradient)** → 기울기가 너무 커져서 학습이 불안정해짐.
- 둘 다 **딥러닝 학습을 방해하는 문제**지만, **기울기 소실**은 주로 **시그모이드, Tanh 사용 시 발생**, **기울기 폭발**은 **가중치가 너무 커질 때 발생**.

---

## **5. 결론**
- **기울기 소실 문제는 깊은 신경망에서 역전파 도중 기울기가 점점 작아져서 학습이 잘 안 되는 현상**이야.
- **Sigmoid, Tanh 같은 활성화 함수가 주요 원인**이며, 깊은 층에서 기울기가 0에 가까워짐.
- 해결 방법으로는 **ReLU 계열 활성화 함수, 배치 정규화, 적절한 가중치 초기화 기법**을 사용하면 돼.

즉, 깊은 신경망을 만들 때는 **ReLU 같은 활성화 함수를 쓰는 게 좋고, 배치 정규화도 적용하면 안정적인 학습이 가능**해!
