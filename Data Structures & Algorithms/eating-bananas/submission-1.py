from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Solution 1: double for loops exceeds time limit
        # max_time = max(piles)
        # speed = 0
        # for s in range(1, max_time+1):
        #     accumulated_time = 0
        #     for p in piles:
        #         accumulated_time += ceil(p / s)
        #     if accumulated_time <= h:
        #         return s

        # Solution 2
        min_speed = 1
        max_speed = max(piles)
        mid_speed = 0

        while min_speed < max_speed:
            mid_speed = (min_speed + max_speed) // 2

            accumulated_time = 0
            for p in piles:
                accumulated_time += ceil(p / mid_speed)
            if accumulated_time <= h:
                max_speed = mid_speed
            else:
                min_speed = mid_speed + 1

        return min_speed