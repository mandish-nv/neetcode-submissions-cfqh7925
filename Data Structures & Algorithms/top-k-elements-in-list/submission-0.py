from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        main_dict = {}
        for n in nums:
            main_dict[n] = main_dict.get(n, 0) + 1

        items = list(main_dict.items())
        n = len(items)

        for i in range(n):
            for j in range(0, n-i-1):
                if (items[j][1] < items[j+1][1]):
                    items[j], items[j+1] = items[j+1], items[j]

        results = items[:k]

        result = []
        for r, s in results:
            result.append(r)

        return result
