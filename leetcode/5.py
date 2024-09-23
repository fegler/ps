class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ret = [0,0]

        for i in range(len(s)):
            dp[i][i] = True 
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True 
                ret = [i, i+1]
        
        for length in range(2, len(s)):
            for i in range(len(s)-length):
                j = i + length
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True 
                    ret = [i, j]
        start, end = ret 
        return s[start:end+1]