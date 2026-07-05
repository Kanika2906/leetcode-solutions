class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        count = 0
        for i,j in d.items():
            if j==1:
                count+=i
        return count 
        
        