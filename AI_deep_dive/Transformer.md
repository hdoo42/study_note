---
id: Transformer
aliases:
  - Transformer
tags: []
---

# Transformer
아래 내용은 2017년 구글 브레인 팀의 논문 **"Attention Is All You Need"** 에서 처음 제안된 **Transformer** 모델을 중심으로, 이 모델의 구조와 핵심 아이디어를 정리한 것이다. 설명 순서는 다음과 같다:

1. **Transformer** 모델의 개요  
2. **Encoder-Decoder** 구조  
3. **Scaled Dot-Product Attention**  
4. **Multi-Head Self-Attention** 기법  
5. **Positional Encoding**  
6. **Residual Connection & Layer Normalization**  
7. **Decoder** 의 Masked Self-Attention  
8. **학습 과정** 및 복잡도 분석  
9. **응용 및 확장** (GPT, BERT, Vision Transformer 등)

---

## 1. **Transformer** 모델의 개요
**Transformer** 는 순차적(Sequential)인 처리에 의존적이었던 RNN 계열 모델의 한계를 극복하고, **Attention** 메커니즘만을 이용해 시퀀스 데이터를 병렬적으로 처리할 수 있도록 설계된 모델이다.  
- **RNN/LSTM** 기반 모델: 시퀀스를 시간축으로 순차 처리 → **장기 의존성** 문제와 병렬화의 어려움  
- **CNN** 기반 모델: 로컬 컨볼루션 윈도우 제한 → 전역 문맥(global context) 포착 한계  
- **Transformer** 는 Attention을 통해 모든 위치의 토큰들이 서로를 참조할 수 있으므로, **병렬 처리가 가능**하고 **장기 의존성** 문제를 효과적으로 해결한다.

---

## 2. **Encoder-Decoder** 구조
**Transformer** 는 전통적인 Seq2Seq 구조와 유사하게 **Encoder** 와 **Decoder** 로 구성되며, 둘 다 반복(recurrent) 구조가 없다.

- **Encoder**: 입력 시퀀스를 여러 층의 Self-Attention 레이어와 피드 포워드(feed-forward) 레이어를 통해 **공간적·개념적 의미**로 인코딩한다.  
- **Decoder**: 인코더가 추출한 정보를 바탕으로 **출력 시퀀스를 단계적으로 생성**한다. 이때 **미래 단어**를 참조할 수 없도록 마스킹(Masking)된 Self-Attention을 사용한다.

### Encoder 블록 구성
1. **Self-Attention** 레이어  
2. **Feed-Forward Network(FFN)**  
3. 각 서브 레이어마다 **Residual Connection** + **Layer Normalization**  

### Decoder 블록 구성
1. **Masked Self-Attention** 레이어 (출력 단어의 미래 정보 차단)  
2. **Encoder-Decoder Attention** (인코더에서 나온 정보 참조)  
3. **Feed-Forward Network**  
4. 각 서브 레이어마다 **Residual Connection** + **Layer Normalization**

---

## 3. **Scaled Dot-Product Attention**
Transformer의 가장 핵심적인 연산은 **Attention** 이며, 그 중에서도 **Scaled Dot-Product Attention** 이 기본이다.

$$
\text{Attention}(Q, K, V) = \text{softmax}\biggl(\frac{Q K^T}{\sqrt{d_k}}\biggr) V
$$

- $Q$ (Query)  
- $K$ (Key)  
- $V$ (Value)  
- $d_k$: Key 벡터의 차원

### 동작 원리
1. **유사도 계산**: $Q K^T$는 Query와 Key 간의 내적(dot product)로, 얼마나 연관성이 있는지 측정한다.  
2. **스케일링**: $\sqrt{d_k}$로 나누어, 차원이 커질수록 내적 값이 너무 커지는 문제를 완화한다.  
3. **정규화**: 소프트맥스(Softmax)를 취해 가중치 분포를 만든다.  
4. **가중합**: 해당 분포를 $V$에 곱하여 최종 Attention 출력을 얻는다.

---

## 4. **Multi-Head Self-Attention** 기법
논문에서는 단일 Attention보다 **Multi-Head Attention** 을 제안하여 **여러 시각(Representation Subspace)** 으로 정보를 동시에 학습하도록 했다.

$$
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) \, W_O
$$

- 각 Head마다 $Q, K, V$를 독립적으로 학습(가중치 행렬: $W_Q, W_K, W_V$)하여 서로 다른 부분(패턴)에 집중  
- 출력들을 **Concat**한 후에 추가 가중치 $W_O$를 곱해 최종 출력을 만든다.

### **Self-Attention** 의 등장
- **Self-Attention** 은 RNN의 은닉 상태처럼 토큰 단위로 정보를 전이하지 않고, **한 번의 연산으로 시퀀스 내 모든 토큰 간 상호 작용**을 계산한다.  
- 인코더, 디코더 내부에서 각각 **Self-Attention** 을 사용하며, 디코더에서는 생성 중인 단어보다 뒤에 있는 단어를 보지 못하도록 마스킹을 적용한다(**Masked Self-Attention**).

---

## 5. **Positional Encoding**
RNN은 순차적 구조로 토큰의 순서를 자연스럽게 반영하지만, **Transformer** 는 병렬 처리를 하기 때문에 **토큰의 위치 정보**(순서)를 추가로 주어야 한다. 이를 위해 **Positional Encoding** 을 사용한다.

