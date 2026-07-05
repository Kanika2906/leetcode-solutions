class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = set(nums1)
        numss = set(nums2)
        return(list(nums&numss))
        