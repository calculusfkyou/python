#num1, num2, num3 = eval(input ('Enter three numbers separated by commas:'))
#total = num1 + num2 + num3
#average = total /3
#print('total = %d, and average = %.2f' %(total, average))

# from cmath import pi
# import math
# radius = eval(input('Enter the radius:'))
# area = radius * radius * math.pi
# perimeter = 2 * math.pi * radius
# print('Area = %.2f' %(area))
# print('Perimeter = %.2f'%(perimeter))
# def build_tree(postorder, inorder):
#     if not postorder:
#         return ''
#     root=postorder[-1]
#     idx=inorder.index(root)
#     left=build_tree(postorder[:idx], inorder[:idx])
#     right=build_tree(postorder[idx:-1], inorder[idx+1:])
#     return root+left+right

# while True:
#     try:
#         n= int(input())
#         for i in range(n):
#             m,postorder,inorder=input().split()
#             preorder=build_tree(postorder,inorder)
#             print(preorder)
#     except EOFError:
#         break

for i in range(1,92 ):
    print(i+i+1+i+2+i+3+i+4+i+5+i+6+i+7+i+8+i+9,end=" ")