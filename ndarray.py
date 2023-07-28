import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9])
print(arr)
print('arr shape =', arr.shape)
print('number of dimensions =', arr.ndim)
print('number of values =', arr.size)
print('data type :', arr.dtype)
print('class :', type(arr))

arr2 = np.array([[3, 1, 4], [1, 5, 9]])
print(arr2)
print('arr2 shape =', arr2.shape)
print('number of dimensions =', arr2.ndim)
print('number of values =', arr2.size)
print('data type :', arr2.dtype)
print('class :', type(arr2))