class Solution(object):
    def generate(self, numRows):
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            ans=[[1],[1,1]]
            for i in range(numRows-2):
                temp=[1]
                for j in range(len(ans[-1])-1):
                    temp.append(ans[-1][j]+ans[-1][j+1])
                temp.append(1)
                ans.append(temp)
            return ans