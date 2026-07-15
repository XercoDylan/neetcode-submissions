class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_positions = sorted([i for i in range(len(position))], reverse=True,key = lambda i: position[i])
        fleets = []

        for car in car_positions:
            duration = (target - position[car])/speed[car]

            if len(fleets) == 0 or duration > fleets[-1]:
                fleets.append(duration)



        return len(fleets)