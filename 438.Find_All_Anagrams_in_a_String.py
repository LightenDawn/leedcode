# 438. Find All Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 
# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


# Failure - 原先想使用permutation去跑p的排列組合，再進行判斷
#           結果會run-time error => 若p的元素過多則會超出運算時間


from collections import Counter

# Solution 1 – (參考網路)

# 解題邏輯: 
# 使用Counter()將指定的字串進行判定是否相等，相等則回傳當前索引值
# 將myDictS[i]-1之後pop掉，引入下一個值

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        myDictP= Counter(p)
        myDictS= Counter(s[:len(p)])
        output=[]
        i=0
        j=len(p)
        
        while j<=len(s):
            if myDictS==myDictP:
                output.append(i)

            myDictS[s[i]]-=1
            if myDictS[s[i]]<=0:
                myDictS.pop(s[i])
            
            if j<len(s):    
                 myDictS[s[j]]+=1
            j+=1
            i+=1
            
        return output  


# Solution 2 – (參考網路)

# 解題邏輯:
# 使用sliding window
# 而 Sliding Window 的 pattern 常用 window 內的所有 element 來解題，例如透過每回合操作 window 內的總和，來達到解題的目的。

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        
        p = Counter(p)                    # Convert list of anagram letters to a Counter (hashtable)
        ans = []
           
        window = None
        for i in range(0,n-m+1):
            if i == 0: 
                window = Counter(s[:m])   # Initialize window with beginning of s => length = length of anagram letters
            else:    
                window[s[i-1]] -= 1       # Move window to right: 1. remove character on the left
                window[s[i+m-1]] += 1     #                       2. add character on the right
            # len(window – p) => 相減元素，若相減玩還有元素存在，則不進入以下判斷式
            if len(window - p) == 0:      # Check if window is anagram (direct comparison of counters does not work with 0 entries)
                ans.append(i)
                
        return ans

