class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for i in range(len(accounts)):
            sum1 = 0
            sum1 = sum(accounts[i])
            l.append(sum1)
        r = max(l)
        return r
            
            