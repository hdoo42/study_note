---
id: adjacent_side
aliases:
  - Adjacent Side
tags: []
---

# Adjacent Side
직각삼각형에서 **인접변 (Adjacent Side)** 은 해당 각도에 바로 붙어 있는 두 변 중, **빗변 (Hypotenuse)** 을 제외한 변을 의미합니다. 예를 들어, 직각삼각형에서 하나의 각을 $\theta$라고 할 때,

- **빗변 (Hypotenuse)**: 직각삼각형에서 가장 긴 변으로, 직각을 마주 보는 변입니다.
- **인접변 (Adjacent Side)**: $\theta$에 인접(붙은) 한 변으로, $\theta$와 함께 삼각형의 한 변을 이루지만 빗변은 아닙니다.
- **대변 (Opposite Side)**: $\theta$와 마주 보고 있는 변입니다.

간단한 그림으로 표현하면:

> [!CODE]- 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> 
> # 각 theta (라디안 단위, 여기서는 30°)
> theta = np.pi / 6  # 30도
> 
> # 단위원(빗변을 1로 놓은 경우)
> # 인접변 = cos(theta), 대변 = sin(theta)
> adjacent = np.cos(theta)
> opposite = np.sin(theta)
> hypotenuse = 1  # 단위원에서 빗변은 1
> 
> # 삼각형의 꼭짓점 좌표
> # A: 직각이 위치하는 원점 (0, 0)
> # B: 인접변 끝 (adjacent, 0)
> # C: 대변 끝 (adjacent, opposite) - 빗변의 다른 끝
> A = np.array([0, 0])
> B = np.array([adjacent, 0])
> C = np.array([adjacent, opposite])
> 
> plt.figure(figsize=(6, 6))
> 
> # 삼각형 그리기
> plt.plot([A[0], B[0]], [A[1], B[1]], 'b-', lw=2)  # 인접변 (Adjacent Side)
> plt.plot([B[0], C[0]], [B[1], C[1]], 'g-', lw=2)  # 대변 (Opposite Side)
> plt.plot([C[0], A[0]], [C[1], A[1]], 'r-', lw=2)  # 빗변 (Hypotenuse)
> 
> # 꼭짓점 표시
> plt.plot(A[0], A[1], 'ko')
> plt.text(A[0]-0.1, A[1]-0.1, "A (0,0)", fontsize=12)
> plt.plot(B[0], B[1], 'ko')
> plt.text(B[0]-0.1, B[1]-0.1, f"B ({adjacent:.2f}, 0)", fontsize=12)
> plt.plot(C[0], C[1], 'ko')
> plt.text(C[0]+0.02, C[1], f"C ({adjacent:.2f}, {opposite:.2f})", fontsize=12)
> 
> # 각 변에 라벨 달기
> plt.text((A[0]+B[0])/2, (A[1]+B[1])/2-0.1, "인접변 (Adjacent)", fontsize=12, color='b', ha='center')
> plt.text((B[0]+C[0])/2+0.1, (B[1]+C[1])/2, "대변 (Opposite)", fontsize=12, color='g', va='center')
> plt.text((A[0]+C[0])/2-0.1, (A[1]+C[1])/2+0.1, "빗변 (Hypotenuse)", fontsize=12, color='r', ha='center')
> 
> # 각 theta 표시 (원점에서 그린 작은 호)
> arc_radius = 0.2
> angle_arc = np.linspace(0, theta, 100)
> x_arc = arc_radius * np.cos(angle_arc)
> y_arc = arc_radius * np.sin(angle_arc)
> plt.plot(x_arc, y_arc, 'm-', lw=2)
> plt.text(arc_radius+0.05, arc_radius/2, r"$\theta$", color='m', fontsize=14)
> 
> # 그래프 설정
> plt.xlim(-0.5, 1.2)
> plt.ylim(-0.5, 1.2)
> plt.gca().set_aspect('equal', adjustable='box')
> plt.title("직각삼각형: 인접변, 대변, 빗변", fontsize=14)
> plt.xlabel("x")
> plt.ylabel("y")
> plt.grid(True)
> plt.show()
> ```

![adjacent_line.png](assets/imgs/adjacent_line.png)

이와 같이, 각 $\theta$에 대해 인접변은 $\theta$의 바로 옆에 위치하며, 삼각함수인 $\cos\theta$를 정의할 때 사용됩니다. 예를 들어,  
$$
\cos\theta = \frac{\text{인접변의 길이}}{\text{빗변의 길이}}
$$
로 정의됩니다.
