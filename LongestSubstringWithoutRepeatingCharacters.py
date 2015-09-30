class Solution(object):
	"""docstring for Solution"""
	def lengthOfLongestSubstring(self, s):
		strSet = set()

		start = 0
		
		longestLength = 0

		for i in range(len(s)):
			if s[i] not in strSet:
				strSet.add(s[i])
				
			else:
				longestLength = max(longestLength, len(strSet))
				while s[start] != s[i]:
					strSet.remove(s[start])
					start += 1
				# update start index
				start += 1


		# print(longestLength)
		return max(longestLength, len(strSet))			


s = "bpfbhmipx"
solution = Solution()
solution.lengthOfLongestSubstring(s)
		