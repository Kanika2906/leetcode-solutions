class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        h = {}
        for right in range(len(s)):
            h[s[right]] = h.get(s[right],0)+1
            while h[s[right]]>2:
                h[s[left]]-=1
                left+=1
                if h[s[left]]==0:
                    del h[s[left]]
            ans = max(ans,right-left+1)
        return ans


