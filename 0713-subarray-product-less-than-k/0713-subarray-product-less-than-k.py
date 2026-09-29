class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        count = 0
        left = 0
        product = 1
        if k<=1:
            return 0
        for right in range(0,len(nums)):
            product*=nums[right]
            while product>=k:
                product//=nums[left]
                left+=1
            if product<k:
                count+=right-left+1
        return count