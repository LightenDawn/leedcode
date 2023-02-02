# A square matrix is said to be an X-Matrix if both of the following conditions hold:
# 1.	All the elements in the diagonals of the matrix are non-zero.
# 2.	All other elements are 0.
# Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.
 
# Example 1:
 
# Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
# Output: true
# Explanation: Refer to the diagram above. 
# An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
# Thus, grid is an X-Matrix.

# Example 2:
 
# Input: grid = [[5,7,0],[0,3,1],[0,5,0]]
# Output: false
# Explanation: Refer to the diagram above.
# An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
# Thus, grid is not an X-Matrix.


# Failure: 

# 解題邏輯: 
# 此題邏輯為
# 1.	對角線不為0
# 2.	其餘值大於0

class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        last = len(grid) - 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == j:
                    if grid[i][j] == 0:
                        return False
                if (j + i) == last:
                    if grid[i][j] == 0:
                        return False
                if i == 0 or i == len(grid) - 1:
                    if j == 0 or j == len(grid[i]) - 1:
                        if grid[i][j] == 0:
                            return False
                    else:
                        if grid[i][j] != 0:
                            return False
                else:
                    if j == 0 or j == len(grid[i]) - 1:
                        if grid[i][j] != 0:
                            return False
        return True

# 我的解題方式卡在倒數第二關 83 / 84 testcases passed
# 而我用了很白癡的暴力解題方式，看了其他人的解題後恍然大悟。


#Solution 1 - (參考網路)

# 解題邏輯: 
# 對角線>0，其餘為0。

class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        last = len(grid) - 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == j or (i+j) == len(grid)-1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] > 0:
                    return False
        return True
