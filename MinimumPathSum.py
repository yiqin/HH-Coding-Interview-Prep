class Solution(object):
	"""docstring for Solution"""
	def minPathSum(self, grid):
		# print(grid)
		m = len(grid)
		if m == 0:
			return 0
		n = len(grid[0])

		# define the matrix
		result = [[0 for i in range(n)] for j in range(m)]

		for i in range(m):
			if i == 0:
				result[i][0] = grid[i][0]
			else:
				result[i][0] = grid[i][0] + result[i-1][0]

		for i in range(n):
			if i == 0:
				result[0][i] = grid[0][i]
			else:
				result[0][i] = grid[0][i] + result[0][i-1]

		for i in range(1, m):
			for j in range(1, n):
				result[i][j] = min(result[i-1][j], result[i][j-1])+grid[i][j]


		# print(result)
		return result[m-1][n-1]


grid = [[1, 2, 3, 4, 5],
		[1, 1, 1, 1, 1],
		[2, 1, 2, 3, 4],
		[4, 2, 6, 2, 1]]

solution = Solution()
solution.minPathSum(grid)