class Solution(object):
	"""docstring for Solution"""
	def maximumGap(self, nums):

		if len(nums) < 2:
			return 0
		nums.sort()

		maximumGap = 0

		for i in range(len(nums)-1):
			tmpGap = nums[i+1] - nums[i]
			if maximumGap < tmpGap:
				maximumGap = tmpGap

		return maximumGap


nums = [2,1,5,1,9]

solution = Solution()
result = solution.maximumGap(nums)

print(result)

		