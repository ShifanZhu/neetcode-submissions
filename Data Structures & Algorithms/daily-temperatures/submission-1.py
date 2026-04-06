class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i, t in enumerate(temperatures):
            sub_temp = temperatures[i:]
            larger_mask = [1 if st > t else 0 for st in sub_temp]
            # print("sub_temp", sub_temp)
            # print("larger_mask", larger_mask)
            first_larger_idx = larger_mask.index(1) if 1 in larger_mask else 0
            result.append(first_larger_idx)

        return result