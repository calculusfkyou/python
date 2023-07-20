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

# from collections import deque
# def bfs_shortest_path(graph, start, end):
#     visited = set()
#     queue = deque([(start, [start])])  # 使用元組 (頂點, 路徑) 來追蹤路徑

#     while queue:
#         vertex, path = queue.popleft()
#         if vertex == end:
#             return path  # 找到終點，返回路徑
#         if vertex not in visited:
#             visited.add(vertex)
#             neighbors = graph[vertex]
#             for neighbor in neighbors:
#                 queue.append((neighbor, path + [neighbor]))  # 將新頂點加入路徑

#     return None  # 若沒有找到路徑，返回None
# while True:
#     try:
#         # 讀取輸入
#         n, m = map(int, input().split())
#         edges = []
#         for _ in range(m):
#             ai, bi = map(int, input().split())
#             edges.append((ai, bi))
#         # 建立圖的鄰接表表示
#         graph = {}
#         for ai, bi in edges:
#             if ai not in graph:
#                 graph[ai] = []
#             if bi not in graph:
#                 graph[bi] = []
#             graph[ai].append(bi)
#             graph[bi].append(ai)
#         # 從頂點1到頂點n的最短路徑
#         start = 1
#         end = n
#         shortest_path = len(bfs_shortest_path(graph, start, end))
#         # print("最短路徑:", shortest_path)
#         print(shortest_path-2)
#     except EOFError:
#         break
# 7 8
# 1 2
# 1 3
# 2 4
# 3 4
# 4 5
# 4 6
# 5 7
# 6 7  

# def get_factors(n):
#     factors = []
#     # 質因數分解
#     for i in range(2, int(n**0.5) + 1):
#         while n % i == 0:
#             factors.append(i)
#             n //= i
#     if n > 1:
#         factors.append(n)
#     print(factors)
#     # 求得所有因數
#     num_factors = len(factors)
#     all_factors = set()
#     for i in range(1 << num_factors):
#         factor = 1
#         for j in range(num_factors):
#             if (i >> j) & 1:
#                 factor *= factors[j]
#         all_factors.add(factor)
    
#     return sorted(all_factors)

# # 測試
# num = 36
# factors = get_factors(num)
# print(factors)

