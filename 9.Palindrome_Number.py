# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


#Solution 1
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 將int(x)轉換成str(x)才能用python的slice方法
        x = str(x)
        # 回傳x是否與反轉後的x相等
        return x == x[::-1]

solution = Solution()
solution.isPalindrome(121)
solution.isPalindrome(-121)
solution.isPalindrome(10)

#Solution 2 - 參考官方
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 如果x小於0(有負數) 和 x/10的餘數=0加上x本身不為0的情況
        if x<0 or (x%10 == 0 and x!=0): return False
        reverse_x = 0
        while x > reverse_x:
            reverse_x = reverse_x * 10 + x%10
            x /= 10
        # 若有中間數則用後方的判斷式判斷
        return reverse_x == x or reverse_x/10 == x
        # 12321 => reverse_x = 123, x = 12

solution = Solution()
solution.isPalindrome(121)
solution.isPalindrome(-121)
solution.isPalindrome(10)


#Solution 3 - 參考網路
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10 == 0 and x!=0): return False
        number = 1
        while x / number > 10:
            # 計算x有幾位數
            number *= 10
        while x:
            # x的head
            left = x // number
            # x的tail
            right = x%10
            # 若x的head != x的tail，表示不為回文
            if left != right: return False
            # x去頭去尾 -> 122221 -> 2222
            x = (x%number) / 10
            # 因為去頭去尾，用去兩位數，因此除100
            number /= 100
        return True

solution = Solution()
solution.isPalindrome(121)
solution.isPalindrome(-121)
solution.isPalindrome(10)