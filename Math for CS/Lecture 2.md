---
id: Lecture 2
aliases: []
tags: []
---

### MITOCW 강의 2 – 단일 변수 미적분학 요약

강의는 이전 시간의 미분 정의와 접선의 기울기로서의 기하학적 해석을 재검토하면서 이어집니다. 강사는 미분에 대해 또 다른 관점인 변화율에 대해서도 탐구합니다.

#### **다루는 주요 주제:**
1. **미분의 변화율 해석**
  - 미분은 단순한 기하학적 의미를 넘어 순간적인 변화율을 나타냅니다.
  - 평균 변화율인 $\Delta y / \Delta x$ 개념은 $\frac{dy}{dx}$의 한계값으로서 순간 변화율의 정의로 이어집니다.

2. **물리학에서의 변화율 예제**
  - **전류:** $dq/dt$는 전하의 변화율을 나타냅니다.
  - **속도:** 시간에 따른 거리의 미분인 $ds/dt$는 속도를 정의합니다.
  - **예제: 호박 낙하 실험**
    - 80m 높이의 건물에서 호박이 떨어지는 실험은 방정식 $h = 80 - 5t^2$를 따릅니다.
    - 평균 속도: $(0 - 80) / (4 - 0) = -20$ m/s.
    - 충돌 시 순간 속도: $h'(t) = -10t$이므로 $h'(4) = -40$ m/s (약 90 mph).

3. **시간 기반 이상의 응용**
  - **온도 구배:** $dT/dx$는 기상학과 관련된 위치에 따른 온도 변화를 측정합니다.
  - **GPS 감도:** GPS 위치 오차 전파([[GPS location error propagation|GPS_location_error_propagation]])를 미분을 사용하여 분석할 수 있습니다.

4. **극한과 연속성 소개**
  - **간단한 극한:** $0/0$과 같이 부정형이 아니라면 단순 대입으로 해결할 수 있습니다.
  - **한쪽 극한:** 다음과 같이 정의됩니다:
    - **오른쪽 극한:** $\lim_{x \to a^+} f(x)$.
    - **왼쪽 극한:** $\lim_{x \to a^-} f(x)$.
  - **예제:** 좌우 극한이 다른 구간별 함수는 불연속성을 보여줍니다.

5. **불연속성의 유형**
  - **점프 불연속성:** 좌측과 우측 극한은 존재하지만 값이 다릅니다.
  - **제거 가능한 불연속성:** 극한은 존재하지만 함수값과 다릅니다.
  - **무한불연속성:** 함수가 $\pm \infty$로 발산합니다.
  - **진동 불연속성:** 함수가 한 점 근처에서 무한히 진동합니다.

6. **정리: 미분 가능성은 연속성을 내포함**
  - 만약 함수가 $x_0$에서 미분 가능하다면, $x_0$에서 연속이어야 합니다.
  - 증명은 함수의 극한 정의를 이용하여 미분 가능 조건을 적용하는 방식으로 진행됩니다.

#### **결론**
- 강의는 미분이 단순히 기하학적 접선의 기울기뿐만 아니라 실제 상황에서의 변화율을 나타낸다는 점을 강조합니다.
- 불연속성은 미분 가능성에 영향을 주며, 이는 잘 정의된 함수의 정의에 중요한 역할을 합니다.
- 다음 강의에서는 극한 계산과 미분법 규칙에 대해 더 자세히 다룰 예정입니다.
