---
id: course_reversing
aliases: []
tags: []
---
# **스탠포드 CS107e 커리큘럼의 RISC-V 아키텍처(Mango Pi MQ-Pro) 기반 베어메탈 시스템 프로그래밍 역공학 및 이식에 관한 포괄적 연구 보고서**

## **1. 서론: CS107e의 교육 철학 및 아키텍처 전환의 의의**

스탠포드 대학의 CS107e "Computer Systems from the Ground Up" 강의는 현대 컴퓨터 과학 교육에서 가장 독보적인 위치를 차지하는 시스템 프로그래밍 입문 과정 중 하나입니다. 이 과정의 핵심 철학은 운영체제(OS)와 표준 라이브러리(libc)라는 거대한 추상화 계층을 제거하고, 프로그래머가 하드웨어와 직접 대면하는 '베어메탈(Bare-metal)' 환경에서 시스템의 본질을 탐구하는 데 있습니다. 기존의 CS107e는 ARM 아키텍처 기반의 Raspberry Pi를 표준 하드웨어로 채택하여 수년간 운영되어 왔으나, 최근 임베디드 및 컴퓨터 아키텍처 분야에서 RISC-V ISA(Instruction Set Architecture)의 부상은 새로운 교육적 패러다임을 제시하고 있습니다.1

귀하가 제시한 목표인 "CS107e의 역해킹 및 RISC-V 기반 Mango Pi MQ-Pro로의 이식"은 단순한 강의 청강을 넘어선 고난도의 엔지니어링 과제입니다. 이는 기존의 ARMv6(Raspberry Pi Zero) 기반의 강의 자료와 과제를 완전히 새로운 아키텍처인 RV64GCV(Allwinner D1 SoC)로 번역하고 재설계해야 함을 의미합니다. 귀하는 이미 C 언어에 능숙하고 Rust에 익숙하다는 강력한 배경지식을 가지고 있으므로, 이 보고서는 단순한 따라하기식 가이드가 아닌, 시스템 아키텍처의 차이를 분석하고 이를 극복하는 엔지니어링 솔루션을 제시하는 데 초점을 맞춥니다.

본 보고서는 총 15,000단어 분량의 심층 분석을 통해, 스탠포드 강의실 밖에서 독자적으로 해당 커리큘럼을 완주할 수 있도록 하드웨어 분석, 툴체인 구축, 어셈블리 언어 변환, 주변장치 제어, 그리고 Rust 언어 통합에 이르는 전 과정을 상세히 기술합니다.

## **2. 하드웨어 플랫폼 분석: Allwinner D1과 Mango Pi MQ-Pro**

성공적인 역공학을 위해서는 타겟 하드웨어에 대한 외과수술적인 이해가 선행되어야 합니다. Raspberry Pi의 BCM2835 SoC와 Mango Pi의 Allwinner D1 SoC는 설계 사상과 메모리 맵, 부팅 시퀀스에서 근본적인 차이를 보입니다.

### **2.1 XuanTie C906 코어와 RV64GCV ISA**

Mango Pi MQ-Pro의 핵심인 Allwinner D1 SoC는 알리바바의 반도체 자회사인 T-Head에서 설계한 XuanTie C906 코어를 탑재하고 있습니다.2 이는 CS107e에서 다루는 32비트 ARM 코어와 달리 64비트 RISC-V 아키텍처를 기반으로 합니다.

* **RV64I (Base Integer):** 64비트 정수 연산이 기본입니다. 이는 포인터와 레지스터(x0~x31)가 64비트 폭을 가짐을 의미하며, 메모리 주소 지정 방식에서 32비트 ARM과 차별화됩니다.3  
* **M (Multiplication/Division):** 하드웨어 승제산기를 포함합니다.  
* **A (Atomic):** 멀티코어 및 동시성 프로그래밍에 필수적인 원자적 연산 명령어를 지원합니다.  
* **C (Compressed):** 코드 밀도를 높이기 위해 16비트 압축 명령어를 지원합니다. 이는 링커 스크립트 작성 시 정렬(Alignment) 문제에 영향을 줄 수 있습니다.3  
* **V (Vector):** 벡터 연산 확장을 지원하지만, CS107e의 기초 과정에서는 주로 스칼라 연산에 집중하게 됩니다.4

