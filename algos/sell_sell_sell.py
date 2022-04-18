"""
Suppose we are given an array of n integers which represent the value of some stock over time. Assuming you are allowed
to buy the stock exactly once and sell the stock once, what is the maximum profit you can make? Can you write an
algorithm that takes in an array of values and returns the maximum profit?

For example, if you are given the following array:

[2, 7, 1, 8, 2, 8, 14, 25, 14, 0, 4, 5]

The maximum profit you can make is 24 because you would buy the stock when its price is 1 and sell when it's 25. Note
that we cannot make 25, because the stock is priced at 0 after it is priced at 25 (e.g you can't sell before you buy).
"""
import sys


def bf_solution(a: list[int]) -> int:
    # O(n**2) solution
    max_profit = float("-inf")

    for i in range(len(a)):
        for e in a[i:]:
            profit = e - a[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit


def linear_solution(a: list[int]) -> int:
    # O(n) solution
    if a[0] > a[1]:
        buy = a[1]
        sell = a[0]
    else:
        buy = a[0]
        sell = a[1]

    possible_buys = []

    for e in a[2:]:
        if e < buy:
            possible_buys.append(e)
        elif e > sell:
            sell = e
        elif len(possible_buys):
            for j, pb in enumerate(possible_buys):
                if e - pb > sell - buy:
                    buy = pb
                    sell = e
                    possible_buys = possible_buys[j + 1:]

    return sell - buy


def find_buy_sell_stock_prices(array):
    if array is None or len(array) < 2:
        return None

    current_buy = array[0]
    global_sell = array[1]
    global_profit = global_sell - current_buy

    for i in range(1, len(array)):
        current_profit = array[i] - current_buy

        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = array[i]

        if current_buy > array[i]:
            current_buy = array[i]

    result = global_sell - global_profit, global_sell

    return result


if __name__ == '__main__':
    print(find_buy_sell_stock_prices([2, 7, 1, 8, 2, 8, 14, 25, 14, 0, 4, 5]))

