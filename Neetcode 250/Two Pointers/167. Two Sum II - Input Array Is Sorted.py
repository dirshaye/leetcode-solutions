# Problem: 167. Two Sum II – Input Array is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Tags: Two Pointers
# Difficulty: Medium

# Time Complexity:
# - Best case: O(1)   — pair found in first check
# - Worst case: O(n)  — traverse entire array once
# Space Complexity: O(1)

# Two-pointer magic: just walk two dudes toward each other until they high-five 🎯

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left <= right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # 1-based index
            elif current_sum > target:
                right -= 1
            else:
                left += 1
