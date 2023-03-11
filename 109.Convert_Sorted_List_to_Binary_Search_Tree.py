# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:


# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.


# Example 2:

# Input: head = []
# Output: []



#Solution 1 (參考網路+自己寫)

# 解題邏輯: 
# 先用迴圈把鏈結串列的值assign給list，再透過自己定義的function去將list的內容一個一個加入到樹中。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        new_arr = []
        while head:
            new_arr.append(head.val)
            head = head.next
        node = TreeNode()
        node = self.addNode(new_arr, 0, len(new_arr) - 1)
        return node

    def addNode(self, arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(arr[mid])

        node.left = self.addNode(arr, start, mid-1)
        node.right = self.addNode(arr, mid+1, end)

        return node
