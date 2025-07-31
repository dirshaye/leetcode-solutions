class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        s_reversed = s.strip()[::-1]
        count = 0
        for char in s_reversed:
            if char == ' ':
                break
            count +=1
        return count

        