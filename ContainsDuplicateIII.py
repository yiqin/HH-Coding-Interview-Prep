class Solution(object):
	"""docstring for Solution"""
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		nums.sort()
		print(nums)

		numsDict = dict()

		for i in range(len(nums)):
			j = i - k
			if j < 0:
				j == 0
			for jj in range(j, i):
				diff = nums[i] - nums[jj]
				



nums = [50, 1, 3, 9, 12, 20, 30]
solution = Solution()
solution.containsNearbyAlmostDuplicate(nums, 2, 2)