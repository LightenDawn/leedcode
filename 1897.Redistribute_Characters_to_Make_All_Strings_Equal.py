# You are given an array of strings words (0-indexed).
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
# Return true if you can make every string in words equal using any number of operations, and false otherwise.
 
# Example 1:
# Input: words = ["abc","aabc","bc"]
# Output: true
# Explanation: Move the first 'a' in words[1] to the front of words[2],
# to make words[1] = "abc" and words[2] = "abc".
# All the strings are now equal to "abc", so return true.

# Example 2:
# Input: words = ["ab","a"]
# Output: false
# Explanation: It is impossible to make all the strings equal using the operation.

from collections import Counter
from functools import reduce
from math import mod, add

#Solution 1 - (參考網路)

# 解題邏輯: 
# 先將list中的字串全部轉為單一字
# words = ["abc","aabc","bc"] => words = “abcaabcbc”
# 再使用Counter()計算裡面字元出現幾次
# 最後再用字數/words的長度，若餘數不為0則return False

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        total_words = len(words)
        string = ''.join(words)
        FreqMap = Counter(string)

        for char, freq in FreqMap.items():
            if freq % total_words != 0:
                return False
        return True


#Solution 2 - (參考網路)

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        return all(map(lambda c: mod(c, len(words)) == 0, reduce(add, map(Counter, words)).values()))


#Solution 3 - (參考網路)

# 解題邏輯: 
# 建立一個長度為26的空列表儲存a-z出現的次數。
# For loop去循環抓出在列表中的字元，並且在先前的空列表加總出現次數。
# 再用for loop抓出字元出現的次數，去除以words的長度。
# 若餘數不為0 return False。

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        new_arr = [0]*26
        for i in words:
            for j in i:
                new_arr[ord(j) - ord('a')] += 1
        for i in new_arr:
            if i % len(words):
                return False
        return True


#Solution 4 - (參考網路)

# 解題邏輯: 
# 與先前類似，只是用dict儲存內容。

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        new_dict = {}
        for i in words:
            for j in i:
                if j not in new_dict:
                    new_dict[j] = 1
                else:
                    new_dict[j] += 1
        for key, value in new_dict.items():
            if value % len(words):
                return False
        return True

#另一種寫法

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        new_dict = {}
        for word in words:
            for char in word:
                new_dict[char] = new_dict.setdefault(char, 0) + 1 # 2擇1
                new_dict[char] = new_dict.get(char, 0) + 1
        for key, value in new_dict.items():
            if value % len(words):
                return False

        return True


#Solution 5 - (參考最佳解)

# 解題邏輯: 
# 先將words轉成字串。
# 再用set()，總結出現過哪些字元。
# 用for loop跑set()內的字元，再用count()的方式，計算words中出現該字元的次數為何。
# 將該次數除以words的長度，若不為0 return False。

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        words_str = ''.join(words)
        words_set = set(words_str)
        
        for i in words_set:
            if words_str.count(i) % len(words) != 0:
                return False
        return True
