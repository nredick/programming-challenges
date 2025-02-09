class Solution:
    # NOTE: DP approach - O(n) time and space (BEST)
    def fib(self, n: int) -> int:
        # nth fibonacci number 
        
        # idea: using dp, keep track of prev calc numbers to calc next fib number 
        
        f = [0, 1] # first two fibonacci numbers 
        
        for i in range(2, n+1): # loop including n 
            f.append(f[i-1] + f[i-2]) # calc ith fib number 
        
        return f[n] # ret nth fib number 
    
    # time complexity: O(n) -- loop to n 
    # space complexity: O(n) -- store n fib numbers 

#     # NOTE: RECURSIVE approach -- much slower, no extra space 
#     def fib(self, n: int) -> int:
        
#         if n == 0 or n == 1: 
#             return n 
#         else: 
#             return self.fib(n-1) + self.fib(n-2)