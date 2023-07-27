add=lambda a,b: a+b
print(add(2,3))

find_max=lambda x,y: x if(x>y) else y
print(find_max(-5,3))

L=[1,2,3,4,5,6,7,8]
even_list=[i for i in L if(i%2==0)]
print(even_list)

odd_list=lambda x:[i for i in x if(i%2==1)]
print(odd_list(L))