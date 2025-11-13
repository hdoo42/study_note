import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D 시각화를 위한 모듈

# 예시로 사용할 벡터
u = np.array([1, 3, 0])
v = np.array([3, 1, 1])

# Cross Product 계산
n = np.cross(u, v)

# 3D 플롯 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 원점
origin = np.array([0, 0, 0])

# 벡터 u, v, n을 그리기
ax.quiver(origin[0], origin[1], origin[2], 
          u[0], u[1], u[2], 
          color='red', label='u', arrow_length_ratio=0.1)

ax.quiver(origin[0], origin[1], origin[2], 
          v[0], v[1], v[2], 
          color='green', label='v', arrow_length_ratio=0.1)

ax.quiver(origin[0], origin[1], origin[2], 
          n[0], n[1], n[2], 
          color='blue', label='u x v', arrow_length_ratio=0.1)

# 범위 지정 (보기 좋게 세팅)
ax.set_xlim([-1, 3])
ax.set_ylim([-1, 3])
ax.set_zlim([-1, 3])

# 축 라벨 및 범례
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title('Cross Product Visualization')
plt.show()

