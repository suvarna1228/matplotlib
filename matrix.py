import numpy as np
import math
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) 
print("shape:",a.shape)
if len(a.shape)== a.ndim:
    print("true")
else:
    print("false")
print("dimention:",a.ndim)
print("array",a.size)
if a.size == math.prod(a.shape):
    print("true")
else:
    print("false")

print("datatype:",a.dtype)