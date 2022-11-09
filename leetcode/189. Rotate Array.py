from typing import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotations will repeat after len(nums), use mod to get min rotations
        rot = k % len(nums)
        if rot > 0: # if 0, don't need to rotate the array 
            nums[:] = nums[-rot:] + nums[:-rot] # rotate the array

# Runtime: 523 ms, faster than 56.12% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.4 MB, less than 76.64% of Python3 online submissions for Rotate Array.