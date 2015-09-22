class Solution(object):
	"""docstring for Solution"""
	def largestNumber(self, nums):

		def my_cmp(x, y):
			sx = str(x)
			sy = str(y)
			s1 = sx + sy
			s2 = sy + sx

			if int(s1) > int(s2):
				return -1
			elif int(s1) == int(s2):
				return 0
			else:
				return 1

		nums = sorted(nums, cmp = my_cmp)

		# print(nums)

		if nums[0] == 0:
			return "0"
		else:
			return "".join([str(n) for n in nums])


nums = [3, 30, 34, 5, 9]
solution = Solution()
result = solution.largestNumber(nums)
print(result)