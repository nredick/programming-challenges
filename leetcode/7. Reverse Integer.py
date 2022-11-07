from typing import *


class Solution:
    # def reverse(self, x: int) -> int:
    #     s = str(abs(x))[::-1] # convert int to positive, then to string, then reverse the string

    #     if not int(s) <= 2**31-1: # check that reversed value is within constraints
    #         return 0

    #     # check if negative
    #     if x < 0:
    #         return -1*int(s)

    #     return int(s)

    def reverse(self, x: int) -> int: # O(n) time, O(1) space
        pos = abs(x)  # get absolute value of x

        rev = 0  # reversed value
        while pos: 
            n = pos % 10
            rev = rev * 10 + n
            pos = pos // 10

        if rev >= 2**31-1:  # check that reversed value is within constraints
            return 0

        if x < 0:  # check if negative
            return -1*rev

        return rev



if __name__ == "__main__":
    s = Solution()
    # print(s.reverse(123))
    print(s.reverse(-123))
    # print(s.reverse(120))
    # print(s.reverse(0))
    # print(s.reverse(1534236469))
