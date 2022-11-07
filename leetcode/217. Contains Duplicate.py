from typing import * 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort the array => repeated values will be next to each other 
        tmp = sorted(nums)
        for i in range(1, len(nums)): # check if adjacent values are the same 
            if tmp[i-1] == tmp[i]:
                return True # if the same, return true 
        return False 
        
# testing 
if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))