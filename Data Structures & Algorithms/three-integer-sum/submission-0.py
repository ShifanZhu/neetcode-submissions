class Solution:
    def twoSum(self, nums: List[int], target):
        left = 0
        right = len(nums) - 1
        nums = sorted(nums)
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [nums[left], nums[right]]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        print("nums: ", nums)

        nums = sorted(nums)
        print("sorted nums: ", nums)
        for i, num in enumerate(nums):
            target = -num
            two_sum_return = self.twoSum(nums, target)

            if len(two_sum_return) == 2:
                result = [two_sum_return[0], two_sum_return[1], num]
                results.append(result)

        return results