# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
 
# Example 1:
 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


#Solution 1 - (參考網路)

# 解題邏輯: 
# 最簡單的方式就是使用快慢指針 fast/slow，也可以寫成 runner/walker。快指針一次走兩步，慢指針一次走一步，如果他們有碰上，那就是有環。 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False


#Solution 2 - (參考網路)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        traveled = {'cycle': False}
        
        def iterate(node):
            if not node:
                return
            if node not in traveled:
                traveled[node] = 1
            else:
                traveled['cycle'] = True
                return
            iterate(node.next)
        
        iterate(head)
        
        return traveled['cycle']
