from typing import List

def best_time_to_buy_sell_bruteforce(prices: List[int]) -> int:
    max_profit = 0
    for buy_day in range(len(prices)):
        for sell_day in range(buy_day + 1,len(prices)):
            current_profit = prices[sell_day] - prices[buy_day]
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit



if __name__ == "__main__":
    example = [2, 3, 4, 1, 5]
    result_bruteforce = best_time_to_buy_sell_bruteforce(example)
    print( example, "→", result_bruteforce)
