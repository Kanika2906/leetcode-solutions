class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        no = 0
        r = len(grid)
        c = len(grid[0])
        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j]<0:
                    no+=1
        return no
        