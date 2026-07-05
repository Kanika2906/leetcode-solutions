from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven = 0
        sumOdd = 0
        for i in range(1,2*n+1):
            if i%2==0:
                sumEven +=i
            else:
                sumOdd +=i
        return gcd(sumOdd,sumEven)
            
        