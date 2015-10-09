class Solution(object):
	"""docstring for Solution"""
	def isPowerOfTwo(self, n):
		while n%2 == 0 and n != 0:
			n = n/2
		if n == 1:
			return True
		else:
			return False

solution = Solution()
result = solution.isPowerOfTwo(0)
print(result)