class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        s=0
        for i  in stones:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in jewels:
            t = d.get(i,0)
            s+=t
            
        return s
