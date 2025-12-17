import numpy as np
#
# ## quiz 18
# a = np.array([[0,1,2], [3,4,5]])
# print(np.tile(a,2))
# print(np.tile(a, (3,2)))
#
#
# np.linspace(2, 12, 5)
#
# np.random.randint(0, 2)
#
# lst = [1,2,3,4]
# result = np.random.shuffle(lst)
# print(lst)
# print(result)
#
# A = np.array([[1,3], [2,4]])
# B = np.array([[0,2], [2,1]])
#
# print(np.dot(A,B))
# print(np.dot(B, A))
# print(np.inner( np.dot(A,B), np.dot(B,A)))
#
a = np.empty((50,50))
b = np.zeros_like(a)
b

## quiz 15
# data = np.arange(1, 13).reshape(3,4)
# data1 = data.reshape(4,3)
# data1.flags
# data2 = data.flatten()
# data2.flags
# data[0][0]= 20
#
# print(data)
# print(data1)
# print(data2)


# import pandas as pd
# from pandas.testing import assert_frame_equal
#
# pd.options.mode.copy_on_write = True
# # df = pd.DataFrame(
# #     {
# #         "i32": np.array([1, 2, 3], dtype="int32"),
# #         "i64": np.array([0.1, 0.2, 0.3], dtype="int64"),
# #     }
# # )
# #
# # df2 = pd.DataFrame(
# #     {
# #         "i64": np.array([1, 2, 3, 4], dtype="int64"),
# #         "i642": np.array([1, 2, 3, 4], dtype="int64"),
# #     }
# # )
# #
# # df._data
# # df2._data
# #
# # df3 = df2[0::2]
# # df3._data
# # blk = df3._mgr.blocks[0]
# # blk.values
# # blk.mgr_locs
# #
# # df = pd.DataFrame({
# #     "A": pd.Series([1, 2, None], dtype="Int64")
# # })
# #
# # df._data
#
# df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})
#
# subset = df["foo"]
#
# subset.iloc[0] = 100
#
# df
#
#
try: 
    x = 5 + "ham"
except ZeroDivisionError:
    print("darn it")

finally:
    print("Let's go futher!")

y= 10 + 2

# random.randint(1, 100)

# class A(object):
#     def __init__(self, x):
#         self.x=x
#     def f(self):
#         return 10 * self.x
#     def g(self):
#         return 100*self.x
#
# class B(A):
#     def __init__(self, x=42, y=99):
#         super().__init__(x)
#         self.y=y
#     def f(self):
#         return 1000* self.x
#     def g(self):
#         return (super().g(), self.y)
#
#
# a = A(5)
# b = B(7)
# print(a.f())
# print(a.g())
# print(b.f())
# print(b.g())
