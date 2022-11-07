from typing import *
from collections import Counter


class Solution:
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # iterate over both arrays
    #     intersection = []
    #     for n in nums1: # iter nums1
    #         for j, m in enumerate(nums2): # iter nums2
    #             if n == m: # if values are the same
    #                 intersection.append(n) # add to intersection
    #                 nums2.pop(j) # remove from nums2 so it doesn't get counted again
    #                 break # break out of nums2 loop, new n

    #     return intersection

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use Counter lib to count the number of times a value appears in an array
        c1 = Counter(nums1) # count of all the values in nums1
        c2 = Counter(nums2) # count of all the values in nums2
        
        # use set operator & to get new set with elements common to both 
        # use Counter.elements() method to create list of each element w appropriate count 
        return list((c1 & c2).elements())


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2, 2, 1]))
