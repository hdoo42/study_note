---
id: policy_in_rl
aliases:
  - 정책
  - Policy
  - 강화학습 정책
tags: [reinforcement_learning, AI, probability, decision_making]
---

# 정책 (Policy in Reinforcement Learning)

정책(Policy)은 강화학습에서 가장 핵심적인 개념 중 하나로, 에이전트가 특정 상태에서 어떤 행동을 선택할지 결정하는 전략을 의미합니다. 수학적으로는 상태에서 행동으로의 매핑 함수로 표현되며, 일반적으로 $\pi$로 표기합니다.

## 정책의 수학적 정의

정책은 다음과 같이 정의될 수 있습니다:

- **결정론적 정책(Deterministic Policy)**: 각 상태에 대해 정확히 하나의 행동을 매핑
  $$\pi(s) = a$$
  여기서 $s$는 상태, $a$는 행동입니다.

- **확률적 정책(Stochastic Policy)**: 각 상태에서 가능한 행동들에 대한 확률 분포로 표현
  $$\pi(a|s) = P(A_t = a | S_t = s)$$
  여기서 $\pi(a|s)$는 상태 $s$에서 행동 $a$를 선택할 확률을 나타냅니다.

확률적 정책은 [[probability|확률]] 개념을 활용하여 에이전트의 행동을 결정합니다. 이러한 확률적 접근 방식은 탐색(exploration)과 활용(exploitation) 사이의 균형을 유지하는 데 도움을 줍니다.

## 정책의 종류

### 1. 매개변수화된 정책 (Parameterized Policies)

신경망이나 다른 함수 근사기를 사용하여 정책을 표현합니다. 매개변수 $\theta$를 이용하여 $\pi_\theta(a|s)$로 표기합니다.

```
예: 신경망으로 표현된 정책에서 입력은 상태 s, 출력은 각 행동에 대한 확률 분포
```

### 2. 가우시안 정책 (Gaussian Policy)

연속적인 행동 공간에서 많이 사용되는 정책으로, 행동의 확률 분포를 정규 분포로 모델링합니다.

$$\pi_\theta(a|s) = \frac{1}{\sigma_\theta(s)\sqrt{2\pi}} \exp\left(-\frac{(a-\mu_\theta(s))^2}{2\sigma_\theta(s)^2}\right)$$

여기서 $\mu_\theta(s)$는 평균, $\sigma_\theta(s)$는 표준편차를 나타냅니다.

### 3. 소프트맥스 정책 (Softmax Policy)

이산적인 행동 공간에서 흔히 사용되는 정책으로, 각 행동의 선호도를 계산하고 소프트맥스 함수를 통해 확률로 변환합니다.

$$\pi_\theta(a|s) = \frac{\exp(h_\theta(s, a))}{\sum_{a'} \exp(h_\theta(s, a'))}$$

여기서 $h_\theta(s, a)$는 상태 $s$에서 행동 $a$의 선호도를 나타냅니다.

## 정책 최적화 방법

정책을 최적화하는 방법은 크게 세 가지로 나눌 수 있습니다:

1. **정책 기반 방법(Policy-based Methods)**: 정책을 직접 최적화
   - 정책 그래디언트(Policy Gradient)
   - REINFORCE 알고리즘

2. **가치 기반 방법(Value-based Methods)**: 가치 함수를 학습하고 이를 기반으로 정책 유도
   - Q-learning
   - DQN(Deep Q-Network)

3. **액터-크리틱 방법(Actor-Critic Methods)**: 정책(Actor)과 가치 함수(Critic)를 동시에 학습
   - A3C(Asynchronous Advantage Actor-Critic)
   - PPO(Proximal Policy Optimization)
   - SAC(Soft Actor-Critic)

## 정책과 확률의 관계

정책, 특히 확률적 정책은 [[probability|확률론]]의 개념을 강화학습에 적용한 예입니다. 정책이 확률 분포 형태를 취함으로써 다음과 같은 이점을 얻습니다:

1. **탐색-활용 균형(Exploration-Exploitation Trade-off)**: 확률적 정책은 에이전트가 새로운 행동을 시도(탐색)하면서도 이미 알고 있는 좋은 행동을 활용할 수 있게 합니다.

2. **불확실성 모델링(Uncertainty Modeling)**: 환경의 불확실성과 불완전한 정보를 다루는 데 적합합니다.

3. **다중 최적 행동(Multiple Optimal Actions)**: 여러 행동이 비슷하게 좋은 경우, 확률적으로 이들 사이에서 선택할 수 있습니다.

4. **정책 그래디언트 계산(Policy Gradient Calculation)**: 확률적 정책은 미분 가능하므로 그래디언트 기반 최적화 방법을 적용할 수 있습니다.

## 정책의 평가와 개선

강화학습의 핵심 과정은 정책을 평가하고 개선하는 반복적인 사이클입니다:

1. **정책 평가(Policy Evaluation)**: 현재 정책 $\pi$의 가치 함수를 계산
2. **정책 개선(Policy Improvement)**: 계산된 가치 함수를 바탕으로 더 나은 정책 $\pi'$ 생성

이 과정이 반복되면서 점차 최적 정책에 수렴합니다.

## 응용 분야

정책은 다음과 같은 다양한 강화학습 응용 분야에서 중요한 역할을 합니다:

- 로봇 제어 및 자율 주행
- 게임 AI (알파고, 스타크래프트 AI 등)
- 추천 시스템
- 자원 할당 및 스케줄링
- 금융 포트폴리오 관리

---

