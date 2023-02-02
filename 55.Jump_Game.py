# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

from collections import reduce

#Solution 1 - 參考網路
# 透過for loop中的enumerate()功能進行解題，透過列表的特性，enumerate出key和value值，並且透過相加的方式去判斷是否有符合跳格子的特性，最終return出答案。

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maximum = 0
        for i, n in enumerate(nums):
            if i > maximum:
                return False
            maximum = max(maximum, i+n)
        return True
# 如果i=>index大於跳格子的最大值時，代表無法抵達終點 return False


#Solution 2 - 參考網路

# 從nums列表的最後開始判斷，依據索引值i加上該值，是否有大於或等於該索引的值，去判斷return該為True或False。
# 若是for loop跑完，目標值也為0則回傳True(return not False => True),否則回傳False(return not True => False)。

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

