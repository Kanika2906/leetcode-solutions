class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        n=num
        while n>0:
            digit=n%10
            if digit!=0 and num % digit==0:
                count+=1
            n//=10
        return count
        