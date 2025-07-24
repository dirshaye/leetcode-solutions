from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def rotate(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        k %= n  # Normalize k
        rotate(0, n - 1)
        rotate(0, k - 1)
        rotate(k, n - 1)