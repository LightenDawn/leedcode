# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

# Example 1:
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"

# Example 2:
# Input: "aeiou"
# Output: ""


#Solution 1
class Solution(object):
	def rem_vowel(self, string):
		"""
        :type string: string
        :rtype: string
        """
		vowels = ['a', 'e', 'i', 'o', 'u']
		new_str = ""
		for i in range(string):
			if i in vowels:
				continue
			else:
				new_str += i
		return new_str

s = Solution()
print(s.rem_vowel("GeeksforGeeks - A Computer Science Portal for Geeks"))


#Solution 2
class Solution(object):
  def rem_vowel(string):
      vowels = ['a','e','i','o','u']
      result = [letter for letter in string if letter.lower() not in vowels]
      result = ''.join(result)
      return result
