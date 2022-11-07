from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create lists of sets representing each row, col, and square 
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        
        for r in range(9): # iter over the row indices 
            for c in range(9): # iter over the col indices
                val = board[r][c] # value at that board tile 
                
                # ignore empty tiles, make sure val is not already in row, col, or square 
                if val != "." and (val in rows[r] or val in cols[c] or val in squares[r//3][c//3]):
                    return False
                
                # add new distinct value to appropriate row/col/square 
                rows[r].add(val)
                cols[c].add(val)
                squares[r//3][c//3].add(val)
        
        return True