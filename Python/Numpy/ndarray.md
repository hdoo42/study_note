---
id: ndarray
aliases: []
tags:
  - impl
---

> [!IMPORTANT]
> From `numpy/numpy/_core/include/numpy/ndarraytypes.h`

```c
/*
 * The main array object structure.
 *
 * It has been recommended to use the inline functions defined below
 * (PyArray_DATA and friends) to access fields here for a number of
 * releases. Direct access to the members themselves is deprecated.
 * To ensure that your code does not use deprecated access,
 * #define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
 * (or NPY_1_8_API_VERSION or higher as required).
 */
/* This struct will be moved to a private header in a future release */
typedef struct tagPyArrayObject_fields {
    PyObject_HEAD
    /* Pointer to the raw data buffer */
    char *data;
    /* The number of dimensions, also called 'ndim' */
    int nd;
    /* The size in each dimension, also called 'shape' */
    npy_intp *dimensions;
    /*
     * Number of bytes to jump to get to the
     * next element in each dimension
     */
    npy_intp *strides;
    /*
     * This object is decref'd upon
     * deletion of array. Except in the
     * case of WRITEBACKIFCOPY which has
     * special handling.
     *
     * For views it points to the original
     * array, collapsed so no chains of
     * views occur.
     *
     * For creation from buffer object it
     * points to an object that should be
     * decref'd on deletion
     *
     * For WRITEBACKIFCOPY flag this is an
     * array to-be-updated upon calling
     * PyArray_ResolveWritebackIfCopy
     */
    PyObject *base;
    /* Pointer to type structure */
    PyArray_Descr *descr;
    /* Flags describing array -- see below */
    int flags;
    /* For weak references */
    PyObject *weakreflist;
#if NPY_FEATURE_VERSION >= NPY_1_20_API_VERSION
    void *_buffer_info;  /* private buffer info, tagged to allow warning */
#endif
    /*
     * For malloc/calloc/realloc/free per object
     */
#if NPY_FEATURE_VERSION >= NPY_1_22_API_VERSION
    PyObject *mem_handler;
#endif
} PyArrayObject_fields;
```

`PyArrayObject_fields`는 NumPy의 C 레벨 핵심 구조체로, 모든 `ndarray` 객체의 기반이 됩니다. 이 구조체는 배열의 데이터 버퍼, 차원, 모양, 메모리 레이아웃(strides) 등 배열을 정의하는 모든 필수 정보를 담고 있습니다.

> ℹ️ **참고:** C 코드 주석에서 언급했듯이, NumPy C API를 사용할 때는 이 구조체 멤버에 직접 접근하는 것이 비권장(deprecated)됩니다. 대신 `PyArray_DATA(arr)`, `PyArray_NDIM(arr)`, `PyArray_SHAPE(arr)`와 같은 공식 매크로와 함수를 사용해야 향후 버전과의 호환성을 보장할 수 있습니다.

---

## 구조체 멤버 상세

다음은 `PyArrayObject_fields` 구조체를 구성하는 주요 멤버들입니다.

### `PyObject_HEAD`
Python 객체의 표준 헤더 매크로입니다. 모든 CPython 객체는 이 헤더로 시작해야 합니다. 여기에는 다음이 포함됩니다:
* **참조 카운트 (Reference Count):** 객체가 얼마나 많이 참조되는지를 추적하여, 0이 되면 메모리에서 해제합니다.
* **타입 객체 포인터 (`ob_type`):** 객체의 타입(이 경우 `PyArray_Type`)을 가리킵니다.

### `char *data`
배열의 원시(raw) 데이터가 저장된 메모리 버퍼의 시작 주소를 가리키는 포인터입니다.
* `char *` (바이트 포인터) 타입인 이유는, 이 버퍼가 `float64`, `int32`, `uint8` 또는 복합 구조체 등 어떤 데이터 타입이든 담을 수 있어야 하기 때문입니다.
* 실제 데이터의 타입과 해석 방법은 `descr` 멤버가 결정합니다.

### `int nd`
배열의 차원 수(Number of Dimensions)를 나타냅니다.
* Python의 `ndarray.ndim` 속성에 해당합니다.
* 예: 1차원 벡터는 `nd=1`, 2차원 행렬은 `nd=2`, 3차원 텐서는 `nd=3`입니다.

