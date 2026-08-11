class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest = 0
        my_set = set(nums)
        for i in my_set:
            if i-1 not in my_set:
                current = i
                count = 1
                while current+1 in my_set:
                    count+=1
                    current+=1
                largest = max(largest,count)
        return largest
        