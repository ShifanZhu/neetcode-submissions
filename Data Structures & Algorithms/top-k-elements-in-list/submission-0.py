from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_cnter = Counter(nums)
        print("nums_cnter: ", nums_cnter)

        nums_cnter_sorted = sorted(nums_cnter.items(), key=lambda x: -x[1])

        print("nums_cnter sorted: ", nums_cnter)
        return [nums for nums, freq in nums_cnter_sorted[:k]]