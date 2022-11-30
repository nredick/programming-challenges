from typing import List
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        # case - dont need to refuel 
        if target <= startFuel: 
            return 0 # can reach target without refueling 
        
        # idea: 
        # - only get gas if you need it 
        # - keep track of stations passed w heapq, store -gas => pop returns station w most gas
        # - if you run out between stations, you should've stopped at the largest you passed
        
        stations.append([target, 0])
        passed_stations = []
        
        # current position and fuel in tank
        position, fuel = 0, startFuel
        
        stops = 0
        
        for station, gas in stations: # iter over stations, including target 
            
            # calc distance to next station & set current position to the next station
            dist, position = station - position, station
            
            if dist > fuel: # we will run out of gas 
                
                # use gas we passed by 
                while passed_stations and dist > fuel: 
                    fuel += -heapq.heappop(passed_stations) # get passed gas station that had most gas 
                    stops += 1
                
                if dist > fuel: # used gas from all passed stations but still dont have enough 
                    return -1 # not possible to reach destination 
            
            fuel -= dist 
            heapq.heappush(passed_stations, -gas)
            
        return stops

# NOTE: heapq is a binary heap, with O(log n) push and O(log n) pop

## Complexity Analysis

### time complexity: O(n log n)

# best case: O(1) if target <= startFuel
# worst case: O(n*logn) if we have to use all stations passed
# ^ n for looping over stations, logn for pushing/popping from heap

### space complexity: O(n) for extra heap space 