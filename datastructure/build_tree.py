# 給後序和中序，輸出前序排列
def build_tree(postorder, inorder):
    if not postorder:
        return ''
    root=postorder[-1]
    idx=inorder.index(root)
    left=build_tree(postorder[:idx], inorder[:idx])
    right=build_tree(postorder[idx:-1], inorder[idx+1:])
    return root+left+right
while True:
    try:
        n= int(input())
        for i in range(n):
            m,postorder,inorder=input().split()
            preorder=build_tree(postorder,inorder)
            print(preorder)
    except EOFError:
        break

# 給前序和中序，輸出後序排列
"""
def build_tree(preorder, inorder):
    if not preorder:
        return ''
    root = preorder[0]
    idx = inorder.index(root)
    left = build_tree(preorder[1:idx + 1], inorder[:idx])
    right = build_tree(preorder[idx + 1:], inorder[idx + 1:])
    return left + right + root

while True:
    try:
        n = int(input())
        for i in range(n):
            m, preorder, inorder = input().split()
            postorder = build_tree(preorder, inorder)
            print(postorder)
    except EOFError:
        break   
"""