---
id: Secant Line
aliases:
  - Secant line
tags:
  - trigonometric fuction
---

# Secant line
시컨트 선(할선, 割線)은 **곡선 위의 두 점을 연결하는 직선**을 의미합니다. 예를 들어, 함수 $y=f(x)$의 그래프에서 두 점 $P(x_0, f(x_0))$와 $Q(x_0+\Delta x, f(x_0+\Delta x))$를 생각해보면, 이 두 점을 잇는 직선이 바로 시컨트 선입니다.  

이 시컨트 선의 **기울기**는  
$$
\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}
$$  
로 계산되며, 이 값은 두 점 사이의 평균 변화율을 나타냅니다.  

미분의 정의에서는 $Q$가 $P$에 아주 가까워질 때 ($\Delta x \to 0$) 시컨트 선의 기울기가 점점 곡선의 **Tangent Line(접선)** 의 기울기에 가까워지게 되는데, 이 극한값이 바로 **도함수** $f'(x_0)$입니다.

# $Q.$ Secant line과 tangent  line의 이름의 의미가 뭐야? 삼각함수의 성질과 연결해서 설명해줘.

**tangent (탄젠트)** 와 **secant (시컨트)** 라는 삼각함수의 이름은 원과 관련된 고대 기하학적 구성에서 유래했으며, 이 구성은 삼각함수의 성질과 밀접하게 연결되어 있습니다.

1. **기하학적 구성**  
   - 단위원(반지름이 1인 원)을 생각해보면, 원 위의 한 점은 $(\cos\theta, \sin\theta)$로 나타낼 수 있습니다.  
   - 원의 **tangent (탄젠트) line**은 원의 한 점에서 딱 한 점에서만 닿는 직선입니다.  
   - 원의 한 점, 예를 들어 $(1,0)$에서의 접선에 대해, x축의 접선에, 각 $\theta$의 방향으로 뻗은 직선을 그리면 이 직선과 접선이 만나는 점을 얻을 수 있습니다.

2. **tangent (탄젠트)**  
   - 이 구성에서, 각 $\theta$에 대해 원의 중심에서 시작한 직선(반지름)이 원의 접선과 만나는 점까지의 수평 거리(즉, $(1,0)$에서 접선상의 교점까지의 길이)는 **tangent (탄젠트)**의 값, 즉 $\tan\theta$로 정의됩니다.  
   - ‘탄젠트’라는 용어는 라틴어 *tangens*에서 유래했으며, “닿는다”라는 의미로, 직선이 원에 단 한 점에서 “닿는다”는 사실을 반영합니다.

3. **secant (시컨트)**  
   - 같은 구성에서, 원의 중심(0,0)에서 그 직선이 접선과 만나는 점까지의 길이는 **secant (시컨트)**의 값, 즉 $\sec\theta$로 정의됩니다.  
   - ‘시컨트’라는 용어는 라틴어 *secare*에서 유래했으며, “자를” 또는 “관통하다”라는 의미로, 원을 두 점에서 “자를” 수 있는 직선의 성질을 나타냅니다.

4. **삼각함수의 성질과 연결**  
   - 이 기하학적 구성 덕분에, **tangent (탄젠트)** 와 **secant (시컨트)** 함수는 자연스럽게 서로 연결됩니다.  
   - 예를 들어, 직각삼각형에서 $\tan\theta$는 “대변/인접변”으로 정의되고, $\sec\theta$는 “빗변/인접변” (또는 $1/\cos\theta$)으로 정의됩니다.  
   - 단위원을 활용한 그림에서는 피타고라스 정리에 의해  
     $$
     \tan^2\theta + 1 = \sec^2\theta
     $$
     라는 항등식이 도출되는데, 이는 두 함수 사이의 밀접한 관계를 잘 보여줍니다.

요약하면, 원에서 한 점에만 닿는 **tangent (탄젠트)** 의 성질과 원을 두 점에서 자르는 **secant (시컨트)** 의 성질은, 삼각함수를 기하학적으로 해석하는 과정에서 자연스럽게 도입되었으며, 이로 인해 삼각함수의 정의와 여러 항등식(예, $\tan^2\theta + 1 = \sec^2\theta$)이 탄생하게 되었습니다.

