from math import ceil
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        visited_start = False
        visited_end = False

        size = len(nums)
        start = 0
        end = size - 1
        index = (end - start) // 2

        if size == 1:
            return 0 if nums[0] == target else -1

        if size == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        while ((not (visited_start and visited_end)) or ((end - start) > 1)) and index < size:

            val = nums[index]
            if val == target:
                return index
            else:
                if val < target:
                    if start == index:
                        index = index + 1
                        start = index
                        visited_start = True
                    else:
                        start = index
                        index = index + (end - start) // 2
                        visited_start = True
                else:
                    if end == index:
                        index = index - 1
                        end = index
                        visited_end = True
                    else:
                        end = index
                        index = index - ceil((end - start) // 2)
                        visited_end = True
        else:
            return - 1
