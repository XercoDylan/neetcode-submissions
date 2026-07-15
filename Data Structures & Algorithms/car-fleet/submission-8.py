class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        car_durations = []
        car_positions = sorted([i for i in range(len(position))], reverse=True,key = lambda i: position[i])

        for car in car_positions:
            duration = (target - position[car])/speed[car]
            if len(car_durations) == 0:
                car_durations.append(duration)
            else:
                if duration > car_durations[-1]:
                    car_durations.append(duration)
                else:
                    car_durations.append(car_durations[-1])

        for i in range(len(car_positions) - 1, 0, -1):
            current_car = car_positions[i]
            duration = (target - position[current_car])/speed[current_car]
            slowest_duration = car_durations[i - 1]

            if duration > slowest_duration:
                fleets += 1




        return fleets

