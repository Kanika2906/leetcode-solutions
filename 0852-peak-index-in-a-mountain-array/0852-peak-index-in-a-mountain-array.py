class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l = 0
        r = len(arr)-1
        ans = r
        while l<=r:
            mid = (l+r)//2
            if arr[mid]<arr[mid+1]:
                l = mid+1
            else:
                ans = mid
                r = mid-1
        return ans