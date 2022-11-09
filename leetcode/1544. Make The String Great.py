class Solution:
    # recursive solution -- best for space complexity, bad time complexity 
    # def makeGood(self, s: str) -> str: # worst case: O(n^2) time, O(1) space
    #     for i in range(len(s)-1):
    #         if abs(ord(s[i]) - ord(s[i+1])) == 32:
    #             if len(s) == 2:
    #                 return ""
    #             return self.makeGood(s[:i] + s[i+2:])
    #     return s

    # iterative solution -- best for time complexity, worse space complexity
    # data structure: stack
    def makeGood(self, s: str) -> str: # worst case: O(n) time, O(n) space
        ans = [] # empty stack to store the characters
        for c in s: # iterate over the string
            # check that the stack is not empty and that the top of the stack is the same character but different case using ASCII values
            if len(ans) != 0 and abs(ord(c) - ord(ans[-1])) == 32:
                ans.pop() # if same char but diff case, pop it from top of stack
            else:
                ans.append(c) # otherwise, append the character to the stack
        return "".join(ans)


# RESULTS: 
# ITERATIVE:	37 ms	14 MB	python3
# RECURSIVE:	80 ms	13.9 MB	python3


if __name__ == "__main__":
    s = Solution()
    print(s.makeGood("abBAcC"))
    print(s.makeGood("leEeetcode"))
