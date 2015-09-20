class Solution(object):
	def rotate(self, matrix):
		# print(matrix)
		n = len(matrix)
		#print(n)
		# clockwiseMatrix = [ [0 for i in range(n)] for j in range(n)]
		#print(clockwiseMatrix)
		if n == 1:
			return matrix

		for i in range(n-1):
			for j in range(n-i):
				matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

		for i in range(n/2):
			matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
			

		# print(matrix)

		return matrix


matrix = [[1, 2], [3, 4]]

solution = Solution()
solution.rotate(matrix)