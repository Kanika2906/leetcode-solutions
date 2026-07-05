class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=[]
        sum1 = 0
        for i in nums:
            sum1 += i
            runningSum.append(sum1)
        return runningSum