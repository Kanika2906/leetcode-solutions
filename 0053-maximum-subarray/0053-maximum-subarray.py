class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        result = float("-inf")
        for i in nums:
            total+=i
            result = max(result,total)
            if total<0:
                total = 0
        return result