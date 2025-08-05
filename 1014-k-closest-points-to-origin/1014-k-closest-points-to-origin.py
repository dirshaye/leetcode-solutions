class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        max_heap = []
        for x, y in points:
            distance = -(x*x + y*y)
            heapq.heappush(max_heap, (distance, [x,y]))
            if len (max_heap) > k:
                heapq.heappop(max_heap)

        return [point for _, point in max_heap]


        

        