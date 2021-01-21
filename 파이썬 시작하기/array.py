import numpy as np

arr = np.array([1,2,3])
print(arr)
print(type(arr))

matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)

A = np.array([[1,2], [3,4]])
B = np.array([[1,1], [1,1]])
C = A+B
print(C)

a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[2,3],[2,3]])
c = np.matmul(a, b)
print(c)

d = np.array([[1,2],[3,4]])
k = 10
e = k*d
print(e)