# Problem: 15. 3Sum
# Link: https://leetcode.com/problems/3sum/
# Tags: Two Pointers, Sorting
# Difficulty: Medium

# Time Complexity:
# - Best case: O(n^2)
# - Worst case: O(n^2)
# Space Complexity: O(1) (excluding result list)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        threesum_list = []

        for i in range(n):
            j, k = i+1, n-1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    threesum_list.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return threesum_list
