import numpy as np

a = np.arange(24).reshape((6,4))
np.savetxt('a.csv',a,fmt='%.1f',delimiter=',')
#print(a[:,1:3,:])
#print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a)

b = np.arange(100).reshape(5,10,2)
b.tofile("b.dat",sep=",",format='%d')
c = np.fromfile("b.dat",dtype=np.int,sep=",")#维度信息丢失
print(c)

np.save("d.npy",b)
d = np.load("d.npy")
print(d)