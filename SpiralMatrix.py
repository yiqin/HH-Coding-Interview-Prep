class Solution(object):
	"""docstring for Solution"""
	def spiralOrder(self, matrix):

		# print(matrix[0][1])
		
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return []

		m = len(matrix)
		n = len(matrix[0])
		marked = [[True for i in range(n)] for j in range(m)]
		# print(marked)
		result = []

		x = 0
		y = 0

		def addResult():
			result.append(matrix[x][y])
			marked[x][y] = False

		addResult()

		direction = 0
		
		# modular
		# 0 right
		# 1 down
		# 2 right
		# 3 up

		while True:
			

			# print(x, y)
			if direction%4 == 0:
				if y+1 < m and marked[x][y+1]:
					y = y+1
					addResult()
					continue
				else:
					direction += 1
					print(direction)

			elif direction%4 == 1:
				if x+1 < n and marked[x+1][y]:
					x = x + 1
					addResult()
					continue
				else:
					direction += 1

			elif direction%4 == 2:
				if y-1 >= 0 and marked[x][y-1]:
					y = y - 1
					addResult()
					continue
				else:
					direction += 1

			else:
				if x-1 >= 0 and marked[x-1][y]:
					x = x - 1
					addResult()
					continue
				else:
					direction += 1

			# print("This is a break")
			# break
			if len(result) == (m-1)*(n-1):
				break

		print(result)

		return result

# [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

solution = Solution()
solution.spiralOrder(matrix)