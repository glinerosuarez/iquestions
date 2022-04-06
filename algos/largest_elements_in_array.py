"""
Given an array with k distinct elements, write a function to return all elements that have at least two elements greater
than themselves in the same array:
For example:

#Given the following:
array = [2,3,9,7,6]
#Your function should return:
[2,3,6]
"""
from typing import List


def brute_force_solution(a: List[int]) -> List[int]:
    res = list()
    n = len(a)

    for i in range(n):
        count = 0
        for j in range(n):
            if a[i] < a[j]:
                count += 1
                if count == 2:
                    res.append(a[i])
                    break

    return res


def two_max_solution(a: List[int]) -> List[int]:
    res = list()
    n = len(a)

    max_val = second_max_val = float("-inf")

    for i in range(n):
        if a[i] > max_val:
            second_max_val = max_val
            max_val = a[i]
        elif second_max_val < a[i] < max_val:
            second_max_val = a[i]

    for e in a:
        if e < second_max_val:
            res.append(e)

    return res


if __name__ == '__main__':
    assert two_max_solution([2, 3, 9, 7, 6]) == [2, 3, 6]
