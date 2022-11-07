from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums) # need to keep track of size 
        insert = 1
        for i in range(1, size):
            if nums[i] != nums[i-1]: # if unique element
                nums[insert] = nums[i]
                insert += 1
        return insert