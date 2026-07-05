class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies=max(candies)
        ans=[]
        for i in candies:
            if (extraCandies + i)>=max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans