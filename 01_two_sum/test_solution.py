import pytest

from solution import (
    two_sum_bruteforce,
    two_sum_dictionary,
    two_sum_two_pointers
)

FUNCTIONS = [two_sum_bruteforce, two_sum_dictionary, two_sum_two_pointers]

# Параметры для тестов: (nums, target, expected)

# Базовые тесты
BASIC_CASES = [
    ([2, 7, 11, 15], 9, [0, 1], "базовый: простая сумма"),
    ([3, 2, 4], 6, [1, 2], "базовый: средние числа"),
    ([3, 3], 6, [0, 1], "базовый: дубликаты чисел"),
]

# Расширенные тесты
EXTENDED_CASES = [
    ([-1, -2, -3, -4, -5], -8, [2, 4], "расширенный: все отрицательные"),
    ([-3, 4, 3, 90], 0, [0, 2], "расширенный: смешанные знаки"),
    ([0, 4, 3, 0], 0, [0, 3], "расширенный: нули"),
    ([1, 2, 3, 4, 5, 6], 11, [4, 5], "расширенный: последовательные числа"),
    ([1, 2, 8, 4, 5], 12, [2, 3], "расширенный: сумма в середине"),
    ([1, 2, 3, 4, 5], 9, [3, 4], "расширенный: сумма в конце"),
    ([9000000, 2000000, 3000000, 4000000], 5000000, [1, 2], "расширенный: большие числа"),
]

# Граничные тесты
BOUNDARY_CASES = [
    ([1, 2], 3, [0, 1], "граничный: минимальная длина массива (2)"),
    (list(range(1, 10001)), 19999, [9998, 9999], "граничный: максимальная длина массива (10000)"),
    ([-10 ** 9, 0], -10 ** 9, [0, 1], "граничный: минимальное значение элемента (-10^9)"),
    ([10 ** 9, 0], 10 ** 9, [0, 1], "граничный: максимальное значение элемента (10^9)"),
    ([-5 * 10 ** 8, -5 * 10 ** 8], -10 ** 9, [0, 1], "граничный: минимальный target (-10^9)"),
    ([5 * 10 ** 8, 5 * 10 ** 8], 10 ** 9, [0, 1], "граничный: максимальный target (10^9)"),
]

NEGATIVE_CASES = [
    ([1, 2, 3, 4, 5], 100, "негативный: нет пары, сумма слишком велика"),
    ([10, 20, 30, 40], -50, "негативный: нет пары, сумма слишком мала")
]

POSITIVE_TEST_CASES = BASIC_CASES + EXTENDED_CASES + BOUNDARY_CASES

class TestTwoSum:
    @pytest.mark.parametrize("func", FUNCTIONS)
    @pytest.mark.parametrize("nums,target,expected,label", POSITIVE_TEST_CASES)
    def test_positive_cases(self, func, nums, target, expected, label):
        result = func(nums, target)

        """Проверка, что функция возвращает правильные индексы (в любом порядке)."""
        assert sorted(result) == sorted(expected), f"Ожидались индексы {expected}, получено {result}"

        """Проверка, что результат состоит из двух чисел."""
        assert isinstance(result, list), "Результат должен быть списком"
        assert len(result) == 2, f"Длина результата должна быть 2, получено {len(result)}"

        """Проверка, что индексы разные."""
        assert result[0] != result[1], "Индексы не должны совпадать"

        """Проверка, что сумма двух найденных чисел равна target."""
        assert nums[result[0]] + nums[result[1]] == target, \
            f"Сумма чисел не равна target: {result} != {target}"


    @pytest.mark.parametrize("func", FUNCTIONS)
    @pytest.mark.parametrize("nums,target,label", NEGATIVE_CASES)
    def test_no_solution(self, func, nums, target, label):
        """Проверка, что функция возвращает пустой список, если решения не существует. """
        result = func(nums, target)
        assert result == [], "Ожидался пустой список при негативном сценарии"
