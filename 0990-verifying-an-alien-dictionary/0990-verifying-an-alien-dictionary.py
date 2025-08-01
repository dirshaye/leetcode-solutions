class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}

        def helper(w1, w2):
            for c1, c2 in zip(w1, w2):
                if rank[c1] < rank[c2]:
                    return True
                elif rank[c1] > rank[c2]:
                    return False
            return len(w1) <= len(w2)

        for i in range(len(words)-1):
            if not helper(words[i], words[i+1]):
                return False
        return True