$$
PE_{(pos, 2i)} = \sin \bigl(pos / 10000^{2i/d_{model}}\bigr), \quad 
PE_{(pos, 2i+1)} = \cos \bigl(pos / 10000^{2i/d_{model}}\bigr)
$$

- $pos$: 토큰의 위치 (0, 1, 2, …)  
- $i$: 임베딩 벡터 차원의 인덱스  
- **사인(Sin)**, **코사인(Cos)** 함수를 사용해 위치 정보를 임베딩 차원에 따라 다른 주기로 인코딩  
- 이렇게 얻은 위치 벡터를 **입력 임베딩**에 더해 줌으로써 **상대적·절대적 위치** 정보를 모델에 제공한다.

---

## 6. **Residual Connection & Layer Normalization**
Transformer 블록 내부의 각 서브 레이어(Attention 혹은 FFN) 출력에 **Residual Connection**(잔차 연결)을 적용하고, 이어 **Layer Normalization** 을 수행한다.

$$
\text{LayerOutput} = \text{LayerNorm}(X + \text{SubLayer}(X))
$$

- **Residual Connection** 은 깊은 신경망 학습 시 발생하는 **그래디언트 소실** 문제를 완화하고, 학습 안정성을 높인다.  
- **Layer Normalization** 은 미니배치 방향이 아니라 **특징(feature) 차원 방향으로 정규화**하여, 길이가 다양한 시퀀스에 안정적으로 적용 가능하다.

---

## 7. **Decoder** 의 Masked Self-Attention
디코더에서는 이미 생성된 단어들만 보면서 다음 단어를 예측해야 한다. 따라서 디코더 블록의 첫 번째 서브 레이어에서 사용되는 **Self-Attention** 에 **마스킹(Masking)** 을 적용한다.

- **미래 단어(토큰)** 에 해당하는 부분을 $-\infty$로 설정해, 소프트맥스 이후 해당 위치로의 확률이 0이 되도록 만든다.  
- 이를 통해 디코더는 **시점 t 이전 단어** 정보만 활용하여 시점 t의 단어를 생성한다.

---

## 8. **학습 과정** 및 복잡도 분석
### 학습 알고리즘
- **Teacher Forcing** 방식으로 **Decoder** 에는 정답 시퀀스를 한 칸씩 밀어 넣어준다.  
- **Cross Entropy** 기준으로 역전파(Backpropagation)를 통해 가중치를 학습한다.

### 시간 복잡도
- **Self-Attention** 연산은 시퀀스 길이를 $n$이라 할 때, 일반적으로 $O(n^2)$의 연산량이 필요하다.  
- RNN에 비해 **병렬화**가 가능해, 실제 학습 속도는 더 빠른 경향이 있다. (긴 시퀀스에서는 여전히 $n^2$이 부담이 되지만, 대규모 GPU 병렬화를 통해 가속 가능)

---

## 9. **응용 및 확장**
### 1) **GPT** 계열
- **OpenAI**의 GPT 시리즈는 **Decoder** 만을 사용하여 언어 모델링에 최적화된 구조를 가진다.  
- 대규모 데이터와 파라미터로 학습 후, 다양한 자연어 처리 태스크에 **Zero-Shot, Few-Shot** 성능을 발휘한다.

### 2) **BERT**
- **Google**의 BERT는 **Encoder** 만을 사용한 양방향(Bidirectional) 언어 모델로, **마스크드 언어 모델(MLM)** 및 **Next Sentence Prediction** 기법으로 학습한다.  
- 문장의 **표현(Embedding)** 을 풍부하게 학습하여, 범용적인 다운스트림 태스크(질의응답, 분류 등)에 활용 가능하다.

### 3) **Vision Transformer(ViT)**
- 이미지 패치를 하나의 토큰으로 취급하고, **Self-Attention** 방식으로 시각 정보를 처리한다.  
- CNN 없이도 SOTA급 성능 달성 → 최근 비전 분야에서도 **Transformer** 가 큰 흐름이 되었다.

### 4) **음성 처리, 시계열, 멀티모달** 등
- 음성 인식/합성(TTS), 시계열 예측, 영상+텍스트 멀티모달 처리 등 다양한 분야에서 **Transformer** 기반 모델이 우수 성능을 보이고 있다.

---

## 마무리
**Transformer** 는 단순히 RNN을 대체한 것이 아니라, **Attention** 메커니즘 중심으로 **병렬 처리**, **장기 의존성 극복**, **유연한 구조** 등을 제공하여 **딥러닝의 패러다임을 바꾼 대표적인 모델** 이다. 이후 등장한 GPT, BERT, ViT 등 다양한 변형 모델들도 대부분 Transformer 구조를 기반으로 발전해 왔으며, 대규모 파라미터 및 대량 데이터 학습이 가능해지면서 **NLP, CV, 음성, 멀티모달** 등 전 영역에서 우수한 성능을 발휘하고 있다.

> - **참고 논문**: Vaswani et al., "Attention Is All You Need," *NeurIPS* (2017)  
> - **핵심 키워드**: Attention, Multi-Head, Encoder-Decoder, Positional Encoding, Masked Self-Attention, Parallelization  

