# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
 
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

from collections import Counter

#Solution 1

# 解題邏輯: 
# 使用Counter()去計算有哪些元素與出現幾次，若只出現1次則return該值。


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = Counter(nums)
        for key, value in nums.items():
            if value == 1:
                return key


#Solution2 

# 解題邏輯: 
# Count => 計算出現次數
# Temp => 暫存數字，預設為None (若不為None會出現錯誤)
# If count == 1 and temp != i:
# 如果出現過一次，且目前的值不等於temp值，則break，並且回傳temp

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = None
        nums = sorted(nums)
        for i in range(len(nums)):
            if count == 1 and temp != nums[i]:
                break
            count += 1
            if temp == nums[i]:
                count = 0
            temp = nums[i]
        return temp


#Solution 3 

# 解題邏輯: 
# 使用字典，先用for loop把nums中所有數字出現的次數進行加總。
# 並且再用一個for loop去查找字典中只有出現過一次的值。

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_dict = {}
        for i in nums:
            new_dict[i] = new_dict.setdefault(i, 0) + 1
        for key in new_dict:
            if new_dict[key] == 1:
                return key
        return 0


#Solution 4 

# 解題邏輯: 
# 建立一個新的變數儲存nums的集合(元素只出現過一次)。
# 再用count(i)去計算出現在nums次數的值，若為1則return該值。

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = set(nums)
        for i in new:
            if nums.count(i) == 1:
                return i


#Solution 5 - (參考網路)

# 解題邏輯: 
# XOR => 兩者相同時為False，兩者不同時為True
# nums = [4,1,2,1,2]
# 第一輪 XOR = XOR(0) ^ nums[i](4) = 4
# 第二輪 XOR = XOR(4) ^ nums[i](1) = 4+1 = 5
# 第三輪 XOR = XOR(5) ^ nums[i](2) = 5+2 = 7
# 第四輪 XOR = XOR(7) ^ nums[i](1) = 7-1 = 6(因為1出現過)
# 第五輪 XOR = XOR(6) ^ nums[i](2) = 6-2 = 4(因為2出現過) 	
# 最後return 4
 

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        XOR = 0
        for i in range(len(nums)):
            XOR ^= nums[i]
        return XOR


#Solution 6 -  (參考網路)

# 解題邏輯: 
# 加總nums的集合並且*2，再減去nums的加總。

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)
