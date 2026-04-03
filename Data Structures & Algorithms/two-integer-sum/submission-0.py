class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return sorted([i, lookup[complement]])
            lookup[num] = i
        print("num_dict", nums_dict)