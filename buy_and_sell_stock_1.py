# Best Time to Buy and Sell Stock given that you can only buy and sell once
from typing import List


def buy_and_sell_1(prices: List[int]) -> int:
    profit = 0
    curr_min = prices[0]
    for num in prices:
        if num < curr_min:
            curr_min = num
        if num - curr_min > profit:
            profit = num - curr_min

    return profit


if __name__ == "__main__":
    test_array = [7, 1, 5, 3, 6, 4]

    print(buy_and_sell_1(test_array))
