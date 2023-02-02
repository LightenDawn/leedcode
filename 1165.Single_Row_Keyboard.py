# There is a special keyboard with all keys in a single row.
# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.
# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

# Example 1:
# Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
# Output: 4
# Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
# Total time = 2 + 1 + 1 = 4. 

# Example 2: 
# Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode" 
# Output: 73


#Solution 1 

# 解題邏輯: 
# 先創建一個字典，並且將keyboard的值分別keying進去個別的值。
# 創建一個要回傳的值和儲存的位置(save)。
# 用for loop去跑word的每個字元，並且從new_dict中獲取他的索引值。
# 透過save儲存上一輪的position，到下輪後用new_dict[i]-pos獲取當前的索引值，再用絕對值變成正號，加總於count中，最後回傳。

class Solution:
  def CalculateTime(self, keyboard, word):
    new_dict = {}
    for i in range(len(keyboard)):
      new_dict[keyboard[i]] = i
    count = 0
    save = 0
    for i in word:
      if save == 0:
        save = new_dict[i]
        count += save 
        continue
      else:
        count += abs(new_dict[i] - save)
        save = new_dict[i]
    return count
    
s = Solution()
print(s.CalculateTime("pqrstuvwxyzabcdefghijklmno","leetcode"))


#Solution 2 - 參考網路

# 首先用先前學到的enumerate()，分別把keyboard的index值和value值分別出來存進new_dict{}中。
# 再用本輪索引值 – 上輪索引值的絕對值，加總於count中，再儲存本輪索引值到pos中，最後回傳count。

class Solution:
  def CalculateTime(self, keyboard, word):
    new_dict = {}
    for value, key in enumerate(keyboard):
      new_dict[key] = value
    count = 0
    pos = 0
    for i in word:
      count += abs(new_dict[i] - pos)
      pos = new_dict[i]
    return count

s = Solution()
print(s.CalculateTime("pqrstuvwxyzabcdefghijklmno","hello"))
