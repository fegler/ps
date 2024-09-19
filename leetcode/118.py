class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for i in range(1, numRows):
            now = [1]
            for j in range(1, i):
                now.append(ret[i-1][j-1]+ret[i-1][j])
            now.append(1)
            ret.append(now)
        return ret