# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
# A substring is a contiguous sequence of characters within a string
 
# Example 1:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

# Example 2:
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".

# Example 3:
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.


#Solution 1 

# 解題邏輯: 
# 先用列表中的字串長度去做排序。
# 再依序比較[0~len(s)]是否有再[i+1~len(s)]中出現過，若有則新增到空列表中。
# 最後return新建的列表。

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words = sorted(words, key=len)
        new_arr = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    new_arr.append(words[i])
                    break
        return new_arr


#Solution 2 

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words = sorted(words, key=len)
        new_arr = []
        left, right = 0, 1
        while left < len(words)-1:
            if words[left] in words[right]:
                new_arr.append(words[left])
                left += 1
                right = left + 1
                continue
            if right == len(words)-1:
                left += 1
                right = left + 1
            else:
                right += 1
        return new_arr


#Solution 3 - (參考網路)

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        arr = ' '.join(words)
        subStr = [i for i in words if arr.count(i)>=2]
        return subStr


#Solution 4 - (參考網路)

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def add(word):
            node = trie
            for c in word:
                node = node.setdefault(c, {})
                node['#'] = node.get('#', 0) + 1

        def get(word):
            node = trie
            for c in word:
                node = node.get(c)
                if node is None: return False
            return node['#'] > 1

        trie = {}
        for word in words:
            for i in range(len(word)):
                add(word[i:])
        return [word for word in words if get(word)]
