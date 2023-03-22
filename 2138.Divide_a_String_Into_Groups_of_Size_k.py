# A string s can be partitioned into groups of size k using the following procedure:
# •	The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each character can be a part of exactly one group.
# •	For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
# Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.
# Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.
 
# Example 1:
# Input: s = "abcdefghi", k = 3, fill = "x"
# Output: ["abc","def","ghi"]
# Explanation:
# The first 3 characters "abc" form the first group.
# The next 3 characters "def" form the second group.
# The last 3 characters "ghi" form the third group.
# Since all groups can be completely filled by characters from the string, we do not need to use fill.
# Thus, the groups formed are "abc", "def", and "ghi".

# Example 2:
# Input: s = "abcdefghij", k = 3, fill = "x"
# Output: ["abc","def","ghi","jxx"]
# Explanation:
# Similar to the previous example, we are forming the first three groups "abc", "def", and "ghi".
# For the last group, we can only use the character 'j' from the string. To complete this group, we add 'x' twice.
# Thus, the 4 groups formed are "abc", "def", "ghi", and "jxx".


#Solution 1 (自己寫)

# 解題邏輯: 
# 用while-loop各自將分成k大小的字串存進new_arr中，最後判斷若index+k大於原本字串長度時，需要添增fill的字串內容進去，並且回傳。

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        length = len(s)
        index = 0
        answer = []
        while index < length:
            answer.append(s[index:index+k])
            index += k
            if index > length:
                answer[-1] += (fill * (k-len(answer[-1])))
        return answer
 

#Solution 2 (自己寫)

# 解題邏輯: 與上題大同小異

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        new_arr = []
        new_str = ""
        for i in s:
            if len(new_str) < k:
                new_str += i
            else:
                new_arr.append(new_str)
                new_str = i
        if len(new_str) < k:
            new_arr.append(new_str + (fill * (k-len(new_str))))
        else: new_arr.append(new_str)
        return new_arr
 

#Solution 3 (自己寫)

# 解題邏輯: 將上述的內容總和之後，精簡化。

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        new_arr = []
        length = (len(s) + 2) // k
        for i in range(0, len(s), k):
            new_arr.append(s[i:i+k])
        if len(new_arr[-1]) != k:
            new_arr[-1] += fill * (k-len(new_arr[-1]))
        return new_arr
 

#Solution 4 (自己寫)

# 解題邏輯: 
# 與先前不同，先判斷s字串的長度是否可以整除於k，若不行則將fill加入字串中，使s字串能夠整除於k。
# 再將s字串分割成k個群組存進new_arr中回傳。

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        while (len(s))%k != 0:
            s += fill
        new_arr = []
        for i in range(0, len(s), k):
            new_arr.append(s[i:i+k])
        return new_arr
 

#Solution 5 (參考網路)

# 不同寫法而已

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        l=[]
        if len(s)%k!=0:
            s+=fill*(k-len(s)%k)
        for i in range(0,len(s),k):
            l.append(s[i:i+k])
        return l
 

#Solution 6 (參考網路 -> 運算最佳解)

# 解題邏輯: 
# 利用python的slice特性，縮減s的長度，並且天增進新的array中。
# 最後判斷s的長度是否為0，不為零則要fill字串進去，並添增進array中回傳。

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        amogus=[]
        while len(s)>=k:
            amogus.append(s[:k])
            s=s[k:]
        if len(s)>0:
            x=k-len(s)
            amogus.append(s+x*fill)
        return amogus
 
