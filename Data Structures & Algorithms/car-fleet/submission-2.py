class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [[p, s] for p, s in zip(position, speed)]
        position_speed.sort(reverse=True, key=lambda x: x[0])
        
        fleetSet = []
        for pos, spd in position_speed:
            time = (target-pos)/spd
            
            if not fleetSet or fleetSet[-1] < time:
                fleetSet.append(time)

        return len(set(fleetSet))
