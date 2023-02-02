# You are given an m x n integer matrix matrix with the following two properties:
# •	Each row is sorted in non-decreasing order.
# •	The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
 
# Example 1:
 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


#Solution 1

# 直接透過matrix的每個子陣列去作判別target是否在此陣列中，是則true，否則false。

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if target in i:
                return True
        return False


#Solution 2 - 參考網路

# 解題邏輯: 
# 使用二分搜尋法。

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        # row -> 行(有幾行), col -> 列(子陣列有幾個)
        start = 0
        # 起點為0
        end = row * col - 1
        # 終點為 行 * 列 - 1 => 若為4*3矩陣，總元素有 4*3-1 = 11
        mid = (start + end) / 2
        # 總共元素的中間值, 若是4*3矩陣則中間值為11/2=5
        while start <= end:
            element = matrix[mid/col][mid%col]
            # 從元素的中心點找起, 若為4*3矩陣 -> 初始為matrix[1][1]
            if element == target:
                return True
            elif element < target:
                start = mid + 1
                # 若是目標大於目前值, 則要往後面序列找
            else:
                end = mid - 1
                # 若是目標小於目前值, 則要往前面序列找
            mid = start + (end - start) / 2
        return False


#Solution 3 - (參考最佳運算解)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        R, C = len(matrix), len(matrix[0])
        # row -> 行(有幾行), col -> 列(子陣列有幾個)
        l, r = 0, R * C - 1
        while l<r:
            mid = (l + r) // 2
            row = mid // C
            col = mid % C
            if matrix[row][col] >= target:
                r = mid
            else:
                l = mid + 1
        if matrix[l//C][r%C] == target:
            return True
        else:
            return False


#Solution 4 - (空間最佳解)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x = 0
        for i in matrix:
            if i.count(target)!= 0 : x += 1
        
        if x != 0:
            return True
        else:
            return False
