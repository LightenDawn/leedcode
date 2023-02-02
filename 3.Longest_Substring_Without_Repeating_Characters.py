# Given a string s, find the length of the longest 
# substring
#  without repeating characters.
 
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

from collections import Counter

#Solution 1 

# 解題邏輯: 
# 先判斷字串是否只有一個字母，若是則回傳1。
# 若為空字串則回傳0。
# 接著建立一個空列表和Counter值。
# For loop迴圈跑從0到len(s)-1的值 -> 以免內層迴圈超出列表索引
# 先將字母加入列表中。
# 再判斷s.count(i) == len(s)，若相同則代表此字串只包含1個字母，因此回傳1。
# 再進行for loop第二層迴圈，如果s[j]的字母沒有在列表中出現過，則將s[j]加入列表中，並且將列表的最大長度傳入counter中；若無則清空列表並且跳出回圈。
# 最後回傳Counter值。

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1: return 1
        if s == "": return 0
        new_list = []
        counter = 0
        for i in range(len(s)-1):
            new_list.append(s[i])
            if s.count(s[i]) == len(s):
                return 1
            for j in range(i+1, len(s)):
                if s[j] not in new_list:
                    new_list.append(s[j])
                    counter = max(counter, len(new_list))
                else:
                    new_list = []
                    break
        return counter


#Solution 2 - (參考網路)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


#Solution 3 - (參考網路)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
