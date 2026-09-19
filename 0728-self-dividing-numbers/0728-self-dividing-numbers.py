class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans =[]
        for i in range(left,right+1):
            t =i
            valid = True
            while t>0:
                d = t%10
                if d == 0 or i%d!=0:
                    valid = False
                    break
                t = t//10
            if valid:
                ans.append(i)
        return ans

