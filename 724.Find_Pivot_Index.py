# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.
 
# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0


#Solution 1 

# 解題邏輯: 
# 本題要找到關鍵值，且關鍵值的左邊和右邊的加總數相等，並且回傳該索引值，否則回傳-1。

# 因此用python中的slice解法，但此種解法相當耗費運算時間。

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

#另一種解法
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        counter = 0
        for i in range(len(nums)):
            if counter == sum(nums[i+1:]):
                return i
            counter += nums[i]
        return -1


#Solution 2 - (參考一些tips，自己寫的)

# 解題邏輯: 
# 設置兩個變數
# Sum_l => 左邊的加總，起始為0
# Sum_r => 右邊的加總，起始為sum(nums)
# 用for loop開始跑，若是sum_l == sum_r則return該索引，否則return -1
# Tricky的地方 -> 
# Sum_r必須先減去當前索引的value，否則會不對稱。

# 例如: 
# (錯的範例)
#         for i in range(len(nums)):
#             if sum_l == sum_r:
#                 return i
# 		   sum_r -= nums[i]
#             sum_l += nums[i]
# nums = [1,7,3,6,5,6]
# 1.	Nums[0] -> sum_r = 28, sum_l = 0
# 2.	Nums[1] -> sum_r = 27, sum_l = 1
# 3.	Nums[2] -> sum_r = 20, sum_l = 8
# 4.	Nums[3] -> sum_r = 17, sum_l = 11
# 5.	Nums[4] -> sum_r = 11, sum_l = 17
# 6.	Nums[5] -> sum_r = 6, sum_l = 22
# 7.	Nums[6] -> sum_r = 0, sum_l = 28

# (對的示範)
#         for i in range(len(nums)):
#             sum_r -= nums[i]
#             if sum_l == sum_r:
#                 return i
#             sum_l += nums[i]
# nums = [1,7,3,6,5,6]
# 1.	Nums[0] -> sum_r = 27, sum_l = 0
# 2.	Nums[1] -> sum_r = 20, sum_l = 1
# 3.	Nums[2] -> sum_r = 17, sum_l = 8
# 4.	Nums[3] -> sum_r = 11, sum_l = 11
# return 3

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        sum_l = 0
        sum_r = sum(nums)
        for i in range(len(nums)):
            sum_r -= nums[i]
            if sum_l == sum_r:
                return i
            sum_l += nums[i]
        return -1
