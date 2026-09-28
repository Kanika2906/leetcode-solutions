class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left = 0
        window_sum = sum(arr[:k])
        window_avg = window_sum//k
        ans = 1 if window_avg>=threshold else 0
        for right in range(k,len(arr)):
            window_sum+=arr[right]
            window_sum-=arr[left]
            left+=1
            window_avg = window_sum//k
            if window_avg>=threshold:
                ans+=1
        return ans
