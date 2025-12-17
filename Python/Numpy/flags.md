---
id: 1763016599-LOUH
aliases:
  - flag
tags: []
---
이 플래그들은 NumPy C-API 레벨에서 `PyArrayObject` (Python의 `ndarray`)의 메모리 레이아웃, 속성, 그리고 `NpyIter` (반복자)의 동작 방식을 제어하는 데 사용되는 비트 마스크(bitmask)입니다.

-----

## 1\. NumPy ndarray 플래그 (NPY\_ARRAY\_\*)

`ndarray` 객체의 속성을 나타내거나, 배열 생성 함수에 특정 속성을 요청하기 위해 사용됩니다.

### 📜 주요 속성 및 메모리 플래그

이 플래그들은 `PyArray_FLAGS(arr)` 매크로를 통해 **기존 배열의 상태를 확인**하는 데 주로 사용됩니다.

| 플래그                             | 값 (Hex)  | 설명                                                                                                                                                          |
| :------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`NPY_ARRAY_C_CONTIGUOUS`**    | `0x0001` | **C-스타일 메모리 연속성**을 나타냅니다. (Row-major) <br> 마지막 차원(인덱스)이 메모리에서 가장 빠르게 변합니다.                                                                                  |
| **`NPY_ARRAY_F_CONTIGUOUS`**    | `0x0002` | **Fortran-스타일 메모리 연속성**을 나타냅니다. (Column-major) <br> 첫 번째 차원(인덱스)이 메모리에서 가장 빠르게 변합니다.                                                                        |
| **`NPY_ARRAY_OWNDATA`**         | `0x0004` | 배열 객체가 \*\*자신이 가리키는 데이터의 소유권(OWNDATA)\*\*을 가짐을 의미합니다. <br> 이 플래그가 설정되면, 배열 객체가 소멸될 때 데이터도 함께 해제(`free`)됩니다.                                                 |
| **`NPY_ARRAY_ALIGNED`**         | `0x0100` | 배열 데이터가 해당 데이터 타입에 맞게 \*\*메모리 정렬(ALIGNED)\*\*되어 있음을 의미합니다. <br> (예: 8바이트 double은 8의 배수 주소에서 시작)                                                             |
| **`NPY_ARRAY_WRITEABLE`**       | `0x0400` | 배열 데이터가 \*\*쓰기 가능(WRITEABLE)\*\*함을 의미합니다.                                                                                                                   |
| **`NPY_ARRAY_WRITEBACKIFCOPY`** | `0x2000` | 이 배열이 다른 배열의 복사본이며, 소멸 시 원본 배열에 변경 사항을 \*\*다시 써야 함([[WRITEBACKIFCOPY\|WRITEBACKIFCOPY]])\*\*을 나타냅니다. <br> 주로 `PyArray_ResolveWritebackIfCopy` 함수와 함께 사용됩니다. |

### 📥 함수 인자용 요청 플래그

이 플래그들은 `PyArray_FromAny`와 같은 배열 생성 함수에 인자로 전달되어 **원하는 배열의 속성을 요청**하는 데 사용됩니다.

| 플래그 | 값 (Hex) | 설명 |
| :--- | :--- | :--- |
| **`NPY_ARRAY_FORCECAST`** | `0x0010` | 안전하지 않더라도 \*\*강제 형 변환(FORCECAST)\*\*을 허용합니다. |
| **`NPY_ARRAY_ENSURECOPY`** | `0x0020` | 항상 \*\*새로운 복사본(ENSURECOPY)\*\*을 생성하도록 강제합니다. <br> (결과물은 항상 `CONTIGUOUS`, `ALIGNED`, `WRITEABLE`이 보장됩니다.) |
| **`NPY_ARRAY_ENSUREARRAY`** | `0x0040` | 반환 값이 `ndarray`의 서브클래스가 아닌 \*\*기본 `ndarray` 객체(ENSUREARRAY)\*\*임을 보장합니다. |
| **`NPY_ARRAY_ELEMENTSTRIDES`** | `0x0080` | `strides` 배열이 바이트(byte) 단위가 아닌 **요소 크기(ELEMENTSTRIDES)** 단위인지 확인합니다. <br> (주로 레코드 배열(record-array)에서 사용됩니다.) |
| **`NPY_ARRAY_NOTSWAPPED`** | `0x0200` | 배열 데이터가 \*\*네이티브 엔디언(NOTSWAPPED)\*\*인지 확인합니다. (바이트 스왑이 필요 없음) |
| **`NPY_ARRAY_ENSURENOCOPY`** | `0x4000` | \*\*복사본 생성을 금지(ENSURENOCOPY)\*\*합니다. <br> (View를 반환할 수 없는 경우 오류가 발생합니다.) |

### 🔀 조합 플래그

