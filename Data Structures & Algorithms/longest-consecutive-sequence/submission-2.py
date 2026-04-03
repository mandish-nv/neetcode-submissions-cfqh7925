class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        temp = nums[:]
        sort = []
        for _ in nums:
            sort.append(min(temp))
            temp.remove(min(temp))

        temp = 1
        longest = 1 
        print(sort)
        for idx_s, s in enumerate(sort):
            if idx_s == 0:
                continue
            if sort[idx_s] == sort[idx_s - 1]:
                continue
            if sort[idx_s] == sort[idx_s - 1] + 1:
                temp = temp + 1
            else:
                if temp > longest:
                    longest = temp
                temp = 1
                
        if temp > longest:
            longest = temp

        return longest

                

            