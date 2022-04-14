"""
Suppose you are given a list of Q 1D points. Write code to return the value in Q that is the closest to value j. If two
values are equally close to j, return the smaller value.
Example:
Q = [1, -1, -5, 2, 4, -2, 1]
j = 3
#Output: 2
"""
from typing import List


def solution(a: List[int], j: int) -> int:
    _id = None
    distance = float("inf")

    for i, e in enumerate(a):

        d = abs(e - j)
        if d < distance:
            _id = i
            distance = d
        elif d == distance:
            if a[_id] > e:
                _id = i

    return a[_id]


if __name__ == '__main__':
    print(solution([1, -1, -5, 2, 4, -2, 1], 3))


