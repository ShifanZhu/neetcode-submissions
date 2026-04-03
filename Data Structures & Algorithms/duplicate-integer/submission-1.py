class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Solution 1:

        # val_dict = dict()
        # for num in nums:
        #     if num in val_dict:
        #         return True
        #     else:
        #         val_dict[num] = 0
        # return False

        # Solution 2:

        return len(nums) != len(set(nums))