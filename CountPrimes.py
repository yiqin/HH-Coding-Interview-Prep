import math

class Solution(object):
	def countPrimes(self, n):
		if n <= 0:
			return 0

		results = 1

		checked = [False for i in range(n+1)]
		
		checked[0] = True
		checked[1] = True


		for i in range(3, n+1, 2):
			if not checked[i]:
				if self.isPrimes(i):
					results += 1

				for j in range(i+i, n+1, i):
					if not checked[i]:
						checked[j] = True

		return results

	def isPrimes(self, n):
		for i in range(3, int(math.sqrt(n)+1), 2):
			if n%i == 0:
				return False

		return True


solution = Solution()
result = solution.countPrimes(999983)

# print(result)
		