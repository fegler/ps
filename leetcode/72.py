class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        def recur(w1_idx, w2_idx):
            if w1_idx == len(word1):
                return len(word2) - w2_idx
            if w2_idx == len(word2):
                return len(word1) - w1_idx

            if memo[w1_idx][w2_idx] != -1:
                return memo[w1_idx][w2_idx]

            ## match 
            if word1[w1_idx] == word2[w2_idx]:
                min_dist = recur(w1_idx+1, w2_idx+1)
            else:
            ## remove 
                rem = recur(w1_idx+1, w2_idx) + 1
                ## insert
                ins = recur(w1_idx, w2_idx+1) + 1
                ## replace 
                rep = recur(w1_idx+1, w2_idx+1) + 1
                min_dist = min(rem, ins, rep)
            memo[w1_idx][w2_idx] = min_dist
            return memo[w1_idx][w2_idx]
        return recur(0, 0)