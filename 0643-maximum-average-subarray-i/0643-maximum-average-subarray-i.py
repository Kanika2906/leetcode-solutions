class Solution:
    def findMaxAverage(self, arr: list[int], k: int) -> float:
        window_sum = sum(arr[:k])
        window_avg = window_sum/k
        ans = window_avg
        for right in range(k,len(arr)):
            window_sum+=arr[right]
            window_sum-=arr[right-k]
            window_avg = window_sum/k
            ans = max(ans,window_avg)
        return ans