from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, n in reversed(list(enumerate(digits))):
            print(i, digits[i])
            if n < 9:  # then we can add 1
                digits[i] += 1
                return digits
            # make it 0 and loop will go on to add 1 to the next digit
            digits[i] = 0

        # not returned by now => new digit needs to be added to the front
        return 
    


if __name__ == "__main__":
    s = Solution()
    # print(s.plusOne([1,2,3]))
    # print(s.plusOne([4,3,2,1]))
    print(s.plusOne([9, 9, 9]))
