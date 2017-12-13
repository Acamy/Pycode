import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
print(np.sum(a))
print(np.mean(a,axis=0))
print(np.mean(a,axis=1))
print(np.average(a,axis=0,weights=[10,5,1]))