# Given the root of a binary tree, return the preorder traversal of its nodes' values.
 
# Example 1:
 
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]


#Solution 1 - (自己想的，有參考網路資料)

# 解題邏輯: 
# 想用遞迴解題，但是遲遲想不到如何回傳array值，後來想到建立一個新的function，並且新增一個arr變數傳進去，再透過自身遞迴的方式解題。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return root
        arr = []
        self.preorder(root, arr)
        return arr
    
    def preorder(self, root, arr):
        if root:
            arr.append(root.val)
            self.preorder(root.left, arr)
            self.preorder(root.right, arr)


#Solution 2 - (參考網路)

# 另一種遞迴方式

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root: return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        else: return []


#Solution 3 - (參考網路上)

# 解題邏輯: 
# 使用stack的特性 LIFO，把堆疊中的值一個一個取出。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = [root]
        answer = []
        while node:
            temp = node.pop()
            if temp:
                answer.append(temp.val)
                node.append(temp.right)
                node.append(temp.left)
        return answer


#Solution 4 - Solution 4: (參考網路)

# 解題邏輯: (Morris Traversal -> 企業愛考題)
# Algorithm 
# 1.	Initialize an answer array. We also need two pointers, curr and last. Initialize curr as the root node. 
# 用curr儲存root的值，last尋找左子樹中的最大值 -> 好以跟樹根節點進行交換
# 2.	While curr is not NULL, check if it has a left child or not: 
# -	If it has a left child, let `last` be the **rightmost** node of `curr`'s **left** subtree. Add `curr` to the answer and modify `last`'s right child as `curr`. 
# -	Otherwise, add `curr` to the answer and move on to `curr`'s right child. 
# 當樹不為空時，檢查是否有左子樹
# 如果有左子樹，找到last -> 左子樹中的最大值，將last的右節點指向當前的樹根，最後將當前節點指向節點的左子樹
# 若沒有左子樹了，則將當前節點指向右子樹
# 3.	During the iteration, if we visit a node whose right child is curr, it implies that we are currently at the last node of this curr node. We reset last's right child to NULL and move on to curr's right child. 
# 如果當訪問的節點的右子樹直與當前節點的值相等，代表我們完成訪問最後節點了，因此將last的右節點變為None，並且開始進行右子樹的訪問。
# 4.	Return answer after the iteration stops.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        curr = root
        while curr:
            if not curr.left:
                answer.append(curr.val)
                curr = curr.right
            else:
                last = curr.left
                while last.right and last.right!=curr:
                    last = last.right
                
                if not last.right:
                    answer.append(curr.val)
                    last.right = curr
                    curr = curr.left
                else:
                    last.right = None
                    curr = curr.right
        return answer
