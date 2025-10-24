from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    example = [1]
    result = contains_duplicate(example)
    print(result)