강화학습에서 정책은 에이전트의 행동 전략을 정의하는 핵심 요소입니다. 특히 확률적 정책은 [[probability|확률론]]을 기반으로 하여 복잡하고 불확실한, 그리고 부분적으로만 관측 가능한 환경에서 효과적인 의사결정을 가능하게 합니다.
---
id: policy_in_rl
aliases:
  - 정책
  - Policy
  - RL 정책
tags: [reinforcement_learning, probability, AI, decision_making]
---

# 정책 (Policy)

정책(Policy)은 강화학습(Reinforcement Learning)에서 에이전트가 특정 상태에서 어떤 행동을 선택할지 결정하는 전략 또는 함수입니다. 이는 확률적 관점에서 상태에서 행동으로의 매핑을 정의합니다.

## 기본 개념

강화학습에서 정책 $\pi$는 일반적으로 다음 두 가지 형태 중 하나로 표현됩니다:

1. **결정적 정책(Deterministic Policy)**:
   - 각 상태 $s$에 대해 정확히 하나의 행동 $a$를 지정
   - $a = \pi(s)$ 형태로 표현

2. **확률적 정책(Stochastic Policy)**:
   - 각 상태 $s$에서 가능한 모든 행동 $a$에 대한 확률 분포를 정의
   - $\pi(a|s) = P(A_t = a | S_t = s)$ 형태로 표현
   - 이는 "상태 $s$에서 행동 $a$를 선택할 확률"을 의미

## 확률적 정책의 중요성

확률적 정책은 다음과 같은 이유로 강화학습에서 널리 사용됩니다:

1. **탐색과 활용의 균형(Exploration-Exploitation Trade-off)**:
   - 확률적 정책은 에이전트가 새로운 행동을 탐색하면서도 좋은 행동을 활용할 수 있게 함
   - 결정적 정책은 항상 같은 행동만 선택하므로 탐색이 제한됨

2. **불확실성 처리**:
   - 현실 세계의 불확실성이나 부분 관측 가능한 환경에서 보다 강건한 결정을 내릴 수 있음
   - 확률적 결정은 [[probability|확률적 환경]]에 더 적합

3. **다중 최적 행동**:
   - 여러 행동이 동일하게 최적일 때 확률적으로 선택 가능
   - 상대방이 있는 게임에서 예측 불가능성 제공(예: 가위바위보)

## 정책 최적화

강화학습의 목표는 최적의 정책 $\pi^*$를 찾는 것으로, 이는 기대 보상을 최대화하는 정책입니다:

$$\pi^* = \arg\max_{\pi} \mathbb{E}_{\tau \sim \pi} \left[ \sum_{t=0}^{T} \gamma^t r(s_t, a_t) \right]$$

여기서:
- $\tau$는 정책 $\pi$를 따른 상태-행동 궤적
- $\gamma$는 할인 계수(discount factor)
- $r(s_t, a_t)$는 상태 $s_t$에서 행동 $a_t$를 취했을 때의 보상

## 정책 표현 방법

현대 강화학습에서는 정책을 다양한 방식으로 표현합니다:

1. **테이블 기반(Tabular) 정책**:
   - 각 상태-행동 쌍에 대한 값을 테이블에 저장
   - 상태 공간이 작을 때만 실용적

2. **함수 근사(Function Approximation)**:
   - 신경망 등을 사용하여 정책 함수를 근사
   - 복잡한 고차원 상태 공간에서 효과적

3. **파라미터화된 정책**:
   - $\pi_\theta(a|s)$ 형태로, $\theta$는 학습 가능한 파라미터
   - 정책 경사(Policy Gradient) 알고리즘에서 주로 사용

## 주요 정책 기반 알고리즘

1. **REINFORCE**: 가장 기본적인 정책 경사 알고리즘
2. **Actor-Critic**: 가치 함수와 정책을 동시에 학습
3. **Proximal Policy Optimization (PPO)**: 안정적인 정책 업데이트를 위한 알고리즘
4. **Trust Region Policy Optimization (TRPO)**: 성능 저하를 방지하는 정책 최적화 방법
5. **Soft Actor-Critic (SAC)**: 최대 엔트로피 강화학습 프레임워크

## 정책과 가치 함수의 관계

강화학습에서는 정책과 함께 가치 함수(Value Function)가 중요한 개념입니다:

- **상태 가치 함수(State Value Function)** $V^\pi(s)$: 정책 $\pi$를 따를 때 상태 $s$에서 시작하여 얻을 수 있는 기대 보상
- **행동 가치 함수(Action Value Function)** $Q^\pi(s, a)$: 정책 $\pi$를 따를 때 상태 $s$에서 행동 $a$를 취한 후 얻을 수 있는 기대 보상

최적 정책 $\pi^*$는 최적 가치 함수 $V^*$와 $Q^*$와 관련이 있습니다:
$$\pi^*(a|s) = \begin{cases} 
1 & \text{if } a = \arg\max_{a'} Q^*(s, a') \\
0 & \text{otherwise}
\end{cases}$$

## 응용 사례

강화학습의 정책은 다양한 분야에서 활용됩니다:

1. **게임 AI**: AlphaGo, OpenAI Five 등
2. **로보틱스**: 로봇 제어 및 자율 주행
3. **금융**: 포트폴리오 관리 및 거래 전략
4. **추천 시스템**: 개인화된 콘텐츠 추천
5. **자원 관리**: 에너지 시스템, 네트워크 라우팅 등

---

정책은 강화학습의 핵심 개념으로, 에이전트가 환경과 상호작용하는 방식을 결정합니다. 확률적 정책의 사용은 강화학습이 불확실한 환경에서도 효과적으로 학습하고 결정을 내릴 수 있게 하는 중요한 요소입니다.