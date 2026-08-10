class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p) / s for p, s in sorted(zip(position, speed))]
        curr_slowest, fleet = 0, 0

        for t in time[::-1]:
            if curr_slowest < t:
                fleet += 1
                curr_slowest = t
        
        return fleet