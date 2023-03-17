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