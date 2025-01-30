---
id: main
aliases: []
tags: []
---
# 1.1 딥러닝 모델 학습이 잘 되는 이유
## Q. What is no free lunch in context of optimization?
The **No Free Lunch (NFL) theorem** in optimization states that no single optimization algorithm is universally better than all others across all possible problems. This means that for any optimization algorithm, its performance is **problem-dependent**, and an algorithm that works well for one type of problem may perform poorly on another.

### Key Implications:
1. **No universally best optimizer**  If an algorithm performs better than another on some problems, there must be other problems where it performs worse.
2. **Problem-specific tuning**  Optimization methods must be tailored to the structure of the problem being solved.
3. **Trade-offs are inevitable**  Choosing an algorithm requires considering the nature of the problem, computational resources, and other constraints.

This principle is particularly relevant in **machine learning, heuristic search, and evolutionary algorithms**, where different methods excel in different domains.

---

## Q. What is inductive bias
**Inductive bias** refers to the assumptions a learning algorithm makes to generalize from limited training data to unseen data. Since learning from finite data is inherently underdetermined (many hypotheses can fit the same data), an algorithm needs some built-in preferences to favor one generalization over another.

### Key Aspects of Inductive Bias:
1. **Assumptions about the hypothesis space**: The learner assumes a certain structure in the data, like linear separability in linear regression.
2. **Regularization**: Techniques like L1/L2 regularization in machine learning impose constraints to prevent overfitting.
3. **Prior Knowledge**: Human-designed biases, such as convolutional neural networks (CNNs) assuming spatial locality in images.
4. **Bias-Variance Tradeoff**: A strong bias reduces the search space but may oversimplify the problem (high bias, low variance), while weak bias allows flexibility but risks overfitting (low bias, high variance).

In essence, **inductive bias is what allows a model to generalize, but it also limits what it can learn**. The choice of bias determines how well a model can perform on different types of tasks.

---

## 1. 다항식 근사와 신경망

### 1.1 다항식 근사가 잘 된다는 말의 의미
신경망(특히 다층 퍼셉트론)은 *“범용 근사(Universal Approximation)”* 성질을 가진다고 알려져 있습니다. 이는 **충분히 많은 뉴런(은닉층 노드)과 적절한 활성화 함수**가 있다면, 임의의 연속 함수(예: 다항식, 지수함수 등)를 원하는 정밀도로 근사할 수 있다는 이론적 결과입니다.

- **다항식**은 $x^2, x^3, x^7 + 3x^5 - 2x + 1$ 같은 식의 유한항 다항 표현입니다.
- 신경망은 **가중치(Weight)** 와 **편향(Bias)** 를 조정해 가며, 활성화 함수를 통해 *“비선형 변환”* 을 쌓습니다.
- 이때, 다항식 정도의 함수를 근사하는 데에는 매우 복잡한 구조가 요구되지 않습니다. 비교적 “작은” 신경망이라도, 가중치와 편향을 잘 학습하면 **낮은 차수의 다항식**을 충분히 잘 흉내낼 수 있게 됩니다.

정리하면, **낮은 차수의 다항식은 형태가 단순하기 때문에** 일반적인 범용 근사 능력을 갖춘 신경망으로 비교적 쉽게(은닉층 노드 수가 많지 않아도) 근사할 수 있다는 뜻입니다.

---

## 2. 곱셈 연산의 신경망 표현

### 2.1 “곱셈 한 번”을 뉴런 4개로 근사한다?
두 입력 $x$와 $y$가 있을 때, 이 둘의 **곱$x \times y$** 을 계산하는 함수를 “아주 작은 신경망”으로 근사할 수 있다는 데에는 다음과 같은 원리가 작동합니다.

1. **신경망의 기본 연산**  
   - 각 뉴런은 (1) 여러 입력을 받아서 **가중합(Weighted Sum)** 을 구하고, (2) 활성화 함수를 통과시킵니다.  
   - 예: $\text{출력} = \sigma(w_1 x + w_2 y + b)$, 여기서 $\sigma$는 ReLU나 시그모이드 같은 활성화 함수.

2. **곱셈의 ‘형태’를 분해**  
   - 곱셈은 $(x+y)^2 = x^2 + 2xy + y^2$ 같은 항들을 포함하거나, 논리 연산 관점에서 보면 ‘AND’와 유사한 특성이 있습니다(두 값이 클 때 결과가 크다).
   - 적절한 수의 뉴런과 가중치 조합을 통해, ‘부분적으로 곱셈을 흉내내는 형태’(예: $x+y$, $|x-y|$, $x^2$, $y^2$ 등)를 만들어내고, 이들을 다시 조합해서 최종 출력이 $xy$처럼 보이도록 할 수 있습니다.

3. **작은 신경망으로도 충분**  
   - 이론적으로 곱셈 함수는 단순히 2차 다항식($xy$는 2차 항이죠) 중 하나입니다.  
   - 4개 뉴런(또는 그와 유사한 규모)의 은닉층 구조를 갖춘 2층 신경망(입력층-은닉층-출력층)에서도, 적절한 가중치와 편향을 찾으면 곱셈을 근사하는 것이 가능합니다.  
   - 특히 ReLU(렐루)나 시그모이드, 탄젠트H 등 *적당한 비선형 활성화 함수*를 사용하면, 4개 안팎의 은닉 뉴런만으로도 $xy$를 매우 정확하게 모사할 수 있다는 것이 여러 연구 및 예시로 알려져 있습니다.

