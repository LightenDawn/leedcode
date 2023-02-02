# You are given an array of n strings strs, all of the same length.
# The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:
# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
# Return the number of columns that you will delete.
 
# Example 1:
# Input: strs = ["cba","daf","ghi"]
# Output: 1
# Explanation: The grid looks as follows:
#   cba
#   daf
#   ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

# Example 2:
# Input: strs = ["a","b"]
# Output: 0
# Explanation: The grid looks as follows:
#   a
#   b
# Column 0 is the only column and is sorted, so you will not delete any columns.

# Example 3:
# Input: strs = ["zyx","wvu","tsr"]
# Output: 3
# Explanation: The grid looks as follows:
#   zyx
#   wvu
#   tsr
# All 3 columns are not sorted, so you will delete all 3.


#Solution 1

# 解題邏輯: 
# 題目要求把strs中沒有照順序排列的字母給刪除。
# 例如: ["cba","daf","ghi"]
# c  b  a
# d  a  f
# g  h  i
# c -> d -> g 是有照a-z字母排列，因此不刪除
# d -> a -> f 其中d -> a 為錯誤的排序，因此需要刪除
# g -> h -> I 有照a-z字母排列，因此不刪除
# 結果return為 1
# 因此，本題邏輯為strs的每個字串的索引依序漸進，所以我用ord()這個功能進行判斷，strs[0][0] -> strs[1][0] -> strs[2][0]是否ord()的順序是由小至大，是則繼續，否則列入刪除列項之一。

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        length = len(strs[0])
        temp = 0
        for j in range(length):
            for i in range(len(strs)):
                if ord(strs[i][j]) >= temp:
                    temp = ord(strs[i][j])
                    continue
                else:
                    count += 1
                    break
            temp = 0
        return count


#Solution 2 - (參考運算最佳解)

# 解題邏輯: 
# 使用zip()，透過zip()中的 * -> 解壓縮功能，最符合此題的解題邏輯。

# Zip()是將多個list的相對應位置鏈結起來，因此稱為壓縮。
# 如: a = [‘c’, ’d’, ’g’] b = [‘b’, ‘a’, ‘h’] c = [‘a’, ‘f’, ‘I’]
# Zip(a, b, c) => [('c', 'b', 'a'), ('d', 'a', 'f'), ('g', 'h', 'i')]

# Zip(*)則為解壓縮的功能。
# 如: a = [('c', 'b', 'a'), ('d', 'a', 'f'), ('g', 'h', 'i')]
# Zip(*a) = ([‘c’, ’d’, ’g’], [‘b’, ‘a’, ‘h’], [‘a’, ‘f’, ‘I’]) 

# 因此透過解壓縮後，用該列去判斷是否有排序過，若無則刪除的列表+1。

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ret = 0
        
        for c in zip(*strs): 
            if list(c) != sorted(c): 
                ret += 1
                
        return ret 


#Solution 3 - (參考空間最佳解)

# 解題邏輯: 
# 與我的方式類似，但是寫得更加淺顯易懂。

class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n, m = len(strs), len(strs[0])
        res = 0
        for i in range(m):
            flg = False
            for j in range(1,n):
                flg = strs[j][i] < strs[j-1][i]
                if flg:
                    break
            if flg:
                res += 1
        return res
