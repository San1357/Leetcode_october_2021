# Using Linear Search
# Problem : Search a 2D Matrix II
# Problem no : 240


# time  complexity :  O(N^2)


#CODE:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0, len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == target :
                    return True
        return False
        
