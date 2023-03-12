# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
 
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []



#Solution 1 (自己寫)

# 解題邏輯: 
# 將題目給的每個鏈結串列依次加入到new_arr中，再透過排序該列表後依次加入到新的鏈結串列中，最後回傳。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        new_arr = []
        for i in lists:
            while i:
                new_arr.append(i.val)
                i = i.next
        new_arr = sorted(new_arr)
        length = 0
        node = ListNode()
        trace = node
        while length < len(new_arr):
            new_node = ListNode(new_arr[length])
            node.next = new_node
            node = node.next
            length += 1
        return trace.next
