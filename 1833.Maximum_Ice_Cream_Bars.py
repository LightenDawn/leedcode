# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 
# Return the maximum number of ice cream bars the boy can buy with coins coins.
# Note: The boy can buy the ice cream bars in any order.
 
# Example 1:
# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

# Example 2:
# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.

# Example 3:
# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

import bisect

#Solution 1 

# 解題邏輯: 
# 題目是要求自身coins有多少可以買多少個冰淇淋，因此要求冰淇淋加總後，小於coins的值，即為回傳的答案。

# 例如: [1,3,2,4,1] -> 1+1+2+3 <= 7 所以應該回傳4個冰淇淋

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs = sorted(costs)
        for i in range(1, len(costs)):
            costs[i] += costs[i-1]
        counter = 0
        for i in costs:
            if i > coins:
                return counter
            else:
                counter += 1
        if counter:
            return counter
        return 0


#Solution 2

# 解題邏輯: 
# 用單純相加的方式去做判斷，因此，判斷式會稍微複雜一點。

# 條件: 
# 1.	Coins(總金額)應該大於cost[i]的花費
# 2.	Coins(總金額)應該大於等於sum + cost[i]的花費
# 3.	Coins(總金額)應大於sums值 -> 不必要

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        if not costs: return 0
        costs = sorted(costs)
        summer = 0
        counter = 0
        for i in costs:
            if coins > i and summer+i <= coins:
                summer += i
                counter += 1
            else:
                return counter
        return counter


#Solution 3 - (使用bisect)

# 解題邏輯: 
# 配合第一個解決方案的應用，當序列加總後，coins可以尋找他在costs中的位置，當找到後應為在右方。

# 例如: [1,3,2,4,1] -> [1,2,4,7,11] -> coins = 7 -> 使用bisect_bisect_right後，找到的位置為index = 4 [1,2,4,7,7,11]
# 若使用bisect_bisect_left -> [1,2,4,7,7,11] 會return index = 3

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        if not costs: return 0
        costs = sorted(costs)
        for i in range(1, len(costs)):
            costs[i] += costs[i-1]
        find_pos = bisect.bisect_right(costs, coins)
        if find_pos == 0: return 0
        return find_pos


#Solution 4

# 解題邏輯: 
# 回傳值用新列表的長度進行判斷，若是沒有能買的冰淇淋回傳0，其餘回傳len(new_arr)。

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        if not coins: return 0
        costs = sorted(costs)
        new_arr = []
        for i in range(len(costs)):
            if costs[i] < coins and not new_arr:
                new_arr.append(costs[i])
            elif costs[i] < coins and new_arr[-1] + costs[i] <= coins:
                new_arr.append(new_arr[-1] + costs[i])
        return len(new_arr)


#Solution 5 - (參考後自己寫)

# 解題邏輯: 
# 直接判斷是否小於目前金額，若是則總金額扣掉冰淇淋金額，繼續判斷。

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs = sorted(costs)
        counter = 0
        for i in costs:
            if i <= coins:
                counter += 1
                coins -= i
        return counter


#Solution 6 - (參考網路上)

# 解題邏輯: 
# 此為python3的解法，其中 := 為賦值，須注意的地方。

class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        return sum(1 for ice in sorted(costs) if (coins:= coins-ice) >= 0)
# 邏輯 -> 如果(總金額 := 總金額 – 冰淇淋的錢) >= 0 則加總次數+1
