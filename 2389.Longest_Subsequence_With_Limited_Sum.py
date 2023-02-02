# You are given an integer array nums of length n, and an integer array queries of length m.

# Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:

# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

# Example 2:

# Input: nums = [2,3,4,5], queries = [1]
# Output: [0]
# Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.

import bisect

#Solution 1 - 參考提示後寫的

# 先將nums內的數字依序排列(sorted)，並且將nums內的數字依序用for loop挑出來相加，若是小於queries的數字則一直相加下去，直到序列結束或大於該值。
# 最後將值append進要回傳的列表中，並return回去。

class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        counter = 0
        plus = 0
        answer = []
        for i in range(len(queries)):
            for j in range(len(nums)):
                if plus + nums[j] <= queries[i]:
                    plus += nums[j]
                    counter += 1
                else:
                    answer.append(counter)
                    counter = 0
                    plus = 0
                    break
                if counter == len(nums):
                    answer.append(counter)
                    counter = 0
                    plus = 0
        return answer


#Solution 2

# 先將nums中的數字進行排序，並且用for loop將數字相加。
# 如: [1, 2, 3] => [1, 3, 6] 依序疊加
# 並且運用bisect.bisect_left(a, x, lo=0, hi=len(a), key=None)的功能，該功能會搜尋x列表的數字應當排在a的何處索引。
# 如: nums = [1 ,3, 6] queries = [2] => index = 1 (排在1後面3前面)
# 如: nums = [1, 2, 2, 3, 6] queries = [2] => index = 1 (排在1後面2前面) 若是為bisect.bisect_right()則index = 3

class Solution(object):
    def answerQueries(self, nums, queries):
        nums=sorted(nums)
        answer=[]
        for i in range(1,len(nums)):
            nums[i]+= nums[i-1]
        print(nums)
            
            
        for query in queries:
            index= bisect.bisect_right(nums,query)
            answer.append(index)
               
        return answer


#Solution 3 - 參考網路

# 使用二分搜尋法，降低運算時間。
# 首先找出中位數，若是中位數等於欲尋找的值則直接回傳。
# 若是中位數大於欲尋找地值，則遞迴尋找0~中位數-1。
# 若中位數等於列表的長度或中位數+1大於欲尋找地值，則回傳中位數。
# 否則遞迴尋找中位數+1~len(列表)

class Solution(object):
    
    def binary_search(self, arr, low, high, x):
        if (arr[low] > x):
            return -1
 
        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            
            elif (mid == len(arr) -1) or arr[mid + 1] > x:
                return mid

            # Else the element can only be present in right subarray
            else:
                return self.binary_search(arr, mid + 1, high, x)

        else:
            # Element is not
            if arr[high] > x:
                return high -1
            return high
        

    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums) 
        cur_sum = 0
        sum_arr = []
        for num in nums:
            cur_sum += num
            sum_arr.append(cur_sum)
                        
        out = []
        for query in queries:
            out.append(self.binary_search(sum_arr, 0, len(nums) -1, query) + 1)
            
        return out
