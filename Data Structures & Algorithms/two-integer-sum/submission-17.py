class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in previous:
                return [previous[diff], idx]
            
            previous[n] = idx
