import pytest
from solution import contains_duplicate

FUNCTIONS = [contains_duplicate]

# Параметры для тестов: (nums, expected, label)

# Базовые тесты из примеров LeetCode
BASIC_CASES = [
    ([1, 2, 3, 1], True, "базовый: пример 1 из LeetCode, есть дубликат"),
    ([1, 2, 3, 4], False, "базовый: пример 2 из LeetCode, все уникальные"),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True, "базовый: пример 3 из LeetCode, множественные дубликаты"),
]

# Расширенные тесты
EXTENDED_CASES = [
    ([1, 2, 3, 4, 2], True, "расширенный: дубликат в середине"),
    ([5, 5, 5, 5, 5], True, "расширенный: все элементы одинаковые"),
    ([-1, -2, -3, -1], True, "расширенный: отрицательные дубликаты"),
    ([0, 0, 1, 2], True, "расширенный: нули и другие числа"),
    ([10000, 200000, 30000, 400000], False, "расширенный: все уникальные, большие числа"),
]

# Граничные тесты
BOUNDARY_CASES = [
    ([1], False, "граничный: минимальная длина массива (1)"),
    ([0, 10**4], False, "граничный: длина 2, уникальные элементы"),
    ([10**9, -10**9, 0, 10**9], True, "граничный: включает мин/макс значения"),
    (list(range(10**5)), False, "граничный: массив максимальной длины, все уникальные"),
    ([1]*10**5, True, "граничный: массив максимальной длины, все одинаковые"),
]

POSITIVE_TEST_CASES = BASIC_CASES + EXTENDED_CASES + BOUNDARY_CASES

class TestContainsDuplicate:
    @pytest.mark.parametrize("func", FUNCTIONS)
    @pytest.mark.parametrize("nums,expected,label", POSITIVE_TEST_CASES)
    def test_positive_cases(self, func, nums, expected, label):
        result = func(nums)
        assert isinstance(result, bool), f"Результат должен быть bool, получено {type(result)}"
        assert result == expected, f"Ожидался результат {expected}, получено {result} - {label}"
