class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val_dict = dict()
        for num in nums:
            if num in val_dict:
                return True
            else:
                val_dict[num] = 0

        return False