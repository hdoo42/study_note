---
id: 1763123916-EDWI
aliases:
  - ArrayManager vs BlockManager
tags: []
---
# 📌 Pandas Data Manager — BlockManager vs ArrayManager

> 최근 Pandas 내부 저장 방식, ArrayManager 폐기 이슈 정리

---

## 🎯 핵심 요약

* Pandas 내부에는 **데이터 저장 백엔드**가 존재

  * BlockManager (기본)
  * ArrayManager (실험적 → **Deprecated**)
* Pandas 2.2.0 이후:

  > “ArrayManager와 `mode.data_manager` 옵션은 deprecated.
  > **향후 BlockManager만 유지**”
* ArrayManager는 Arrow 및 nullable dtype 확장을 위해 도입되었지만
  유지 비용, CI 상태 불량 등의 이유로 폐기 결론

---

## ❓ BlockManager란?

* **여러 컬럼을 dtype 기반 Block 단위(2D NumPy)로 저장**
* Block 유형:

  * Int64Block
  * FloatBlock
  * ObjectBlock
  * ExtensionBlock(EA Block)

👉 벡터화 연산 성능 최적화에 유리

---

## ❓ ArrayManager란?

* **각 컬럼을 독립 1D 배열로 저장**
* ExtensionArray / Arrow 기반 dtype과 자연스럽게 호환
* 하지만:

  * 성능 경로 복잡화
  * 테스트(=CI) 커버 부족
  * 다양한 버그 존재

👉 실험적 백엔드였으나 유지 불가 판단

---

## 🔍 ExtensionBlock(EA Block)이란?

* ExtensionArray를 저장하는 BlockManager 내부 Block
* 예: Nullable Int(`Int64`), Boolean(`boolean`), StringDtype, Categorical 등

```python
df = pd.DataFrame({"A": pd.Series([1,2,None], dtype="Int64")})
df._data
```

결과:

```
BlockManager
ExtensionBlock: dtype=Int64
```

➡ ArrayManager가 아니라
➡ **BlockManager 내부의 EA Block 사용 중**

---

## ❌ 왜 ArrayManager를 자동으로 쓰지 않는가?

* nullable dtype을 사용한다고 자동으로 ArrayManager가 되지 않음
* BlockManager는 계속 ExtensionBlock을 통해 EA 지원

---

## 🧨 Deprecated 상황

**경고 메시지**

```
FutureWarning: data_manager option is deprecated and will be removed in a future version.
Only the BlockManager will be available.
```

> ArrayManager 백엔드와 옵션이 폐기되며
> 앞으로는 BlockManager만 사용 가능

---

## 🧪 CI 관련 코멘트 (pandas-dev)

ArrayManager 폐기 이슈에서 나온 내용 요약:

* CI(자동화 테스트)에서 ArrayManager가 **현재 수천 개 테스트 실패**
* zero-copy NumPy 지원을 위해서는 block 구조가 필요
* 두 백엔드를 병행 유지하는 건 불가능
* 대안 방향: **2D ExtensionArray**, **Arrow dtype 통합**

---

## 🔮 향후 Pandas 로드맵 방침 (정리)

| 항목               | 방향성                           |
| ---------------- | ----------------------------- |
| 내부 저장 방식         | **BlockManager 유지**           |
| dtype            | Arrow/EA 기반 확장                |
| null 처리          | bitmask 기반 nullable 구조 강화     |
| interoperability | pyarrow ↔ pandas zero-copy 확대 |

---

## 🧩 개발자 관점 가이드

| 항목           | 권장 전략                                              |
| ------------ | -------------------------------------------------- |
| 내부 구조 분석     | BlockManager 기반으로 파악                               |
| 신규 데이터 모델 설계 | Arrow / EA 친화적 설계                                  |
| Pandas 내부 접근 | `_mgr`, `_data`, `_blocks` 등 BlockManager 구조 이해 필수 |
| 의존성 고려       | scikit-learn, NumPy interoperability 유지            |

---

## 📚 추가 참고

* DEPR 이슈: “DEPR: ArrayManager (GH 55043)”
* pandas 2.2.0 What’s New — `mode.data_manager`, ArrayManager deprecated
* Pandas Roadmap — Arrow 기반 dtype 전략 강화
* Copy-on-Write 기능 및 Arrow backend가 핵심

---

## 📌 최종 결론

> ArrayManager는 **실험 종료**,
> 앞으로는
> **BlockManager + ExtensionArray/Arrow dtype**
> 조합으로 진화한다.

---

## 📓 대화 내 질문 요약

| 질문                   | 핵심 답변                               |
| -------------------- | ----------------------------------- |
| 블록매니저가 뭐야?           | dtype별 Block으로 묶는 저장 방식             |
| ArrayManager는?       | 컬럼 독립 저장 방식(실험용 → 폐기)               |
| EA Block은?           | ExtensionArray를 담는 BlockManager의 블록 |
| ArrayManager 왜 안 써줘? | Deprecated 상태, 옵션 제거 예정             |
| CI가 뭐야?              | 자동 빌드/테스트 시스템                       |
| 로드맵은?                | BlockManager 유지 + Arrow/EA 집중       |

---

## 👍 권장 학습 순서

1️⃣ BlockManager 내부 구조
2️⃣ ExtensionArray & EA Block
3️⃣ Arrow dtype 모델
4️⃣ [[Copy-on-Write Memory Strategy|Copy-on-Write Memory Strategy]]
