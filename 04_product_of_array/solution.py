from typing import List
import math

def product_of_array_naive(nums: List[int]) -> List[int]:
    result = []
    for except_element_idx in range(len(nums)):
        product = 1
        for multiplier_idx in range(len(nums)):
            if except_element_idx != multiplier_idx:
                product *= nums[multiplier_idx]
        result.append(product)
    return result

def product_of_array_parts(nums: List[int]) -> List[int]:
    pass
    # result = []
    # nums_length = len(nums)
    # left_products = [1] * nums_length
    # right_products = [1] * nums_length
    # for i in range(nums_length):
    #     left_nums = nums[:i]
    #     left_products[i] *= left_nums
    # for i in range(nums_length):
    #     right_nums = nums[i:]
    #     right_products[i] *= right_nums
    # for i in range(nums_length):
    #     result.append(left_products[i] * right_products[i])
    # return result

if __name__ == '__main__':
    example = [1, 2, 3, 4]
    result_naive = product_of_array_naive(example)
    print(result_naive)
    result_parts = product_of_array_parts(example)
    print(result_parts)
