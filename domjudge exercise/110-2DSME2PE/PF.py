# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def dfs(node):
#     if not node:
#         return 0, 0
#     left_sum, left_max = dfs(node.left)
#     right_sum, right_max = dfs(node.right)
#     node_sum = left_sum + right_sum + node.val
#     node_max = max(left_max, right_max, node_sum * (total_sum - node_sum))
#     return node_sum, node_max

# while True:
#     try:
#         nodes = input().split()
#         total_sum = 0
#         root = TreeNode(int(nodes[0]))
#         queue = [root]
#         i = 1
#         while queue:
#             node = queue.pop(0)
#             if i < len(nodes) and nodes[i] != 'None':
#                 node.left = TreeNode(int(nodes[i]))
#                 queue.append(node.left)
#             i += 1
#             if i < len(nodes) and nodes[i] != 'None':
#                 node.right = TreeNode(int(nodes[i]))
#                 queue.append(node.right)
#             i += 1
#             total_sum += node.val
#         print(dfs(root)[1])
#     except:
#         break

def l(index,res,grid):
    if res==None:
        res=[]
    if (index)>=len(grid):
        return res
    if grid[index]=="None":
        return res
    res.append(grid[index])
    res=l((index+1)*2-1,res,grid)
    res=l((index+1)*2,res,grid)
    return res
    
while True:
    try:
        grid=input().split()
        res=[]
        ans=[]
        total=0
        for x in grid:
            if x!="None":
                total+=int(x)
        for i in range(1,len(grid)):
            res.append(sum(list(map(int,(l(i,None,grid))))))
        for i in res:
            ans.append((total-i)*i)
        print(max(ans))
    except EOFError:
        break