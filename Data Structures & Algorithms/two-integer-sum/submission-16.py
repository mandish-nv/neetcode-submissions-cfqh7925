class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, n in enumerate(nums):
            res = target - n
            if res in seen:
                return [seen[res], idx]
            seen[n] = idx
        return []