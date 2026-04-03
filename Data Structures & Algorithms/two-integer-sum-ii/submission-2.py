class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in numbers:
            diff = target - n
            if diff in numbers:
                if diff > n:
                    return [numbers.index(n) + 1, numbers.index(diff) + 1]
                