from typing import List

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i, num in enumerate(nums): # iter over nums 
    #         try: 
    #             j = nums.index(target - num) # find diff of target and current num in arr 
            
    #             if j != -1 and i != j: # if in arr & not using duplicate to sum, return indices
    #                 return [i, j]
    #         except ValueError: # catch value errors
    #             pass


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # idea: use a hashtable to keep track of numbers looked at 
        # - if target - curr in hastable then we have a sum 
        # table is {item: idx of item in nums}
        
        table = {}
        
        for idx, num in enumerate(nums): 
            
            diff = target - num
            
            if diff in table: # O(1) table hasing access 
                return [table[diff], idx]
            else: 
                table[num] = idx 