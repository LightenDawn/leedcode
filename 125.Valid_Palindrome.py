# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
 
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


#Solution 1 

# 解題邏輯: 
# 建立一個新的字串，把舊字串中不是字母和數字的符號去除掉。
# 使用isalnum() => 判斷是不是alpha(字母)或num(數字)。
# 最後在判斷新的字串和反轉後的新字串是否一致，一致則回傳True。

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ""
        for i in s.lower():
            if i.isalnum():
                new_s += i
        if new_s == new_s[::-1]: return True
        return False


#Solution 2 

# 解題邏輯: 
# 有點沒意義的解題方式，單純將新字串判斷反轉後是否一致。

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ""
        for i in s.lower():
            if i.isalnum():
                new_s += i
        mid = (len(new_s))//2
        if len(new_s)%2 == 0:
            left = new_s[:mid]
            right = new_s[mid:]
        else:
            left = new_s[:mid]
            right = new_s[mid+1:]
        if left == right[::-1]: return True
        return False


#Solution 3 - (參考網路)

# 解題邏輯: 
# 直接從字串s中的索引0和索引(字串長度)開始進行比對，若不是字母和數字則索引+1或-1，若是字母和數字則開始比對字串[start]和字串[end]是否一致，不一致直接return False。

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s)-1
        while start < end:
            if s[start].isalnum() == False:
                start += 1
            elif s[end].isalnum() == False:
                end -= 1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1
        return True


#Solution 4 - (參考網路)

# 解題邏輯: 
# 直接用一行程式碼運算s字串中若是字母和數字的則+總。
# 最後用字串和反轉字串判斷是否一致。

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]