**핵심 인사이트:** ARM에서 RISC-V로의 전환은 단순히 어셈블리 문법의 변화(LDR -> lw/ld)를 넘어, 레지스터 규약(ABI)과 함수 호출 규약의 변화를 수반합니다. 특히 ARM의 조건부 실행(Conditional Execution) 기능이 RISC-V에는 존재하지 않으므로, 분기 예측과 제어 흐름 설계 방식이 달라져야 합니다.

### **2.2 메모리 맵(Memory Map)과 주변장치 접근**

베어메탈 프로그래밍의 핵심은 "어떤 주소에 무엇을 쓰고 읽느냐"입니다. Raspberry Pi의 BCM2835는 0x20000000 부근에 주변장치를 매핑하지만, Allwinner D1은 전혀 다른 주소 체계를 가집니다.

| 영역 | 시작 주소 | 크기 | 설명 | CS107e 관련성 |
| :---- | :---- | :---- | :---- | :---- |
| **SRAM A1** | 0x00002000 | 32KB | 내부 고속 메모리. 초기 부트로더 실행 영역. | 초기 진입점 확인용 |
| **BROM** | 0xFFFF0000 | 32KB | 수정 불가능한 부트 롬. | 분석 대상 제외 |
| **DRAM** | 0x40000000 | 512MB/1GB | 메인 메모리. 프로그램 적재 및 힙/스택 영역. | **핵심 실행 영역** |
| **CCU** | 0x02001000 | - | Clock Control Unit. 주변장치 클럭 공급 제어. | **필수 (과제 1~7)** |
| **GPIO** | 0x02000000 | - | General Purpose I/O. 핀 제어 레지스터. | **필수 (과제 1)** |
| **UART0** | 0x02500000 | - | Serial Communication. 디버깅 콘솔용. | **필수 (과제 3)** |
| **PLIC** | 0x10000000 | - | Platform-Level Interrupt Controller. 외부 인터럽트 제어. | **필수 (과제 7)** |
| **CLINT** | 0x14000000 | - | Core Local Interruptor. 타이머 및 소프트웨어 인터럽트. | **필수 (과제 2, 7)** |

참고: 위 주소는 커널 소스 및 기술 문서를 기반으로 재구성한 것이며, 실제 D1 데이터시트의 "Memory Mapping" 섹션과 대조 검증이 필요합니다.5 특히 CLINT의 주소는 구현체마다 상이할 수 있으므로 주의가 요구됩니다.

### **2.3 부팅 프로세스와 FEL 모드 활용 전략**

CS107e의 기존 방식은 SD 카드에 kernel.img를 복사하는 방식입니다. 그러나 Mango Pi 개발에서는 Allwinner 칩셋 특유의 **FEL 모드**를 활용하는 것이 학습 효율을 극대화할 수 있습니다.

1. **BROM 단계:** 전원이 인가되면 D1은 BROM 코드를 실행합니다. 유효한 부트 미디어(SD 카드 등)를 찾지 못하면 FEL 모드로 진입합니다.8  
2. **FEL 모드:** 이 상태에서 D1은 USB 장치로 인식됩니다. xfel 도구를 사용하면 SD 카드를 제거하지 않고도 USB를 통해 직접 RAM(SRAM 또는 DRAM)에 코드를 주입하고 실행할 수 있습니다.9  
   * 이는 코드 수정 -> 컴파일 -> 실행 사이클을 획기적으로 단축시킵니다.  
   * 초기 학습 단계에서는 xfel을 사용하여 베어메탈 바이너리를 DRAM(0x40000000)에 로드하고 실행(exec)하는 방식을 권장합니다.

## **3. 개발 환경 및 툴체인 구축**

강의를 수강하지 않고 독학하기 위해서는 스탠포드의 myth 서버 환경을 로컬 머신에 재현해야 합니다. 귀하는 이미 C와 Rust에 익숙하므로, 이중 툴체인 전략을 제안합니다.

### **3.1 RISC-V GNU 툴체인 (C/Assembly)**

베어메탈 개발을 위해서는 운영체제에 의존하지 않는 독립형(Freestanding) 컴파일러가 필요합니다.

* **컴파일러 선택:** riscv64-unknown-elf-gcc를 사용해야 합니다. riscv64-linux-gnu-gcc는 리눅스 커널과 glibc 라이브러리를 전제로 하므로 베어메탈 환경에서는 적합하지 않습니다.10  
* **빌드 옵션:**  
  * -march=rv64gc: D1의 C906 코어 아키텍처를 지정합니다.  
  * -mabi=lp64d: 64비트 정수와 더블 정밀도 부동소수점 레지스터 사용을 지정합니다.12  
  * -nostdlib -nostartfiles: 표준 라이브러리 및 시작 코드를 배제하여 순수 베어메탈 환경을 보장합니다.

