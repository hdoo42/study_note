---
id: Non-Autoregressive
aliases: []
tags:
  - LLM
  - Non-Autoregressive
  - NLP
  - 딥러닝
---
# Non-Autoregressive LLM: 최신 연구 및 적용

**Non-Autoregressive Language Model (NAR LLM)** 은 전체 시퀀스를 병렬로 생성하여 추론 속도를 향상시키는 접근 방식입니다. 최근 연구들은 이러한 모델의 성능을 개선하고 다양한 응용 분야에 적용하기 위한 다양한 방법을 제안하고 있습니다.

---

## 🧪 최신 연구 동향

### 1. **Diffusion-LM**: 확산 기반 언어 모델
- **개요**: 확산 모델을 활용하여 텍스트를 생성하는 방식으로, 복잡한 제어가 가능한 텍스트 생성을 목표로 합니다.
- **특징**: 연속적인 확산 과정을 통해 텍스트를 생성하며, 기존의 오토리그레시브 모델보다 더 정밀한 제어가 가능합니다.
- **참고**: [Diffusion-LM 논문](https://arxiv.org/abs/2205.14217)

### 2. **UT5**: 비오토리그레시브 T5 모델
- **개요**: T5 모델을 기반으로 비오토리그레시브 방식으로 사전 학습을 수행하여, 추론 속도를 개선합니다.
- **특징**: 언롤드 디노이징(unrolled denoising)을 통해 성능을 향상시키며, 다양한 자연어 생성 작업에서 우수한 성능을 보입니다.
- **참고**: [UT5 논문](https://arxiv.org/abs/2311.08552)

### 3. **INarIG**: 반복적인 비오토리그레시브 지시 생성 모델
- **개요**: 반복적인 디코딩 과정을 통해 비오토리그레시브 모델의 성능을 향상시키는 방법을 제안합니다.
- **특징**: 디코더의 모든 토큰 표현을 반복적으로 계산하여, 추론 속도에 큰 영향을 주지 않으면서 성능을 개선합니다.
- **참고**: [INarIG 논문](https://aclanthology.org/2023.findings-emnlp.948.pdf)

---

## 🚀 LLM 적용 사례

### 1. **CALM**: 텍스트 생성 가속화
- **개요**: Transformer 디코더에서 조기 종료(early exit)를 활용하여 텍스트 생성 속도를 향상시킵니다.
- **특징**: 여러 작업에서 텍스트 생성 속도를 크게 향상시키면서도 정확도 저하 없이 성능을 유지하거나 향상시킵니다.
- **참고**: [CALM 블로그](https://medium.com/unstructured-io/speeding-up-text-generation-with-non-autoregressive-language-models-e51638d7da43)

### 2. **비오토리그레시브 기계 번역**
- **개요**: 전체 출력 시퀀스를 한 번의 전방 패스로 생성하여 추론 속도를 개선합니다.
- **특징**: 추론 속도는 향상되지만, 출력 토큰 간의 의존성을 무시하기 때문에 번역 품질은 오토리그레시브 모델보다 낮을 수 있습니다.
- **참고**: [Apple 연구](https://machinelearning.apple.com/research/non-autoagressive-neural-machine)

---

## 📊 비교: 오토리그레시브 vs. 비오토리그레시브

| 특성             | 오토리그레시브 모델 | 비오토리그레시브 모델 |
|------------------|---------------------|-----------------------|
| 생성 방식        | 순차적 생성          | 병렬 생성              |
| 추론 속도        | 느림                | 빠름                  |
| 토큰 간 의존성   | 강함                | 약함                  |
| 생성 품질        | 높음                | 낮을 수 있음           |
| 대표 모델        | GPT, Transformer    | NAT, Diffusion-LM     |

---

## 🔗 참고 문헌

- [Diffusion-LM 논문](https://arxiv.org/abs/2205.14217)
- [UT5 논문](https://arxiv.org/abs/2311.08552)
- [INarIG 논문](https://aclanthology.org/2023.findings-emnlp.948.pdf)
- [CALM 블로그](https://medium.com/unstructured-io/speeding-up-text-generation-with-non-autoregressive-language-models-e51638d7da43)
- [Apple 연구](https://machinelearning.apple.com/research/non-autoagressive-neural-machine)


