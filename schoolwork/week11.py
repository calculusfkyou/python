#8queen
global count,bs
bs=8
count=0
positions=[0]*8

def plotBoard(positions,bs):
    for i in positions:    # add code to produce the 8 x 8 plot
        board=["*"]*8
        board[i]="Q"
        for j in board:
            print(j,end="")
        print() 
def legal(positions,r,c):
    for i in range(r):
        if positions[i]==c:
            return False
        if (r-i)==abs(c-positions[i]):
            return False
    return True
def trySolve(positions,r):
    global count,bs
    if r>=bs:
        count=count+1
        if count==n: # change this to the input number 
            print(positions)
            plotBoard(positions,bs)
        return
    else:
        for c in range(bs):
            if legal(positions,r,c):
                positions[r]=c
                trySolve(positions,r+1)
# read in n
n=int(input())
trySolve(positions,0)