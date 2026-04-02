class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = []
        mult = 1
        for idx_n, n in enumerate(nums):
            for idx_m, m in enumerate(nums):
                if (idx_n == idx_m):
                    continue
                mult = mult * m
            result.append(mult)
            mult = 1

        return result