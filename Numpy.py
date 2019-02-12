import numpy as np
import time
import sys
a = np.array([[1,2,3]])
print(a)
b = np.array(([1,2,3],([7,8,9])))
print(b)
#Numpy array occupy less time
s = range(1000)
print(sys.getsizeof(5)* len(s))
d = np.arange(1000)
print(d.size * d.itemsize)

size= 1000000
l1 = range(size)
l2 = range(size)
a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [(x,y) for x,y in zip(l1,l2)]
print((time.time() - start) * 1000)
start = time.time()
result = a1 + a2
print((time.time() - start) * 1000)

print(a.ndim)
print(b.ndim)
print(a.shape)
print(b.shape)
print(a.itemsize)
print(a.dtype)
print(a.size)
print(b[1,2])
c = np.array([(1,2,3,4),(7,8,9,10),(96,97,98,77)])
print(c[0:,2])