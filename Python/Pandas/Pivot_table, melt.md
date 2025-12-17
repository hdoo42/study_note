---
id: Pivot_table, melt
aliases: []
tags: []
---

한 줄로 말하면
- **pivot_table / melt는 “행·열을 뒤집어서” 같은 데이터를 다른 모양(레이아웃)으로 바꾸는 도구**라는 뜻이에요.
그 “다른 모양”을 보통 **wide format** / **long format**이라고 부릅니다.

---

## 1. wide format vs long format 이게 뭐야?

예시 데이터:

| student | math | english |
| ------- | ---- | ------- |
| A       | 80   | 90      |
| B       | 70   | 85      |

이건 **wide format** 입니다.

* `student`는 **행 구분용**(키)
* `math`, `english` 각각이 **열**로 떨어져 있음

이걸 **long format**으로 바꾸면 보통 이렇게 바꿔요:

| student | subject | score |
| ------- | ------- | ----- |
| A       | math    | 80    |
| A       | english | 90    |
| B       | math    | 70    |
| B       | english | 85    |

* 과목 이름(`math`, `english`)이 각각 열이 아니라
  **subject 라는 하나의 열의 값**으로 들어갔고
* 점수는 `score` 하나의 열로 통합됐죠.

---

## 2. `melt()` : wide → long 으로 펴는(녹이는) 함수

위 wide 데이터를 pandas로 만들면:

```python
import pandas as pd

df = pd.DataFrame({
    "student": ["A", "B"],
    "math": [80, 70],
    "english": [90, 85],
})
```

### melt 사용

```python
long_df = df.melt(
    id_vars="student",        # 고정해서 남길 열(키 역할)
    value_vars=["math", "english"],  # 녹여서 한 열로 합칠 열들
    var_name="subject",       # 녹여진 열 이름이 들어갈 새 열 이름
    value_name="score"        # 값이 들어갈 새 열 이름
)
```

`long_df`:

| student | subject | score |
| ------- | ------- | ----- |
| A       | math    | 80    |
| B       | math    | 70    |
| A       | english | 90    |
| B       | english | 85    |

**해석**
“열에 나뉘어 있던 값(math, english)을
‘행 방향’으로 길게 늘어뜨려서 한 열(subject, score)로 만든다” → 그래서 **wide → long**.

---

## 3. `pivot_table()` : long → wide 로 다시 접는 함수

위에서 만든 `long_df`를 다시 wide 형식으로 되돌려볼 수 있어요.

```python
wide_df = long_df.pivot_table(
    index="student",     # 행 인덱스로 쓸 열
    columns="subject",   # 열 이름이 될 값
    values="score",      # 채워 넣을 값
)
```

`wide_df`:

| subject | english | math |
| ------- | ------- | ---- |
| student |         |      |
| A       | 90      | 80   |
| B       | 85      | 70   |

(인덱스/컬럼 계층은 `.reset_index()`나 `.rename_axis(None, axis=1)` 등으로 정리할 수 있음)

**해석**
“long 형식에서 같은 student + subject 조합의 score를
행/열 좌표에 맞게 다시 펼쳐서 wide 형태 표로 만든다” → **long → wide**.

---

## 4. 그래서 ‘구조 변경 및 결합’이란?

문장 다시 보면:

> pivot_table() 또는 melt()를 사용하여
> 데이터의 레이아웃(wide/long format)을 유연하게 재구성할 수 있다

이게 의미하는 건:

1. **구조 변경**

   * `melt()`로 **여러 열을 한 열로 합쳐서 long 형태**로 만들 수 있고,
   * `pivot_table()`로 **long 형태를 다시 열 여러 개로 나눈 wide 형태**로 만들 수 있다.
   * 이 과정에서 동일한 데이터지만 “행/열 배치 방식”을 바꿀 수 있다.

2. **결합**

   * `pivot_table()`은 집계 기능도 있어서 (예: 평균, 합계 등)
   * 여러 행을 **groupby + 집계 + 모양 바꾸기** 한 번에 할 수 있음
     (예: 학생/과목별 평균 점수 표 만들기)

예를 들어, 이런 long 데이터가 있을 때:

| student | subject | score |
| ------- | ------- | ----- |
| A       | math    | 80    |
| A       | math    | 90    |
| A       | english | 95    |

```python
df.pivot_table(
    index="student",
    columns="subject",
    values="score",
    aggfunc="mean"
)
```

→ 학생별·과목별 **평균 점수**가 들어간 wide 테이블을 만들어줍니다.
이게 “구조 변경 + 집계(결합)”의 전형적인 용도.

---

## 5. 한 줄 요약

* **melt**: 열들을 한데 모아서 **wide → long** (행이 늘어나고 열이 줄어듦)
* **pivot_table**: long 데이터를 기준별로 모아서 표 형태로 **long → wide**, 필요하면 집계까지
* 그래서 “같은 데이터를 분석하기 편한 모양으로,
  wide/long 사이를 왔다 갔다 하면서 **유연하게 재구성**할 수 있다”는 뜻이에요.

원하면,
지금 쓰고 있는 실제 데이터 샘플(컬럼 이름 몇 개만) 알려주면
그걸 기준으로 “이렇게 melt, 이렇게 pivot_table 하면 된다” 식으로 딱 맞는 예시도 바로 만들어줄게요.

