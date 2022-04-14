"""
Write a function that outputs the smallest missing number in a sorted array of n unique integers. The integers in the
array range from 0 to m-1, where m > n. The function should be called 0SmallestMissingNumber and the 3 inputs are:

the array
the "start value" of the array
the length of the array - 1
For example:

 #Input:
 [0, 1, 3, 4, 8, 9], n = 6, m = 10
 #Output:
 2

 #Input:
 [4, 7, 9, 11], n = 4, m = 12
 #Output:
 0
"""
from typing import List


def solution(a: List[int], n: int, m: int) -> int:
    missing = 0 # first value
    for e in a:
        if e == missing:
            missing += 1
        else:
            return missing


def bs_solution(a: List[int], start: int, end: int) -> int:
    if start > end: return end + 1
    if start != a[start]: return start

    mid = int((start + end) / 2)

    # Left half has all elements
    # from 0 to mid
    if a[mid] == mid: return bs_solution(a, mid+1, end)

    return bs_solution(a, start, mid)


if __name__ == '__main__':
    assert bs_solution([0, 1, 3, 4, 8, 9], 0, 10) == 2
    assert bs_solution([4, 7, 9, 11], 0, 12) == 0
