import numpy as np

arr1=np.array([1,2,3,4,5,6,7,8])
print('arr1 =',arr1)
print(arr1.shape)
print(arr1.ndim)

arr2=arr1.reshape(2,4)
print('arr2 =',arr2)
print(arr2.shape)
print(arr2.ndim)

arr3=arr1.reshape(1,8)
print('arr3 =',arr3)
print(arr3.shape)
print(arr3.ndim)

arr4=arr1.reshape(1,-1)
print('arr4 =',arr4)
print(arr4.shape)
print(arr4.ndim)

arr5=arr1.reshape(2,-1)
print('arr5 =',arr5)
print(arr5.shape)
print(arr5.ndim)

arr6=arr5.reshape(-1)
print('arr6 =',arr6)
print(arr6.shape)
print(arr6.ndim)

arr7=arr1.reshape(2,2,2)
print('arr2 =',arr7)
print(arr7.shape)
print(arr7.ndim)

arr8=arr1.reshape(2,2,-1)
print('arr8 =',arr8)
print(arr8.shape)
print(arr8.ndim)

arr9=arr8.reshape(-1)
print('arr9 =',arr9)
print(arr9.shape)
print(arr9.ndim)

