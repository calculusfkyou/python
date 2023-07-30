import numpy as np

# .sum() 可以算總和
arr=np.array([9,8,7,6,5,4,3,2,1])
mat=arr.reshape(3,-1)
print('mat =')
print(mat)
print(mat.shape)
print(mat.ndim)
print(mat.sum())  

# .transpose() -> 列與行轉換
mat_T=mat.T  # mat_T = mat.transpose()
print('transpose of mat =')
print(mat_T)
print('mat =')
print(mat)

# np.diag -> 取對角線得一維陣列
d=np.diag(mat)
print(d)
print(d.sum())
print(mat.trace())

# .flatten() -> 將多維陣列轉換成一維陣列
vect=mat.flatten()
print('vect =',vect)
print(vect.shape)

# np.arrange()
# ex : [1 2 3 4 5]
r5=range(5)
print(r5)
print(type(r5))

list_r5=list(r5)
print(type(list_r5))

np_r5=np.arrange(5)
print(np_r5)
print(type(np_r5))

r=np.arrange(3,9)
print(r)

# np,arrange 不包含尾
print(np.arrange(3,9))
print(np.arrange(3,9,2))
print(np.arrange(0,1,0.1))
print(np.arrange(0,1.01,0.1))
# np.linspace(begin,end,val) 包含尾
# val 的值表示會在區間內取幾個值 endpoint可控制小數點
print(np.linspace(0,1,10))
print(np.linspace(0,1,10,endpoint=False))
print(np.linspace(0,1,11))

# np.zeros() 預設陣列元素等於0
# np.ones()  預設陣列元素等於1
# np.eye()   預設陣列對角等於1 
# dtype可控制資料型態
A=np.zeros((2,3))
print(A)
B=np.zero((2,3),dtype=int)
print(B)
C=np.ones((3,2))
print(C)
D=np.ones(5,dtype=int)
print(D)
E=np.eye(5,dtype=np.int32)
print(E)

# np.vstack((arr1,arr2))  垂直合併
# np.hstack((arr1,arr2))  水平合併
# np.vsplit(arr,val)      val為分成個小陣列
# np.hsplit(arr,val)
arr1=np.array([[1,2,3][4,5,6]])
print("arr1 =",arr1)
arr2=np.array([[6,5,4],[1,2,3]])
print('arr2 =',arr2)
arr3=np.vstack((arr1,arr2))
print('arr3 =',arr3)
arr4=np.hstack((arr1,arr2))
print('arr4 =',arr4)
arr5,arr6=np.vsplit(arr3,2)
print('arr5 =',arr5)
print('arr6 =',arr6)
arr7,arr8,arr9=np.hsplit(arr4,3)
print('arr 7=',arr7)
print('arr8 =',arr8)
print('arr9 =',arr9)

# .copy()      可避免多維陣列複製後因指標影響到原陣列的情況
# np.sort()    對陣列裡元素排序，多維陣列可直接使用
x=np.array([[-1,2,-3,4],[5,-6,7,-8]])
y=x
y[0,0]=0
print('y =',y)
print('x =',x)
z=x.copy()
z[0,0]=1
print('z =',z)
print('x =',x)
print('y =',y)
s=np.sort(x)
print('s =',s)
print('x =',x)
x.sort()
print('x =',x)