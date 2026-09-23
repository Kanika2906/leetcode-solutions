class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d ={}
        for i in magazine:
            d[i]=d.get(i,0)+1
        for i in range(0,len(ransomNote)):
            if ransomNote[i] not in d:
                return False
            else:
                d[ransomNote[i]]-=1
            if d[ransomNote[i]]<0:
                return False
        return True
