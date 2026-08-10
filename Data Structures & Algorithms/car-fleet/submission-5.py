class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - p) / s for p, s in sorted(zip(position, speed))]
        fleet, curr_slowest = 0, 0
        
        for time in times[::-1]:
            if curr_slowest < time:
                fleet += 1
                curr_slowest = time

        return fleet