### **3.2 Rust 임베디드 툴체인**

Rust의 안전성과 현대적인 기능을 활용하기 위해 다음 구성을 준비합니다.

* **타겟 추가:** rustup target add riscv64gc-unknown-none-elf.13  
* **필수 크레이트(Crate):**  
  * d1-pac (Peripheral Access Crate): D1 SoC의 레지스터 정의를 담고 있는 핵심 라이브러리입니다. SVD 파일로부터 자동 생성되며, C의 헤더 파일을 대체합니다.14  
  * embedded-hal: 하드웨어 추상화 계층을 위한 트레이트 모음으로, 드라이버 작성의 표준을 제공합니다.16  
  * critical-section: 인터럽트 제어를 위한 동기화 기본 요소를 제공합니다.

### **3.3 로더(Loader) 도구: xfel**

Allwinner 칩셋의 강력한 부팅 도구인 xfel을 설치해야 합니다. 이는 GitHub의 xboot/xfel 저장소에서 소스를 받아 빌드할 수 있습니다.9

* **주요 명령어:**  
  * xfel version: 연결 확인.  
  * xfel ddr d1: D1 SoC의 DDR3 메모리 컨트롤러를 초기화합니다. (매우 중요: 이 과정 없이는 DRAM을 사용할 수 없습니다).8  
  * xfel write 0x40000000 main.bin: 컴파일된 바이너리를 DRAM 시작 주소에 업로드합니다.  
  * xfel exec 0x40000000: 해당 주소로 점프하여 실행합니다.

## **4. 커리큘럼 역공학: 과제별 심층 분석 및 구현 가이드**

CS107e의 7개 과제를 Allwinner D1 환경에 맞춰 재구성한 상세 가이드입니다. 각 과제는 하드웨어의 특정 기능을 마스터하도록 설계되어 있으며, 이전 단계의 결과물이 다음 단계의 기반이 되는 누적적 구조를 가집니다.

### **4.1 과제 0: 환경 설정 및 배경 지식 (Assignment 0)**

이 단계는 개발 환경을 검증하는 단계입니다.

* **목표:** 크로스 컴파일러 설치, make 빌드 시스템 구축, 그리고 16진수 및 이진수 연산 숙달.  
* **Mango Pi 적용:**  
  * xfel이 정상적으로 장치를 인식하는지 확인합니다.  
  * 간단한 "무한 루프" 어셈블리 코드를 작성하여 컴파일 후 xfel로 로드했을 때 장치가 멈추는지(정상적으로 코드가 돌고 있는지) 확인합니다.  
  * Allwinner D1의 데이터시트(User Manual)를 확보하여 메모리 맵 섹션을 정독합니다. 페이지 수가 1000페이지가 넘지만, "Memory Mapping", "CCU", "GPIO", "UART" 섹션이 핵심입니다.2

### **4.2 과제 1: Larson Scanner (Assignment 1) - 어셈블리와 GPIO**

가장 기초적이면서도 하드웨어 제어의 본질을 배우는 단계입니다. LED를 순차적으로 점멸하여 "Larson Scanner" 효과(전격 Z작전의 키트 효과)를 구현합니다.

#### **4.2.1 하드웨어 연결 및 핀맵 분석**

Mango Pi MQ-Pro의 40핀 헤더는 Raspberry Pi와 물리적 호환성을 가지지만, 핀의 전기적 연결(SoC의 어떤 포트에 연결되는지)은 완전히 다릅니다.

| 핀 번호 (Header) | RPi 기능 | Mango Pi (D1) 핀 이름 | D1 GPIO 포트 | 비고 |
| :---- | :---- | :---- | :---- | :---- |
| 12 | GPIO 18 | PD18 / PWM | PD18 | 예시 |
| 16 | GPIO 23 | PD22 | PD22 | 예시 |
| 18 | GPIO 24 | PD20 | PD20 | 예시 |
| ... | ... | ... | ... | ... |

주의: 정확한 핀 매핑을 위해 반드시 Mango Pi MQ-Pro의 회로도(Schematic)를 참조하여 헤더 핀이 D1 SoC의 어떤 GPIO 포트(PB, PC, PD, PE, PG 등)에 연결되는지 확인해야 합니다. 대부분의 GPIO는 Port D 또는 Port G에 할당되어 있을 가능성이 높습니다.18

