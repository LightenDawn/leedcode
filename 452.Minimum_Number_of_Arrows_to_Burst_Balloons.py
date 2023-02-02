# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
 
# Example 1:
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

# Example 2:
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

# Example 3:
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].


#Solution 1 - (參考版本)

# 解題邏輯: 
# 在points陣列中每個索引為一顆氣球，分別記錄該氣球的起點與終點(大小)
# 例如 : points = [[10,16],[2,8],[1,6],[7,12]] 有四顆氣球
# 此題需要判別要設最少幾隻飛鏢，可以把全部氣球刺破。

# 參考網路上的小撇步，需要以points[x][1] -> end去做判斷
# 會遇到以下情形: 
# [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]] 
# [[6,7][3,9],[6,9],[1,10],[4,11],[8,12],[9,12]] -> 用索引1做排序後之結果
# 先建立一個負無限大的值
# points.sort(key= lambda x: x[1]) -> points = x => x[1] = points[x][1]
# end = float(“-inf”)
# counter = 0
# for a,b in range(len(points)):
# 	if a > end:
# 		counter += 1
# 		end = b
# return counter

# end = -∞ -> if a=6 > end -∞ => end = b = 7 (counter += 1)
# end = 7 -> if a=8 > end=7 => end = b = 12 (counter += 1)
# end = 12

# return 2

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[1])
        count = 0
        end = float("-inf")
        for a, b in points:
            if end < a:
                count += 1
                end = b
        return count



#Solution 2 - (參考網路+自己寫)

# inrange 儲存的值為在範圍內的值，若是有其他索引的start值大於inrange(end)值，代表超出範圍外，需要再多加一支飛鏢才能射破該範圍的氣球。

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[1])
        counter = 1
        inrange = points[0][1]
        for i in range(len(points)):
            if points[i][0] > inrange:
                inrange = points[i][1]
                counter += 1
        return counter
