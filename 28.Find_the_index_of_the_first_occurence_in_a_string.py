# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        n_length = len(needle)
        for i in range(len(haystack)):
            # 查找 i to i+n_length的值是否符合needle
            if haystack[i:i+n_length] == needle:
                return i
        return -1



#Solution 2
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


#Solution 3
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 若needle為空或長度大於haystack
        if not needle or len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            for j in range(len(needle)):
                # 判斷是否會index out of range
                if i+j+1 > len(haystack):
                    return -1
                # 從第i+j點判斷是否與needle的內容相同
                if haystack[i+j] == needle[j]:
                    if j+1 == len(needle):
                        return i
                else:
                    break
        return -1