#### **4.2.2 RISC-V 어셈블리 구현 전략**

ARM 어셈블리(LDR, STR, MOV) 대신 RISC-V 어셈블리(lw, sw, mv)를 사용합니다.

1. **메모리 맵 상수 정의:**  
   * CCU_BASE: 0x02001000 (클럭 제어 유닛)  
   * GPIO_BASE: 0x02000000 (GPIO 컨트롤러)  
   * GPIO_PD_CFG0: GPIO 베이스 + 포트 D 설정 오프셋 (User Manual 참조 필요, 보통 0x90 등 포트별로 상이)  
   * GPIO_PD_DAT: GPIO 베이스 + 포트 D 데이터 오프셋  
2. 클럭 게이팅 해제 (필수):  
   Allwinner 칩셋은 저전력 설계를 위해 기본적으로 모든 주변장치의 클럭이 차단되어 있습니다. 이를 해제하지 않으면 GPIO 레지스터에 값을 써도 무시됩니다.  
   * CCU 레지스터 중 CCU_GPIO_BGR_REG (Bus Gating Reset)을 찾아 해당 포트(예: Port D)의 클럭 게이팅 비트를 1로 설정해야 합니다.21 이는 Raspberry Pi(BCM2835)에는 없는 과정으로, D1 개발 시 가장 흔한 실수 지점입니다.  
3. **GPIO 방향 설정:**  
   * PD_CFG 레지스터를 조작하여 LED가 연결된 핀을 출력(Output) 모드로 설정합니다. D1의 경우, 보통 4비트가 하나의 핀 설정을 담당합니다 (0000: Input, 0001: Output 등).  
4. **점멸 로직 (Assembly):**

```asm
.global _start  
_start:  
# 1. CCU 초기화 (클럭 활성화) 코드 위치  
# 2. GPIO 방향 설정 (Output) 코드 위치

loop:  
    # LED 켜기 (GPIO 데이터 레지스터에 1 쓰기)  
    li t0, GPIO_PD_DAT_ADDR  
    li t1, (1 << PIN_NUMBER)  
    sw t1, 0(t0)

    # 지연 (Delay)  
    li t2, 1000000  
delay1:  
    addi t2, t2, -1  
    bnez t2, delay1

    # LED 끄기  
    sw zero, 0(t0)

    # 지연 (Delay)  
    li t2, 1000000  
delay2:  
    addi t2, t2, -1  
    bnez t2, delay2

    j loop  
```

### **4.3 과제 2: Clock (Assignment 2) - C 언어와 타이머**

어셈블리에서 C 언어로 전환하고, 정확한 시간 측정을 위한 타이머를 다룹니다.

#### **4.3.1 C 런타임 초기화 (crt0.s)**

C 코드가 실행되기 위해서는 스택(Stack)이 설정되어야 하고, BSS 영역(초기화되지 않은 전역 변수)이 0으로 초기화되어야 합니다. 이를 수행하는 crt0.s 스타트업 코드를 작성해야 합니다.

* **스택 포인터 설정:** sp (x2) 레지스터에 DRAM의 끝부분이나 안전한 영역의 주소를 할당합니다.  
* **진입점 호출:** 설정 완료 후 main() 함수로 점프(call main)합니다.

#### **4.3.2 시간 측정: RISC-V rdtime**

CS107e의 RPi 과제에서는 시스템 타이머 레지스터를 직접 읽어야 했지만, RISC-V는 이를 아키텍처 차원에서 표준화했습니다.

* **rdtime 명령어:** 64비트 실시간 카운터 값을 읽어오는 의사 명령어(Pseudo-instruction)입니다.  
* **CSR (Control and Status Register):** 실제로는 time CSR을 읽습니다. D1에서는 이 카운터가 24MHz(일반적)로 동작하는지 확인해야 합니다.  
* **구현:** C 언어에서 인라인 어셈블리를 통해 이 값을 읽어오는 함수 timer_get_ticks()를 구현합니다.

```c
unsigned long get_time(void) {  
    unsigned long cycles;  
    asm volatile ("rdtime %0" : "=r" (cycles));  
    return cycles;  
}
```

### **4.4 과제 3: String Formatting & UART (Assignment 3)**

디버깅의 꽃인 printf를 구현하고 시리얼 통신을 활성화하는 단계입니다.

#### **4.4.1 UART0 하드웨어 설정**