### `npy_intp *dimensions`
배열의 각 차원별 크기, 즉 **형태(shape)** 를 저장하는 C 배열을 가리키는 포인터입니다.
* 이 C 배열의 길이는 `nd`와 같습니다.
* Python의 `ndarray.shape` 튜플에 해당합니다.
* 예: `(3, 4)` 형태의 배열은 `nd=2`이며, `dimensions`는 `[3, 4]` 값을 가진 메모리 주소를 가리킵니다.

### `npy_intp *strides`
**NumPy의 핵심 기능인 '뷰(View)'와 효율적인 메모리 접근을 가능하게 하는 가장 중요한 멤버입니다.**
* `strides`는 각 차원에서 **다음 원소로 이동하기 위해 건너뛰어야 할 바이트(byte) 수**를 정의하는 C 배열입니다.
* 이 배열의 길이 역시 `nd`와 같습니다.
* **예시:** 8바이트(`float64`) 타입을 가진 `(3, 4)` 형태의 C-contiguous (C 스타일) 배열
    * `dimensions`: `[3, 4]`
    * `strides`: `[32, 8]`
        * **`strides[1] = 8`**: 1번 차원(열)에서 다음 원소로 가려면 $8$바이트($= 1 \times 8$)를 이동합니다.
        * **`strides[0] = 32`**: 0번 차원(행)에서 다음 원소로 가려면 $32$바이트($= 4 \times 8$)를 이동합니다.
### `PyObject *base`
메모리 관리와 '뷰(view)' 메커니즘을 담당하는 멤버입니다.
* **뷰(View)의 경우:** 만약 이 배열이 다른 배열의 '뷰'(예: 슬라이싱)라면, `base`는 원본이 되는 배열 객체를 가리킵니다. 이는 원본 배열의 데이터가 메모리에서 해제되지 않도록 참조 카운트를 유지하는 역할을 합니다.
* **데이터 소유(Own)의 경우:** 배열이 `np.zeros()`처럼 데이터를 직접 생성하고 소유한 경우, `base`는 `NULL`일 수 있습니다. (데이터 소유 여부는 `flags` 멤버의 `NPY_ARRAY_OWNDATA`로 확인합니다.)
* **[[WRITEBACKIFCOPY|WRITEBACKIFCOPY]]:** 특별한 메모리 관리 플래그가 설정된 경우, `base`는 쓰기 작업이 완료된 후 데이터를 복사해야 할 원본 배열을 가리킬 수 있습니다.

### `PyArray_Descr *descr`
배열의 **데이터 타입(Data Type)**을 설명하는 `PyArray_Descr` 구조체를 가리키는 포인터입니다.
* Python의 `ndarray.dtype` 객체에 해당합니다.
* 여기에는 다음과 같은 상세 정보가 포함됩니다:
    * 타입 (예: 'f' for float, 'i' for int)
    * 원소의 크기 (itemsize, 예: `float64`는 8바이트)
    * 바이트 순서 (Endianness: 리틀 엔디안 / 빅 엔디안)

### `int flags`
배열의 속성과 상태를 나타내는 정수형 비트 플래그입니다. 주요 플래그는 다음과 같습니다:
* `NPY_ARRAY_C_CONTIGUOUS`: C 스타일 (행 우선) 메모리 연속성 여부.
* `NPY_ARRAY_F_CONTIGUOUS`: Fortran 스타일 (열 우선) 메모리 연속성 여부.
* `NPY_ARRAY_OWNDATA`: 이 배열 객체가 `data` 버퍼의 소유자인지 여부. `False`이면 `base` 객체가 데이터를 소유한 '뷰'입니다.
* `NPY_ARRAY_WRITEABLE`: 배열이 쓰기 가능한지 여부.

### `PyObject *weakreflist`
Python의 약한 참조(weak references)를 지원하기 위한 표준 CPython 필드입니다.

### `void *_buffer_info` (NPY_1_20+)
Python의 PEP 3118 버퍼 프로토콜을 지원하기 위한 내부용 프라이빗 필드입니다.

### `PyObject *mem_handler` (NPY_1_22+)
NumPy가 기본 `malloc`/`free` 대신 사용자 정의 메모리 할당자(custom memory allocator)를 사용할 수 있도록 지원하는 필드입니다.

---

이 구조체에 대해 더 궁금한 점이 있나요? 예를 들어, `strides`가 C 스타일과 Fortran 스타일 배열에서 어떻게 달라지는지, 또는 `PyArray_Descr` (dtype) 구조체는 어떻게 구성되어 있는지 더 자세히 설명해 드릴 수 있습니다.

