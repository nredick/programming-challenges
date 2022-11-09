# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass # dummy function

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # its the bad version if version i is bad and v i-1 is not
        # binary search 
        
        start, end = 1, n
        
        while start <= end:
            mid = int(start + (end-start) / 2)
            if isBadVersion(mid):
                end = mid - 1
            else: 
                start = mid + 1
        
        return start