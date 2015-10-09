class Solution(object):
	"""docstring for Solution"""
	def rob(self, nums):
		results = [0 for i in range(len(nums))]
		if len(nums) == 0:
			return 0
		results[0] = nums[0]

		if len(nums) == 1:
			return nums[0]

		if len(nums) == 2:
			return max(nums[0], nums[1])

		results[1] = max(nums[0], nums[1])

		for i in range(2, len(nums)):
			results[i] = max(results[i-2]+nums[i], results[i-1])

		print(results)
		
		return results[len(results)-1]


nums = [2, 1, 1, 2]
solution = Solution()
solution.rob(nums)