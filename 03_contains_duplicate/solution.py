from typing import List

def contains_duplicate_set(nums: List[int]) -> bool:
    """
    Решение с использованием множества
    Время: O(n) Память: O(n)
    """
    return len(nums) != len(set(nums))

def contains_duplicate_sort(nums: List[int]) -> bool:
    """
    Решение через сортировку
    Время: O(n log n) Память: O(1)
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

if __name__ == '__main__':
    example = [1, 2, 3, 4]
    result_set = contains_duplicate_set(example)
    print(result_set)
    result_sort = contains_duplicate_sort(example)
    print(result_sort)
