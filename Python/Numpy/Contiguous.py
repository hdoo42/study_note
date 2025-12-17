import numpy as np

def info(name, arr):
    print(f"{name:8s} shape={arr.shape}, dtype={arr.dtype}, "
          f"strides={arr.strides}, C={arr.flags['C_CONTIGUOUS']}, F={arr.flags['F_CONTIGUOUS']}")

# 0) 기본 배열: C-연속 (row-major)
a = np.arange(12, dtype=np.int8).reshape(3, 4)
info("a", a)                  # 기대: C=True, F=False, strides=(4, 1)

# 1) 전치: 보통 F-연속 (column-major) 뷰
aT = a.T
info("a.T", aT)               # 기대: C=False, F=True,  strides=(1, 4)

# 2) 마지막 축을 간격 2로 슬라이스 → '비연속' 뷰
s = a[:, ::2]
info("a[:,::2]", s)           # 기대: C=False, F=False, strides=(4, 2)

# 3) 첫 축을 간격 2로 슬라이스 → 이것도 '비연속'
t = a[::2, :]
info("a[::2,:]", t)           # 기대: C=False, F=False, strides=(8, 1)

# 4) 비연속 뷰를 C/F-연속으로 '복사해서' 맞추기
sC = np.ascontiguousarray(s)
sF = np.asfortranarray(s)
info("sC", sC)                # 기대: C=True,  F=False, strides=(2, 1)
info("sF", sF)                # 기대: C=False, F=True,  strides=(1, 3)

# 5) 브로드캐스트 뷰( stride=0 등장 ) → 연속 아님
x  = np.ones((4, 1), dtype=np.int8)          # 기본 C-연속
bx = np.broadcast_to(x, (4, 5))              # 읽기전용 뷰, 열을 '복제'
info("x",  x)                                # 기대: strides=(1, 1),   C=True,  F=False
info("bx", bx)                               # 기대: strides=(1, 0),   C=False, F=False

