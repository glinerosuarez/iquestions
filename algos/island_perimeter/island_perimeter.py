from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        squares = 0
        intersections = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            downs = 0
            for col in range(cols):
                if grid[row][col]:
                    squares += 1
                    right = grid[row][col + 1] if col < cols - 1 else 0
                    down = grid[row + 1][col] if row < rows - 1 else 0
                    downs += down
                    intersections += right + down
            if downs == 0 and squares > 0:
                break

        return squares * 4 - intersections * 2


