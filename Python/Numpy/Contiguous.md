---
id: 1763017881-EMJF
aliases:
  - Contigous
tags: []
---
# NumPy의 C-contiguous와 Fortran-contiguous: 무엇이며 왜 중요한가

## 핵심 요약

* **C-contiguous(C-order)**: 마지막 축이 메모리에서 **가장 빠르게** 변함(행 우선, row-major). 파이썬/NumPy 기본.
* **Fortran-contiguous(F-order)**: 첫 번째 축이 메모리에서 **가장 빠르게** 변함(열 우선, column-major). 전통적 Fortran/BLAS·LAPACK 관례.
* 연속성(contiguity)은 **strides(바이트 단위 건너뛰기)** 로 정의되며, 이는 **성능(캐시/벡터화)**, **복사 발생 여부**, **C/Fortran 라이브러리 연동**에 큰 영향을 준다.
* 많은 연산은 어떤 배열 레이아웃도 처리하지만, **연속적이지 않거나 기대와 다른 순서**일 때 **숨은 복사**가 생겨 성능이 떨어질 수 있다.

---

## 1) 메모리 레이아웃과 strides 개념

NumPy 배열은 요소를 한 덩어리로 메모리에 저장하고, 각 축을 따라 다음 요소까지 **몇 바이트를 건너뛰는지**를 `strides`로 기록합니다.

* **C-contiguous**: `strides`가 “마지막 축이 itemsize만큼, 그 앞 축은 뒤 축 크기의 곱 × itemsize …” 패턴을 가집니다.
  예: `a.shape == (N, M)`이면 대략 `a.strides == (M*itemsize, itemsize)`
* **Fortran-contiguous**: 반대로 “첫 축이 itemsize, 다음 축은 앞 축 크기의 곱 × itemsize …” 패턴입니다.
  예: `a.shape == (N, M)`이면 대략 `a.strides == (itemsize, N*itemsize)`

> 직관:
> * C-order = **행 우선**(row-major) → `a[i, j]`에서 `j`가 빠르게 이동
> * F-order = **열 우선**(column-major) → `a[i, j]`에서 `i`가 빠르게 이동

간단한 2D 예(요소 인덱싱 순서):

```
C-order (row-major):           F-order (column-major):
(0,0) (0,1) (0,2) ...          (0,0) (1,0) (2,0) ...
(1,0) (1,1) (1,2) ...          (0,1) (1,1) (2,1) ...
...
```

> 참고: 1D 배열은 동시에 C-contiguous이자 F-contiguous일 수 있습니다. 슬라이스(예: `a[:, ::2]`)처럼 **stride가 일정 배수가 아니면** 둘 다 아닐 수도 있습니다.

---

## 2) 왜 중요한가 (성능·메모리·연동)

### A. 성능/캐시/벡터화
* **연속 접근**(contiguous)은 CPU 캐시 효율과 벡터화에 유리합니다.
* **비연속(strided)** 접근은 같은 연산이라도 캐시 미스가 늘어 느려질 수 있습니다.
* 많은 유니버설 함수(ufunc)는 비연속 배열도 처리하지만, 내부에서 **임시 연속 복사본**을 만들 수 있어 **추가 메모리·시간**이 듭니다.

### B. 복사 없이 view/reshape 가능 여부
* `reshape`, `ravel`, `transpose` 등은 가능한 경우 **view**를 반환하지만, **연속성/순서가 맞지 않으면 복사**가 발생합니다.
* 레이아웃을 맞추면 **zero-copy view** 가능성이 높아집니다.

### C. C/Fortran 라이브러리 연동
* NumPy는 내부적으로 C와 Fortran 코드 모두와 상호작용합니다.
* 많은 **Fortran 기반 BLAS/LAPACK 루틴**은 **F-order**를 선호합니다. 필요 시 NumPy가 **전치/복사**로 맞춥니다.
* 반대로 **C API/ctypes/Numba/Cython** 등은 **C-order** 배열을 기대하는 경우가 흔합니다.
* 올바른 순서를 맞추면 **불필요한 변환 없이** 빠르게 호출됩니다.

---

## 3) 레이아웃 확인·변환·생성 패턴
### 확인

```python
import numpy as np

a = np.arange(12).reshape(3, 4)     # 기본 C-order
a.flags['C_CONTIGUOUS']  # True/False
a.flags['F_CONTIGUOUS']  # True/False
a.strides                # 바이트 단위 strides 확인
np.isfortran(a)          # F-order인지 간단 확인
```

### 변환(필요할 때만!)

```python
b = np.ascontiguousarray(a)  # C-order 보장 (필요하면 복사)
c = np.asfortranarray(a)     # F-order 보장 (필요하면 복사)
```

### 원하는 순서로 생성

```python
np.empty((N, M), order='C')  # 기본값
np.empty((N, M), order='F')  # F-order로 바로 생성
```

### 평탄화/복사 시 의도 표현

```python
a.ravel(order='C')           # C 순서로 펼치기(복사 or view)
a.ravel(order='F')           # F 순서로 펼치기
a.copy(order='A')            # A: F 배열이면 F, 그 외 C
a.copy(order='K')            # K: 가능한 한 기존 strides 보존
```

### reshape의 `order` 인자 주의점

