# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

# Example 1:

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:

# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


#Solution 1 - 參考網路

# Definition for a binary tree node.
# 先判斷題目給的nums是否為空列表，若是則回傳空樹。
# 接著找尋nums列表的中位數，透過中位數去依序排序左子、右子樹。
# 此題解法:遞迴
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # base case
        if not nums: return None
        
        # getting the mid
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        
        # left node is given the responsibility till mid, 
        # but not including mid
        node.left = self.sortedArrayToBST(nums[:mid])
        # right node is given the responsibility from mid+1 
        # till the end
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node


#Solution 2

# Definition for a binary tree node.
# 與前題大同小異，但是透過呼叫function完成。
# Divide and Conquer的方式，給予新的function列表、起頭和結尾的值。
# 透過中位數去分別排序左子樹與右子樹的順序。
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.makeBST(nums, 0, len(nums))
    
    def makeBST(self, nums, start, end):
        if start >= end: return None
        return TreeNode(
            val=nums[ (start + end)//2 ],
            left=self.makeBST(nums, start, (start + end)//2),
            right=self.makeBST(nums, 1+((start+end)//2), end)
        )


#Solution 3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )
