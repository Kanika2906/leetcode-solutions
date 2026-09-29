class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        seen = set()
        window_sum = 0
        left = 0
        ans = window_sum
        for right in range(len(nums)):
            while nums[right] in seen:
                window_sum -=nums[left]
                seen.remove(nums[left])
                left+=1
            window_sum+=nums[right]
            seen.add(nums[right])
            if right-left+1 == k:
                ans = max(ans,window_sum)
                window_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
        return ans