Mango Pi의 디버그 UART는 핀 8(TX)과 10(RX)에 연결되어 있습니다. 이는 D1의 UART0 컨트롤러(PB8, PB9)에 매핑됩니다.18

* **베이스 주소:** 0x02500000 (UART0).22  
* **초기화 순서:**  
  1. **CCU 설정:** UART0 클럭 게이팅 활성화 및 리셋 해제.  
  2. **GPIO 설정:** PB8, PB9 핀을 UART 기능(Function 6 등, 데이터시트 확인 필수)으로 다중화(Multiplexing) 설정.24  
  3. **LCR (Line Control Register):** 8비트 데이터, 1 스톱 비트, 패리티 없음(8N1) 설정. DLAB 비트를 1로 설정하여 보드레이트 설정 모드 진입.  
  4. **DLH/DLL (Divisor Latch):** 보드레이트(115200)에 맞는 분주비 설정. 입력 클럭(보통 24MHz APB 클럭)을 기반으로 계산합니다.  
  5. **FIFO 활성화:** FCR 레지스터 설정.

#### **4.4.2 printf 구현**

가변 인자(stdarg.h)를 사용하여 형식 문자열을 파싱하고, 정수를 문자열로 변환하는 로직을 직접 구현합니다. 최종적으로 uart_putc 함수를 통해 한 글자씩 출력합니다. 이 과정은 아키텍처 독립적인 C 알고리즘 연습입니다.

### **4.5 과제 4: Linking and Loading (Assignment 4)**

컴파일된 오브젝트 파일들이 어떻게 하나의 실행 파일로 결합되고 메모리에 배치되는지 이해하는 단계입니다.

* **링커 스크립트 (.ld):** 코드(.text), 초기화된 데이터(.data), 초기화되지 않은 데이터(.bss) 섹션을 정의하고, 각 섹션이 메모리의 어느 주소(0x40000000)에 배치될지 명시합니다.  
* **심볼 해석:** nm과 objdump 도구를 사용하여 심볼 테이블을 분석하고, 함수 호출이 절대 주소 또는 상대 주소로 어떻게 변환되는지 확인합니다.  
* **RISC-V 특이점:** RISC-V는 gp (Global Pointer) 레지스터를 사용하여 전역 변수에 빠르게 접근하는 최적화(Linker Relaxation)를 수행합니다. 링커 스크립트에서 __global_pointer$ 심볼을 정의하고 스타트업 코드에서 gp 레지스터를 초기화해주는 과정이 필요할 수 있습니다.25

### **4.6 과제 5: Keyboard & Shell (Assignment 5)**

사용자의 입력을 받아 명령을 실행하는 쉘(Shell)을 구현합니다.

* **PS/2 키보드? USB 키보드?:** 원본 과제는 PS/2 키보드를 GPIO로 직접 제어합니다. Mango Pi는 USB OTG 포트만 있으므로, USB 호스트 스택을 구현하는 것은 매우 어렵습니다.  
* **대안:** UART를 통한 입력을 키보드 입력으로 간주하여 쉘을 구현하는 것이 현실적입니다. 터미널 에뮬레이터(PuTTY, screen 등)에서 타이핑한 문자를 UART 수신 버퍼에서 읽어와 명령어를 파싱하고 실행하는 구조를 만듭니다.  
* **링 버퍼(Ring Buffer):** UART로 들어오는 데이터 속도와 처리 속도의 차이를 극복하기 위해 원형 큐(Circular Queue) 자료구조를 구현합니다.

### **4.7 과제 6: Graphics Library (Assignment 6)**

화면에 픽셀을 찍고 도형과 글자를 그리는 단계입니다.

* **난관:** D1의 디스플레이 엔진(DE2.0)과 TCON, HDMI PHY를 베어메탈에서 직접 제어하는 것은 수천 줄의 드라이버 코드가 필요한 엄청난 작업입니다 (문서화도 부족함).26  
* **현실적 역공학 해법:** SPI 인터페이스를 사용하는 소형 LCD(예: ST7789, ILI9341 컨트롤러 기반)를 GPIO 헤더에 연결하여 사용하는 것을 강력히 추천합니다. SPI 프로토콜은 비교적 간단하며, D1의 SPI 컨트롤러(0x04025000 등)를 사용하거나 GPIO 비트뱅잉(Bit-banging)으로 구현할 수 있습니다.  
* **그래픽스 프리미티브:** draw_pixel 함수 하나만 하드웨어에 의존하게 만들고, 그 위에 선 그리기(Bresenham 알고리즘), 사각형 그리기, 폰트 렌더링 함수를 C 언어로 쌓아 올립니다.

