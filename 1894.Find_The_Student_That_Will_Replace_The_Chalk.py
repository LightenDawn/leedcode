# There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. After that, the teacher will restart the process, starting with the student number 0 again.
# You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to replace the chalk.
# Return the index of the student that will replace the chalk.
 
# Example 1:
# Input: chalk = [5,1,5], k = 22
# Output: 0
# Explanation: The students go in turns as follows:
# - Student number 0 uses 5 chalk, so k = 17.
# - Student number 1 uses 1 chalk, so k = 16.
# - Student number 2 uses 5 chalk, so k = 11.
# - Student number 0 uses 5 chalk, so k = 6.
# - Student number 1 uses 1 chalk, so k = 5.
# - Student number 2 uses 5 chalk, so k = 0.
# Student number 0 does not have enough chalk, so they will have to replace it.

# Example 2:
# Input: chalk = [3,4,1,2], k = 25
# Output: 1
# Explanation: The students go in turns as follows:
# - Student number 0 uses 3 chalk so k = 22.
# - Student number 1 uses 4 chalk so k = 18.
# - Student number 2 uses 1 chalk so k = 17.
# - Student number 3 uses 2 chalk so k = 15.
# - Student number 0 uses 3 chalk so k = 12.
# - Student number 1 uses 4 chalk so k = 8.
# - Student number 2 uses 1 chalk so k = 7.
# - Student number 3 uses 2 chalk so k = 5.
# - Student number 0 uses 3 chalk so k = 2.
# Student number 1 does not have enough chalk, so they will have to replace it.

import bisect
from collections import accumulate

#Solution 1 

# 解題邏輯: 
# 先加總chalk的和，再用temp去暫存k%total的總和 -> 若是整除則為第0人，若是無則需要用for loop一個一個遍歷搜尋。

class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(chalk)
        temp = k%total
        if temp == 0:
            return 0
        for i in range(len(chalk)):
            temp = temp - chalk[i]
            if temp < 0:
                return i


#Solution 2 - (參考運算最佳解)

# 解題邏輯: 
# 編寫方式比我的簡潔有力，不用多新增變數去儲存k除以chalk總和的數，直接用k本身去儲存就好 -> 空間使用程度比我低。
# 用enumerate()去將索引和值分別給ind和val，透過if去判斷是否為該學生，否則繼續找下去。

class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        k %= sum(chalk)
        for ind, val in enumerate(chalk):
            if k < val:
                return ind
            k -= val
        if k == 0: return 0


#Solution 3 - (參考一行解題)

# 解題邏輯: 
# 使用之前學過的二分搜尋法bisect()。

# Original方法 -> compile沒成功
class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        return bisect.bisect(list(accumulate(chalk)), k % sum(chalk))
# 使用bisect.bisect() -> 預設是找尋目標值的右側 -> bisect_right()
# 目標列表先用累加accumulate()，把粉筆數依序加總。
# 例如: [1, 2, 3, 4] -> [1, 3, 6, 10]
# 然後弄出要找尋的目標值, k % sum(chalk)



#Solution 4
# Improve方法 -> Compile成功
class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(1, len(chalk)):
            chalk[i] += chalk[i-1]
        return bisect.bisect(list(chalk), k % chalk[-1])
# 使用之前學習到的方式(累加)，從序列[1]開始累加起。

# 重點: 
# k %= sum(chalk) 和 k = k % sum(chalk)功能類似，但有些許差異。
# 若是sum(chalk)加總的值太過龐大，會轉成long int變數，因此會造成以下情況。

# (int) k = (int) k % (ol) sum(chalk) -> 會出現error message
# ol -> long int

# 而用%= /= -= += 則會出現以下情況
# (int) k = (int) (k % (long) sum(chalk)) -> 把sum(chalk)也變回int變數
