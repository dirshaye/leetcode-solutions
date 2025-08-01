class Solution:
    def greatestLetter(self, s: str) -> str:
        chars = set(s)
        best = ''

        for c in range(26):
            lower = chr(ord('a')+c)
            upper = chr(ord('A')+c)

            if lower in chars and upper in chars:
                best = upper

        return best
        