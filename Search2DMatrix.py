class Solution(object):
    def searchMatrix(self, matrix, target):

    	m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m*n -1

        while start <= end:
            mid = (start+end)/2
            midX = mid/n
            midY = mid%n

            if matrix[midX][midY] == target:
                return True

            if matrix[midX][midY] < target:
                start = mid+1
            else:
                end = mid-1

        return False



matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]


solution = Solution()
result = solution.searchMatrix(matrix, 4)
print(result)


