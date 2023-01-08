class Node:
    def __init__(self, key):
        self.key = key
        self.lptr = None
        self.rptr = None

# global count
def insertBST(tree, target):
    for j in range(1,50):
        if tree == None:
            tree = Node(target)
            bstarray[j]=target
            # count=1
            return tree
        if tree.key > target:
            j=j*2
            tree.lptr = insertBST(tree.lptr, target)
        elif tree.key < target:
            j=j*2+1
            tree.rptr = insertBST(tree.rptr, target)
    return tree

def maxbst(tree):
    if tree==None:
        return 0
    return(max(1+maxbst(tree.rptr),1+maxbst(tree.lptr)))

bst = None
# data = list(map(int, input().split()))
data =[9,5,6,3,1,10,14,12,15,20]
global bstarray
bstarray=[None]*(50)
for i in data:
    bst = insertBST(bst, i)




# bstarray=[None]*((2**maxbst(bst))+1)


#9  5  6  3  1  10  14  12  15  20
print(bstarray)