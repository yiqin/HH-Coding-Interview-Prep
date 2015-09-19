class Solution(object):
	"""docstring for Solution"""
	def isPalindrome(self, x):

		string = str(x)

		n = len(string)

		beginning = 0
		ending = n - 1

		while beginning < ending:

			if string[beginning] != string[ending]:
				return False

			beginning += 1
			ending -= 1

		return True

solution = Solution()
result = solution.isPalindrome(123454321)
print(result)