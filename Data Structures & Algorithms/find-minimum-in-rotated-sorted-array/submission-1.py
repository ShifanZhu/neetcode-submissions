class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min_num = 1000
        # for num in nums:
        #     if num < min_num:
        #         min_num = num
        # return min_num

        left = 0
        right = len(nums) - 1
        mid = 0

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]