자주 사용되는 플래그 조합을 미리 정의해 둔 매크로입니다.

| 플래그 | 구성 | 설명 |
| :--- | :--- | :--- |
| **`NPY_ARRAY_BEHAVED`** | `ALIGNED \| WRITEABLE` | 잘 동작하는(BEHAVED) 배열 (정렬되고 쓰기 가능) |
| **`NPY_ARRAY_CARRAY`** | `C_CONTIGUOUS \| BEHAVED` | 일반적인 C-스타일 배열 (C 연속성, 정렬됨, 쓰기 가능) |
| **`NPY_ARRAY_FARRAY`** | `F_CONTIGUOUS \| BEHAVED` | 일반적인 Fortran-스타일 배열 (F 연속성, 정렬됨, 쓰기 가능) |
| **`NPY_ARRAY_CARRAY_RO`** | `C_CONTIGUOUS \| ALIGNED` | C-스타일 읽기 전용(Read-Only) 배열 |
| **`NPY_ARRAY_FARRAY_RO`** | `F_CONTIGUOUS \| ALIGNED` | Fortran-스타일 읽기 전용(Read-Only) 배열 |
| **`NPY_ARRAY_DEFAULT`** | `NPY_ARRAY_CARRAY` | 배열 생성 시 기본값 |
| **`NPY_ARRAY_IN_ARRAY`** | `NPY_ARRAY_CARRAY_RO` | 함수의 **입력(IN)** 인자로 적합한 배열 (C-RO) |
| **`NPY_ARRAY_OUT_ARRAY`** | `NPY_ARRAY_CARRAY` | 함수의 **출력(OUT)** 인자로 적합한 배열 (C-RW) |
| **`NPY_ARRAY_INOUT_ARRAY`** | `NPY_ARRAY_CARRAY` | 함수의 **입출력(INOUT)** 인자로 적합한 배열 (C-RW) |

-----

## 2\. NumPy 반복자 플래그 (NPY\_ITER\_\*)

`NpyIter` (NumPy C-API의 핵심 반복자)를 생성할 때 반복 방식과 각 피연산자(operand)의 요구 사항을 지정하는 플래그입니다.

### 🌐 전역 반복자 플래그 (Global Flags)

이터레이터 전체의 동작을 제어합니다.

| 플래그 | 값 (Hex) | 설명 |
| :--- | :--- | :--- |
| **`NPY_ITER_C_INDEX`** | `0x00000001` | 반복 중에 **C-스타일 인덱스**를 추적합니다. |
| **`NPY_ITER_F_INDEX`** | `0x00000002` | 반복 중에 **Fortran-스타일 인덱스**를 추적합니다. |
| **`NPY_ITER_MULTI_INDEX`** | `0x00000004` | 반복 중에 **다차원 인덱스**(`multi-index`)를 추적합니다. |
| **`NPY_ITER_EXTERNAL_LOOP`** | `0x00000008` | 이터레이터가 아닌 \*\*외부 사용자 코드(EXTERNAL\_LOOP)\*\*가 최내곽 1차원 루프를 직접 처리하도록 합니다. (UFunc의 핵심 최적화) |
| **`NPY_ITER_COMMON_DTYPE`** | `0x00000010` | 모든 피연산자를 \*\*공통 데이터 타입(COMMON\_DTYPE)\*\*으로 변환(캐스팅)합니다. |
| **`NPY_ITER_REFS_OK`** | `0x00000020` | 피연산자가 객체 참조(reference)를 포함해도 괜찮음(REFS\_OK)을 나타냅니다. (이 경우 GIL이 필요할 수 있음) |
| **`NPY_ITER_ZEROSIZE_OK`** | `0x00000040` | 크기가 0인 피연산자를 허용합니다. |
| **`NPY_ITER_REDUCE_OK`** | `0x00000080` | 리덕션(reduction) 연산을 허용합니다. (예: `axis`가 지정된 `sum`) |
| **`NPY_ITER_RANGED`** | `0x00000100` | 전체 배열이 아닌 특정 범위(RANGED)에 대해서만 반복할 수 있게 합니다. |
| **`NPY_ITER_BUFFERED`** | `0x00000200` | \*\*버퍼링(BUFFERED)\*\*을 활성화합니다. <br> (데이터 타입 변환이나 메모리 정렬이 필요할 때 내부 버퍼를 사용합니다.) |
| **`NPY_ITER_GROWINNER`** | `0x00000400` | 버퍼링 사용 시, 가능한 경우 내부 루프의 크기를 동적으로 \*\*확장(GROWINNER)\*\*합니다. |
| **`NPY_ITER_COPY_IF_OVERLAP`** | `0x00002000` | 피연산자 간 메모리 **겹침(OVERLAP)이 감지되면 임시 복사본**을 만들어 안전하게 연산합니다. |

