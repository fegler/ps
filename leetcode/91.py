class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1 for _ in range(len(s)+1)]
        def recur(idx):  
            if memo[idx] != -1:
                return memo[idx]
            if idx >= len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx == len(s)-1:
                return 1
            
            ## single use
            ret = recur(idx+1)

            ## double use 
            if int(s[idx:idx+2]) <= 26:
                ret += recur(idx+2)
            memo[idx] = ret
            return memo[idx]
        return recur(0)