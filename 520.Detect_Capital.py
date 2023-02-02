# We define the usage of capitals in a word to be right when one of the following cases holds:
# •	All letters in this word are capitals, like "USA".
# •	All letters in this word are not capitals, like "leetcode".
# •	Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.
 
# Example 1:
# Input: word = "USA"
# Output: true

# Example 2:
# Input: word = "FlaG"
# Output: false


#Solution 1 

# 題目的條件為 -> 全部都大寫 return True
# 				全部都小寫 return True
# 				開頭大寫，其他小寫 return True
# 				其他 return False
# 因此，首先判斷word是否全都大寫，是則回傳True，否則繼續。
# 用for loop判斷是否開頭大寫，且其中是否有大寫，是則回傳False，否則回傳True。
# For loop偵測結束都沒出錯，則回傳True。

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word:
            return True
        isCap = False
        for i in range(len(word)):
            if ord(word[0]) < 97:
                if isCap == False:
                    isCap = True
                    continue
            if ord(word[i]) < 97:
                return False
        return True


#Solution 2 

# 單純用if-else:進行判斷，根據第一題的邏輯分析去判定word是否符合條件。
# 題目的條件為 -> 全部都大寫 return True
# 				全部都小寫 return True
# 				開頭大寫，其他小寫 return True
# 				其他 return False

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word or word.lower() == word:
            return True
        if ord(word[0]) < 97 and word[1:] == word[1:].lower():
            return True
        else:
            return False


#Solution 3 

# 單純用islower()和isupper()進行判斷。

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
