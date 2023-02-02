# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from collections import Counter

#Solution 1 - 參考網路
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 不允許使用O(1)的額外記憶體，因此修改nums本身內容
        nums[:] = sorted(set(nums))
        return len(nums)


#Solution 2 - 參考前題自己寫的
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(Counter(nums))
        return len(nums)


#Solution 3 - 參考網路
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x += 1
        return x



#此題不能用sort()或sorted()，因為沒有更新列表而是利用相同列表重新定義新列表
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 此處的nums記憶體位置為140171600838320
        print(id(nums))
        nums = sorted(Counter(nums))
        # 此處的nums記憶體位置為140171611156720
        print(id(nums))
# 此測試在leedcode上執行

# 解決方法為nums[:] -> 會複製記憶體位置，根據記憶體位置進行動作
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 此處的nums記憶體位置為140171600838320
        print(id(nums))
        nums[:] = sorted(Counter(nums))
        # 此處的nums記憶體位置為140171600838320
        print(id(nums))