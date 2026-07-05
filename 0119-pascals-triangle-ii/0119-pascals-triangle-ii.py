from math import factorial
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[]
        for n in range(rowIndex+1):
            p=[]
            for r in range(n+1):
                ncr=factorial(n)//(factorial(n-r)*factorial(r))
                p.append(ncr)
            l.append(p)
        return l[rowIndex]