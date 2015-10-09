class Solution(object):
	"""docstring for Solution"""
	def solve(self, board):

		# i
		n = len(board)
		if n == 0:
			return []

		
		# j
		m = len(board[0])
		

		# print(board)
		checkedMatrix = [[-1 for i in range(len(board[0]))] for j in range(len(board))]
		# print(checkedMatrix)

		# store visiting positions
		queue = list()

		aboutToChange = list()

		for i in range(len(board)):
			for j in range(len(board[0])):
				# find the 0
				current = board[i][j]
				if current == "0" and checkedMatrix[i][j] == -1:

					isRegion = True
					queue.append([i, j])
					aboutToChange.append([i,j])

					while len(queue) != 0:
						firstItem = queue[0]
						# 
						queue = queue[1:len(queue)]

						ii = firstItem[0]
						jj = firstItem[1]
						checkedMatrix[ii][jj] = 0

						if ii == 0 or ii == n-1 or jj == 0 or jj == m-1:
							isRegion = False
						# check four items
						if ii-1 >= 0 and checkedMatrix[ii-1][jj] == -1 and board[ii-1][jj] == "0":
							queue.append([ii-1, jj])
							aboutToChange.append([ii-1, jj])
						if ii+1 <= n-1 and checkedMatrix[ii+1][jj] == -1 and board[ii+1][jj] == "0":
							queue.append([ii+1, jj])
							aboutToChange.append([ii+1, jj])
						if jj-1 >= 0 and checkedMatrix[ii][jj-1] == -1 and board[ii][jj-1] == "O":
							queue.append([ii, jj-1])
							aboutToChange.append([ii, jj-1])
						if jj+1 <= m-1 and checkedMatrix[ii][jj+1] == -1 and board[ii][jj+1] == "0":
							queue.append([ii, jj+1])
							aboutToChange.append([ii, jj+1])

					# print("end of queue")
					if isRegion:
						for i in range(len(aboutToChange)):
							aboutToChangeItem = aboutToChange[i]
							# print(aboutToChangeItem)
							board[aboutToChangeItem[0]][aboutToChangeItem[1]] = "X"

					queue = list()
					aboutToChange = list()

		# print(board)





board = [["X", "X", "X", "X"], ["X", "0", "0", "X"], ["X", "X","0","X"],["X","0","X","X"]]

solution = Solution()
solution.solve(board)