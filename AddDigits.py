class Solution(object):
	def addDigits(self, num):

		sum = 0
		while True:
			print(num)

			modular = num%10
			sum += modular
			num = num/10
			if num == 0 and sum < 10:
				return sum
			elif num == 0:
				num = sum
				sum = 0


solution = Solution()
result = solution.addDigits(38)
print(result)