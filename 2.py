import numpy as np
import math

a= np.array([2, 1, 5, 3, 7, 4, 6, 8])

print(np.sort(a))

b= np.array([1, 2, 3, 4])
c=np.array([5, 6, 7, 8])
print("b+c:",np.concatenate((b,c)))

x=np.array([[1, 2], [3, 4]])
y=np.array([[5, 6]])
print("x+y:",np.concatenate((x,y),axis=0))

d=np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],[[0, 1, 2, 3],[4, 5, 6, 7]],[[0 ,1 ,2, 3],[4, 5, 6, 7]]])
print(d.ndim)
print(d.size)
print(d.shape)
# print(d)
print(d.reshape(2,3,4))