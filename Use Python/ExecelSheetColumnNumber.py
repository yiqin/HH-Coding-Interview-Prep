class Solution(object):
	"""docstring for Solution"""
	def titleToNumber(self, s):
		n = len(s)

		result = 0

		for i in range(n):
			c = s[n-1-i]
			val = self.getValue(c)

			result += val * (26**(i))

		return result
			# print(result)

	def getValue(self, c):
		return ord(c) - ord('A')+1



solution = Solution()
solution.titleToNumber("AB")