import numpy as np
import math

a=np.array([1, 2, 3, 4, 5, 6])
print(a.shape)
b=a[np.newaxis,:]
print(b.shape)
c=a[:,np.newaxis]
print(c.shape)
d=np.expand_dims(a,axis=1)
print(d.shape)
e=np.expand_dims(a,axis=0)
print(e.shape)
