# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 
# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5


#Solution 1

# 解題邏輯:
# 用遞迴方式尋找左子樹/右子樹中最小的高度。
# PS. 可能會遇到右傾樹/左傾樹

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


#Solution 2

#與前題類似，寫法略微不同

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return (left+right+1) if (left == 0 or right == 0) else min(left, right) + 1 



#Soltuon 3 - 參考網路

# 首先，運用python的map()功能。
# map()會根據提供的函數對指定序列做映射。 
# 第一個參數function以參數序列中的每一個元素調用function 函數，返回包含每次function 函數返回值的新列表。
# 使用map()可以優化for loop的運算速度。

# 從樹葉找起。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        d = map(self.minDepth, (root.left, root.right))
	      #  解釋 => map(動作, 資料) => 將後方的資料要進行的動作
        return 1 + (min(d) or max(d))
        #  超級重點
        #  Truthy1 or Truthy2 return Truthy1
        #  Truthy2 or Truthy1 return Truthy2
        #  兩者皆為True時, 返回第一個值
        #  False or True return False => ([] or 144) => 144
        #  True or False return False =>

        # example:
        # root = [3,9,20,null,null,15,7]						  
        # 第一輪 : root => 9 ; d => [0, 0]
        # 第二輪 : root => 15 ; d => [0, 0]
        # 第三輪 : root => 7 ; d => [0, 0]
        # 第四輪 : root => 20 ; d => [1, 1]
        # 第五輪 : root => 3 ; d => [1, 2]


#Solution 4

#與前題類似

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)


#Solution 5 - 參考網路

# DFS(Depth-First Search)深度優先搜尋。
# 其Visiting順序：「Current(V)-left(L)-right(R)」可以解讀成「先遇到的node就先Visiting」，因此，每一組「Current-left-right」必定是CurrentNode先Visiting，接著是leftchild，最後才是rightchild。

class Solution:
    def minDepth(self, root):
        
        if not root:
            # base case for empty node or empty tree
            return 0
        
        if not root.left and not root.right:
            # leaf node
            return 1
        
        elif not root.right:
            # only has left sub-tree
            return self.minDepth(root.left) + 1
        
        elif not root.left:
            # only has right sub-tree
            return self.minDepth(root.right) + 1
        
        else:
            # has left sub-tree and right sub-tree
            return min( map(self.minDepth, (root.left, root.right) ) ) + 1


#Solution 6 - 參考網路

# BFS(Breadth-First Search)廣度優先搜尋。
# 在Binary Tree: Traversal(尋訪)與Binary Tree: 建立一棵Binary Tree
# queue在Binary Tree中進行Level-Order Traversal，其概念便是：各個node相對於root有其對應的level，按照level由小到大依序對node進行Visiting。

from collections import deque
class Solution:
    def minDepth(self, root):

        visit_queue = deque([(root, 1)])

        while len(visit_queue) != 0:
            # BFS Traversal

            next_visit, cur_depth =visit_queue.popleft()

            if next_visit is None:
                # empty node or empty tree
                continue
            
            if next_visit.left is None and next_visit.right is None:
                # reach a leaf node
                # get the minimal depth of binary tree, early return
                return cur_depth

            #append left and right child into visit_queue, increase current depth by 1
            visit_queue.append( (next_visit.left, cur_depth+1) )
            visit_queue.append( (next_visit.right, cur_depth + 1) )

        # depth 0 for empty-tree
        return 0
