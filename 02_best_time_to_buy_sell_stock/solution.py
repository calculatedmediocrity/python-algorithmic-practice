from typing import List

def best_time_to_buy_sell_bruteforce(prices: List[int]) -> int:
    """
    Решение методом полного перебора
    Время: O(n²), Память: O(1)
    """
    max_profit = 0
    for buy_day in range(len(prices)):
        for sell_day in range(buy_day + 1,len(prices)):
            current_profit = prices[sell_day] - prices[buy_day]
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit

def best_time_to_buy_sell_optimal(prices: List[int]) -> int:
    """
    Решение с проходом одного цикла(отслеживание минимума)
    Время: O(n), Память: O(1)
    """
    min_price = 10**5
    max_profit = 0
    for day in range(len(prices)):
        current_price = prices[day]
        # Обновляем минимальную цену, если нашли меньшую
        if current_price < min_price:
            min_price = current_price
        # Вычисляем потенциальную прибыль
        current_profit = current_price - min_price
        # Обновляем максимум, если текущая прибыль больше
        if current_profit > max_profit:
            max_profit = current_profit
    return max_profit

if __name__ == "__main__":
    example = [2, 3, 4, 1, 5]
    result_bruteforce = best_time_to_buy_sell_bruteforce(example)
    print( example, "→", result_bruteforce)
    result_optimal = best_time_to_buy_sell_optimal(example)
    print(example, "→", result_optimal)
