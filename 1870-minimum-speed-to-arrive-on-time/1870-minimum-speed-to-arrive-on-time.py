class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        left = 1
        right = 10**7
        ans = -1
        while left<=right:
            mid = left+((right -left)//2)
            time = 0
            for i in range(len(dist)-1):
                time+= (dist[i]+mid-1)//mid
            time+=dist[-1]/mid
            if time<=hour:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans 
