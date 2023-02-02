# You are given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.
# Return the minimum number of steps to make the given string empty.
# A string is a subsequence of a given string if it is generated by deleting some characters of a given string without changing its order. Note that a subsequence does not necessarily need to be contiguous.
# A string is called palindrome if is one that reads the same backward as well as forward.
 
# Example 1:
# Input: s = "ababa"
# Output: 1
# Explanation: s is already a palindrome, so its entirety can be removed in a single step.

# Example 2:
# Input: s = "abb"
# Output: 2
# Explanation: "abb" -> "bb" -> "". 
# Remove palindromic subsequence "a" then "bb".

# Example 3:
# Input: s = "baabb"
# Output: 2
# Explanation: "baabb" -> "b" -> "". 
# Remove palindromic subsequence "baab" then "b".


#Solution 1 

class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return 1
        else: return 2


#Solution 2 (參考網路)

# You need to know the difference between subarray and subsequence. Subarray need to be consecutive。 (連續的)
# Subsequence don't have to be consecutive。(非連續的)

# Intuition 
# If it's empty sting, return 0; 
# If it's palindrome, return 1; 
# Otherwise, we need at least 2 operation.

# Explanation 
# We can delete all characters 'a' in the 1st operation, and then all characters 'b' in the 2nd operation. 
# So return 2 in this case


class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return 1
        if not s: return 0
        return len(set(s))
