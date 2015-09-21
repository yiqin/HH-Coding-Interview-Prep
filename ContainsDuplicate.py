class Solution(object):
	"""docstring for Solution"""
	def containsDuplicate(self, nums):
		numsSet = set()
		# print(nums)

		for i in range(len(nums)):
			if nums[i] in numsSet:
				return True
			else:
				numsSet.add(nums[i])

		return False


nums = [1, 2, 3, 4, 5, 6, 1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)