* `reshape(newshape, order='C'|'F')`의 `order`는 **요소를 어떤 순서로 읽어 재배열할지**를 뜻합니다.
  **기존 배열의 실제 저장 순서를 바꾸는 것이 아닙니다.** (필요하면 복사 발생)

---

## 4) 자주 겪는 상황과 팁

### 4.1 전치/슬라이싱 후 전달 시 복사

```python
a = np.arange(12).reshape(3, 4)  # C-order
at = a.T                         # 보통 F-contiguous view
# C-연속 배열만 받는 C 함수에 넘겨야 한다면:
ct = np.ascontiguousarray(at)    # 여기서 복사 발생 가능 (필요할 때만 수행)
```

* **팁**: 가능한 한 **축 매개변수**를 제공하는 API(예: `np.sum(a, axis=0)` 등)를 사용해 **전치 자체를 피하면** 복사/stride 비용을 아낄 수 있습니다.

### 4.2 간격 슬라이스(`::k`)는 대개 비연속

```python
b = a[:, ::2]                    # 대부분 C/F 모두 아닌 배열
```

* 이런 배열을 고성능 루틴에 넘기면 **숨은 복사**가 생길 수 있습니다. 성능이 민감하면 미리 `ascontiguousarray`/`asfortranarray`로 명시하세요.

### 4.3 브로드캐스팅과 strides=0

* 브로드캐스팅된 뷰는 **stride가 0**인 축이 생길 수 있으며, 이는 연속성이 아닙니다.
* 대부분의 NumPy 연산은 이를 잘 처리하지만, 외부 라이브러리에 넘길 때는 **실제 연속 복사**가 필요할 수 있습니다.

### 4.4 선형대수 루틴과 레이아웃 선택

* **무거운 선형대수(고차원 행렬 연산)** 위주라면 입력을 **F-order로 유지**하면 불필요한 내부 전치/복사를 피할 때가 많습니다.
* **일반 과학계산/이미지 처리/파이썬 레벨 반복**이 많으면 **C-order**가 자연스럽고 도구 호환성도 좋습니다.

---

## 5) 언제 무엇을 선택할까? (실무 규칙)

* **기본은 C-order**: NumPy 기본, 파이썬 생태계와의 상호운용(Numba/Cython/ctypes/PyTorch 등)에 유리.
* **Fortran/BLAS·LAPACK 중심 워크로드**: 입력 행렬을 **F-order로 생성/유지**해서 내부 복사 회피 시도.
* **핫 루프/핫 경로**: 프로파일링 후 비연속 접근이 병목이면 **명시적 변환**으로 연속성 확보.
* **외부 API 요구사항**: 함수/라이브러리가 요구하는 레이아웃(C 또는 F)을 **사전에 맞춰서** 넘긴다.

---

## 6) 작은 체크리스트

* 레이아웃 필요 조건 확인: `arr.flags['C_CONTIGUOUS']`, `arr.flags['F_CONTIGUOUS']`
* 외부 호출 전: 요구 레이아웃에 맞추어 `np.ascontiguousarray`/`np.asfortranarray`
* 전치/복사 비용 회피: 축 인자를 쓰는 연산으로 전치 생성 자체를 피할 수 있는지 검토
* 생성 시부터 결정: `np.empty/zeros/ones(..., order='F')`로 **처음부터** 원하는 순서로

---

## 7) 미니 FAQ

**Q. `a.T`는 복사인가요?**
A. 보통 **view**입니다. 다만 전치된 뷰는 연속성이 바뀌며, 어떤 연산/호출에선 **복사**가 필요할 수 있습니다.

**Q. `reshape`가 왜 가끔 복사하나요?**
A. 요청한 모양/순서를 기존 strides로 표현할 수 없으면 복사합니다. 이는 연속성/순서와 밀접합니다.

**Q. 1D 배열은 어떤가요?**
A. 1D는 일반적으로 C/F 둘 다 연속(true)입니다.

**Q. “빠른” 레이아웃은 항상 하나뿐인가요?**
A. 아닙니다. **패턴과 접근 순서**가 중요합니다. 특정 알고리즘/루틴이 기대하는 순서에 맞추는 것이 핵심입니다.

---

## 8) 짧은 예제 모음

```python
# 1) 기본 C-order
a = np.arange(12, dtype=np.float64).reshape(3, 4)
a.flags['C_CONTIGUOUS'], a.flags['F_CONTIGUOUS']  # (True, False)

# 2) 전치 → 보통 F-order view
at = a.T
at.flags['C_CONTIGUOUS'], at.flags['F_CONTIGUOUS']  # (False, True)

# 3) 열 우선으로 바로 만들기
f = np.empty((3, 4), order='F')
f.flags['F_CONTIGUOUS']  # True

# 4) 외부 C 함수에 넘기기 전에 보장
safe = np.ascontiguousarray(at)   # 필요하면 복사

# 5) BLAS 친화적 입력 만들기
A = np.asfortranarray(np.random.randn(2000, 2000))

# 6) stride가 0인 브로드캐스트 예
x = np.ones((4, 1))
y = np.ones((1, 5))
z = x + y  # (4,5) 브로드캐스트 계산
```

---

필요하시면, **귀하의 실제 연산 패턴**(예: 행 단위 반복, 열 단위 연산, 대형 행렬 곱 중심 등)에 맞춰 **권장 레이아웃과 변환 지점**을 짚어 드릴게요.

