class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        mid = size // 2

        left = 0
        right = size - 1
        

        while left <= right:
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1

            mid = (left + right) // 2

        return -1