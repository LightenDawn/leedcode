# There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.
# In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.
# The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).
# Return an integer array answer of length 2 where:
# •	answer[0] is the minimum number of moves you can play, and
# •	answer[1] is the maximum number of moves you can play.
 
# Example 1:
# Input: a = 1, b = 2, c = 5
# Output: [1,2]
# Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

# Example 2:
# Input: a = 4, b = 3, c = 2
# Output: [0,0]
# Explanation: We cannot make any moves.

# Example 3:
# Input: a = 3, b = 5, c = 1
# Output: [1,2]
# Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.


#Solution 1 - (參考網路)

# 解題邏輯: 
# 首先找出最大值，並且找出最大值需要移動的步數，而為了計算需先找出最大值與最小值的真空區。

# 例如: a=3, b=5, c=1 -> 真空區為5-1=4 其中可移動的步數 –2 =2 (一個是直接到定位，一個是分次移動到定位)

# 再來找出最小值，最小值最多只能移動兩步，因為最小值可以從頭部或尾部移動到中間值的旁邊，除了以下兩種情況: 
# 1.	只有一個真空區存在於兩個數字之間，例如: 1,3,8，只需要將8直接移動到2變1,2,3，因此只需移動1步。
# 2.	A,b,c原本就是連續值，min則為0

class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        maxi = max(a,b,c) - min(a,b,c) - 2
        mini = max((min(abs(a-b), abs(b-c), abs(a-c), 3)-1), 1)
        if maxi == 0: mini = 0
        return [mini, maxi]
