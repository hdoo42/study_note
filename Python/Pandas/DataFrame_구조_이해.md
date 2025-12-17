---
id: DataFrame_구조_이해
aliases: []
tags: []
---

# pandas `DataFrame` 구조 이해

*DataFrame = (Index, Columns Index, column별 1D array들) + alignment 로직*

---

## 0. TL;DR: DataFrame을 이렇게 보면 편하다

pandas의 `DataFrame`은 공식 정의로는

> “열(column)마다 서로 다른 dtype을 가질 수 있는 **2차원 레이블 데이터 구조**” ([pandas.pydata.org][1])

이 문장을 조금 더 구현 친화적으로 바꾸면:

> **DataFrame = (행 Index, 열 Index) + (열마다 1D 배열) + Index 기반 alignment 로직**

즉,

* **행·열 축의 레이블을 표현하는 두 개의 `Index` 객체**와 ([pandas.pydata.org][2])
* **각 열을 이루는 1차원 배열(NumPy array 또는 ExtensionArray)**,
* 그리고 이 둘을 이용해서 연산 시 **자동으로 행·열을 맞춰 주는 alignment 규칙**

으로 이해할 수 있다.

---

## 1. DataFrame 개요

* `DataFrame`은

  * 2차원 형식(행 × 열)의 데이터를 담고,
  * 각 축(axis)에 대한 **레이블(이름)** 을 가진다.
* 열마다 dtype이 다를 수 있다 (예: int, float, string, datetime 등).([pandas.pydata.org][1])

pandas 공식 문서 표현을 그대로 옮기면:

> * 스프레드시트(엑셀)나 SQL 테이블과 비슷한 구조
> * 혹은 “`Series` 객체들의 dict”로 생각해도 된다. ([pandas.pydata.org][1])

이 문장을 우리의 mental model에 맞게 다시 쓰면:

* **행 방향**: 하나의 `Index`가 “각 행의 이름”을 관리한다.
* **열 방향**: 또 다른 `Index`(columns)가 “각 열의 이름”을 관리한다.
* **데이터**: 각 열은 `Series`처럼 **1D 배열을 하나씩 갖고 있다.**

---

## 2. 구성 요소 ①: 행 인덱스 (`Index`)

### 2.1 `Index`란?

`Index`는 pandas에서 모든 축 레이블을 표현하는 공통 타입이다. 공식 정의는:

> “모든 pandas 객체에서 축 레이블을 저장하는 기본 객체이며, 정렬·alignment에 쓰이는 불변 시퀀스” ([pandas.pydata.org][2])

**DataFrame의 행 인덱스**는:

* “각 행을 식별하는 키 집합”
* 예: `RangeIndex(0, 100)`, 문자열 인덱스, DatetimeIndex, MultiIndex 등.

```python
import pandas as pd

df = pd.DataFrame(
    {"name": ["A", "B", "C"], "score": [10, 20, 30]},
    index=["s1", "s2", "s3"],
)

df.index      # Index(['s1', 's2', 's3'], dtype='object')
```

### 2.2 Index의 역할

pandas 문서에서 축 레이블(=Index)의 역할은 크게 세 가지로 정리되어 있다. ([pandas.pydata.org][3])

1. **데이터의 의미를 표현하는 메타데이터**
2. **자동/명시적 alignment**를 가능하게 하는 기준
3. 직관적인 서브셋 선택 (`loc`, `iloc` 등)에 사용되는 기준

우리가 집중할 부분은 (2)번, 즉 **alignment의 기준**이다.

---

## 3. 구성 요소 ②: 열 인덱스 (`Columns Index`)

DataFrame의 `columns` 역시 `Index` 객체이다.

```python
df.columns    # Index(['name', 'score'], dtype='object')
type(df.columns)  # pandas.Index
```

* 열 이름을 관리하는 **별도의 Index**
* `rename`, `reindex`, `drop` 등 대부분의 열 조작은 이 `columns` Index를 조작하는 형태로 구현됨. ([pandas.pydata.org][4])

즉, DataFrame의 “축 정보”는:

* **행 축**: `df.index`
* **열 축**: `df.columns`

두 개의 `Index` 객체로 완전히 분리되어 있음.

---

## 4. 구성 요소 ③: column별 1D array (데이터 영역)

`DataFrame`의 각 열은 결국 `Series`이고, `Series`는 내부적으로 **1D 배열**을 하나 가진다.

* 대부분은 **NumPy 1D array** (`ndarray`),
* 일부 타입은 **ExtensionArray** (nullable integer, string, Arrow-backed array 등).([pandas.pydata.org][1])

