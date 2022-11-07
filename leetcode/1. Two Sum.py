from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums): # iter over nums 
            try: 
                j = nums.index(target - num) # find diff of target and current num in arr 
            
                if j != -1 and i != j: # if in arr & not using duplicate to sum, return indices
                    return [i, j]
            except ValueError: # catch value errors
                pass