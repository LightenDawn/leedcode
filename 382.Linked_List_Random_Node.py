# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Implement the Solution class:

# Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
 

# Example 1:


# Input
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 3, 2, 2, 3]

# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.getRandom(); // return 1
# solution.getRandom(); // return 3
# solution.getRandom(); // return 2
# solution.getRandom(); // return 2
# solution.getRandom(); // return 3
# // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.



import random
# Solution 1: (自己寫)

# 解題邏輯: 
# 首先建立一個變數去儲存鏈結串列的所有值，並且將該變數分享給getRandom()做取用。
# 再透過getRandom()去做從串列中獲取隨機變數，最後回傳。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.new_arr = []
        while head:
            self.new_arr.append(head.val)
            head = head.next

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.new_arr)
        

# Solution 2: (參考網路)

# 解題邏輯: 
# 直接將鏈結串列共享給getRandom()，在該function把鏈結串列的長度計算出來，透過該長度去隨機索引值。
# 計算出索引值後，重新付值給curr，並且做for-loop的方式取值回傳。

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        curr = self.head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        number = random.randint(0, length-1)
        curr = self.head
        for i in range(number):
            curr = curr.next
        return curr.val