아래 그림은 **단위원 (Unit Circle)**, 한 점에서의 **접선 (Tangent Line)**, 그리고 각도 $\theta$에 따른 **시컨트 (Secant)** 및 **탄젠트 (Tangent)** 값이 어떻게 기하학적으로 나타나는지를 보여줍니다.

![unit_circle_with_tangent_secant_line.png](assets/imgs/unit_circle_with_tangent_secant_line.png)



보통 사용되는 고전적인 구성은 다음과 같습니다.

1. 원의 중심을 $O=(0,0)$으로 하고, 반지름이 1인 단위원을 그립니다.
2. $A=(1,0)$에서 단위원에 접하는 **접선 (Tangent Line)**을 그리면, 이는 $x=1$인 수직선이 됩니다.
3. 원점에서 시작하여 $x$축과 이루는 각도가 $\theta$인 반직선을 그립니다. 이 반직선은 단위원과 만나 점 $B=(\cos\theta, \sin\theta)$를 형성합니다.
4. 이 반직선을 **연장**하면 접선과 만나는 점 $C=(1, \tan\theta)$가 생깁니다.
   - 여기서 $\tan\theta$는 점 $A$에서 $C$까지의 길이로 해석되고,
   - $OC$의 길이는 $\sec\theta$ (즉, $1/\cos\theta$)가 됩니다.
5. 또한 직각삼각형 $OAC$에서 피타고라스 정리에 따라
   $$
   \tan^2\theta + 1 = \sec^2\theta
   $$
   라는 항등식이 성립합니다.

다음은 위 설명을 Python의 matplotlib을 이용하여 그린 그래프 코드입니다:
> [!CODE]-
> 
>   ```python
>   import numpy as np
>   import matplotlib.pyplot as plt
> 
>   # 단위원 그리기
>   theta_vals = np.linspace(0, 2*np.pi, 400)
>   x_circle = np.cos(theta_vals)
>   y_circle = np.sin(theta_vals)
> 
>   plt.figure(figsize=(8, 8))
>   plt.plot(x_circle, y_circle, 'b-', label='Unit Circle')
> 
>   # 점 A = (1, 0) 및 A에서의 접선 (x=1)
>   plt.plot(1, 0, 'ro')
>   plt.text(1.05, 0, 'A (1,0)')
>   y_tangent = np.linspace(-1.5, 2.5, 100)
>   plt.plot(np.ones_like(y_tangent), y_tangent, 'g--', label='Tangent Line at A')
> 
>   # 각도 theta 선택 (예: theta0 = 45° = π/4)
>   theta0 = np.pi / 4
> 
>   # 원 위의 점 B = (cosθ, sinθ)
>   B = (np.cos(theta0), np.sin(theta0))
>   plt.plot(B[0], B[1], 'ko')
>   plt.text(B[0] - 0.15, B[1] - 0.1, r'$B(\cos\theta,\sin\theta)$')
> 
>   # 원점에서 B를 지나 확장하는 반직선 (각 θ의 ray)
>   t = np.linspace(0, 1.8, 100)
>   x_ray = t * np.cos(theta0)
>   y_ray = t * np.sin(theta0)
>   plt.plot(x_ray, y_ray, 'm-', label='Ray at angle θ')
> 
>   # 반직선과 접선의 교점 C = (1, tanθ)
>   C = (1, np.tan(theta0))
>   plt.plot(C[0], C[1], 'ko')
>   plt.text(C[0] + 0.05, C[1], r'$C(1,\tan\theta)$')
> 
>   # 선분 그리기: 원점에서 C까지 (secθ)
>   plt.plot([0, C[0]], [0, C[1]], 'c--', label='Secant (length = secθ)')
> 
>   # 선분 그리기: A에서 C까지 (tanθ)
>   plt.plot([1, C[0]], [0, C[1]], 'r-', label='Tangent segment (length = tanθ)')
> 
>   # 그래프 설정
>   plt.axis('equal')
>   plt.xlim(-1.5, 2)
>   plt.ylim(-1.5, 2.5)
>   plt.xlabel('x')
>   plt.ylabel('y')
>   plt.title('Unit Circle with Tangent and Secant for angle θ')
>   plt.legend()
>   plt.grid(True)
>   plt.show()
>   ```

  이 코드를 실행하면,  
  - **단위원**이 파란색 선으로 그려지고,  
  - 점 $A=(1,0)$에서의 **접선** (녹색 점선)이 나타납니다.  
  - 원점에서 시작하여 각 $\theta$ (여기서는 $\theta=\pi/4$)인 반직선(자홍색 선)은 원 위의 점 $B=(\cos\theta,\sin\theta)$를 지나며,  
  - 그 반직선이 접선과 만나는 점 $C=(1,\tan\theta)$가 표시됩니다.

  이를 통해 삼각함수 **탄젠트 ($tan\theta$)** 와 **시컨트 ($sec\theta$)** 의 기하학적 의미가 명확히 드러납니다.

