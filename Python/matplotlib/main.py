import matplotlib.pyplot as plt
import numpy as np

# 4.
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# answer
plt.plot(x,y)
plt.plot(x,y,"o")
# plt.plot(x, y, color="b", marker="o", linestyle="None")
plt.show()

# 5.
# plt.axis(( 0,6,0,20 ))
# plt.axis([0, 6, 0, 20])
# plt.plot(x, y, [0,6, 0,20])
# plt.xlim(0, 6)
# plt.ylim(0, 20)
plt.xticks(range(0,7))
plt.yticks(range(0,21))
#
# # 6.
# plt.plot(x,y, label= "stock-price")
# plt.legend()
#
plt.show()

# # 7
# import numpy as np
# import matplotlib.pyplot as plt
#
# N = 5
# menMeans = (20, 35, 30, 35, 27)
# womenMeans = (25, 32, 34, 20, 27)
# x = np.arange(N)
# width = 0.35
# p1 = plt.bar(x - width / 2, menMeans, width, color="red", label="Men")
# p2 = plt.bar(x + width / 2, womenMeans, width, label="Women")
# plt.ylabel("Scores")
# plt.title("Scores by group and gender")
# plt.xticks(x, ("G1", "G2", "G3", "G4", "G5"))
# plt.yticks(np.arange(0, 81, 10))
# plt.legend()
# plt.show()

# #8
# import numpy as np
# import matplotlib.pyplot as plt
# N=50
# x = np.random.rand(N-1)
# y = np.random.rand(N-1)
# # (x.shape, y.shape)
# colors = np.random.rand(N)
# # colors.shape
# area = (30 * np.random.rand(N))**2
# # area.shape
# plt.scatter(x,y,s=area, c=colors, alpha = 0.5)
# plt.show()

#9
import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(21) #1
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(22) #2
plt.show()
#
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# #10
# plt.subplot(211)
# plt.cla()

plt.show()

# # 25
#
# import numpy as np
#
# sample = np.array(["1", "2", "3", "unknown", "5"])
# print(sample)
#
# # sample_with_nan = np.where(np.char.isnumeric(sample), sample, np.nan)
# # print(sample_with_nan)
# # numeric_data = sample_with_nan.astype(float)
#
# mask = np.char.isnumeric(sample)
#
# numeric_data = np.full(sample.shape, np.nan, dtype=float)
#
# numeric_data[mask] = sample[mask].astype(float)
#
# print(numeric_data)

# # 30
#
# from sklearn.preprocessing import Binarizer
#
# X = [[1, -1, 2], [2, 0, 0], [0, 1, -1]]
#
# bnz = Binarizer(threshold=1.1)
# bnz.transform(X)
#

#31

from sklearn.preprocessing import LabelBinarizer

lb = LabelBinarizer()
y = ['A','B','A','A','B','C','C','A','C','B']
lb.fit(y)
lb.classes_
y2 = lb.transform(y)
y2

#32

# #32-1
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import ADASYN
#
# # 1. 예제 데이터 생성 (불균형 데이터: 90% vs 10%)
# X, y = make_classification(
#     n_samples=1000, 
#     n_classes=2, 
#     weights=[0.9, 0.1], 
#     flip_y=0, 
#     random_state=42
# )
#
# print(f"원본 데이터 분포: {Counter(y)}")
# # 출력 예: Counter({0: 900, 1: 100})
#
# # 2. ADASYN 객체 생성 및 적용
# # sampling_strategy='auto'는 1:1 비율이 되도록 맞춥니다.
# adasyn = ADASYN(random_state=42, sampling_strategy='auto')
#
# X_resampled, y_resampled = adasyn.fit_resample(X, y)
#
# # 3. 결과 확인
# print(f"ADASYN 적용 후 분포: {Counter(y_resampled)}")
# # 출력 예: Counter({0: 900, 1: 899}) -> 거의 1:1로 맞춰짐
#
# from imblearn.pipeline import Pipeline # sklearn pipeline이 아님에 주의
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import make_classification
#
# # 1. 예제 데이터 생성 (불균형 데이터: 90% vs 10%)
# X, y = make_classification(
#     n_samples=1000, 
#     n_classes=2, 
#     weights=[0.9, 0.1], 
#     flip_y=0, 
#     random_state=42
# )
#
# # 데이터 분리
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
#
# # 파이프라인 구축 (ADASYN -> 분류기)
# pipeline = Pipeline([
#     ('oversampler', ADASYN(random_state=42)),
#     ('classifier', DecisionTreeClassifier())
# ])
#
# # 학습 (알아서 학습 데이터만 오버샘플링 후 모델 훈련)
# pipeline.fit(X_train, y_train)
#
# # 평가 (테스트 데이터는 오버샘플링 되지 않은 상태로 평가됨)
# score = pipeline.score(X_test, y_test)
# print(f"정확도: {score:.4f}")
