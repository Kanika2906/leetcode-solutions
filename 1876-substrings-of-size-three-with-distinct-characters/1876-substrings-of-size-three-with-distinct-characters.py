class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        seen = set()
        count = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            if right-left+1 == 3:
                count+=1
                seen.remove(s[left])
                left+=1
        return count
