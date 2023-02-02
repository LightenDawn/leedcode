# Given a binary tree, determine if it is height-balanced.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:

# Input: root = []
# Output: true

#Solution 1 - 參考網路

# 運用Divide and Conquer，將一顆樹分為左子樹和右子樹一個一個查看，因此，遇到最壞的情況(遍歷整棵樹)，時間複雜度為O(n)。
# 先用遞迴的方式，將樹分為左子樹、右子樹，同時判斷其是否有樹葉(leaf)的存在和左子樹與右子樹之間的高度差是否小於2，若不是則為False。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return 1 + max(left,right)
        return check(root) != -1


#Solution 2 - 參考網路

# 解題邏輯: 
# 與先前大同小異，拆成兩部分，首先創建一個尋找深度的function，若是深度相差小於2、左子樹和右子樹達到平衡，則回傳為是完整二元樹，反之。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            if root is None : return 0
            return max(depth(root.left), depth(root.right)) + 1

        if root is None:
            return True
        left = depth(root.left)
        right = depth(root.right)

        return abs(left - right) <= 1  and self.isBalanced(root.left) and self.isBalanced(root.right)
