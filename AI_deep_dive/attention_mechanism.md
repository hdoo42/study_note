---
id: attention_mechanism
aliases:
  - Attention mechanism
tags: []
---

# Attention mechanism
Attention 메커니즘은 시퀀스 데이터에서 중요한 부분에 가중치를 부여하여 모델이 보다 효과적으로 학습할 수 있도록 하는 기법이다. 이는 특히 자연어 처리(NLP) 및 시계열 데이터 분석에서 필수적인 역할을 한다.

## 1. **배경 및 필요성**
기존의 RNN, LSTM, GRU 기반 모델들은 입력 시퀀스를 순차적으로 처리하기 때문에 긴 시퀀스를 다룰 때 **장기 의존성([[long-term_dependency 1|long-term_dependency]])** 문제를 겪는다. 이를 해결하기 위해 등장한 **Attention** 메커니즘은 전체 입력을 한 번에 고려하면서 특정 부분에 더 집중하는 방식으로, 중요한 정보를 효과적으로 선택할 수 있도록 한다.

## 2. **Attention의 기본 원리**
Attention은 기본적으로 다음과 같은 수식으로 정의된다.

$$
\text{Attention}(Q, K, V) = \text{softmax} \left( \frac{QK^T}{\sqrt{d_k}} \right) V
$$

여기서,  
- $Q$ (Query): 현재 우리가 집중해야 할 정보  
- $K$ (Key): 입력 시퀀스의 모든 요소  
- $V$ (Value): 최종적으로 출력할 값  
- $d_k$: Key 벡터의 차원 (스케일링을 위해 사용)  

Query와 Key의 내적([[dot_product 1|dot product]])을 통해 중요도를 측정한 후, [[Softmax 1|Softmax]]를 적용하여 확률 분포를 만든다. 이 확률을 Value에 곱하여 최종적으로 가중합(weighted sum)을 구하면 특정 위치의 정보를 강화하여 사용할 수 있다.

## 3. **Self-Attention**
Self-Attention은 하나의 시퀀스 내에서 서로 다른 위치의 단어들이 서로 얼마나 관련이 있는지를 학습하는 방식이다. 이는 트랜스포머([[Transformer 1|Transformer]]) 모델의 핵심적인 요소로 사용된다.

$$
\text{Self-Attention}(X) = \text{softmax} \left( \frac{XW_Q (XW_K)^T}{\sqrt{d_k}} \right) XW_V
$$

여기서 $X$는 입력 임베딩, $W_Q, W_K, W_V$는 학습 가능한 가중치 행렬이다.

## 4. **Multi-Head Attention**
트랜스포머 모델에서는 하나의 Attention만 사용하는 것이 아니라 여러 개의 Attention을 병렬로 적용하여 학습 능력을 향상시킨다.

$$
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, ..., \text{head}_h) W_O
$$

각 Head는 서로 다른 부분에 집중할 수 있도록 독립적인 가중치를 사용하며, 최종적으로 여러 Attention을 결합하여 보다 풍부한 표현력을 갖는다.

## 5. **Transformer와 Attention**
트랜스포머 모델(Transformer, Vaswani et al. 2017)은 Attention을 활용하여 RNN 없이도 시퀀스를 효과적으로 학습할 수 있도록 한다. 여기서는 **Self-Attention과 Multi-Head Attention**을 사용하여 입력 시퀀스를 처리하며, 이를 통해 병렬화가 가능해지고 장기 의존성 문제를 해결할 수 있다.

### Transformer 구조:
1. **Encoder**
   - 입력을 여러 개의 Self-Attention Layer를 통해 인코딩
   - Multi-Head Attention + Feed Forward Network 적용
   - Residual Connection 및 Layer Normalization 포함

2. **Decoder**
   - Encoder에서 얻은 출력을 기반으로 디코딩 수행
   - Masked Self-Attention을 사용하여 미래 정보를 차단
   - Multi-Head Attention과 Feed Forward Network 적용

## 6. **응용 사례**
Attention 메커니즘은 다양한 딥러닝 모델에서 활용된다.
- **기계 번역 (NMT)**: 번역 시 특정 단어에 가중치를 주어 문맥을 이해
- **이미지 인식 (Vision Transformers, ViT)**: CNN 없이도 Self-Attention을 활용하여 특징 추출
- **생성 모델 (ChatGPT, BERT, T5)**: 문맥을 이해하고 중요한 정보를 선택하는 데 사용

## 7. **결론**
Attention은 단순한 가중치 기법이 아니라, 신경망이 중요한 정보를 선택하고 활용하는 방식의 핵심적인 발전이다. 트랜스포머 모델의 등장 이후, NLP를 포함한 다양한 분야에서 필수적인 요소가 되었으며, CNN, RNN 등 기존 모델을 대체하는 중요한 역할을 하고 있다.
