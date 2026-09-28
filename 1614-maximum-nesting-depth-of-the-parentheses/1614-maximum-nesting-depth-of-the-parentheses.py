class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        depth = 0
        for i in s:
            if i =='(':
                depth+=1
                ans = max(ans,depth)
            elif i ==")":
                depth-=1
        return ans
