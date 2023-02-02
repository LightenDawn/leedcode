# A string is a valid parentheses string (denoted VPS) if it meets one of the following:
# •	It is an empty string "", or a single character not equal to "(" or ")",
# •	It can be written as AB (A concatenated with B), where A and B are VPS's, or
# •	It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:
# •	depth("") = 0
# •	depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
# •	depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
# •	depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.
# Given a VPS represented as string s, return the nesting depth of s.
 
# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:
# Input: s = "(1)+((2))+(((3)))"
# Output: 3


#Solution 1 

# 解題邏輯: 
# 直接用max()存取最大值

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        res = 0
        for i in s:
            if i == "(":
                counter += 1
                res = max(res, counter)
            if i == ")":
                counter -= 1
        return res


#Solution 2 - (參考)

# 解題邏輯: 
# 使用stack的特性(LIFO)，後進先出。

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        depth = 0
        max_depth = 0
        for i in s:
            if i == "(":
                stack.append(i)
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            if i == ")":
                if stack[len(stack) - 1] == "(":
                    stack.pop()
                    depth -= 1
        return max_depth

# s = "(1+(2*3)+((8)/4))+1"
# stack = [(, (] -> “)” depth = 2, max_depth = 2
# stack = [(] -> depth = 1, max_depth = 2
# stack = [(, (, (] -> “)” depth = 3, max_depth = 3
# stack = [(, (] -> depth = 2, max_depth = 3
# stack = [(] -> depth = 1, max_depth = 3
# return max_depth = 3


#Solution 3 - (參考)

# 大同小異

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        tmp=0
        for i in s:
            if (i=='('):
                tmp+=1
                ans=max(ans,tmp)
            elif(i==')'):
                tmp-=1
                ans=max(ans,tmp)
        return ans


#Solution 4 

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter, result = 0, 0
        for ch in s:
            if ch == "(":
                counter += 1
            elif ch == ")":
                counter -= 1
            
            result = max(counter, result)
        
        return result
