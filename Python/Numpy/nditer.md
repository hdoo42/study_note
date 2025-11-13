```c
/*
 * The data layout of the iterator is fully specified by
 * a triple (itflags, ndim, nop).  These three variables
 * are expected to exist in all functions calling these macros,
 * either as true variables initialized to the correct values
 * from the iterator, or as constants in the case of specialized
 * functions such as the various iternext functions.
 */

struct NpyIter_InternalOnly {
    /* Initial fixed position data */
    npy_uint32 itflags;
    npy_uint8 ndim;
    int nop, maskop;
    npy_intp itersize, iterstart, iterend;
    /* iterindex is only used if RANGED or BUFFERED is set */
    npy_intp iterindex;
    /* The rest is variable */
    char iter_flexdata[];
};
```

이 구조체는 **NumPy(넘파이)의 C API 내부**에서 사용되는 `NpyIter` (NumPy 이터레이터)의 핵심 데이터 구조입니다. 이름(`InternalOnly`)에서 알 수 있듯이, NumPy 라이브러리 내부 구현용이며 외부에서 직접 사용하도록 설계되지 않았습니다.

이 구조체는 **이터레이터 객체의 '헤더(header)'** 역할을 합니다.

### 🔭 주요 특징: 유연한 배열 멤버 (Flexible Array Member)

이 구조체를 이해하는 데 가장 중요한 특징은 마지막 필드인 `char iter_flexdata[];`입니다.
- 이것은 C99 표준의 **'유연한 배열 멤버(flexible array member)'** 기능입니다.
- 이것의 의미는 `NpyIter_InternalOnly` 구조체 자체는 이터레이터에 필요한 고정된 크기의 '헤더' 정보만을 담고, 실제 이터레이션에 필요한 **가변적인 크기의 데이터** (예: 각 피연산자의 정보, 스트라이드(stride), 차원 크기 등)가 이 구조체 바로 뒤에 연속적인 메모리 블록으로 할당된다는 뜻입니다.
- `iter_flexdata`는 그 가변 데이터가 시작되는 위치를 가리키는 일종의 '핸들'처럼 사용됩니다.

---

### 🔧 필드별 설명

함께 제공된 주석에 따르면, `itflags`, `ndim`, `nop` 세 가지 변수가 이터레이터의 전체 데이터 레이아웃을 정의하는 핵심 요소입니다.

- `npy_uint32 itflags`:
    
    - 이터레이터의 **동작을 제어하는 플래그(bit flags)** 집합입니다.
        
    - 예를 들어, '읽기 전용', '쓰기 가능', '버퍼링 사용' 등의 상태를 비트로 저장합니다.
        
- `npy_uint8 ndim`:
    
    - 이터레이션이 처리할 **배열의 차원 수(number of dimensions)**를 나타냅니다.
        
- `int nop`:
    
    - 이터레이터가 한 번에 처리하는 **피연산자(operands)의 수**입니다.
        
    - 예를 들어, `c = a + b` 연산이라면 `a`, `b`, `c` 세 개의 피연산자(`nop=3`)가 있을 수 있습니다.
        
- `int maskop`:
    
    - 피연산자 중 **마스크(mask)로 사용되는 피연산자**가 있는지, 있다면 그 인덱스가 몇 번인지를 저장합니다. (NumPy의 마스킹 연산에 사용)
        
- `npy_intp itersize`:
    
    - 이터레이션의 **총 크기** (전체 요소 수)입니다. `npy_intp`는 포인터/인덱스용 정수 타입입니다.
        
- `npy_intp iterstart`, `iterend`:
    
    - 이터레이션이 **특정 범위(range)만** 다루도록 설정된 경우, 그 시작과 끝 인덱스를 저장합니다.
        
- `npy_intp iterindex`:
    
    - 현재 이터레이션이 진행 중인 **위치(인덱스)**입니다. 주석에 언급된 대로 'RANGED' 또는 'BUFFERED' 플래그가 설정되었을 때 사용됩니다.
        
- `char iter_flexdata[]`:
    
    - 위에서 설명한 대로, 이 구조체 헤더 뒤에 바로 따라붙는 **가변 길이 데이터 영역의 시작점**을 나타냅니다.
        

요약하자면, 이 구조체는 NumPy가 다차원 배열을 효율적으로 순회하기 위해 필요한 모든 고정 메타데이터(플래그, 차원, 피연산자 수 등)를 담는 헤더이며, 실제 데이터 포인터나 스트라이드 같은 가변 정보는 이 헤더 직후의 메모리(`iter_flexdata`가 가리키는 위치)에 저장됩니다.
