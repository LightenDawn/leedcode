# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.
 
# Example 1:
 
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2:
# Input: head = [0]
# Output: 0


#Solution 1 

# 解題邏輯:
# 先透過while loop，將linked list中的所有值給取出來給list，再用[::-1] list反轉，因為題目給定的 1 0 1 => 4 2 1 => 從最右邊為2^0開始依序向左遞增，因此列表反轉後，就可以從左邊遞增上去。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        new_arr = []
        while head:
            new_arr.append(head.val)
            head = head.next
        new_arr = new_arr[::-1]
        total = 0
        for i in range(len(new_arr)):
            if new_arr[i] == 1:
                total += 2 ** i
        return total


#Solution 2

# 與前題類似，只是減少運算需求程度 -> 反轉字串的部分

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        new_arr = []
        while head:
            new_arr.append(head.val)
            head = head.next
        total = 0
        for i in range(len(new_arr)-1, -1, -1):
            if new_arr[i] == 1:
                total += 2 ** (len(new_arr) - 1 - i)
        return total


#Solution 3 - (自己寫) -> 最佳解

# 解題邏輯: 
# 使用字串的方式。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        s = ""
        while head:
            s += str(head.val)
            head = head.next
        total = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                total += 2 ** (len(s) - 1 - i)
        return total
