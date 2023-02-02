# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
 
# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

# Example 3:
# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).


#Solution 1 

# 解題邏輯: 
# 如果n小於或等於0，代表不是3的指數，因此回傳False。
# 用while迴圈去跑n/3，如果有餘數代表不為3的指數，回傳False，直到n剩下1。

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while n > 0:
            if n % 3 == 0:
                n /= 3
            elif n==1:
                return True
            else:
                return False


#Solution 2

# 解題邏輯: 
# 使用遞迴的方式進行。

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        if n%3 == 0: return self.isPowerOfThree(n/3)
        elif n==1: return True
        else: return False


#Solution 3 - (網路上的遞迴)

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        elif n < 3: return False
        if not n%3: return self.isPowerOfThree(n/3)


#Solution 4 - (參考網路)

# 解題邏輯: 
# 使用變數儲存餘數，而最後餘數應該要為1，商為0。
# 因為3^0 = 1。

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        k = 0
        while n != 0 and k < 1:
            k = n%3
            n /= 3
        if n == 0 and k == 1:
            return True
        else:
            return False
