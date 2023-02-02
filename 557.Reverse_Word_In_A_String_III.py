# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
 
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"


#Solution 1

# 解題邏輯: 
# 將s字串用split把每一段單字分割，再用反轉的方式加回到新字串中，並且return。
# 會遇到的問題 -> 最後面return回去的字串會多一格空格，因為我是用強制+” “的方式，最愚蠢的做法。

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_rev = ""
        for i in s.split(" "):
            s_rev += i[::-1] + " "
        return s_rev[0:-1]


#Solution 2 

# 解題邏輯: 
# 先將s字串給個別split()，變成list[]。
# 再用for loop將各個字元反轉，最後再用’’.join(s)把字元+空白逐字加回去。

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return ' '.join(s)


#Solution 3 - 參考網路

# 解題邏輯: 
# 將前兩題的邏輯濃縮成一段程式碼

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda x: x[::-1], s.split(' ')))


#Solution 4 - 參考網路
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(i[::-1] for i in s.split(' '))
