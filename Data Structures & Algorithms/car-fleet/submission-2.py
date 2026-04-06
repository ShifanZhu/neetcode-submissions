class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # num = len(position)
        # lst = [0] * num

        # for i in range(num):
        #     lst[i] = (target - position[i]) / speed[i]


        # result = len(set(lst))
        # return result

        car = []

        for p, s in zip(position, speed):
            car.append((p, (target-p)/s))

        print("car: ", car)
        car.sort(reverse=True)
        print("car: ", car)
        fleet = 0
        prev_t = 0
        for p, t in car:
            if t > prev_t:
                fleet += 1
                prev_t = t
        return fleet