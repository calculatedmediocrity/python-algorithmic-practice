import pytest
from typing import List
from solution import product_of_array_naive,product_of_array_parts

# Функции для тестирования
FUNCTIONS = [product_of_array_parts]

# Параметры для тестов: (nums, expected, label)

# Базовые тесты из примеров LeetCode
BASIC_CASES = [
    ([1, 2, 3, 4], [24, 12, 8, 6], "базовый: пример 1 из LeetCode"),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0], "базовый: пример 2 из LeetCode с нулями"),
]

# Расширенные тесты
EXTENDED_CASES = [
    ([2, 3, 5, 7], [105, 70, 42, 30], "расширенный: простые числа"),
    ([1, 1, 1, 1], [1, 1, 1, 1], "расширенный: все единицы"),
    ([0, 1, 2, 3], [6, 0, 0, 0], "расширенный: с нулем в начале"),
    ([1, 2, 0, 4], [0, 0, 8, 0], "расширенный: с нулем в середине"),
    ([1, 2, 3, 0], [0, 0, 0, 6], "расширенный: с нулем в конце"),
    ([-2, -3, 4, 5], [-60, -40, 30, 24], "расширенный: отрицательные числа"),
    ([10, 10, 10], [100, 100, 100], "расширенный: одинаковые числа"),
]

# Граничные тесты согласно требованиям LeetCode
BOUNDARY_CASES = [
    # Длина массива
    ([2, 3], [3, 2], "граничный: минимальная длина массива (2)"),
    ([-30, 30], [30, -30], "граничный: минимальная длина с граничными значениями"),
    # Этот тест не завершится при наивном решении — mark.slow для исключения
    pytest.param(
        [1] * 10 ** 5,
        [1] * 10 ** 5,
        "граничный: максимальная длина массива (10**5)",
        marks=pytest.mark.slow
    ),

    # Значения по диапазону
    ([-30, -29, -30], [870, 900, 870], "граничный: минимальные значения (-30)"),
    ([30, 30], [30, 30], "граничный: максимальные значения (30)"),
    ([-30, 30, 0], [0, 0, -900], "граничный: мин/макс значения с нулем"),

]

POSITIVE_TEST_CASES = BASIC_CASES + EXTENDED_CASES + BOUNDARY_CASES


class TestProductExceptSelf:
    @pytest.mark.parametrize("func", FUNCTIONS)
    @pytest.mark.parametrize("nums,expected,label", POSITIVE_TEST_CASES)
    def test_positive_cases(self, func, nums, expected, label):
        result = func(nums)

        """Проверка, что функция возвращает список правильной длины."""
        assert isinstance(result, list), "Результат должен быть списком"
        assert len(result) == len(expected), f"Длина результата должна быть {len(expected)}, получено {len(result)}"

        """Проверка, что результат совпадает с ожидаемым."""
        assert result == expected, f"Ожидался результат {expected}, получено {result} - {label}"
