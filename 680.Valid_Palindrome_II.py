# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
 
# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false


#Solution 1 - (參考網路)

# 解題邏輯: 
# 先給定left從0開始找起，right從len(s)-1開始找起，若是left和right的值不相同，再比對left+1和right+1的字串是否相等(因為可以容許刪除一個字元，再來判定是否加以達到回文的要求)。
# 若不同則return False
# Else return True

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left+1:right+1]
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1
        return True


#Solution 2 - (參考網路)

# 解題邏輯與前題類似，只是運用遞迴形式。

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.newValidPalindrome(s, 0, len(s)-1, 0)
    def newValidPalindrome(self, s, left, right, count):
        while left <= right:
            if s[left]!=s[right]:
                count += 1
                if count > 1: return False
                result = False
                if left+1 <= right:
                    result |= self.newValidPalindrome(s, left+1, right, count)
                if left <= right-1:
                    result |= self.newValidPalindrome(s, left, right-1, count)
                return result
            left += 1
            right -= 1
        return True