간단한 예:

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "i": np.array([1, 2, 3], dtype="int64"),
    "f": np.array([0.1, 0.2, 0.3], dtype="float64"),
    "s": ["a", "b", "c"],
})

df.dtypes
# i      int64
# f    float64
# s     object
# dtype: object
```

구현 관점에서:

* 각 열은 “값을 담고 있는 **1D 배열** + 그 배열을 설명하는 dtype”으로 표현된다.
* pandas 내부에서는 같은 dtype의 여러 열을 **하나의 큰 배열 block**으로 묶어 관리하기도 하는데, 이건 아래 BlockManager에서 한 번 더 짚는다. ([Uwe’s Blog][5])

---

## 5. alignment 로직: Index를 기준으로 자동 정렬

`DataFrame`의 **진짜 핵심 기능**은 단순히 2D 배열을 감싸는 게 아니라, **Index 기반으로 자동 정렬(alignment)** 을 수행한다는 점이다.

pandas 문서에서는 이렇게 설명한다:

> * 축 레이블 정보는 자동·명시적 데이터 alignment를 가능하게 한다. ([pandas.pydata.org][3])
> * 두 `Series` 또는 `DataFrame` 사이의 산술 연산에서, pandas는 인덱스를 정렬한다. ([O'Reilly Media][6])

### 5.1 행 Index alignment 예시

```python
import pandas as pd

s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
s2 = pd.Series([10, 20, 30], index=["b", "c", "d"])

s1 + s2
```

결과:

* 인덱스는 `a, b, c, d`의 **합집합**이 되며,
* 공통으로 존재하는 index(`b`, `c`)에 대해서만 실제 덧셈이 수행된다. ([Python for Data Science][7])

```text
a     NaN   # s2에는 a가 없음
b    12.0   # 2 + 10
c    23.0   # 3 + 20
d     NaN   # s1에는 d가 없음
dtype: float64
```

여기서 중요한 포인트:

* **Index가 다르면, 위치(position)가 같아도 “같은 행”으로 취급하지 않는다.**
* 위치 기반이 아니라 **레이블 기반**으로 연산이 일어난다.

`DataFrame`끼리 연산할 때도 같은 원리가 적용된다.

### 5.2 열 Index alignment 예시

```python
df1 = pd.DataFrame(
    {"x": [1, 2], "y": [3, 4]},
    index=["a", "b"],
)
df2 = pd.DataFrame(
    {"y": [10, 20], "z": [30, 40]},
    index=["a", "b"],
)

df1 + df2
```

결과 DataFrame의 축:

* 행 인덱스: `["a", "b"]` (공통)
* 열 인덱스: `["x", "y", "z"]` (열 이름의 합집합) ([Stack Overflow][8])

실제 값은:

* `x` 열: `df2`에 `x`가 없으므로 NaN
* `y` 열: 두 DataFrame의 `y`가 더해진 값
* `z` 열: `df1`에 `z`가 없으므로 NaN

즉, DataFrame 간 연산은 **행·열 Index에 대해 outer join처럼 alignment**를 수행한 뒤 산술 연산을 한다고 보면 된다. ([Python for Data Science][7])

### 5.3 정리: alignment의 의미

* **연산 = (축 레이블들의 union) + (공통 레이블에 대해 element-wise 연산)**
* **부족한 부분 = NaN으로 채워진다.**
* 이 로직은 `Series ↔ DataFrame`, `DataFrame ↔ DataFrame` 연산 모두에 적용된다. ([jakevdp.github.io][9])

---

## 6. 구현 한 단계 더: BlockManager와 내부 배열

위 mental model만으로도 대부분의 코드 레벨 이해에는 충분하지만, 구현 레벨에서 한 번 더 내려가면 **BlockManager**라는 레이어가 나온다.

요약하면:

> “BlockManager는 같은 dtype을 가진 여러 열을 **하나의 연속된 메모리 블록**에 보관한다.” ([Uwe’s Blog][5])

* 예를 들어, int64 열 10개가 있으면,

  * 열마다 1D 배열을 따로 들고 있는 대신,
  * 10열을 모아서 (행 수 × 10)짜리 2D 배열 하나로 가지고 있을 수 있다. ([phofl.github.io][10])
* 이렇게 하면

  * 같은 dtype 열에 대한 집계/연산을 할 때 cache locality가 좋아지고,
  * wide DataFrame에서 연산을 보다 효율적으로 수행할 수 있다.

하지만 **외부에서 DataFrame을 다룰 때의 추상화**는 여전히:

* **각 열은 1D 배열을 가진다 (Series 단위 모델)**
* **행/열 Index를 기준으로 연산 시 alignment를 수행한다**

라는 위에서 정리한 mental model로 생각해도 충분하다.

---

## 7. Alignment와 관련된 실무 팁

### 7.1 의도치 않은 alignment 방지

두 DataFrame의 index/columns가 이미 “같은 순서”라고 믿고 있을 때도, pandas는 **항상 레이블을 기준으로** 맞추려고 한다. 그래서:

* 열 이름이 살짝 다르거나,
* index가 살짝 어긋나 있으면,

연산 결과에 예상치 못한 NaN이 많이 생길 수 있다. ([Stack Overflow][8])

이런 문제가 있을 때는:

* 미리 `df1 = df1.sort_index().sort_index(axis=1)` 같이 정렬,
* 혹은 `df1.to_numpy()` / `df1.values`로 ndarray로 변환 후 **위치 기반 연산** 수행,
* 또는 명시적으로 `reindex`를 호출해서 축을 맞춘 뒤 연산하는 것이 안전하다.

### 7.2 Index를 적극적으로 활용

반대로, alignment를 적극적으로 활용하면:

* 다른 기간, 다른 분해 레벨의 시계열을 자연스럽게 합치거나,
* 일부분만 겹치는 데이터셋끼리 outer join처럼 연산하는 것이 매우 편해진다. ([Python for Data Science][7])

예를 들어:

```python
# 서로 다른 날짜에 측정된 시계열 두 개
temp = ...
rain = ...

