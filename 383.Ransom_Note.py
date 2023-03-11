# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# ransomNote(勒索信)是否能由magazine(雜誌)拼湊而成


from collections import Counter

#Solution 1 (自己寫)

# 解題邏輯: 
# 從勒索信開始尋找，若勒索信的字母有出現在雜誌中，則將其去掉，依序進行判斷，若雜誌中沒有可以刪除的字母則回傳False，若離開迴圈(代表勒索信的內容皆在雜誌中)，則回傳True。

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote, magazine = list(ransomNote), list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True


#Solution 2 (自己寫)

# 解題邏輯: 
# 使用Counter去計算字元出現的次數，並且由勒索信的Counter減去雜誌的Counter，若相減後為空 => not False，否則 not True。

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote, magazine = Counter(ransomNote), Counter(magazine)
        return not (ransomNote - magazine)


#Solution 3 (自己寫)

# 解題邏輯: 前題的簡寫

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not (Counter(ransomNote) - Counter(magazine))


#Solution 4 (自己寫)

# 解題邏輯: 
# 與Counter類似的寫法，只是透過dict去做判斷。

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        new_dict = {}
        for i in magazine:
            new_dict[i] = new_dict.setdefault(i, 0) + 1
        del_dict = {}
        for i in ransomNote:
            del_dict[i] = del_dict.setdefault(i, 0) + 1
        return not (dict(Counter(del_dict) - Counter(new_dict)))


#Solution 5 (自己寫)

# 解題邏輯: 
# 透過字串的特性，依序將勒索信的每個字元有出現在雜誌中的去除，若勒索信最後為空 => True，否則False。

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:
            if i in magazine:
                ransomNote = ransomNote.replace(i, '', 1)
                magazine = magazine.replace(i, '', 1)
        if not ransomNote:
            return True
        return False
