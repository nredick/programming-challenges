from typing import List
import string 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s.lower(): 
            # if it's a letter or digit
            if c in string.ascii_lowercase or c in string.digits: 
                chars.append(c)
        return "".join(chars[::-1]) == "".join(chars)


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("0P"))