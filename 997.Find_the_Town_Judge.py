# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# 1.	The town judge trusts nobody.
# 2.	Everybody (except for the town judge) trusts the town judge.
# 3.	There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
 
# Example 1:
# Input: n = 2, trust = [[1,2]]
# Output: 2

# Example 2:
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1



#Solution 1 

# 解題邏輯: 
# 先建立一個list儲存城市的居民有哪些人(例如: n=4, [1,2,3,4])
# 透過該list去尋找誰是城市的審判者，若是trust[0]中有出現過的，則不為審判者。(例如: n=3, trust = [[1,3],[2,3]], 審判者可能為 3)
# 若是list儲存的審判者為0或是大於1個審判者，則回傳-1。
# 再建立一個dict去判定哪些人有信任過別人(沒有信任過的為審判者)，審判者不相信任何人。

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        new_l = [i+1 for i in range(n)]
        for i in trust:
            if i[0] in new_l:
                new_l.remove(i[0])
        if (len(new_l) > 1) or (len(new_l) == 0): 
            return -1
        new_dict = {}
        for i in range(1,n+1):
            new_dict[i] = False
        for i in trust:
            if i[-1] == new_l[0]:
                new_dict[i[0]] = True
        for key, value in new_dict.items():
            if key != new_l[0]:
                if value != True: return -1
        return new_l[0]


#Solution 2 - (參考網路)

# Intuition:
# Consider trust as a graph, all pairs are directed edge.
# The point with in-degree - out-degree = N - 1 become the judge.
# Explanation:
# Count the degree, and check at the end.
# Time Complexity:
# Time O(T + N), space O(N)

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        count = [0] * (n+1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, n+1):
            if count[i] == n-1:
                return i
        return -1
