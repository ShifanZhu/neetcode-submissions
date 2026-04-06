class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        num = len(position)
        lst = [0] * num

        for i in range(num):
            lst[i] = (target - position[i]) / speed[i]

        result = len(set(lst))
        return result
