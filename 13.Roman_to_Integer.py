# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


#Solution 1
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 建立羅馬數字表
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # 建立額外情況的list
        another = ["IV", "IX", "XL", "XC", "CD", "CM"]
        current = 0
        total = 0
        while current < len(s):
            # 若沒有current < len(s) - 1會出現index out of range
            if current < len(s)-1 and s[current] + s[current+1] in another:
                # total加總 大值-小值
                total += roman[s[current+1]] - roman[s[current]]
                # 一次用兩個value，因此current + 2
                current += 2
            else:
                total += roman[s[current]]
                current += 1
        return total

solution = Solution()
solution.romanToInt("III")
solution.romanToInt("LVIII")
solution.romanToInt("MCMXCIV")


#Solution 2
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s)):
            # 判斷若下個羅馬數字大於當前的羅馬數字 ex: IX
            if i < len(s)-1 and roman[s[i]] < roman[s[i+1]]:
                # 先減去當前的羅馬數字 total -= 1
                total -= roman[s[i]]
            else:
                # 加總在roman{}裡面的羅馬數字 total += 10
                total += roman[s[i]]
        return total

solution = Solution()
solution.romanToInt("III")
solution.romanToInt("LVIII")
solution.romanToInt("MCMXCIV")


# Solution 3 - 參考網路
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # 直接用取代的方式暴力破解
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        total = 0
        for i in s:
            total += roman[i]
        return total

solution = Solution()
solution.romanToInt("III")
solution.romanToInt("LVIII")
solution.romanToInt("MCMXCIV")