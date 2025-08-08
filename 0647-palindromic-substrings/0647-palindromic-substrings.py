class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]* n for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = True
            count +=1

        for end in range(n):
            for begin in range(end):
                if s[begin] == s[end]:
                    if end - begin == 1 or dp[begin+1][end-1]:
                        dp[begin][end] = True
                        count +=1
        return count


        


        