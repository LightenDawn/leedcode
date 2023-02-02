# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 
# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


#Solution 1
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if list1 == None and list2 == None: return 
        # if list1 == None and list2 != None: return list2
        # if list1 != None and list2 == None: return list1
        
        # 建立new_node和dummy，dummy可以在最後return
        new_node = dummy = ListNode()
        # 若list1和list2不為None時
        while list1 and list2:
            # 如果list1.val 小於 list2.val
            if list1.val <= list2.val:
                # 將new_node的下個目標指向list1
                new_node.next = list1
                # new_node移至當前位置list1， list1則前往下個目標
                new_node, list1 = list1, list1.next
            else:
                new_node.next = list2
                new_node, list2 = list2, list2.next
        # 檢查list1和list2中是否有剩下的值
        if list1 or list2:
            new_node.next = list1 if list1 else list2
        return dummy.next

