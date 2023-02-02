# Given the root of a binary tree, return the postorder traversal of its nodes' values.
 
# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]


#Solution 1 

# 解題邏輯: 
# 使用遞迴方式呼叫，並且依照L>R>D的順序依序加入列表中，最後回傳。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        new_arr = []
        if not root: return new_arr
        return self.postorder(root, new_arr)
    def postorder(self, root, arr):
        if root:
            self.postorder(root.left, arr)
            self.postorder(root.right, arr)
            arr.append(root.val)
        return arr


#Solution 2 - (參考先前的Preorder)

# 解題邏輯: 
# 使用堆疊的方式，依序將樹的值給pop出來，最後將列表進行反轉。
# D>L>R => 前序為樹根>左子樹>右子樹
# L>R>D => 後序為左子樹>右子樹>樹根
# 所以先拜訪樹根/再拜訪右子樹/再拜訪左子樹 D>R>L
# 最後將列表反轉 => L>R>D

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        new_arr = [root]
        answer = []
        while new_arr:
            temp = new_arr.pop()
            if temp:
                new_arr.append(temp.left)
                new_arr.append(temp.right)
                answer.append(temp.val)
            
        return answer[::-1]


#Solution 3

# 遞迴

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root: return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        else: return []


#Solution 4 - (參考網路)

# 解題邏輯: 
# 使用反Morris Traversal

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        def reverseOrder(left,right):
            while left<right:
                result[left],result[right]=result[right],result[left]
                left+=1
                right-=1
        dummynode= TreeNode(None) #dummy node
        node=dummynode
        node.left=root
        while node!=None:
            print(node.val)
            if node.left==None:
                node=node.right
            else:
                pre=node.left
                while pre.right!=None and pre.right!=node:
                    pre=pre.right
                if pre.right==None:
                    pre.right=node
                    node=node.left
                else:
                    pre=node.left
                    count=1
                    while pre.right!=None and pre.right!=node:
                        result.append(pre.val)
                        pre=pre.right
                        count+=1
                    result.append(pre.val)
                    pre.right=None
                    reverseOrder(len(result)-count,len(result)-1)
                    node=node.right
                    
        return result