# 날짜 index를 기준으로 자동 정렬된 덧셈/비율 계산
ratio = temp / rain
```

이렇게 index 기반 alignment만 이해하고 있으면, DataFrame/Series 연산을 “단순 산술”이 아니라 “조인 + 산술”로 바라볼 수 있게 된다.

---

## 8. 요약

* **정의**: DataFrame은 “열마다 dtype이 다른 2D 레이블 데이터 구조”. ([pandas.pydata.org][1])
* **구성 요소**:

  * 행 인덱스: `Index` (행 레이블)
  * 열 인덱스: `Index` (열 레이블)
  * 데이터: 열마다 하나의 1D 배열 (`Series` / NumPy / ExtensionArray)
* **핵심 기능**:

  * 두 객체 사이의 연산에서, **행/열 Index를 기준으로 자동 정렬(alignment)** 을 수행한다. ([pandas.pydata.org][3])
* **구현 디테일**:

  * 내부적으로는 BlockManager가 같은 dtype의 여러 열을 하나의 큰 배열 block으로 묶어서 관리한다. 그러나 mental model은 “column별 1D array + Index alignment”로 가져가도 충분히 유효하다. ([Uwe’s Blog][5])

이 문서를 Obsidian에 두고, 필요하면 아래처럼 관련 문서를 이어서 작성하면 좋다:

* [[pandas-Series-구조]]
* [[pandas-Index-정리]]
* [[pandas-BlockManager-내부-구조]]
* [[pandas-alignment-예제-모음]]

[1]: https://pandas.pydata.org/docs/user_guide/dsintro.html?utm_source=chatgpt.com "Intro to data structures — pandas 2.3.3 documentation - PyData |"
[2]: https://pandas.pydata.org/docs/reference/api/pandas.Index.html?utm_source=chatgpt.com "pandas.Index — pandas 2.3.3 documentation"
[3]: https://pandas.pydata.org/docs/user_guide/indexing.html?utm_source=chatgpt.com "Indexing and selecting data — pandas 2.3.3 documentation"
[4]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html?utm_source=chatgpt.com "pandas.DataFrame.rename_axis - PyData |"
[5]: https://uwekorn.com/2020/05/24/the-one-pandas-internal.html?utm_source=chatgpt.com "The one pandas internal I teach all my new colleagues"
[6]: https://www.oreilly.com/content/operations-in-pandas/?utm_source=chatgpt.com "Operations in Pandas"
[7]: https://python4data.science/en/latest/workspace/pandas/arithmetic.html?utm_source=chatgpt.com "Arithmetic - Python for Data Science"
[8]: https://stackoverflow.com/questions/35027377/pandas-dataframe-arithmetic-ignoring-column-index?utm_source=chatgpt.com "Pandas DataFrame Arithmetic ignoring column index"
[9]: https://jakevdp.github.io/PythonDataScienceHandbook/03.03-operations-in-pandas.html?utm_source=chatgpt.com "Operating on Data in Pandas | Python Data Science Handbook"
[10]: https://phofl.github.io/pandas-internals.html?utm_source=chatgpt.com "pandas Internals Explained - Patrick Hoefler"
