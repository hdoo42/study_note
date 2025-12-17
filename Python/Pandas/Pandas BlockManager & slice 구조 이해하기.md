---
id: Pandas BlockManager & slice 구조 이해하기
aliases: []
tags: []
---
### 🎯 BlockManager란?

DataFrame의 실제 데이터를 관리하는 **저수준 저장 엔진**
사용자가 보는 표 형태와 달리 내부적으로는 아래 구조를 가진다:

* 동일 dtype(Column)들을 하나의 **2D NumPy 배열(Block)**로 묶음
* BlockManager는 이 Block들을 **열 위치 기준**으로 관리

구조 계층

```
DataFrame (사용자 레벨)
 └─ BlockManager (저장 관리자)
     └─ Block(NumPy ndarray)
```

---

### 📌 NumpyBlock 출력 형식 해석

예시:

```
NumpyBlock: slice(0, 2, 1), 2 x 2, dtype: int64
```

| 항목             | 설명                                               |
| -------------- | ------------------------------------------------ |
| slice(0, 2, 1) | BlockManager 기준 이 Block이 담당하는 **컬럼 위치 범위** → 0,1 |
| 2 x 2          | Block이 가진 NumPy 배열의 shape = (행 2, 열 2)           |
| dtype: int64   | Block 내 모든 값의 dtype                              |

해석:

> 이 Block은 int64 타입의 2개 컬럼을 연속적으로 포함하고 있고
> 데이터는 2x2 NumPy 배열로 저장되어 있다.

---

### 📌 BlockManager의 slice는 **항상 step=1**

즉, 아래 형태만 가능:

```
slice(start, stop, step=1)
```

이유:

* Block은 **연속된 컬럼 위치만 관리**
* 내부 NumPy 배열은 **C-order contiguous**
* stride view(step>1 slicing)는 Block 설계 목적과 상충

---

### ❌ 왜 slice(0,2,2)는 불가능한가?

이는 **띄엄띄엄한 컬럼**(예: 위치 0,2)만 모은 구조를 의미한다.
하지만 pandas는 다음 원칙을 따른다:

1. Block은 **연속된 열 범위만** 포함
2. dtype 기준 묶임 → 중간에 다른 dtype 있으면 Block split
3. stride view 기반 Block은 **허용하지 않음**

예시:

| 위치 | 컬럼 | dtype   |
| -- | -- | ------- |
| 0  | A  | int64   |
| 1  | B  | float64 |
| 2  | C  | int64   |

이 경우:

```
IntBlock: slice(0, 1, 1) -> A
FloatBlock: slice(1, 2, 1) -> B
IntBlock: slice(2, 3, 1) -> C
```

> 같은 dtype이라도 **연속 배치**되지 않으면 Block이 분리된다.

---

### 📌 "slice(0,2,1), 2x2" 예제

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "i64": np.array([1, 2], dtype="int64"),
    "i642": np.array([10, 20], dtype="int64"),
})

df._mgr
```

출력 개념:

```
IntBlock: slice(0,2,1), 2 x 2, dtype: int64
```

조건 정리:

| 조건        | 설명           |
| --------- | ------------ |
| 같은 dtype  | int64        |
| 연속된 2개 컬럼 | 위치 0,1       |
| 2행        | 최종 shape 2x2 |

---

## 🧠 핵심 요약

* BlockManager는 **데이터 저장 최적화 구조**
* Block은 **같은 dtype 컬럼들을 묶는 2D NumPy 배열**
* slice는 Block이 커버하는 **연속 컬럼 위치 범위**
* slice step은 항상 **1**
* 따라서 slice(0,2,2) 같은 패턴은 **나올 수 없다**

---

## 🔍 추가로 탐구해볼 주제

* Block merge/split 발생 조건
* concat/assign 시 Block이 어떻게 재조정되는가
* RangeIndex → Int64Index 승격 규칙
* [[ArrayManager vs BlockManager|ArrayManager vs BlockManager]]