t=[[16,8] ,[15,8] ,[15,7] ,[16,7] ,[16,6] ,[16,5] ,[15,5] ,[15,6], [14,6] ,[14,5], [13,5] ,[13,6] ,[13,7] ,[14,7] ,[14,8] ,[13,8], [12,8], [12,7] ,[11,7], [11,8] ,[10,8] ,[9,8] ,[9,7] ,[10,7] ,[10,6], [9,6] ,[9,5], [10,5] ,[11,5] ,[11,6], [12,6] ,[12,5], [12,4], [12,3] ,[11,3] ,[11,4] ,[10,4] ,[9,4] ,[9,3] ,[10,3] ,[10,2], [9,2], [9,1], [10,1] ,[11,1] ,[11,2], [12,2] ,[12,1] ,[13,1] ,[14,1] ,[14,2] ,[13,2], [13,3] ,[13,4] ,[14,4] ,[14,3], [15,3] ,[15,4] ,[16,4] ,[16,3], [16,2] ,[15,2] ,[15,1] ,[16,1]]
s=[[1, 8] ,[2, 8] ,[2, 7], [1, 7] ,[1, 6], [1, 5], [2, 5] ,[2, 6] ,[3, 6] ,[3, 5] ,[4, 5] ,[4, 6] ,[4, 7], [3, 7] ,[3, 8], [4, 8], [1, 4] ,[1, 3] ,[2, 3] ,[2, 4] ,[3, 4], [4, 4] ,[4, 3], [3, 3] ,[3, 2] ,[4, 2] ,[4, 1] ,[3, 1], [2, 1] ,[2, 2] ,[1, 2] ,[1, 1], [1, 4], [1, 3], [2, 3] ,[2, 4] ,[3, 4] ,[4, 4], [4, 3] ,[3, 3] ,[3, 2], [4, 2] ,[4, 1] ,[3, 1], [2, 1] ,[2, 2], [1, 2] ,[1, 1] ,[1, 4] ,[1, 3] ,[2, 3] ,[2, 4] ,[3, 4] ,[4, 4] ,[4, 3] ,[3, 3], [3, 2], [4, 2] ,[4, 1] ,[3, 1], [2, 1] ,[2, 2] ,[1, 2] ,[1, 1] ,[1, 4] ,[1, 3], [2, 3], [2, 4] ,[3, 4] ,[4, 4] ,[4, 3] ,[3, 3] ,[3, 2] ,[4, 2] ,[4, 1] ,[3, 1] ,[2, 1] ,[2, 2] ,[1, 2], [1, 1] ,[1, 4] ,[1, 3] ,[2, 3] ,[2, 4],[3, 4] ,[4, 4] ,[4, 3], [3, 3], [3, 2] ,[4, 2] ,[4, 1], [3, 1], [2, 1], [2, 2] ,[1, 2], [1, 1], [1, 4], [1, 3] ,[2, 3] ,[2, 4] ,[3, 4] ,[4, 4] ,[4, 3] ,[3, 3] ,[3, 2], [4, 2] ,[4, 1] ,[3, 1] ,[2, 1], [2, 2], [1, 2] ,[1, 1] ,[1, 4] ,[1, 3] ,[2, 3] ,[2, 4] ,[3, 4] ,[4, 4] ,[4, 3] ,[3, 3] ,[3, 2], [4, 2] ,[4, 1] ,[3, 1] ,[2, 1] ,[2, 2] ,[1, 2] ,[1, 1] ,[5, 8] ,[5, 7] ,[6, 7], [6, 8], [7, 8] ,[8, 8] ,[8, 7], [7, 7], [7, 6] ,[8, 6] ,[8, 5] ,[7, 5] ,[6, 5] ,[6, 6], [5, 6] ,[5, 5] ,[5, 4], [5, 3], [6, 3], [6, 4] ,[7, 4], [8, 4], [8, 3], [7, 3] ,[7, 2] ,[8, 2] ,[8, 1], [7, 1] ,[6, 1] ,[6, 2] ,[5, 2] ,[5, 1], [4, 1], [3, 1], [3, 2] ,[4, 2] ,[4, 3] ,[4, 4] ,[3, 4], [3, 3] ,[2, 3] ,[2, 4] ,[1, 4] ,[1, 3] ,[1, 2], [2, 2] ,[2, 1] ,[1, 1]]
temp=[]
for i in range(len(t)):
    temp.append(t[i][0]-s[i][0])
print(*temp)
def copyfield(t,field):
    n1,n2=0,0
    for j in range(3):
        for i in range(len(field)):
            n1=field[i][0]
            n2=field[i][1]
            t.append([n1,n2])
    return t
def copy(temp2,t,cp):
    n1,n2=0,0
    for i in range(cp):
        n1=t[i][0]
        n2=t[i][1]
        temp2.append([n1,n2])
    temp2.reverse()
    return temp2
subn=4  #處理長度
            tempn=4 #處理dis
            p=subn//2   
            cp=subn*subn//4
            t=[]
            for l in range(find_power_of_two(n)-1):
                dis=[]
                count=tempn-1
                disp=tempn//4
                # print(count)
                # print("--------------")
                while count!=3:
                    for i in range(disp):
                        dis.append(count)
                    count-=2
                dis.append(3)
                dis.append(1)
                dis.append(1)
                dis.append(3)
                if n>4:
                    redis=dis[:]
                    redis.reverse()
                    dis+=redis
                # print(dis)
                # print("--------------")
                t=copyfield(t,field)
                for i in range(4):
                    if i==0:
                        for j in range(0,(subn//2)**2):
                            t[j].reverse()
                    elif i==1:
                        for j in range((subn//2)**2,(subn//2)**2*2): 
                            t[j][1]+=p
                    elif i==2:
                        for j in range((subn//2)**2*2,(subn//2)**2*3):
                            t[j][0]+=p
                            t[j][1]+=p
                    else:
                        temp2=[]
                        temp2=copy(temp2,t,cp)
                        print(dis)
                        print("--------------")
                        print(temp2)
                        print("--------------")
                        for j in range(len(temp2)):
                            temp2[j][0]+=dis[j]
                            n1=temp2[j][0]
                            n2=temp2[j][1]
                            t.append([n1,n2])
                field.clear()
                field=copyfield(field,t)
                subn*=2
                tempn*=2
                p=subn//2
                cp=subn*subn//4
                print(t)
                print("--------------")
            # print(t)
            print(*field[k-1])