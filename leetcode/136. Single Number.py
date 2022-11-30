from typing import List

class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     # check for length condition 
    #     if len(nums) < 2: # O(1)
    #         return nums[0]
        
    #     # sort the arr 
    #     tmp = sorted(nums) # O(NlogN), omega(n) :(
        
    #     # edge cases: first & last 
    #     if tmp[0] != tmp[1]: # first is unique # O(1)
    #         return tmp[0]
        
    #     if tmp[-1] != tmp[-2]: # last is unique # O(1)
    #         return tmp[-1]
        
    #     # iter over sorted arr & check if before & after are the same 
    #     for i in range(1, len(nums)-1): # O(n)
    #         if not (tmp[i] == tmp[i-1] or tmp[i] == tmp[i+1]):
    #             return tmp[i]
        
    #     # overall worst case time complexity: 
    #     # O(n) + O(nlogn) = O(nlogn)
    #     # best case time complexity: 
    #     # O(1) -- first & last edge cases, length edge case 

    def singleNumber(self, nums: List[int]) -> int:
        # use XOR -- x + x = 0, only the single number will be leftover 
        ans = 0 
        for n in nums: 
            ans ^= n
        return ans 
    
    # time/space complexity: O(n), Omega(1)

# testing 
if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1,2,2,3,1]))