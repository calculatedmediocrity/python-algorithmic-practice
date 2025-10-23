from typing import List

def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    """
    Решение методом полного перебора
    Время: O(n²), Память: O(1)
    """
    for index1, num in enumerate(nums):
        for index2 in range(index1 + 1,len(nums)):
            if nums[index2] == target - num:
                return [index1, index2]
    # Если пара не найдена, возвращаем пустой список
    return []


def two_sum_dictionary(nums: List[int], target: int) -> List[int]:
    """
    Решение с использованием словаря
    Время: O(n), Память: O(n)
    """
    seen = {}
    for index, num in enumerate(nums):
        desire = target - num
        if desire in seen:
            return [seen[desire], index]
        seen[num] = index
    # Если пара не найдена, возвращаем пустой список
    return []

def two_sum_two_pointers(nums: List[int], target: int) -> List[int]:
    """
    Решение с двумя указателями (требует сортировки)
    Время: O(n log n), Память: O(n)
    """
    # Создаем список кортежей (значение, исходный индекс)
    indexed_nums = list(enumerate(nums))
    # Сортируем по значениям
    indexed_nums.sort(key=lambda x: x[1])
    # Метод двух указателей
    l_pointer, r_pointer = 0, len(nums)- 1
    while l_pointer < r_pointer:
        current_sum = indexed_nums[l_pointer][1] + indexed_nums[r_pointer][1]
        if current_sum > target:
            r_pointer -= 1
        elif current_sum < target:
            l_pointer += 1
        else:
            return [indexed_nums[l_pointer][0], indexed_nums[r_pointer][0]]
    # Если пара не найдена, возвращаем пустой список
    return []


if __name__ == "__main__":
    example = [0, 3, 8, -5, -7, 11, 1]
    result_bruteforce = two_sum_bruteforce(example, 19)
    result_dictionary = two_sum_dictionary(example, 19)
    result_two_pointers = two_sum_two_pointers(example, 19)
    print("Bruteforce: ", example, "→", result_bruteforce)
    print("Dictionary: ", example, "→", result_dictionary)
    print("Two Pointers: ", example, "→", result_two_pointers)
