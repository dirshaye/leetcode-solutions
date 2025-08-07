class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        start, max_len = 0, 1

        for i in range(n):
            dp[i][i] = True


        for end in range(1,n):
            for begin in range(end):
                if s[begin] == s[end]:
                    if end-begin == 1 or dp[begin+1][end-1] == True:
                        dp[begin][end] = True
                        if end-begin+1 > max_len:
                            start = begin
                            max_len = end-begin+1

        return s[start:start+max_len]



    