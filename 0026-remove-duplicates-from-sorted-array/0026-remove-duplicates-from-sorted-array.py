class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        n = len(nums)
        for i in range(0,n):
            if i!=0 and nums[i]!=nums[i-1]:
                nums[index] = nums[i]
                index+=1
        return index