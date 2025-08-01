class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        count = 0

        for c in range(26):
            lower = chr(ord('a') +c)
            upper = chr(ord('A') +c)
            if lower in chars and upper in chars:
                count +=1
        return count 

               

        