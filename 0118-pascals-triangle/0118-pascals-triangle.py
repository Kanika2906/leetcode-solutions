from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        
        for n in range(numRows):
            p=[]
            for r in range(0,n+1):
                ncr=factorial(n)//(factorial(r)*factorial(n-r))
                p.append(ncr)
            l.append(p)
        return l
        
