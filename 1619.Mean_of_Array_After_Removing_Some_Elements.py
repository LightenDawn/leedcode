# Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.
# Answers within 10-5 of the actual answer will be considered accepted.
 
# Example 1:
# Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
# Output: 2.00000
# Explanation: After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.

# Example 2:
# Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
# Output: 4.00000

# Example 3:
# Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
# Output: 4.77778

from random import randint

#Solution 1 

# 解題邏輯: 
# 先把題目給的列表/陣列給排序好，再計算5%~95%區間的陣列元素加總除以元素總數的平均值。
# 運用python的slice方法，去計算加總平均(這邊需要用到符點數)，應題目要求。

class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        length = len(arr)
        minR = (length * 5) / 100
        maxR = (length * 95) / 100
        arr = arr[minR:maxR]
        total = float(sum(arr))/float(len(arr))
        return total


#Solution 2 

# 解題邏輯: 
# 與上題邏輯相同，只是運用for loop去計算區間元素的加總，最後做平均計算。

class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        length = len(arr)
        total = 0
        counter = 0
        for i in range(length / 20, length - (length/20)):
            total += arr[i]
            counter += 1
        total = float(total) / float(counter)
        return total



#Solution 3 - (參考網路)

# 解題邏輯: 
# 與第一題相同，運用slice方法。

class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        removeCount = len(arr)//20
        arr = arr[removeCount:len(arr)-removeCount]
        return (sum(arr)/float(len(arr)))


#Solution 4 - (參考網路)

class Solution(object):
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def quickSelect(self, arr, target, lo, hi):
        while lo < hi:
            # We choose a random element in the range to act as a pivot. It
            # doesn't have to be random for the algorithm to work, but it helps
            # avoid the worst case time complexity of O(n^2).
            self.swap(arr, lo, randint(lo, hi))
            a = lo + 1
            b = hi
            
            # move everything smaller than our pivot to the left, and everything
            # larger to the right.
            while a < b:
                while a < b and arr[a] <= arr[lo]:
                    a += 1
                while a < b and arr[b] > arr[lo]:
                    b -= 1
                self.swap(arr, a, b)
            
            # Make sure we are going to place the pivot in the right spot.
            if arr[a] > arr[lo]:
                a -= 1
            self.swap(arr, a, lo)
            
            # Decide whether to go into the left partition or the right
            # partition.
            if a < target:
                lo = a + 1
            else:
                hi = a - 1

    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        n = len(arr)
        delete = n // 20

        # move the small values to the left
        self.quickSelect(arr, delete, 0, n-1)

        # move the large values to the right
        self.quickSelect(arr, n - delete, delete, n - 1)

        # average the rest
        return sum(arr[delete:-delete]) / float(n - 2 * delete)
