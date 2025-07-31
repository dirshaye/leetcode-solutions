class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_dict ={}
        for char in s:
             if char in unique_dict:
                 unique_dict[char] +=1
             else:
                 unique_dict[char] = 1
        
        for index, char in enumerate(s):
            if unique_dict[char] == 1:
                return index
        return -1

        