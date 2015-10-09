class Solution(object):
	"""docstring for Solution"""
	def climbStairs(self, n):
		result = [ 0 for i in range(n+1)]

		for i in range(0, n+1):
			if i == 0:
				result[0] = 0
			if i == 1:
				result[1] = 1
			if i == 2:
				result[2] = 2
			if i > 2:
				result[i] = result[i-1] + result[i-2]

		return result[n]

solution = Solution()
result = solution.climbStairs(7)
print(result)