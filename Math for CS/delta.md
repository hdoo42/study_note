---
id: delta
aliases: []
tags:
  - notation
---

**$\delta$ (델타, delta)** 는 수학과 과학에서 다양한 의미로 사용되는 그리스 문자이다. 문맥에 따라 의미가 달라질 수 있는데, 대표적인 용도를 정리하면 다음과 같다.

### 1. **변화량 (Difference, Increment)**
   - **$\Delta$ (대문자 델타)와 유사한 의미로 사용됨.**
   - 함수의 작은 변화량을 나타낼 때 사용:
     $$
     \delta x, \delta y
     $$
   - 예: **미적분학에서 미소 변화량 ($\delta x, \delta y$)을 나타낼 때 사용**  
     → $dy = f'(x) dx$에서 $dx$와 유사한 개념으로 쓰일 수도 있음.

### 2. **극한과 연속성 ([[epsilon-delta argument|epsilon-delta argument]])**
   - 함수의 **연속성(Continuity) 및 극한(Limit) 정의**에서 사용됨.
   - **$\varepsilon$-$\delta$ 논법**:
     $$
     \forall \varepsilon > 0, \exists \delta > 0 \text{ such that } 0 < |x - c| < \delta \Rightarrow |f(x) - L| < \varepsilon
     $$
   - 여기서 $\delta$는 $x$의 변화량을 의미하며, $\varepsilon$과의 관계를 조정하는 역할을 함.

### 3. **델타 함수 (Delta Function)**
   - **디랙 델타 함수 $\delta(x)$**:
     - 물리학 및 신호처리에서 **단위 펄스 함수**로 사용됨.
     - 특정한 한 점에서 무한히 크고, 전체적으로 적분값이 1인 함수:
       $$
       \int_{-\infty}^{\infty} \delta(x) dx = 1
       $$
     - 신호처리에서 **충격 신호(impulse signal)** 를 모델링하는 데 사용됨.

### 4. **변분 (Calculus of Variations)**
   - **변분법에서의 미소 변화**:
     - 함수 $f(x)$의 작은 변화량을 나타낼 때 $\delta f$ 사용.
     - 예: **오일러-라그랑주 방정식**에서 사용됨.

### 5. **통계학과 확률론**
   - **크로네커 델타 ($\delta_{ij}$)**:
     $$
     \delta_{ij} =
     \begin{cases}
     1, & i = j \\
     0, & i \neq j
     \end{cases}
     $$
     - 지표(i, j)가 같을 때 1, 다를 때 0을 갖는 함수.
     - 행렬, 선형대수, 텐서 해석 등에서 사용됨.

### 정리
- $\delta$는 **미소 변화량**, **연속성 정의**, **디랙 델타 함수**, **크로네커 델타**, **변분법** 등 다양한 용도로 사용됨.
- 문맥에 따라 의미가 달라지므로, 어떤 분야에서 쓰이는지에 따라 해석해야 함.
