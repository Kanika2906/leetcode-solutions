class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = high
        while low<=high:
            mid = (low+high)//2

            days_needed = 1
            weight_count = 0
            for i in weights:
                if i+weight_count>mid:
                    days_needed+=1
                    weight_count = 0
                weight_count+=i
            
            if days_needed<=days:
                ans = min(mid,ans)
                high = mid-1
            else:
                low = mid+1
        return ans