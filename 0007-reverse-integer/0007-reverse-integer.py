class Solution:
    def reverse(self, x: int) -> int:
        r =0
        if x>0:
            while x>0:
                d = x%10
                r = r*10 + d
                x = x//10
        else:
            x = -(x)
            while x>0:
                d = x%10
                r = r*10 + d
                x = x//10
            r=-(r)

        if r < -2**31 or r > 2**31 - 1:
            return 0
        return r


       
    
        

        
        