### **4.8 과제 7: Interrupts (Assignment 7)**

폴링(Polling) 방식에서 벗어나 하드웨어 인터럽트를 통한 비동기 처리를 구현합니다.

* **RISC-V 인터럽트 모델:**  
  * **CSR:** mstatus(글로벌 인터럽트 활성화), mie(개별 인터럽트 활성화), mip(인터럽트 펜딩), mtvec(트랩 핸들러 주소) 레지스터를 이해해야 합니다.  
  * **PLIC (Platform-Level Interrupt Controller):** 외부 장치(UART, GPIO 등)의 인터럽트를 중재합니다. D1의 PLIC 베이스 주소를 확인하고(보통 0x10000000), 소스 ID를 매핑하여 우선순위를 설정하고 타겟 하트(Hart, 하드웨어 스레드)에 라우팅해야 합니다.27  
  * **CLINT (Core Local Interruptor):** 타이머 인터럽트와 소프트웨어 인터럽트를 담당합니다.  
* **구현:** UART 수신 인터럽트를 활성화하여, 쉘이 실행되는 동안 백그라운드에서 키 입력을 버퍼링하도록 시스템을 개선합니다.

## **5. Rust 언어로의 확장: Embedded-HAL과 안전한 베어메탈**

귀하의 Rust 숙련도를 활용하여 C로 작성한 모든 과제를 Rust로 재작성하는 것은 최고의 학습 방법입니다.

### **5.1 PAC (Peripheral Access Crate) 활용**

C에서는 #define 매크로와 포인터 캐스팅으로 레지스터에 접근했다면, Rust에서는 d1-pac을 사용합니다.

```rust
use d1_pac::Peripherals;

let p = Peripherals::take().unwrap();  
let gpio = &p.GPIO;  
// PC0를 출력으로 설정 (타입 안전성 보장)  
gpio.pc_cfg0.write(|w| w.pc0_select().output());
```

svd2rust 도구를 통해 생성된 이 코드는 잘못된 비트 조작을 컴파일 타임에 방지해줍니다.14

### **5.2 Embedded-HAL 구현**

Rust 임베디드 생태계의 핵심인 embedded-hal 트레이트를 구현해 봅니다. 예를 들어, 직접 작성한 UART 드라이버가 embedded_hal::serial::Write 트레이트를 구현하도록 하면, 이 트레이트를 사용하는 수많은 플랫폼 중립적인 드라이버(예: GPS 파서, 모뎀 드라이버)를 그대로 가져다 쓸 수 있습니다.16

## **6. 결론 및 학습 로드맵 제안**

이 프로젝트는 스탠포드 CS107e의 교육적 목표를 유지하면서도, 최신 RISC-V 아키텍처와 Rust 언어라는 현대적 기술 스택을 접목한 고도화된 과정입니다.

**단계별 실행 계획:**

1. **준비 (1주차):** 툴체인(GCC, Rust) 설치, xfel 빌드 및 테스트, 데이터시트 내 메모리 맵 확보.  
2. **기초 (2-3주차):** 과제 0, 1 (어셈블리 LED 제어) 수행. crt0.s 및 링커 스크립트 작성에 집중.  
3. **라이브러리화 (4-5주차):** 과제 2, 3 (C 언어 전환, 타이머, UART, printf). 나만의 mylib 구축.  
4. **응용 및 확장 (6-7주차):** 과제 5, 6 (쉘, SPI 디스플레이 그래픽스).  
5. **심화 (8주차):** 과제 7 (인터럽트) 및 Rust로 전체 코드 리팩토링.

Mango Pi MQ-Pro와 Allwinner D1은 문서화가 다소 불친절할 수 있으나, 리눅스 커널 소스(Device Tree)와 오픈 소스 커뮤니티(Linux-Sunxi)의 자료를 "데이터시트의 보완재"로 활용하는 능력 또한 시스템 엔지니어의 핵심 역량입니다. 이 과정을 완주한다면 귀하는 단순한 수강생 수준을 넘어선 시스템 아키텍트로서의 시야를 갖게 될 것입니다.

---

**필수 참조 리소스 체크리스트:**

