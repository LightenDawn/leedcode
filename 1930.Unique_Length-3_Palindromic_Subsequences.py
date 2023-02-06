# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# •	For example, "ace" is a subsequence of "abcde".
 
# Example 1:
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")

# Example 2:
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".

# Example 3:
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")

import string
from collections import Counter

# Solution 1 – 參考網路

# 解題邏輯: 
# 透過find尋找最左邊符合當前字母的索引
# rfind尋找最右邊符合當前字母的索引
# 若I (最左邊的索引) 大於-1 -> 則可以找到其中包含哪些值
# 用set()去記好中間包含哪些值，再轉換成len()
# 最後return 總共有幾種可能性

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i+1 : j]))
        return res


# Solution 2 – 參考網路

# 解題邏輯: 
# 與上題同概念，只是用一行程式碼解決問題

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([len(set(s[s.index(c)+1:s.rindex(c)])) for c in set(s)])



# Solution 3 – 參考上述概念後，自己實作

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_counter = Counter(s).keys()
        s_len = len(s) - 1
        counter = 0
        for i in range(len(s_counter)):
            left, right = -1, -1
            for j in range(len(s)):
                if s[j] == s_counter[i] and left < 0:
                    left = j
                if s[s_len - j] == s_counter[i] and right < 0:
                    right = s_len - j
                if left+1 > 0 and right > 0: 
                    break
            if left+1 > 0 and right > 0:
                counter += len(set(s[left+1:right]))
        return counter
