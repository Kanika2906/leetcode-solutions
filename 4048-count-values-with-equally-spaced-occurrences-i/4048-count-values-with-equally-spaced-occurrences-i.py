class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        special = 0
        h = {}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = [i]
            else:
                h[nums[i]].append(i)
        for i in h.values():
            if len(i) == 3:
                if i[1] - i[0] == i[2] - i[1]:
                    special +=1
                
        return special
            