# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# •	Starting with any positive integer, replace the number by the sum of the squares of its digits.
# •	Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# •	Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
 
# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false



#Solution 1 - (參考提示後自己寫)

# 解題邏輯:
# 第一層while loop去判斷是否為1。
# 進入後判斷是否曾經遇過 -> 若是則為cycle -> return False;
# 若無則將目前的n加入visited列表，並且繼續進行。
# 第二層while loop去計算n拆解後的總和。

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = []
        while n!=1:
            if n not in visited:
                visited.append(n)
            else:
                break
            temp = 0
            while n:
                temp += (n%10)**2
                n /= 10
            n = temp
        return n==1


#Solution 2 - 解題邏輯:

# 第一層while loop去判斷是否為1。
# 進入後判斷是否曾經遇過 -> 若是則為cycle -> return False;
# 若無則將目前的n加入visited列表，並且繼續進行。
# 第二層while loop去計算n拆解後的總和。

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = []
        while n!=1:
            if n not in visited:
                visited.append(n)
            else:
                break
            temp = 0
            while n:
                temp += (n%10)**2
                n /= 10
            n = temp
        return n==1


#Solution 3 - (參考網路->hard coded)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_Next(number):
            total = 0
            while number > 0:
                total += (number % 10) ** 2
                number /= 10
            return total
        
        while n!=1 and n not in cycle:
            n = get_Next(n)
        
        return n == 1


#Solution 4 - (參考網路 -> hard coded)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_Next(number):
            total = 0
            while number > 0:
                total += (number % 10) ** 2
                number /= 10
            return total
        
        while n!=1 and n!=4:
            n = get_Next(n)
        
        return n == 1
