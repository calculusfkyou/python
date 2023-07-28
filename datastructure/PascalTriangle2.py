class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            ans=[[1],[1,1]]
            for i in range(rowIndex-1):
                temp=[1]
                for j in range(len(ans[-1])-1):
                    temp.append(ans[-1][j]+ans[-1][j+1])
                temp.append(1)
                ans.append(temp)
            return ans[-1]