# $Q.$ 왜 $sec\theta = \frac{1}{cos\theta}$이야?

  **secant (시컨트)** 함수가 왜 $\mathbf{1/\cos\theta}$로 정의되는지 이해하기 위해, 단위원(Unit Circle)과 직각삼각형의 기하학적 구성을 살펴보자.

  1. **단위원과 $\cos\theta$의 정의**  
   단위원에서는 각 $\theta$에 대해 원 위의 한 점 $B$가  
   $$
   B = (\cos\theta,\, \sin\theta)
   $$
   로 표현된다. 여기서 $\cos\theta$는 각 $\theta$에서의 **인접변의 길이([[AI_deep_dive/adjacent_side|Adjacent Side]])** 를 의미한다고 볼 수 있다.

7. **접선과 확장된 반직선 구성**  
   단위원에서 $A = (1, 0)$은 $x$축 상의 점이다. 이 점에서 접선(tangent line)은 $x=1$인 수직선이다.  
   원점 $O=(0,0)$에서 각 $\theta$를 이루는 반직선을 그리면, 이 반직선은 원 위의 점 $B=(\cos\theta,\,\sin\theta)$를 지나게 된다.  
   이 반직선을 $A$에서 그린 접선과 연장하면 두 선이 만나는 점 $C$가 생기는데, 이 점은  
   $$
   C = \left(1,\, \tan\theta\right)
   $$
   로 표현된다.

8. **삼각형 $OAC$와 $\sec\theta$의 도출**  
   점 $O$, $A$, $C$를 꼭짓점으로 하는 직각삼각형 $OAC$를 생각해보자.  
   - $A = (1,0)$는 $O$에서 $x$방향으로의 **인접변**  
   - $OC$는 **빗변(Hypotenuse)**  
   - $C = (1, \tan\theta)$에서 $A$와 $C$ 사이의 선분 길이는 $\tan\theta$이다.

   이 삼각형에서 각 $\theta$는 $O$에서 이루어지며,  
   $$
   \cos\theta = \frac{\text{인접변의 길이}}{\text{빗변의 길이}} = \frac{OA}{OC} = \frac{1}{OC}
   $$
   따라서, 빗변 $OC$는  
   $$
   OC = \frac{1}{\cos\theta}
   $$
   이 값이 바로 **secant (시컨트)** 의 정의이며,  
   $$
   \sec\theta \equiv \frac{1}{\cos\theta}
   $$

9. **요약**  
   - 단위원에서 $\cos\theta$는 원 위의 점의 $x$-좌표로 정의된다.  
   - $A=(1,0)$에서의 접선과, 원점에서 시작해 각 $\theta$의 반직선을 그렸을 때, 그 반직선이 접선과 만나는 점까지의 길이가 $OC$가 된다.  
   - 직각삼각형 $OAC$에서 $\cos\theta = \frac{1}{OC}$이므로, $OC = 1/\cos\theta$이며, 이를 **secant (시컨트)** 함수라고 정의한다.

즉, **secant**가 $\mathbf{1/\cos\theta}$인 이유는 삼각형의 인접변과 빗변의 비율에서 유도되며, 단위원에서의 기하학적 구성에 의해 자연스럽게 결정되기 때문이다.
