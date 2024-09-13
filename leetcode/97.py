class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {} 
        def recur(s1_idx, s2_idx, s3_idx):
            if s3_idx >= len(s3):
                return True
            if (s1_idx, s2_idx, s3_idx) in memo:
                return memo[(s1_idx, s2_idx, s3_idx)] 
            s1_use, s2_use = False, False
            if s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:
                s1_use = recur(s1_idx+1, s2_idx, s3_idx+1)
                memo[(s1_idx+1, s2_idx, s3_idx+1)] = s1_use
            if s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:
                s2_use = recur(s1_idx, s2_idx+1, s3_idx+1)
                memo[(s1_idx, s2_idx+1, s3_idx+1)] = s2_use
            if s1_use or s2_use:
                return True 
            return False
        if len(s1) + len(s2) != len(s3):
            return False
        return recur(0, 0, 0)