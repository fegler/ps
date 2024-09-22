class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            ret[i] = ret[i & (i-1)] + 1
        return ret