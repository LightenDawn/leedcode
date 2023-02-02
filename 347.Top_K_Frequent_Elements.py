# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import Counter

#Solution 1
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #使用Counter計數nums中的數字各出現幾次
        nums_count = Counter(nums)
        new_list = []
        #most_common([n]) 回傳出現最多次數的n個元素及其出現的次數
        nums_count = nums_count.most_common()
        for i in nums_count:
            if k > 0:
                new_list.append(i[0])
                k -= 1    
        return new_list


solution = Solution()
solution.topKFrequent([1,1,1,2,2,3], 2)
solution.topKFrequent([1], 1)


#Solution 2
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_count = Counter(nums)
        new_list = []
        #使用sorted()實現most_common()
        #sorted(array, get(array[i][0]), 降序)
        nums_count = sorted(nums_count, key=nums_count.get, reverse=True)
        for i in nums_count:
            if k > 0:
                new_list.append(i)
                k -= 1
        return new_list


solution = Solution()
solution.topKFrequent([1,1,1,2,2,3], 2)
solution.topKFrequent([1], 1)


#Solution 3 (參考網路上)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return ([i[0] for i in Counter(nums).most_common(k)])


#Solution 4 (參考網路 - 使用HEAP)
from heapq import heappush, heappop

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {}

        for i in nums:
            #先將各個數字出現的次數儲存到freq_dict中，如先前的Counter
            freq_dict[i] = freq_dict.setdefault(i, 0) + 1
        
        heap = []

        for i in freq_dict:
            #將freq_dict[i]用負數儲存，因為python的heappop是使用min heap
            heappush(heap, (-freq_dict[i], i))
        
        #heap = [(-3,1), (-2,2), (-1,3)]
        
        ans = []
        for i in range(k):
            #從heap找出最小值的value存進ans[]中
            ans.append(heappop(heap)[1])
        
        return ans

solution = Solution()
solution.topKFrequent([1,1,1,2,2,3], 2)
solution.topKFrequent([1], 1)