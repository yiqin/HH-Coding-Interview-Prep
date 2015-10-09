class Solution(object):
	"""docstring for Solution"""
	def isUgly(self, num):
		if num == 1:
			return True

		# this is wrong
		while num%2 == 0 and num != 0:
			num = num/2

		while num%3 == 0 and num != 0:
			num = num/3

		while num%5 == 0 and num != 0:
			num = num/5

		if num == 1:
			return True
		else:
			return False

solution = Solution()
result = solution.isUgly(8)
print(result)

