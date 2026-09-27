class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count = 0
        for row in grid:
            left = 0
            right = c-1
            while left<=right:
                mid = (left+right)//2
                if row[mid]<0:
                    right = mid-1
                else:
                    left = mid+1
            count += c - left
        return count
