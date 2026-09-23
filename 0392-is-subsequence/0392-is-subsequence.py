class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        for i in range(0,len(t)):
            if j<len(s) and s[j]==t[i]:
                j+=1
        return j==len(s)