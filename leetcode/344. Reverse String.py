from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        f = 0 # forward pointer 
        r = len(s)-1 # reverse pointer 
        while f < r: 
                s[f], s[r] = s[r], s[f] # switch 
                # inc/dec pointers 
                f += 1
                r -= 1


if __name__ == "__main__":
    s = Solution()
    string = ["h","e","l","l","o"]
    s.reverseString(string)
    print(string)