### ↘️ 피연산자별 반복자 플래그 (Per-Operand Flags)

이터레이터에 전달되는 \*\*각 배열(피연산자)\*\*의 역할과 요구 사항을 지정합니다.

| 플래그 | 값 (Hex) | 설명 |
| :--- | :--- | :--- |
| **`NPY_ITER_READWRITE`** | `0x00010000` | 피연산자를 **읽고 쓰는(READWRITE)** 용도로 사용합니다. |
| **`NPY_ITER_READONLY`** | `0x00020000` | 피연산자를 \*\*읽기 전용(READONLY)\*\*으로 사용합니다. |
| **`NPY_ITER_WRITEONLY`** | `0x00040000` | 피연산자를 \*\*쓰기 전용(WRITEONLY)\*\*으로 사용합니다. |
| **`NPY_ITER_NBO`** | `0x00080000` | 피연산자 데이터가 \*\*네이티브 바이트 순서(NBO)\*\*여야 함을 요구합니다. |
| **`NPY_ITER_ALIGNED`** | `0x00100000` | 피연산자 데이터가 \*\*메모리 정렬(ALIGNED)\*\*되어야 함을 요구합니다. |
| **`NPY_ITER_CONTIG`** | `0x00200000` | 피연산자 데이터가 (최소한 내부 루프 내에서는) \*\*연속적(CONTIG)\*\*이어야 함을 요구합니다. |
| **`NPY_ITER_COPY`** | `0x00400000` | 위 요구사항(NBO, ALIGNED, CONTIG)을 만족하기 위해 **복사(COPY)를 허용**합니다. |
| **`NPY_ITER_UPDATEIFCOPY`** | `0x00800000` | `COPY`와 동일하지만, 복사본 생성 시 `NPY_ARRAY_WRITEBACKIFCOPY` 플래그를 사용합니다. |
| **`NPY_ITER_ALLOCATE`** | `0x01000000` | 이 피연산자(배열)가 `NULL`인 경우, 이터레이터가 적절한 크기로 \*\*새로 할당(ALLOCATE)\*\*합니다. (UFunc의 `out` 인자 처리) |
| **`NPY_ITER_NO_BROADCAST`** | `0x08000000` | 이 피연산자에 대해 **브로드캐스팅(BROADCAST)을 금지**합니다. |
| **`NPY_ITER_WRITEMASKED`** | `0x10000000` | 이 피연산자는 \*\*마스크된 쓰기(WRITEMASKED)\*\*를 지원합니다. |
| **`NPY_ITER_ARRAYMASK`** | `0x20000000` | 이 피연산자가 `WRITEMASKED` 연산을 위한 \*\*마스크 배열(ARRAYMASK)\*\*임을 나타냅니다. |

-----

## 3\. 기타 C-API 매크로

제공된 코드 스니펫에는 플래그 외에 유용한 매크로들도 포함되어 있습니다.

  * **플래그 확인 매크로:**

      * `PyArray_ISCONTIGUOUS(m)`: `(m)`이 C-스타일 연속적인지 확인합니다.
      * `PyArray_ISWRITEABLE(m)`: `(m)`이 쓰기 가능한지 확인합니다.
      * `PyArray_ISALIGNED(m)`: `(m)`이 정렬되어 있는지 확인합니다.
      * `PyArray_IS_C_CONTIGUOUS(m)`: `PyArray_ISCONTIGUOUS`와 동일합니다.
      * `PyArray_IS_F_CONTIGUOUS(m)`: `(m)`이 Fortran-스타일 연속적인지 확인합니다.

  * **스레딩 및 GIL 관리 매크로:**

      * `NPY_BEGIN_ALLOW_THREADS`: C 코드에서 시간이 오래 걸리는 계산을 수행하기 전에 Python의 GIL(Global Interpreter Lock)을 **해제**합니다. (내부적으로 `Py_BEGIN_ALLOW_THREADS` 사용)
      * `NPY_END_ALLOW_THREADS`: 계산 완료 후 GIL을 **다시 획득**합니다. (내부적으로 `Py_END_ALLOW_THREADS` 사용)
      * `NPY_BEGIN_THREADS`: GIL을 해제하고 스레드 상태를 저장합니다. (`PyEval_SaveThread`)
      * `NPY_END_THREADS`: 스레드 상태를 복원하고 GIL을 다시 획득합니다. (`PyEval_RestoreThread`)
      * `NPY_ALLOW_C_API`: C 콜백 함수 등에서 Python C-API를 안전하게 호출할 수 있도록 GIL 상태를 보장합니다. (`PyGILState_Ensure`)
      * `NPY_DISABLE_C_API`: `NPY_ALLOW_C_API` 이전의 GIL 상태로 복원합니다. (`PyGILState_Release`)

