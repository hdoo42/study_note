---
id: 1763015987-FYFI
aliases:
  - WRITEBACKIFCOPY
tags: []
---

`NPY_ARRAY_WRITEBACKIFCOPY`는 NumPy C API에서 사용되는 **매우 중요한 메모리 관리 플래그**입니다. 이는 배열이 실제 원본 데이터가 아닌 **임시 사본(temporary copy)** 이며, 이 사본의 변경 사항이 나중에 **원본 배열에 다시 쓰여져야(write back)** 함을 나타냅니다.

이 플래그는 `PyArrayObject_fields` 구조체의 `flags` 멤버에 설정되며, 이 경우 `base` 멤버는 **업데이트되어야 할 원본 배열**을 가리키게 됩니다.

---

## `WRITEBACKIFCOPY`의 목적과 동작 원리

NumPy의 많은 함수(특히 C API 레벨)는 특정 메모리 레이아웃(예: C-contiguous), 특정 데이터 타입, 또는 쓰기 가능(writable) 속성을 가진 배열을 요구합니다.

하지만 사용자로부터 전달받은 배열이 이러한 요구 사항(예: Fortran-contiguous이거나, 데이터 타입이 다르거나, 읽기 전용)을 만족하지 못할 수도 있습니다.

이때 NumPy는 두 가지 선택을 할 수 있습니다.

1.  **에러 발생:** "요구 사항에 맞지 않는 배열입니다." (바람직하지 않음)
2.  **임시 사본 생성:** 요구 사항을 만족하는 새 배열(임시 사본)을 만들고, 작업을 수행한 뒤, 결과를 원본에 복사합니다.

`WRITEBACKIFCOPY`는 2번 시나리오를 관리하기 위해 사용됩니다.

### 동작 시나리오

1.  **함수 호출:** 한 함수가 특정 속성(예: C-contiguous, `float64`, 쓰기 가능)을 가진 배열 `A_required`를 인자로 요구합니다.
2.  **원본 배열:** 사용자는 요구 사항을 만족하지 못하는 배열 `B_original` (예: Fortran-contiguous, `int32`, 읽기 전용)을 전달합니다.
3.  **임시 사본 생성:** NumPy는 `B_original`의 데이터를 복사하여 `A_required`의 요구 사항을 만족하는 새로운 임시 배열 `T_temp`를 생성합니다.
4.  **플래그 및 `base` 설정:**
    * `T_temp->flags`에 `NPY_ARRAY_WRITEBACKIFCOPY` 플래그를 설정합니다.
    * `T_temp->base`가 원본 배열 `B_original`을 가리키도록 설정합니다.
5.  **작업 수행:** 함수는 이제 요구 사항을 만족하는 `T_temp` 배열에 데이터를 쓰고 수정 작업을 수행합니다. `T_temp`의 `data` 버퍼 내용이 변경됩니다.
6.  **작업 완료 (Write Back):** `T_temp` 배열의 사용이 끝나거나(예: 참조 카운트가 0이 됨) `PyArray_ResolveWritebackIfCopy(T_temp)` 함수가 명시적으로 호출되면, NumPy는 다음을 수행합니다:
    * `T_temp->flags`에서 `NPY_ARRAY_WRITEBACKIFCOPY` 플래그를 확인합니다.
    * 플래그가 설정되어 있으면, `T_temp->base`가 가리키는 `B_original` 배열을 찾습니다.
    * `T_temp`의 (수정된) `data` 버퍼 내용을 `B_original`의 `data` 버퍼로 **다시 복사(write back)** 합니다. (이 과정에서 필요시 데이터 타입 변환 등이 일어날 수 있습니다.)
    * 원본 `B_original`의 데이터가 최종적으로 업데이트됩니다.

---

## `PyArrayObject_fields`와의 관계

* **`flags`:** 이 배열이 `WRITEBACKIFCOPY` 상태인지 나타냅니다.
* **`base`:** `WRITEBACKIFCOPY` 플래그가 설정된 배열(임시 사본)의 `base` 포인터는, **반드시** 나중에 데이터가 다시 쓰여져야 할 **원본 배열**을 가리켜야 합니다. 이는 '뷰(view)'에서의 `base` 역할(메모리 소유권)과는 다른, 특별한 용도입니다.

## 주요 사용처

* **`ufunc` (Universal Functions):** `ufunc`의 `out` 인자로 전달된 배열이 요구 사항(타입, 레이아웃)에 맞지 않을 때, 임시 '출력 버퍼'를 만들고 `WRITEBACKIFCOPY`를 사용하여 계산 결과를 최종 `out` 배열에 다시 써넣습니다.
* **`PyArray_GetArrayParamsFromObject`:** Python 객체를 C 레벨 `PyArrayObject`로 변환할 때, 요구되는 속성을 맞추기 위해 이 메커니즘이 사용될 수 있습니다.

이 메커니즘 덕분에 NumPy는 다양한 형태의 배열을 유연하게 처리하면서도 데이터 변경 사항이 원본에 정확히 반영되도록 보장할 수 있습니다.


## 관련 문서
[[Contiguous|Contigous]]
