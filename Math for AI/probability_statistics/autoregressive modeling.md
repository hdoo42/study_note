---
title: Autoregressive Modeling
aliases: []
tags: [LLM, language-modeling, autoregressive, NLP]
---

# Autoregressive Modeling

**Autoregressive Modeling**은 시퀀스 데이터를 **앞에서부터 차례로 예측하면서 생성하는 방식**으로, LLM(특히 GPT 계열)의 핵심 작동 원리입니다.

---

## 정의

> 이전까지의 입력을 바탕으로 다음 값을 예측하는 방식.

수식으로는 다음과 같습니다:

$P(x_1, x_2, \ldots, x_n) = \prod_{t=1}^{n} P(x_t \mid x_1, \ldots, x_{t-1})$

각 시점 $t$에서의 토큰 $x_t$는 앞서 등장한 $x_1$부터 $x_{t-1}$까지의 문맥에 따라 예측됩니다.

---

## 예시

- 입력: `"나는"`
- 모델은 다음 단어로 `"밥을"`, `"공부를"` 등 후보의 확률을 계산
- 가장 높은 확률의 `"밥을"` 선택
- 이후 `"나는 밥을"`을 바탕으로 또 다음 단어 예측
- 이런 식으로 문장이 순차적으로 생성됨

---

## 특징

| 항목       | 설명                                          |
|------------|-----------------------------------------------|
| 예측 방식  | 한 토큰씩 순서대로 생성                       |
| 장점       | 문맥을 반영한 자연스러운 문장 생성 가능       |
| 단점       | 느림 (토큰을 하나씩 예측해야 함)              |
| 대표 모델 | GPT, Transformer-decoder 계열                  |
	
---

## Autoregressive vs. [[Non-Autoregressive]]

| 항목          | Autoregressive                         | Non-Autoregressive                     |
|---------------|----------------------------------------|----------------------------------------|
| 예측 방식     | 순차적 (한 단어씩)                     | 병렬적 (여러 단어를 동시에 예측)       |
| 속도          | 느림                                   | 빠름                                   |
| 생성 품질     | 상대적으로 우수                         | 문장 일관성이나 유창성에서 떨어질 수 있음 |

---

## 관련 개념

- GPT
- Transformer Decoder
- Language Modeling
