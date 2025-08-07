class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_the_word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_the_word = True
    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for child in node.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                elif char in node.children:
                    node = node.children[char]
                else:
                    return False
            return node.is_end_of_the_word

        return dfs(0, self.root)
        
                


                
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)