### 2.2 간단 예시(개념적 스케치)
예를 들어, 다음과 같은 과정을 상상해볼 수 있습니다(수학적 정확도보다는 ‘어떻게 근사하는지’ 개념 이해 목적):
1. 은닉 뉴런 1번: $\max(0, x + y)$ 같은 형태(ReLU 가정 시).
2. 은닉 뉴런 2번: $\max(0, x - y)$ 같은 형태.
3. 은닉 뉴런 3번: $\max(0, -x + y)$ 같은 형태.
4. 은닉 뉴런 4번: $\max(0, -(x + y))$ 같은 형태.

이런 식으로 **입력값들의 합, 차, 음수** 등 여러 조합을 만들고, 다시 *출력층에서 가중 합*을 통해 적절히 더하거나 빼 주면, 결과를 $xy$와 흡사하게 만들 수 있습니다. 실제로는 좀 더 정교한 가중치와 편향 설정이 필요하지만, *“곱셈이라는 연산을 여러 부분함수로 쪼개어 근사”*한다는 아이디어입니다.

---

## 3. 왜 가능한가? (직관적·대학생 수준 요약)

1. **비선형 조합의 힘**  
   - 신경망 한 층에서 **선형 조합**(가중치 합)을 만든 뒤, **비선형 활성화 함수**를 통과시키고, 이것을 여러 번 반복하면, *선형 방정식만으로는 표현할 수 없는 복잡한 함수*를 만들 수 있습니다.  
   - 곱셈 $xy$는 선형이 아닌 연산이지만, 충분한 수의 “선형→비선형” 조합 레이어가 있으면 근사 가능.

2. **곱셈 자체가 2차 다항식의 핵심 항**  
   - $x \times y$는 2변수 2차식 중 한 항이므로, 부분적으로 **다항식 근사** 이론 안에 들어갑니다.  
   - 그 결과, “작은” 네트워크로도 곱셈 함수를 근사할 수 있습니다.

3. **범용 근사 정리(Universal Approximation Theorem)**  
   - 간단히 말해, 신경망은 충분한 은닉 뉴런과 적당한 활성화 함수를 갖출 경우 **연속 함수**를 원하는 만큼 정밀하게 근사할 수 있습니다.  
   - *곱셈*은 연속 함수이고, 다항식의 일부이므로, 이를 잘 구현할 수 있는 최소 뉴런 수를 찾을 수 있으며, 그 수가 이론적으로 4개 정도면 된다(혹은 그 이하로도 가능하다는 연구)고 알려져 있습니다.

---

## 4. 요약

- **낮은 차수의 다항식**은 형태가 단순하기 때문에, 일반적인 다층 신경망으로 쉽게(적은 뉴런만으로도) 근사할 수 있습니다.  
- 특히 **곱셈 $xy$** 같은 2차항은 2층 네트워크(은닉층 1개)에 *4개 정도*의 은닉 뉴런을 써도 충분히 근사할 수 있다는 것이 알려져 있습니다.  
- 이는 신경망이 단순 합·차·활성화 함수를 적절히 조합해서 *곱셈 연산을 모방*할 수 있기 때문이며, 범용 근사 정리가 이론적 뒷받침을 합니다.

이렇게 이해하면,  
1. “왜 낮은 차수 다항식을 신경망으로 잘 표현할 수 있는지” → *다항식은 신경망으로 근사하기가 상대적으로 쉽다.*  
2. “왜 단순 곱셈조차도 뉴런 몇 개만 있으면 시뮬레이션 가능한지” → *곱셈은 2차항이며, 간단한 구조(은닉 뉴런 4개 내외)로도 근사할 수 있다.*  

라는 점을 대학생 수준에서 수긍할 수 있게 됩니다.

[[XOR_example|XOR implement with neural network]]

---

여기 주요 어휘들을 영어로 정리해 줄게.  

### **신경망 관련 용어**  
- 신경망 → **Neural Network**  
- 뉴런 → **Neuron**  
- 은닉층 → **[[1738147006-OJEO|Hidden Layer]]**  
- 은닉뉴런 → **[[1738147174-YSNO|Hidden Neouron]]**  
- 가중치 → **Weight**  
- 편향 → **Bias**  
- 활성화 함수 → **Activation Function**  
- 범용 근사 정리 → **Universal Approximation Theorem**  

### **수학 관련 용어**  
- 다항식 → **Polynomial**  
- 차수 → **Degree (of a polynomial)**  
- 2차항 → **Quadratic Term**  
- 선형 조합 → **Linear Combination**  
- 비선형 변환 → **Nonlinear Transformation**  
- 근사 → **Approximation**  
- 곱셈 → **Multiplication**  

### **기본 연산 및 표현**  
- 가중합 → **Weighted Sum**  
- 시뮬레이션 → **Simulation**  
- 비선형성 → **Nonlinearity**  
- 조합 → **Combination**  

### **예제 관련 용어**  
- 입력 → **Input**  
- 출력 → **Output**  
- 함수 → **Function**  
- 변환 → **Transformation**  
- 논리 연산 → **Logical Operation**  
- 음수 → **Negative Value**  
- 절댓값 → **Absolute Value**  

이제 같은 개념을 영어로 이야기할 때도 이해하기 쉬울 거야!

