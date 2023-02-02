# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
 
# Example 1:
 
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
 
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
 
# Input: p = [1,2,1], q = [1,1,2]
# Output: false



#Solution 1 

# 解題邏輯: 
# 使用上一題的preorder遞迴方式進行，把所有資訊append到list中，再互相比對是否相同，是則True，否則False。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        arr1, arr2 = [], []
        self.preorder(p, arr1)
        self.preorder(q, arr2)
        if arr1 == arr2:
            return True
        else:
            return False

    def preorder(self, root, arr):
        if root:
            arr.append(root.val)
            self.preorder(root.left, arr)
            self.preorder(root.right, arr)
        else:
            arr.append(None)
        return arr


#Solution 2 - (參考網路)

# 解題邏輯: 
# 直接用判斷式篩選，再用遞迴的方式依序搜尋，空間複雜度應比我的使用度還低。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p or not q: return False
        return (p.val==q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


#Solution 3 - (參考網路)

# 解題邏輯: 
# 直接將TreeNode資料轉成str，再讓它們去相比對。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return str(p)==str(q)
