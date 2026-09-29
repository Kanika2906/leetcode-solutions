class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h = {}
        f = {}
        left = 0
        for ch in s1:
            f[ch]=f.get(ch,0)+1
        for right in range(len(s2)):
            h[s2[right]] = h.get(s2[right],0)+1
            if right -left+1>len(s1):
                h[s2[left]]-=1
                if h[s2[left]]==0:
                    del h[s2[left]]
                left+=1
            if h==f:
                return True
            else:
                continue
        return False
            
