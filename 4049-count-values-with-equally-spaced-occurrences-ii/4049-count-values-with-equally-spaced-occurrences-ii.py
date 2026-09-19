class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        h ={}
        special = 0
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = [i]
            else:
                h[nums[i]].append(i)
        for i in h.values():
            if len(i)>=3:
                gap = i[1]-i[0]
                valid = True
                for j in range(0,len(i)-1):
                    if i[j+1] - i[j] != gap:
                        valid = False
                        break
                if valid == True:
                    special+=1
                    
        return special
        
            