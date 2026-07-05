class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            count=[0]*26
            for i in s:
                count[ord(i)-ord('a')]+=1
            for i in t:
                p = ord(i)-ord('a')
                count[p]-=1
                if count[p]<0:
                    return False
            
        return all(x == 0 for x in count)