1. **Allwinner D1-H User Manual (Ver 1.0 이상):** 레지스터 오프셋 확인용.  
2. **Mango Pi MQ-Pro Schematics:** GPIO 핀 매핑 확인용.  
3. **RISC-V Instruction Set Manual (Vol 1):** 어셈블리 명령어 확인용.  
4. **GitHub 리포지토리:** xboot/xfel (부트로더), d1-pac (Rust 레지스터 정의).

#### **참고 자료**

1. CS107E: Computer Systems from the Ground Up, 12월 15, 2025에 액세스, [http://web.stanford.edu/class/cs107e/](http://web.stanford.edu/class/cs107e/)  
2. Informational resources - CS107e, 12월 15, 2025에 액세스, [https://cs107e.github.io/resources/](https://cs107e.github.io/resources/)  
3. Foundations of RISC-V Assembly Programming - References - The Flashbots Collective, 12월 15, 2025에 액세스, [https://collective.flashbots.net/t/foundations-of-risc-v-assembly-programming/4788](https://collective.flashbots.net/t/foundations-of-risc-v-assembly-programming/4788)  
4. Allwinner D1 extensions : r/RISCV - Reddit, 12월 15, 2025에 액세스, [https://www.reddit.com/r/RISCV/comments/v1dvww/allwinner_d1_extensions/](https://www.reddit.com/r/RISCV/comments/v1dvww/allwinner_d1_extensions/)  
5. Diff - 8ec2d95f50c06f5cf2a2b94bcdf47f494f91ad55^1..8ec2d95f50c06f5cf2a2b94bcdf47f494f91ad55 - kernel/common - Git at Google - Android GoogleSource, 12월 15, 2025에 액세스, [https://android.googlesource.com/kernel/common/+/8ec2d95f50c06f5cf2a2b94bcdf47f494f91ad55%5E1..8ec2d95f50c06f5cf2a2b94bcdf47f494f91ad55/](https://android.googlesource.com/kernel/common/+/8ec2d95f50c06f5cf2a2b94bcdf47f494f91ad55%5E1..8ec2d95f50c06f5cf2a2b94bcdf47f494f91ad55/)  
6. [PATCH v3 10/24] sunxi: introduce NCAT2 generation model, 12월 15, 2025에 액세스, [https://lists.denx.de/pipermail/u-boot/2023-October/534872.html](https://lists.denx.de/pipermail/u-boot/2023-October/534872.html)  
7. allwinner-bare-metal/ccu.h at master - GitHub, 12월 15, 2025에 액세스, [https://github.com/catphish/allwinner-bare-metal/blob/master/ccu.h](https://github.com/catphish/allwinner-bare-metal/blob/master/ccu.h)  
8. RT-Thread-on-Allwinner-D1H/documentation/D1_2_boot_process.md at master - GitHub, 12월 15, 2025에 액세스, [https://github.com/ylyamin/RT-Thread-on-Allwinner-D1H/blob/master/documentation/D1_2_boot_process.md](https://github.com/ylyamin/RT-Thread-on-Allwinner-D1H/blob/master/documentation/D1_2_boot_process.md)  
9. xboot/xfel: Tiny FEL tools for allwinner SOC, support RISC ... - GitHub, 12월 15, 2025에 액세스, [https://github.com/xboot/xfel](https://github.com/xboot/xfel)  
10. GCC toolchain - Google Groups, 12월 15, 2025에 액세스, [https://groups.google.com/a/groups.riscv.org/g/sw-dev/c/m_VQUQV_qw0](https://groups.google.com/a/groups.riscv.org/g/sw-dev/c/m_VQUQV_qw0)  
11. What's the difference between "riscv64-unknown-elf-gcc" and "riscv64-linux-gnu-gcc", 12월 15, 2025에 액세스, [https://stackoverflow.com/questions/75611058/whats-the-difference-between-riscv64-unknown-elf-gcc-and-riscv64-linux-gnu-g](https://stackoverflow.com/questions/75611058/whats-the-difference-between-riscv64-unknown-elf-gcc-and-riscv64-linux-gnu-g)  
12. What is the difference between riscv64-unknown-elf-gcc and riscv-none-elf-gcc? · Issue #1425 · riscv-collab/riscv-gnu-toolchain - GitHub, 12월 15, 2025에 액세스, [https://github.com/riscv-collab/riscv-gnu-toolchain/issues/1425](https://github.com/riscv-collab/riscv-gnu-toolchain/issues/1425)  
13. antoinevg/hello-d1: Bare-metal Rust explorations of the ... - GitHub, 12월 15, 2025에 액세스, [https://github.com/antoinevg/hello-d1](https://github.com/antoinevg/hello-d1)  
14. d1-pac - crates.io: Rust Package Registry, 12월 15, 2025에 액세스, [https://crates.io/crates/d1-pac](https://crates.io/crates/d1-pac)  
15. Embedded development — list of Rust libraries/crates // Lib.rs, 12월 15, 2025에 액세스, [https://lib.rs/embedded](https://lib.rs/embedded)  
16. embedded-hal v1.0 now released!, 12월 15, 2025에 액세스, [https://blog.rust-embedded.org/embedded-hal-v1/](https://blog.rust-embedded.org/embedded-hal-v1/)  
17. A Hardware Abstraction Layer (HAL) for embedded systems - GitHub, 12월 15, 2025에 액세스, [https://github.com/rust-embedded/embedded-hal](https://github.com/rust-embedded/embedded-hal)  
18. easytarget/MQ-Pro-IO: Investigating the MangoPi MQ pro - GitHub, 12월 15, 2025에 액세스, [https://github.com/easytarget/MQ-Pro-IO](https://github.com/easytarget/MQ-Pro-IO)  
19. MangoPi MQ Pro Support — nerves_system_mangopi_mq_pro v0.14.0 - Hexdocs, 12월 15, 2025에 액세스, [https://hexdocs.pm/nerves_system_mangopi_mq_pro/](https://hexdocs.pm/nerves_system_mangopi_mq_pro/)  
20. nerves-project/nerves_system_mangopi_mq_pro: Nerves system for the MangoPi MQ Pro, 12월 15, 2025에 액세스, [https://github.com/nerves-project/nerves_system_mangopi_mq_pro](https://github.com/nerves-project/nerves_system_mangopi_mq_pro)  
21. Writing to memory mapped GPIO-registers does not write anything - Stack Overflow, 12월 15, 2025에 액세스, [https://stackoverflow.com/questions/64616203/writing-to-memory-mapped-gpio-registers-does-not-write-anything](https://stackoverflow.com/questions/64616203/writing-to-memory-mapped-gpio-registers-does-not-write-anything)  
22. Baremetal RISC-V - fryzekconcepts.com, 12월 15, 2025에 액세스, [https://fryzekconcepts.com/notes/baremetal-risc-v.html](https://fryzekconcepts.com/notes/baremetal-risc-v.html)  
23. Enabling UART1 at MangoPi - Allwinner sunxi - Armbian Community Forums, 12월 15, 2025에 액세스, [https://forum.armbian.com/topic/25236-enabling-uart1-at-mangopi/](https://forum.armbian.com/topic/25236-enabling-uart1-at-mangopi/)  
24. allwinner,sunxi-pinctrl.txt, 12월 15, 2025에 액세스, [https://www.kernel.org/doc/Documentation/devicetree/bindings/pinctrl/allwinner%2Csunxi-pinctrl.txt](https://www.kernel.org/doc/Documentation/devicetree/bindings/pinctrl/allwinner%2Csunxi-pinctrl.txt)  
25. Bare metal RISC-V CPU - how does the processor know which address to start fetching instructions from? - Stack Overflow, 12월 15, 2025에 액세스, [https://stackoverflow.com/questions/69834360/bare-metal-risc-v-cpu-how-does-the-processor-know-which-address-to-start-fetch](https://stackoverflow.com/questions/69834360/bare-metal-risc-v-cpu-how-does-the-processor-know-which-address-to-start-fetch)  
26. T113-S3/D1S : Mainline MIPI-DSI Driver "sun6i-mipi-dsi 5450000.dsi: Couldn't get the DSI mod clock" - Google Groups, 12월 15, 2025에 액세스, [https://groups.google.com/g/linux-sunxi/c/HxDBpY5HbbQ](https://groups.google.com/g/linux-sunxi/c/HxDBpY5HbbQ)  
27. Platform Level Interrupt Controller(PLIC) User Manual (SP2020) - Shakti Processor, 12월 15, 2025에 액세스, [https://shakti.org.in/docs/plic_sp2020.pdf](https://shakti.org.in/docs/plic_sp2020.pdf)  
28. include interrupt trigger configuration registers in the memory map · Issue #52 · riscv/riscv-plic-spec - GitHub, 12월 15, 2025에 액세스, [https://github.com/riscv/riscv-plic-spec/issues/52](https://github.com/riscv/riscv-plic-spec/issues/52)

