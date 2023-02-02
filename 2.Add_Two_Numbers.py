# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]



#Solution 1 - (參考網路)

# 解題邏輯: 
# 首先新增一個新的空Linked List，並且新增一個變數複製他。
# 新增一個變數carry => 是否有進位。

# 再跑while loop，判斷如果l1不是None或l2不是None或carry不等於零 => 代表若是l1和l2為0時，carry不為0(有進位)，則最後新增一次再break。

# 新增兩個變數儲存l1和l2的value，若無則為0。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        curr = node
        carry = 0
        while l1!=None or l2!=None or carry!=0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            per = (l1_val+l2_val+carry)
            new_node = ListNode(per%10)
            carry = per//10
            curr.next = new_node
            curr = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return node.next


#Solution 2 - (參考網路)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + carry
        carry = val // 10
        ret = ListNode(val%10)

        if l1.next!=None or l2.next!=None or carry!=0:
            if l1.next == None:
                l1.next=ListNode(0)
            if l2.next == None:
                l2.next=ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return ret
