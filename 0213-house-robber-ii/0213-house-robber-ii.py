class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        arob1, arob2 = 0,0
        brob1, brob2 = 0,0

        for i in range(len(nums)-1):
            temp = max(nums[i]+arob1, arob2)
            arob1 = arob2
            arob2 = temp
        
        for i in range(1, len(nums)):
            temp = max(nums[i]+brob1, brob2)
            brob1 = brob2
            brob2 = temp

        return max(arob2, brob2)
            
        
        