from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate area between left and right lines
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
