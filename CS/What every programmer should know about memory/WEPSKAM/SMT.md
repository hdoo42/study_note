**SMT(Simultaneous Multithreading, 동시 멀티스레딩)** 의 가장 엄밀하고 컴퓨터 아키텍처 교과서(예: _Hennessy & Patterson_)적인 정의와 해설을 정리해 드립니다.

---

### 1. 엄밀한 정의 (Formal Definition)

**SMT**란, **"하나의 물리적 프로세서 내에서, 여러 개의 독립적인 스레드(Thread)로부터 온 명령어(Instruction)들을 동일한 클럭 사이클(Cycle)에 동시에 이슈(Issue)하여 실행 유닛(Functional Unit)을 공유하는 하드웨어 기술"** 입니다.

여기서 핵심은 **'동일한 사이클(Same Cycle)'** 입니다. 기존의 멀티스레딩(Temporal Multithreading)이 사이클 단위로 스레드를 번갈아 처리했다면, SMT는 한 사이클 내의 **명령어 슬롯(Issue Slots)** 자체를 여러 스레드가 나누어 씁니다.

---

### 2. 아키텍처적 배경과 원리 (Architectural Background)

SMT를 이해하려면 먼저 **슈퍼스칼라(Superscalar)** 구조와 **자원 낭비(Waste)** 의 개념을 이해해야 합니다.

#### 2.1. 전제 조건: 슈퍼스칼라 (Superscalar)

현대의 고성능 CPU는 한 사이클에 여러 개의 명령어(예: 4개, 6개 등)를 동시에 실행할 수 있는 **슈퍼스칼라** 구조입니다. 즉, 덧셈기(ALU), 곱셈기, 메모리 로드 유닛 등 **실행 유닛(Functional Unit)** 이 여러 개 존재합니다.

#### 2.2. 문제점: 두 가지 종류의 낭비 (Waste)

단일 스레드만 실행할 경우, 슈퍼스칼라 프로세서에는 필연적으로 두 가지 빈 공간이 발생합니다.

1. **수직적 낭비 (Vertical Waste):**
    
    - 캐시 미스(Cache Miss)나 분기 예측 실패 등으로 인해, 파이프라인 전체가 멈추는(Stall) 사이클입니다. 이 시간 동안 CPU는 아무것도 하지 않습니다.
        
2. **수평적 낭비 (Horizontal Waste):**
    
    - CPU는 한 번에 4개의 명령어를 처리할 수 있는데(4-issue width), 현재 프로그램의 의존성(Dependency) 때문에 2개만 실행 가능한 경우입니다. 나머지 2개의 슬롯은 낭비됩니다. **ILP(Instruction Level Parallelism, 명령어 수준 병렬성)** 의 한계 때문입니다.
        

#### 2.3. SMT의 해결책: TLP로 ILP 보완

SMT는 **스레드 수준 병렬성(TLP, Thread Level Parallelism)** 을 이용해 이 빈 공간을 메웁니다.

- **수직적 빈 공간**은 다른 스레드의 명령어로 채웁니다.
    
- **수평적 빈 공간**도 다른 스레드의 명령어로 채웁니다. (이것이 SMT의 가장 큰 특징입니다.)
    

---

### 3. 하드웨어 구현 (Hardware Implementation)

교과서적으로 SMT 프로세서는 자원을 **복제(Replicated)** 하는 것과 **공유(Shared)** 하는 것으로 엄격히 구분합니다.

|**구분**|**자원 목록**|**설명**|
|---|---|---|
|**복제 (Replicated)**|**Architectural State**<br><br>  <br><br>(PC, Register File, Rename Table 등)|각 스레드의 실행 흐름과 문맥(Context)을 유지하기 위해 필수적인 **논리적 상태**입니다. 운영체제가 2개의 CPU로 인식하는 근거가 됩니다.|
|**공유 (Shared)**|**Execution Resources**<br><br>  <br><br>(ALU, FPU, L1/L2 Cache, TLB, Branch Predictor)|실제 연산을 수행하거나 데이터를 저장하는 **물리적 자원**입니다. 이 거대한 자원들을 놀리지 않고 공유하는 것이 SMT의 목적입니다.|

- **Partitioned Resources (분할 자원):** 일부 자원(예: Reorder Buffer, Load/Store Queue)은 설계에 따라 스레드 별로 정적 분할하거나 동적으로 경쟁하며 공유합니다.
    

---

### 4. 다른 멀티스레딩 기술과의 비교 (엄밀한 구분)

교과서에서는 SMT를 설명할 때 반드시 **시분할 멀티스레딩(Temporal Multithreading)** 과 비교합니다.

1. **Coarse-Grained Multithreading (거친 입자 멀티스레딩):**
    
    - 긴 지연(예: L2 캐시 미스)이 발생했을 때만 스레드를 교체합니다. 스위칭 오버헤드가 있습니다.
        
2. **Fine-Grained Multithreading (미세 입자 멀티스레딩):**
    
    - 매 사이클마다 라운드 로빈 방식으로 스레드를 교체합니다. 수직적 낭비는 줄이지만, 수평적 낭비(한 사이클 내의 빈 슬롯)는 해결하지 못합니다.
        
3. **Simultaneous Multithreading (SMT):**
    
    - **한 사이클 내에서** 여러 스레드의 명령어를 섞어서 이슈(Issue)합니다. 수직/수평 낭비를 모두 최소화하여 처리량(Throughput)을 극대화합니다.
        

### 5. 요약 (Summary)

> **SMT는 슈퍼스칼라 프로세서의 낭비되는 이슈 슬롯(Issue Slot)과 실행 유닛(Functional Unit)을 활용하기 위해, 아키텍처 상태(State)만 복제하고 실행 자원은 공유하여, TLP(스레드 병렬성)를 통해 부족한 ILP(명령어 병렬성)를 하드웨어적으로 보완하는 기술입니다.**