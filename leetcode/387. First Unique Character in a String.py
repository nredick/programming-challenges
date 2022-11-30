from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # get counts of values 
        counts = Counter(s)
        
        # iter over the string in order 
        for i, c in enumerate(s): 
            if counts[c] == 1: # if the char has a count of one it is the first unique 
                return i # return it's index 
            
        return -1 # none found