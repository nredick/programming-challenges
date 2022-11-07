from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ## 90 deg rotation = transpose then horizontal flip 
        
        # transpose the matrix 
        for i in range(len(matrix)): # iter over rows 
            for j in range(i+1, len(matrix)): # start from i+1 so you don't end up with original 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # flip row/col values 
                
        # flip matrix horizontally by reversing each of the rows 
        for row in matrix: 
            for i, n in enumerate(row[::-1]):
                row[i] = n


if __name__ == "__main__":
    # test cases 
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix)
    print(matrix)

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Solution().rotate(matrix)
    print(matrix)

    matrix = [[1]]
    Solution().rotate(matrix)
    print(matrix)

    matrix = [[1,2],[3,4]]
    Solution().rotate(matrix)
    print(matrix)
