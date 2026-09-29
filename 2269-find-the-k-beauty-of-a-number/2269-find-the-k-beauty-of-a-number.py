class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        s = str(num)
        for i in range(len(s)-k+1):
            window = int(s[i:i+k])
            if window !=0 and num%window==0:
                ans +=1
        return ans