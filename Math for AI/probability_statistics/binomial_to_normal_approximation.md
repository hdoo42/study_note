---
id: binomial_to_normal_approximation
aliases:
  - 이항분포 정규근사
tags:
  - probability
  - statistics
  - binomial
  - normal
  - approximation
---

# 이항분포와 정규분포의 관계

## 1. 이항분포 (Binomial Distribution)

- 시행 횟수: $n$
- 성공 확률: $p$
- 확률 변수 $X$: 성공 횟수  
- PMF:  
  $$
  P(X=k)=\binom nk p^k(1-p)^{n-k},\quad k=0,1,\dots,n.
  $$

## 2. 정규분포 근사 (Normal Approximation)

### 조건
- $n$이 충분히 크고  
- $np \ge 10$ 그리고 $n(1-p)\ge 10$ (경험적 기준)  

### 근사
$$
X\sim \mathrm{Bin}(n,p)\approx N\bigl(\mu=np,\;\sigma^2=np(1-p)\bigr).
$$

따라서  
$$
P(X=k)\approx \frac{1}{\sqrt{2\pi\,np(1-p)}}\exp\!\Bigl(-\frac{(k-np)^2}{2\,np(1-p)}\Bigr).
$$

### 연속성 보정 (Continuity Correction)
이산 $k$를 연속 근사할 때  
$$
P(X=k)\approx P\bigl(k-0.5 < Y < k+0.5\bigr)
$$  
를 사용하면 정확도가 올라갑니다.  

---

## 3. 예시

- 동전 100번 던져 앞면이 60번 나올 확률:  
  $$
  n=100,\;p=0.5,\;\mu=50,\;\sigma=\sqrt{25}=5
  $$  
  $$
  P(X=60)\approx \frac{1}{\sqrt{2\pi}\,5}\exp\!\Bigl(-\frac{(60-50)^2}{2\cdot25}\Bigr)
  $$

