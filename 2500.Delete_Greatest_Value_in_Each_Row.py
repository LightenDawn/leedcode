# You are given an m x n matrix grid consisting of positive integers.
# Perform the following operation until grid becomes empty:
# •	Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
# •	Add the maximum of deleted elements to the answer.
# Note that the number of columns decreases by one after each operation.
# Return the answer after performing the operations described above.
 
# Example 1:
 
# Input: grid = [[1,2,4],[3,3,1]]
# Output: 8
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
# - In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
# - In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
# The final answer = 4 + 3 + 1 = 8.


# Example 2:
 
# Input: grid = [[10]]
# Output: 10
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 10 from the first row. We add 10 to the answer.
# The final answer = 10.


#Solution 1 (自己寫)

# 解題邏輯: 
# 依序刪除2元陣列中的元素，並且每次判斷最大值為何，加總進answer中，最後return。

class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        answer = 0
        while n>0:
            temp = 0
            for i in grid:
                if temp < max(i): temp = max(i)
                i.remove(max(i))
            n = len(grid[0])
            answer += temp
        return answer
 

#Solution 2 (自己寫)

# 解題邏輯: 
# 與上題大同小異，只是用另一種方式呈現。

class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = 0
        n = 0
        answer = 0
        temp = 0
        while n < len(grid[len(grid)-1]):
            temp = max(temp, max(grid[m]))
            grid[m].remove(max(grid[m]))
            m += 1
            if m > len(grid) - 1: 
                m = 0
                answer += temp
                temp = 0
        return answer
 

#Solution 3 (自己寫)

# 解題邏輯: 
# 先將陣列中的每個元素進行排序，再透過從最後一個元素找出最大值加總，直到索引為0為止。

class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        (lambda x: [grid[i].sort() for i in range(x)])(len(grid))
        length = len(grid[-1])
        answer = [0] * length
        while length > 0:
            length -= 1
            for i in grid:
                if i[length] > answer[length]:
                    answer[length] = i[length]
        return sum(answer)
 
