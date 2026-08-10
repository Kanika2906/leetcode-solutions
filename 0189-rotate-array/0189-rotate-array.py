class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        def rotated(nums,left,right):
            while left<right:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1
        rotated(nums,n-k,n-1)
        rotated(nums,0,n-k-1)
        rotated(nums,0,n-1)
        