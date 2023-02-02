# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
 
# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537


#Solution 1 

# 解題邏輯:
# 先前有使用遞迴方式，由於題目給的標準數字最多可達37的長度，因此用遞迴會超時，因此用紀錄的方式去計算第n個的值。

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        new_temp = [0] * 38
        count = 0
        while count <= n:
            if count == 0: new_temp[count] = 0
            if count == 1 or count == 2: new_temp[count] = 1
            if count > 2:
                new_temp[count] = new_temp[count-1] + new_temp[count-2] + new_temp[count-3]
            count += 1
        return new_temp[n]
# [0*38]
# [0,1,0*36]
# [0,1,1,0*35]
# [0,1,1,2,0*34]以此類推


#Solution 2 - (參考網路)

# 解題邏輯: 
# 超帥

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0, 1, 1]
        for i in range(3, n+1):
            res[i%3] = sum(res)
        return res[n%3]



#Solution 3 - (參考網路)

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 181997601, 334745777, 615693474, 1132436852, 2082876103]
        return nums[n]


#Solution 4 - (參考網路)

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b, c = 1, 0, 0
        for _ in range(n): 
            a, b, c = b, c, a+b+c
        return c
