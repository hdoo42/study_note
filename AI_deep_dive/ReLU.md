---
id: 1738157673-VSMS
aliases:
  - ReLU (Rectified Linear Unit)
tags:
  - dl
  - activation
---

# Q. What is ReLU (Rectified Linear Unit)?
### **ReLU (Rectified Linear Unit)란?**
ReLU(Rectified Linear Unit)는 신경망에서 가장 널리 사용되는 활성화 함수 중 하나로, 다음과 같이 정의된다.

$$
f(x) = \max(0, x)
$$

즉, 입력 값이 0보다 크면 그대로 유지하고, 0 이하이면 0으로 만드는 함수이다.

---

## **1. ReLU의 수학적 특성**
ReLU는 여러 가지 중요한 수학적 특성을 가진다.

### **1.1 비선형성 (Non-linearity)**
ReLU는 비선형 함수이며, 신경망에서 비선형성을 부여하여 심층 학습(deep learning)이 가능하게 한다. 단순한 선형 변환만 사용하면 신경망의 깊이가 아무리 깊어도 *단일 선형 변환과 다를 바 없기 때문에, 비선형 활성화 함수가 필수적이다.
* [[1738162050-PHWD|Explanation with examples]]

### **1.2 희소성 ([[1738162610-ZGDT|Sparsity]])**
ReLU는 음수 입력에 대해 0을 출력하므로, 일부 뉴런이 비활성화된다. 이는 뉴런의 희소성을 유도하여 모델의 계산 효율성을 높이고, 과적합(overfitting)을 방지하는 역할을 할 수 있다.

### **1.3 기울기 소실 문제(Vanishing Gradient Problem) 완화**
ReLU는 양수 영역에서 미분 값이 1이므로, 역전파 과정에서 기울기가 0으로 소실되는 문제를 줄여준다. 이는 sigmoid나 tanh와 같은 전통적인 활성화 함수와의 큰 차이점 중 하나다.

---

## **2. ReLU의 한계점**
### **2.1 Dying ReLU 문제**
입력 값이 음수일 경우 항상 0을 출력하므로, 특정 뉴런이 학습 과정에서 영구적으로 비활성화될 가능성이 있다. 이를 **Dying ReLU** 문제라고 한다.

#### **해결책**
- **Leaky ReLU**: $\max(\alpha x, x)$ (일반적으로 $\alpha \approx 0.01$)
- **Parametric ReLU (PReLU)**: $\max(a x, x)$ (여기서 $a$는 학습 가능한 파라미터)
- **ELU (Exponential Linear Unit)**: $f(x) = x$ (if $x > 0$), $f(x) = \alpha (\exp(x) - 1)$ (if $x \leq 0$)

### **2.2 비음수 평균 문제**
ReLU의 출력 값은 항상 0 이상의 값을 가지므로, 평균값이 0보다 커지면서 네트워크의 출력이 치우칠 가능성이 있다. 이를 해결하기 위해 Batch Normalization(BN)을 적용하거나, Zero-centered Activation Function을 고려할 수 있다.

---

## **3. ReLU의 활용 및 변형**
ReLU는 다양한 변형을 통해 신경망 모델에서 효율적으로 사용된다.

### **3.1 CNN(Convolutional Neural Network)에서의 활용**
CNN에서는 합성곱(convolution)과 풀링(pooling) 이후 ReLU를 적용하여 비선형성을 부여하고 특성 표현력을 증가시킨다.

### **3.2 RNN (Recurrent Neural Network)에서의 활용**
전통적인 RNN에서 ReLU를 직접 사용하면 기울기가 너무 커지거나 폭발할 가능성이 있다. 하지만 GRU나 LSTM과 같은 구조에서는 일부에서 ReLU 변형이 사용되기도 한다.

### **3.3 Transformer 및 현대적 신경망에서의 활용**
Transformer 모델에서는 일반적으로 ReLU보다는 **GELU (Gaussian Error Linear Unit)**가 더 널리 사용되지만, 기본적인 FFN (Feedforward Network) 구조에서 ReLU가 사용되기도 한다.

---

## **4. 실험적 분석**
ReLU의 성능을 평가하기 위해, 아래와 같은 실험을 수행할 수 있다.

1. **MNIST 데이터셋을 사용한 MLP(다층 퍼셉트론)에서의 ReLU 성능 평가**
2. **CNN 구조에서 Sigmoid, Tanh, ReLU 비교**
3. **Leaky ReLU와 ELU의 성능 차이 분석**
4. **Batch Normalization과 함께 사용할 경우 ReLU의 효과 분석**

이러한 실험을 통해 ReLU의 성능을 평가할 수 있으며, 특정 모델에서는 적절한 변형(ReLU, Leaky ReLU, PReLU, ELU 등)을 선택하는 것이 중요하다.

---

## **결론**
- ReLU는 심층 신경망에서 가장 널리 사용되는 활성화 함수로, 비선형성을 제공하며 기울기 소실 문제를 완화한다.
- 하지만 Dying ReLU 문제와 같은 단점이 존재하며, 이를 해결하기 위한 다양한 변형이 연구되고 있다.
- CNN과 같은 현대적인 딥러닝 모델에서 기본 활성화 함수로 사용되지만, 특정한 경우에는 다른 활성화 함수(GELU, ELU 등)로 대체될 수 있다.

이해를 더 깊이 하기 위해 ReLU의 다양한 변형을 실제 실험과 함께 분석하는 것도 추천된다.
