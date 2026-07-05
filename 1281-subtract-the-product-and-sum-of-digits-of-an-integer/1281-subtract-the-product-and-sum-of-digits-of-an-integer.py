class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1 =0
        product=1
        temp = n
        while temp>0:
            d = temp%10
            sum1+=d
            product*=d
            temp//=10
        return product - sum1


