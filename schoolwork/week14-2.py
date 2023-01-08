class Node:
    def __init__(self, key):
        self.key = key
        self.lptr = None
        self.rptr = None


def preorderTraverse(tree):
    if tree != None:
        print(tree.key)
        preorderTraverse(tree.rptr)
        preorderTraverse(tree.lptr)


def searchBST(tree, target):
    if tree == None:
        return False
    if tree.key > target:
        searchBST(tree.lptr, target)
    elif tree.key < target:
        searchBST(tree.rptr, target)
    else:
        return True


def insertBST(tree, target):
    if tree == None:
        tree = Node(target)
        return tree
    if tree.key > target:
        tree.lptr = insertBST(tree.lptr, target)
    elif tree.key < target:
        tree.rptr = insertBST(tree.rptr, target)
    return tree

def maxbst(tree):
    if tree==None:
        return 0
    return(max(1+maxbst(tree.rptr),1+maxbst(tree.lptr)))

bst = None
data = list(map(int, input().split()))
for i in data:
    bst = insertBST(bst, i)
#print(maxbst(bst)-1)
#9  5  6  3  1  10  14  12  15  20
# preorderTraverse(bst)