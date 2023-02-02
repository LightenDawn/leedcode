# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
# •	'a' maps to ".-",
# •	'b' maps to "-...",
# •	'c' maps to "-.-.", and so on.
# •	
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# •	For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.
 
# Example 1:
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".

# Example 2:
# Input: words = ["a"]
# Output: 1


#Solution 1 

# 首先先建立一個空字典，並且用words儲存題目需要的摩斯密碼，再用for loop把chr(97)->a對應的英文字母:摩斯密碼進行配對鍵與值。
# 當字典建立完畢後，可以進行題目的摩斯加密，將words的每一個單字給分別抓出來，然後建立一個空字串，再用一個for loop把單字的每個字元加密，並且回加到空字串中，當第二個for loop跑完後，一個單字的加密即完成，最後將加密字元加到new_words中。

# 最後要判斷摩斯加密後是否有重複的單位，所以用for loop去尋找是否有重複的值，若是有則跳過，若無則count += 1。
# 因此，每個要找的值 -> 若從0開始，必須判斷1~列表最後是否有重複的值。

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trans = {}
        password = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        new_words = []
        for i in range(26):
            trans[chr(97 + i)] = password[i]
        for i in range(len(words)):
            new_str = ""
            for w in range(len(words[i])):
                new_str += trans[words[i][w]]
            new_words.append(new_str)
        count = 0
        for i in range(len(new_words)):
            if new_words[i] in new_words[i+1:]:
                continue
            else:
                count += 1
        return count


#Solution 2 - 參考網路
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        password = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = {"".join(password[ord(c) - ord('a')] for c in word) for word in words}
        return len(seen)


#Solution 3 - 參考上題並且改良

# 減少創建dict的空間。

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        password = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        new_word = []
        for word in words:
            new_str = ""
            for c in word:
                new_str += password[ord(c) - ord('a')]
            new_word.append(new_str)
        count = 0
        for i in range(len(new_word)):
            if new_word[i] in new_word[i+1:]:
                continue
            count += 1
        return count


#Solution 4 - 再次改良

# 解題邏輯: 
# 把計算長度的地方改良 -> 用set()的方式簡短攏長的程式碼。

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        password = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        new_word = []
        for word in words:
            new_str = ""
            for c in word:
                new_str += password[ord(c) - ord('a')]
            new_word.append(new_str)
        
        return len(set(new_word))
