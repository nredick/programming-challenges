from typing import *
from collections import Counter


class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     counts = Counter(nums)  # count the occurences of values in nums
    #     try:
    #         zeroes = counts[0]  # get the number of zeroes
    #     except:
    #         return nums  # no zeroes, return as-is

    #     for _ in range(zeroes):
    #         nums.remove(0)  # remove first 0 in list
    #         nums.append(0)  # add a zero to the end

    def moveZeroes(self, nums: List[int]) -> None:
        swap = 0
        for i in range(len(nums)):  # iter over nums
            if nums[i] != 0:  # if the curr value is not 0
                nums[i], nums[swap] = nums[swap], nums[i]  # swap with swap
                swap += 1  # increment swap
            


if __name__ == "__main__":
    s = Solution()
    n = [0, 1, 0, 3, 12]
    s.moveZeroes(n)
    print(n)
