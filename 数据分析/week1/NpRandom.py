import numpy as np

a = np.random.rand(3,4,5)
print(a)

b = np.random.randn(3,4,5)#符合正太分布
print(b)

c = np.random.randint(100,200,(3,4))#均匀分布
print(c)

np.random.seed(10)
print(np.random.randint(100,200,(3,4)))
np.random.seed(10)#通过设置相同的种子来产生相同的随机数组
print(np.random.randint(100,200,(3,4)))