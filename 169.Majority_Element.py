# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from collections import Counter

#Solution 1 

# 解題邏輯: 
# 先用num_set儲存nums的集合
# 再透過num_set去找出該值在nums中有多少個，若為最大值則temp儲存該值數字，最後回傳。

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        maximum = None
        for i in nums_set:
            if maximum < nums.count(i):
                maximum = nums.count(i)
                temp = i
        return temp


#Solution 2 

# 解題邏輯:
# 使用COUNTER()

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count = Counter(nums)
        temp = 0
        for index, value in nums_count.items():
            if value > temp:
                temp = value
                rtype = index
        return rtype


#Solution 3 

# 解題邏輯:
# 使用COUNTER()

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count = Counter(nums)
        temp = 0
        for index, value in nums_count.items():
            if value > temp:
                temp = value
                rtype = index
        return rtype


#Solution 4 - (參考網路)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]


#Solution 5 - (參考網路)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        return max(counts.keys(), key = counts.get)


#Solution 6 - (參考網路)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        majority_element = 0
        
        bit = 1
        for i in range(31):
            # Count how many numbers have the current bit set.
            bit_count = sum(bool(num & bit) for num in nums)

            # If this bit is present in more than n / 2 elements
            # then it must be set in the majority element.
            if bit_count > n // 2:
                majority_element += bit
            
            # Shift bit to the left one space. i.e. '00100' << 1 = '01000'
            bit = bit << 1
                
        # In python 1 << 31 will automatically be considered as positive value
        # so we will count how many numbers are negative to determine if
        # the majority element is negative.
        is_negative = sum(num < 0 for num in nums) > (n // 2)

        # When evaluating a 32-bit signed integer, the values of the 1st through 
        # 31st bits are added to the total while the value of the 32nd bit is 
        # subtracted from the total. This is because the 32nd bit is responsible 
        # for signifying if the number is positive or negative.
        if is_negative:
            majority_element -= bit
        
        return majority_element


#Solution 7 - 參考網路

import random
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


#Solution 8 - 參考網路

import random
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)
