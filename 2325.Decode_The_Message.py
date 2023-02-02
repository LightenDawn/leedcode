# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.

 
# Example 1:

# Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
# Output: "this is a secret"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

# Example 2:

# Input: key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
# Output: "the five boxing wizards jump quickly"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".


#Solution 1
class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        new_dict = {}
        # ASCII code 97 => 'a'
        counter = 97
        for i in key:
            if i == " ":
                continue
            else:
                # 若該值已存在則略過
                if i in new_dict:
                    continue
                # 字典增加key = i, value = Ascii(counter)
                new_dict[i] = str(chr(counter))
            counter += 1
        new_str = ""
        # 解碼
        for i in message:
            if i == " ":
                new_str += i
            else:
                new_str += new_dict[i]
        return new_str


#Solution 2 - 參考網路
# Mapping => 類似於dict的說法，利用hash表的方式(鍵 key: 值 value)，進行查找的動作。
# 首先，建立mapping的字典依序儲存key對應的值，這邊先建立的a-z的字串，用for-loop進行配對。
# 最後在用for-loop的方式將message對應的值融進字串中，回傳解答。
class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1
        
        for char in message:
            res += mapping[char]
                
        return res


#Solution 3
#與前題類似，更精簡化
class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        hashT = {' ': ' '}
        i=97
        for k in key:
            if k not in hashT and k is not ' ':
                hashT[k] = chr(i)
                i+=1
        return "".join(hashT[m] for m in message)


#Solution 4
class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        # 判斷是否曾經拜訪過
        seen = set()
        cipher = {}
        i = 0
        for c in key:
            # 如果c尚未拜訪且不為空格
            if c not in seen and c.isalpha():
                cipher[c] = chr(ord('a') + i)
                i += 1
                # 拜訪過c，因此加入seen
                seen.add(c)
        return "".join([cipher.get(c, c) for c in message])