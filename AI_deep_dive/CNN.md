---
id: CNN
aliases:
  - convolutional neural networks
tags: []
---

# convolutional neural networks
### **Convolutional Neural Network (CNN) 개요**

Convolutional Neural Network(CNN)는 **이미지 처리 및 분석에 특화된 인공 신경망**(Artificial Neural Network, ANN)의 한 종류입니다. 주로 **컴퓨터 비전**(Computer Vision) 분야에서 활용되며, 영상 인식, 객체 탐지, 자율 주행, 의료 영상 분석 등에 사용됩니다.

---

## **1. CNN의 핵심 개념**
CNN은 일반적인 다층 신경망(MLP, Multi-Layer Perceptron)과 다르게, **공간적 특징을 보존**하면서 학습하는 구조를 갖고 있습니다. 핵심 개념은 다음과 같습니다.

### **1) 합성곱([[convolution|Convolution]]) 연산**
- 이미지에서 **특징(feature)을 추출**하는 역할을 합니다.
- 작은 필터(커널, Kernel)를 사용하여 이미지의 특정 패턴(엣지, 텍스처 등)을 감지합니다.
- **예제:** 엣지를 감지하는 필터는 수직선, 수평선 등의 모양을 학습할 수 있습니다.

### **2) 활성화 함수(Activation Function)**
- 비선형성을 추가하여 복잡한 패턴을 학습할 수 있도록 합니다.
- CNN에서는 주로 **ReLU (Rectified Linear Unit)** 함수가 사용됩니다.

### **3) 풀링(Pooling)**
- 특징 맵에서 중요한 정보를 유지하면서 **크기를 줄이는 과정**입니다.
- 일반적으로 **최대 풀링(Max Pooling)** 이 많이 사용됩니다.
- 이미지 크기를 줄여 연산량을 감소시키고, 모델의 일반화 능력을 높입니다.

### **4) 완전 연결층(Fully Connected Layer, FC)**
- CNN의 마지막 단계로, 추출된 특징을 기반으로 **분류(Classification)** 를 수행합니다.
- MLP 구조를 가지며, Softmax 같은 활성화 함수를 사용하여 확률 값을 출력합니다.

---

## **2. CNN의 전체 구조**
CNN의 기본적인 구조는 다음과 같습니다.

1. **입력층(Input Layer):** 이미지 데이터 (예: 28×28 픽셀의 흑백 이미지)
2. **합성곱층(Convolution Layer):** 필터를 사용하여 특징을 추출
3. **활성화 함수(ReLU):** 비선형성 추가
4. **풀링층(Pooling Layer):** 특징 맵 크기 축소
5. **완전 연결층(Fully Connected Layer):** 특징을 바탕으로 분류 수행
6. **출력층(Output Layer):** 최종 분류 결과 도출 (예: 고양이 vs 개)

---

## **3. CNN의 장점**
1. **파라미터 수 감소** → 일반적인 MLP보다 연산량이 적고 학습이 빠름
2. **특징 자동 추출** → 사람이 직접 특징을 정의할 필요 없음
3. **위치 불변성** → 동일한 객체가 이미지 내 다른 위치에 있어도 잘 인식됨

---

## **4. CNN의 대표적인 모델**
- **LeNet-5** (1998): 최초의 CNN 구조, 손글씨 숫자 인식에 사용됨
- **AlexNet** (2012): ImageNet 대회에서 우승하며 CNN의 중요성을 입증
- **VGGNet** (2014): 깊은 CNN 구조로 뛰어난 성능을 보임
- **ResNet** (2015): **스킵 커넥션(Skip Connection)** 을 도입하여 깊은 네트워크에서도 학습이 가능하게 만듦

---

## **5. 활용 분야**
- **이미지 분류(Image Classification):** 고양이/개 분류, 손글씨 숫자 인식
- **객체 탐지(Object Detection):** 얼굴 인식, 자율 주행 자동차의 보행자 탐지
- **의료 영상 분석(Medical Image Analysis):** CT, MRI에서 병변 탐지
- **스타일 변환(Style Transfer):** 사진을 예술적인 스타일로 변환

---

CNN은 현재 **딥러닝 기반의 컴퓨터 비전 분야에서 필수적인 기술**로 자리 잡았습니다. 이미지 데이터를 다룰 때 높은 성능을 보이며, 계속해서 발전하고 있는 분야입니다.
