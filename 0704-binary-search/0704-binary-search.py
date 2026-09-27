class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        def binarysearch(nums,low,high,target):
            if low>high:
                return -1
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return binarysearch(nums,mid+1,high,target)
            else:
                return binarysearch(nums,low,mid-1,target)
        a = binarysearch(nums,left,right,target)
        return a