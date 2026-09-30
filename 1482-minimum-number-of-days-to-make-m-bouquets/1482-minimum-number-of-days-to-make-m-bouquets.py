class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low<=high:
            mid = (low + high)//2
            flower = 0
            bouq = 0 
            for day in bloomDay:
                if day<=mid:
                    flower+=1
                    if flower==k:
                        bouq +=1
                        flower =0
                else:
                    flower = 0
            if bouq>=m:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
            