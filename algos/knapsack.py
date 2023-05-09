"""
What is the 0/1 Knapsack Problem?
We are given N items where each item has some weight and profit associated with it. We are also given a bag with
capacity W, [i.e., the bag can hold at most W weight in it]. The target is to put the items into the bag such that the
sum of profits associated with them is the maximum possible.

Note: The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not
possible to put a part of an item into the bag].

Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
Output: 3
Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the
possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit
is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.

Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
Output: 0
"""


def merge_sort(a: list):
    def merge(la, ra):
        result = []
        i = 0
        j = 0

        while i < len(la) and j < len(ra):
            if la[i] <= ra[j]:
                result.append(la[i])
                i += 1
            else:
                result.append(ra[j])
                j += 1

        result += la[i:]
        result += ra[j:]

        return result

    if len(a) <= 1:
        return a

    mid = len(a) // 2
    l_half = a[:mid]
    r_half = a[mid:]

    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)

    return merge(l_half, r_half)


def quicksort(a: list):
    if len(a) <= 1:
        return a

    pivot = a[0]
    l = [x for x in a if x < pivot]
    m = [x for x in a if x == pivot]
    r = [x for x in a if x > pivot]

    return quicksort(l) + m + quicksort(r)


def solution(N: int, W: int, profit: list, weight: list) -> float:

    k = [[w for w in range(W + 1)] for i in range(N + 1)]

    for i in range(N + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif weight[i - 1] <= w:
                k[i][w] = max(profit[i - 1] + k[i - 1][w - weight[i - 1]], k[i - 1][w])
            else:
                k[i][w] = k[i - 1][w]

    return k[N][W]


if __name__ == '__main__':
    print(solution(N=3, W=50, profit=[60, 100, 120], weight=[10, 20, 30]))
    print(solution(N=3, W=3, profit=[1, 2, 3], weight=[4, 5, 6]))
    print(solution(N=3, W=4, profit=[1, 2, 3], weight=[4, 5, 1]))




