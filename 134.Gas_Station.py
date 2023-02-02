# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
 
# Example 1:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

# Example 2:
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.


#Solution 1 - (參考網路上)

# 解題邏輯: 
# 條件
# 1.	從當前汽油站所加的油，扣去到下個加油站花費的油要大於等於0
# 2.	要能完成一個循環

# 例如: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 從index = 3出發
# Gas[3] = 4 – cost[3] = 1 = 3
# Gas[4] = 5 – cost[4] = 2 + 3(上一輪剩的油) = 6
# Gas[0] = 1 – cost[0] = 3 + 6 = 4
# Gas[1] = 2 – cost[1] = 4 + 4 = 2
# Gas[2] = 3 – cost[2] = 5 + 2 = 0
# 最後剩下的油>=0，因此可以從gas[3]出發 return 3

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        index = 0
        balance, rent = 0, 0

        for i in range(len(gas)):
            if cost[i] > gas[i]+balance:
                rent += -(cost[i]-(gas[i]+balance))
                balance = 0
                index = i + 1
                continue
            else:
                balance += gas[i]-cost[i]
        return index if rent+balance >=0 else -1


#Solution 2 - (參考網路上的)

# 因為此題有唯一解，因此只要找出最後一個符合情況的答案，即為解答。

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, total, tank = 0, 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i+1
                total += tank
                tank = 0
        return -1 if total+tank < 0 else start


#Solution 3 - (參考網路)

class Solution:
    def canCompleteCircuit(self, gas, cost):
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start