"""
Suppose you have an unsorted array of integers. Can you find the number of subarrays that have a sum exactly to the
given number p?
Input:
array = [10, 2, -2, -20, 10]
k = -10
Output : 3
#The following subarrays [10, 2, -2, -20], [2, -2, -20, 10], [-20, 10] have a sum exactly equal to -10

Input:
array = [9, 4, 20, 3, 10, 5]
k = 33
Output : 2
#The following subarrays [9, 4, 20], [20, 3, 10] have a sum exactly equal to 33
"""


def brute_force_solution(a: list[int], k: int) -> int:
    n = len(a)
    count = 0

    for start in range(0, n):
        for end in range(start + 1, n + 1):
            print(a[start:end])
            if sum(a[start:end]) == k:
                count += 1

    return count


def cumsum_solution(a: list[int], k: int) -> int:
    count = 0
    n = len(a)
    (sums := []).append(0)

    for i in range(1, n + 1):
        sums.append(sums[i - 1] + a[i - 1])

    for start in range(n):
        for end in range(start + 1, n + 1):
            if sums[end] - sums[start] == k:
                count += 1

    return count


def cumsum_nospace_solution(a: list[int], k: int) -> int:
    count = 0
    n = len(a)

    for start in range(0, n):
        _sum = 0
        for end in range(start, n):
            _sum += a[end]
            if _sum == k:
                count += 1

    return count


def hashmap_solution(a: list[int], k: int) -> int:
    count = sum = 0
    n = len(a)
    (map := dict())[0] = 1
    print(f"\narray: {a} k: {k}\n")
    for i in range(n):
        print(f"beginning of iteration {i}")
        print(f"values in hashmap {map}")
        print(f"Sum: {sum} and value is: {a[i]}")
        sum += a[i]
        print(f"Sum is now equal to {sum}")
        print(f"Sum - k is equal to {sum - k}")
        if sum - k in map:
            print(f"Sum - k is already in hashmap so we increment the count map[sum - k] times: {map[sum - k]}")
            count += map[sum - k]
        else:
            print(f"Sum - k: {sum - k} is not in hashmap we don't increment count in this iteration")
        print(f"Storing sum in hashmap")
        map[sum] = map.get(sum, 0) + 1
        print(f"Hashmap is now {map}")

    return count


if __name__ == '__main__':
    #assert hashmap_solution([10, 2, -2, -20, 10], -10) == 3
    #assert hashmap_solution([9, 4, 20, 3, 10, 5], 33) == 2
    #assert hashmap_solution([1, 1, 1], 2) == 2
    #assert hashmap_solution([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4
    assert brute_force_solution([1, 1, 3, 4], 6) == 1
