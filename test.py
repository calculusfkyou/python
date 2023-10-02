# from cmath import pi
# import math
# radius = eval(input('Enter the radius:'))
# area = radius * radius * math.pi
# perimeter = 2 * math.pi * radius
# print('Area = %.2f' %(area))
# print('Perimeter = %.2f'%(perimeter))

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



from math import *
if __name__ == "__main__":
    print(sqrt(64))