"""
Hi,
Given an array of integers, can you write a function that returns "True" if there is a triplet (a, b, c) within the
array that satisfies a^2 + b^2 = c^2?

For example:

Input: arr[] = [3, 1, 4, 6, 5]
Output: True

#There is a Pythagorean triplet (3, 4, 5) that exists in the input array.
Input: arr[] = {10, 4, 6, 12, 5}
Output: False

#There is no Pythagorean triplet that exists in the input array.
"""
import math
from typing import Iterable, List


def naive_approach(l: Iterable[int]) -> bool:
    # O(n**3) solution
    for a in l:
        for b in l:
            for c in l:
                if all([c != b, c != a, a != b, a**2 + b**2 == c**2]):
                    return True
    else:
        return False


def is_triplet(ar):
    n = len(ar)
    # Square all the elements
    for i in range(n):
        ar[i] = ar[i] * ar[i]

    # sort array elements
    ar.sort()

    # fix one element
    # and find other two
    # i goes from n - 1 to 2
    for i in range(n-1, 1, -1):
        # start two index variables from
        # two corners of the array and
        # move them toward each other
        j = 0
        k = i - 1
        while j < k:
            # A triplet found
            if ar[j] + ar[k] == ar[i]:
                return True
            else:
                if ar[j] + ar[k] < ar[i]:
                    j = j + 1
                else:
                    k = k - 1
    # If we reach here, then no triplet found
    return False


def sol(l: List[int]) -> bool:
    # O(n)

    i = iter(l)
    a = next(i)
    possible_cs = {}

    for b in i:
        if b in possible_cs: return True
        possible_cs[int(math.sqrt(a**2 + b**2))] = True
    else:
        return False


if __name__ == '__main__':
    solution = is_triplet

    # Test
    assert True is solution([3, 1, 4, 6, 5])
    assert True is solution([3, 2, 4, 6, 5])
    assert True is solution([5, 4, 2, 6, 3])
    assert False is solution([10, 4, 6, 12, 5])
