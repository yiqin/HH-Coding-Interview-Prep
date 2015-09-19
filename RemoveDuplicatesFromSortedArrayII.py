class Solution(object):
	def removeDuplicates(self, nums):
		# dictionary = {}
		if len(nums) == 0:
			return 0

		result = [nums[0]]
		appearTwice = False
		for i in range(1, len(nums)):
			if nums[i] == nums[i-1]:
				if not appearTwice:
					result.append(nums[i])
				appearTwice = True
			else:
				appearTwice = False
				result.append(nums[i])

		# print(result)
		return len(result)




nums = [1, 1, 1, 2]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)