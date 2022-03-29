"""
Given a sorted (in increasing order) array of positive numbers, can you find the smallest positive integer that cannot
be represented as a sum of elements from the array?

Input:  arr[] = [1, 3, 6, 10, 11, 15]
Output: 2

Input:  arr[] = [1, 1, 1, 1]
Output: 5

Input:  arr[] = [1, 1, 3, 4]
Output: 10
"""
from typing import List


def find_smallest(arr: List[int]):

    n = len(arr)
    res = 1  # Initialize result

    # Traverse the array and increment
    # 'res' if arr[i] is smaller than
    # or equal to 'res'.
    for i in range(n):
        if arr[i] <= res:
            res = res + arr[i]
        else:
            break
    return res


if __name__ == '__main__':
    assert find_smallest([1, 3, 6, 10, 11, 15]) == 2
    assert find_smallest([1, 1, 1, 1]) == 5
    assert find_smallest([1, 1, 3, 4]) == 10
