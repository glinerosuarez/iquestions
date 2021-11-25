"""
Suppose you're given a matrix of 1s and 0s that represents a map of rivers. You can assume that the grid cells in your
map are only connected horizontally and vertically (e.g. no diagonal connections). You can assume that 1 represents
water (your river) and 0 represents land/your river bank. Each cell has a length of 1 and is square in your map. Given
this, write code to determine the perimeter of your river.

Examples:

Input: [[1,0]]
Output: 4

Input: [[1,0,1],
        [1,1,1]]
Output: 12
"""
from typing import List


def compute_river_perimeter(map: List[List[int]]):
    y_length, x_length = len(map), len(map[0])

    def depth_first_search(y: int, x: int) -> int:
        if (
                y >= y_length
                or x >= x_length
                or y < 0
                or x < 0
                or map[y][x] == 0
        ):
            return 1

        elif map[y][x] == 1:
            map[y][x] = 2
            return (
                    depth_first_search(y + 1, x)
                    + depth_first_search(y - 1, x)
                    + depth_first_search(y, x + 1)
                    + depth_first_search(y, x - 1)
            )

        else:
            return 0

    # Find the first node
    for row in range(y_length):
        for col in range(x_length):
            if map[row][col] == 1:
                result = depth_first_search(row, col)
                break
            break
    return result


if __name__ == '__main__':
    print("testing solution...")
    assert compute_river_perimeter([[1, 0]]) == 4, f"{compute_river_perimeter([[1, 0]])} is not equal to 4"
    assert compute_river_perimeter([[1, 0, 1],
                                    [1, 1, 1]]) == 12
    print("All test passed :))")
