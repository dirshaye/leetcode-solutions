class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(take):
            n = len(take)
            l, r = 0, n-1

            while l <= r:
                mid = (l+r)//2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid + 1
                else:
                    r = mid-1

        for row in matrix:
            if binarySearch(row):
                return True
            
        return False
               

                    
        