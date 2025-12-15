---
id: Partial Differential Equation
aliases:
  - Partial Differential Equation
tags:
  - PDEs
---

# **편미분 방정식(Partial Differential Equations, PDEs)이란?**

#### **1. 개념**
편미분 방정식(Partial Differential Equation, PDE)은 **여러 개의 독립 변수에 대한 함수**를 포함하며, **이 함수의 편미분(Partial Derivatives)** 을 포함하는 방정식입니다. 즉, **다변수 함수의 변화율을 다루는 방정식**입니다.

PDE는 물리학, 공학, 경제학 등에서 중요한 역할을 하며, 특히 유체역학, 전자기학, 양자역학, 열전달 문제 등에 널리 사용됩니다.

---

#### **2. 일반적인 형태**
편미분 방정식은 일반적으로 다음과 같은 형태를 가집니다.

$$
F\left(x_1, x_2, \dots, x_n, u, \frac{\partial u}{\partial x_1}, \frac{\partial u}{\partial x_2}, \dots, \frac{\partial^2 u}{\partial x_1^2}, \dots \right) = 0
$$

여기서:
- $u = u(x_1, x_2, \dots, x_n)$ 는 **여러 변수의 함수**입니다.
- $\frac{\partial u}{\partial x_i}$ 는 **1차 편미분(First-order Partial Derivative)** 입니다.
- $\frac{\partial^2 u}{\partial x_i^2}$ 는 **2차 편미분(Second-order Partial Derivative)** 입니다.

---

#### **3. 편미분 방정식과 상미분 방정식의 차이**
- **상미분 방정식(Ordinary Differential Equations, ODEs)**: 한 개의 독립 변수만 포함된 미분 방정식.
  - 예: $\frac{dy}{dx} = x^2 + y$ (여기서 독립 변수는 $x$ 하나뿐)
- **편미분 방정식(PDEs)**: 여러 개의 독립 변수를 포함하는 미분 방정식.
  - 예: $\frac{\partial u}{\partial t} = c^2 \frac{\partial^2 u}{\partial x^2}$ (여기서 독립 변수는 $x$ 와 $t$)

---

#### **4. 대표적인 편미분 방정식**
##### **(1) 파동 방정식(Wave Equation)**
$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$$
- **설명**: 특정 매질에서의 파동(예: 소리, 빛, 수면파 등)의 움직임을 기술하는 방정식.
- **응용**: 음향학, 전자기학, 양자역학.

---

##### **(2) 열 방정식(Heat Equation)**
$$
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
$$
- **설명**: 시간에 따른 열의 전도 현상을 기술하는 방정식.
- **응용**: 열전달, 확산 과정, 블랙-숄즈 방정식(금융공학).

---

##### **(3) 라플라스 방정식(Laplace's Equation)**
$$
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0
$$
- **설명**: 정적 상태(steady-state)에서의 물리적 현상을 설명하는 방정식.
- **응용**: 전자기장, 유체 흐름, 중력장 계산.

---

##### **(4) 나비에-스토크스 방정식([[Navier-Stokes Equation|Navier-Stokes Equation]])**
$$
\rho \left( \frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla) \mathbf{u} \right) = - \nabla p + \mu \nabla^2 \mathbf{u} + \mathbf{f}
$$
- **설명**: 유체의 움직임을 기술하는 비선형 편미분 방정식.
- **응용**: 항공역학, 기상학, 해양학.

---

#### **5. PDE의 해법 (Solution Methods)**
편미분 방정식을 풀기 위해 다양한 해법이 사용됩니다.

1. **분리 변수법 (Separation of Variables)**
   - PDE를 여러 개의 ODE로 변환하여 푸는 방법.
   - 예: $u(x, t) = X(x)T(t)$ 로 가정한 후 ODE로 변환.

2. **푸리에 변환(Fourier Transform) 및 라플라스 변환(Laplace Transform)**
   - 미분 연산을 대수 연산으로 변환하여 쉽게 풀이.
   - 신호 처리 및 전자기학에서 자주 사용.

3. **수치해석법 (Numerical Methods)**
   - 유한 차분법(Finite Difference Method, FDM)
   - 유한 요소법(Finite Element Method, FEM)
   - 유한 체적법(Finite Volume Method, FVM)

---

#### **6. 편미분 방정식의 응용**
PDE는 현실 세계의 다양한 문제를 해결하는 데 사용됩니다.

- **물리학**: 파동 방정식(소리, 빛, 양자역학), 열 방정식(열전달).
- **공학**: 유체역학(나비에-스토크스 방정식), 구조역학(탄성체 방정식).
- **금융공학**: 블랙-숄즈 방정식(옵션 가격 모델링).
- **생물학**: 확산 방정식(세포 확산, 종 분포).
- **기상학**: 기후 모델링, 기압 변동.

---

### **결론**
- 편미분 방정식(PDE)은 다변수 함수의 변화율을 포함하는 방정식으로, **물리학, 공학, 경제학 등 다양한 분야에서 필수적인 도구**입니다.
- 대표적인 PDE에는 **파동 방정식, 열 방정식, 라플라스 방정식, 나비에-스토크스 방정식** 등이 있습니다.
- PDE를 풀기 위해서는 **분리 변수법, 푸리에 변환, 수치해석법(FDM, FEM, FVM)** 등의 방법이 활용됩니다.
