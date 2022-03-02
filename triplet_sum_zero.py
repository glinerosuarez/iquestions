"""
Given an array of n distinct elements, can you find all the triplet combinations that sum to zero?
For example:

Input: [0, -1, 2, -3, 1]
Output:
0 -1 1
2 -3 1

Input: [1, -2, 1, 0, 5]
Output: 1 -2  1
"""
from collections import defaultdict


def solution(a):
    result = []
    numbers = defaultdict(int)
    for e in a:
        numbers[e] += 1

    while len(a) > 0:
        i = a.pop()
        for j in a:
            missing = -(i + j)
            numbers[i] -= 1
            numbers[j] -= 1
            if numbers[missing] > 0:
                numbers[missing] -= 1
                result.append([i, j, missing])
            else:
                numbers[i] += 1
                numbers[j] += 1
    return result


if __name__ == '__main__':
    #assert solution([0, -1, 2, -3, 1]) == [[1, 0, -1], [1, 2, -3]]
    #assert solution([1, -2, 1, 0, 5]) == [[1, 1, -2]]
