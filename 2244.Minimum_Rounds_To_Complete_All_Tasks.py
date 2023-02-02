# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.
# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
 
# Example 1:
# Input: tasks = [2,2,3,3,2,4,4,4,4,4]
# Output: 4
# Explanation: To complete all the tasks, a possible plan is:
# - In the first round, you complete 3 tasks of difficulty level 2. 
# - In the second round, you complete 2 tasks of difficulty level 3. 
# - In the third round, you complete 3 tasks of difficulty level 4. 
# - In the fourth round, you complete 2 tasks of difficulty level 4.  
# It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.

# Example 2:
# Input: tasks = [2,3,3]
# Output: -1
# Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.

from collections import Counter
from math import ceil

#Solution 1 - 參考網路

# tasks = [2,2,3,3,2,4,4,4,4,4] -> tasks = Counter(tasks) -> tasks = Counter({4: 5, 2: 3, 3: 2}) -> Counter({key: value})

# 只需要透過tasks的value去抓值，就可以判斷後續所需的回合數。
# dict.values() -> 抓出字典中所有的值

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        tasks = Counter(tasks)
        counter = 0
        for value in tasks.values():
            if value == 1:
                return -1
            if value == 2:
                counter += 1
            if value == 3:
                counter += 1
            if value > 3:
                counter += (value + 2) // 3
        return counter


#Solution 2 - (參考網路上)

# 解題邏輯: 
# 用最純樸的方式硬幹。
# 首先建立一個dict去儲存tasks中每個數字出現的次數。

# 再透過for loop去抓取dict中的key和value，用value值去判斷回合加總的次數，最後return。

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        num_dict = {}

        for t in tasks:
            if t not in num_dict:
                num_dict[t] = 0
            
            num_dict[t] += 1
        
        res = 0
        for key, val in num_dict.items():
            if val == 1:
                return -1
            elif val == 2 or val == 3:
                res += 1
            else:
                rem = val%3
                if rem == 0:
                    res += val//3
                elif rem == 1:
                    res += ((val//3 - 1) + 2)
                else:
                    res += (val//3 + 1)
        
        return res


#Solution 3 - (參考網路上)

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        dict_ = {}
        for task in tasks:
            if task in dict_:
                dict_[task] += 1
            else:
                dict_[task] = 1

        ret = 0
        for x in dict_.keys():
            if dict_[x] == 1:
                return -1
            tmp = ceil(dict_[x]/float(3))
		   #ceil() -> 大於等於該值
            ret = ret + tmp

        return int(ret)

#Solution 4 - class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        task_map = Counter(tasks)
        rounds = 0
        for count in task_map.values():
            if count == 1:
                return -1
            rounds += count // 3 + min(1, count % 3)

        return rounds
