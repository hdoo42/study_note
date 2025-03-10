---
id: one_D_continuous_signal
aliases:
  - 1D Continuous Signal
tags:
  - signal_representation
---

# 1D Continuous Signal
### **1D 연속 신호란?**  

#### **1. 신호(signal)의 개념**  
신호(signal)는 **시간이나 공간에 따라 변하는 물리량을 수학적으로 표현한 것**입니다.  
- 예를 들어, **소리, 전기 신호, 빛, 온도 변화** 등이 신호의 예시입니다.  

신호는 크게 **연속 신호(Continuous Signal)** 와 **이산 신호(Discrete Signal)** 로 나뉩니다.

---

#### **2. 1D 연속 신호(1D Continuous Signal)란?**  
1D 연속 신호는 **시간(time)이나 공간(space)에 대해 연속적인 값을 갖는 1차원 신호**를 의미합니다.  

수학적으로는 **아무리 작은 단위로 쪼개도 값이 정의되어 있는 신호**를 의미하며, 일반적으로 **연속 함수**로 표현됩니다.  

##### **수학적 정의:**  
연속 신호 $x(t)$ 는 **시간 $t$ 에 대해 정의된 연속적인 함수**입니다.

$$
x: \mathbb{R} \to \mathbb{R}, \quad x(t) \in \mathbb{R}
$$

즉, $x(t)$ 는 실수 시간 $t$ 에 대해 실수 값을 가집니다.

---

#### **3. 예제**
##### **(1) 아날로그 오디오 신호**  
- 음악, 사람의 음성 등은 연속적으로 변하는 신호입니다.  
- 마이크로 녹음하면 **전압이 시간에 따라 연속적으로 변하는 신호**가 생성됩니다.

##### **(2) 온도 변화**  
- 하루 동안의 기온 변화는 시간에 대해 연속적으로 변화하는 신호입니다.  
- 예를 들어, 특정 지역의 온도 $T(t)$ 가 시간 $t$ 에 따라 연속적으로 변한다면, 이 또한 **1D 연속 신호**입니다.

##### **(3) 정현파(Sinusoidal Wave)**  
- 가장 기본적인 연속 신호는 정현파(Sine wave)이며, 다음과 같이 표현됩니다.

$$
x(t) = A \sin(2\pi f t + \phi)
$$

  - $A$ : 진폭 (Amplitude)
  - $f$ : 주파수 (Frequency)
  - $\phi$ : 위상 ([[Phase|Phase]])
  - $t$ : 시간  

이 신호는 **모든 시간 $t$ 에 대해 연속적인 값을 갖기 때문에 연속 신호**입니다.

---

#### **4. 1D 연속 신호 vs 1D 이산 신호**
| 구분 | 연속 신호 (Continuous Signal) | 이산 신호 (Discrete Signal) |
|------|---------------------------|-------------------------|
| 정의 | 모든 시간에서 값이 존재 | 특정한 시간에서만 값이 존재 |
| 표현 방식 | 연속 함수 $x(t)$ | 샘플링된 데이터 $x[n]$ |
| 예제 | 아날로그 오디오, 온도 변화 | 디지털 오디오, 픽셀 값 |

**예시:**  
- 연속 신호: 아날로그 오디오 (LP 레코드 소리)  
- 이산 신호: MP3 파일 (디지털 오디오, 샘플링된 신호)

---

#### **5. 결론**
1D 연속 신호는 **시간에 대해 끊김 없이 변하는 신호**로, 물리적으로 **아날로그 신호**로 나타납니다.  
이산 신호와 달리 **모든 시간에서 값이 정의**되며, 신호 처리에서 주로 **아날로그-디지털 변환(ADC)** 과정에서 이산 신호로 변환됩니다.
