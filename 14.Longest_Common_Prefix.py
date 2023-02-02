# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


#Solution 1
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 若strs的元素小於2，則直接回傳唯一的元素或空列表
        if len(strs) < 2: return strs[0]
        # 尋找strs中元素的最小長度
        min_len = min([len(i) for i in strs])
        n = 0
        prefix = ""
        # 從第0個index開始找起
        while n < min_len:
            # flag判定strs中元素的當前索引值是否都相同
            flag = True
            # 先暫存當前索引的字串，以便後續判斷
            temp = ""
            for i in strs:
                # 若為空字串，則將當前字串的第n個索引值加到temp中
                if temp == "":
                    temp += i[n]
                # 若temp的暫存值與當前索引的值不相同
                if temp != i[n]: 
                    # 賦予flag False值，並且跳出迴圈
                    flag = False
                    break
            # 若flag == True，則prefix可以增加temp內的值
            if flag:
                prefix += temp
            else: break
            n += 1
        return prefix

solution = Solution()
solution.longestCommonPrefix(["flower","flow","flight"])
solution.longestCommonPrefix(["dog","racecar","car"])


# Solution 2

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 2: return strs[0]
        min_len = min([len(i) for i in strs])
        # 這次想要使用[].append()和[].pop()，相較前次解決問題較簡易
        prefix = []
        n = 0
        while n < min_len:
            for i in strs:
                # 當prefix中的元素小魚等於n時
                if len(prefix) <= n:
                    # 將當前索引的值引入prefix中
                    prefix.append(i[n])
                # 當prefix的值與當前索引值不相符時
                if i[n] != prefix[n]:
                    # 將在prefix的當前索引值給pop()
                    prefix.pop(n)
                    # 用此種方式break while loop
                    n = min_len
                    break
            n += 1
        return ''.join(prefix)
        
solution = Solution()
solution.longestCommonPrefix(["flower","flow","flight"])
solution.longestCommonPrefix(["dog","racecar","car"])