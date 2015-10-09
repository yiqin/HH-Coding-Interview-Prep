class Solution(object):
	def permute(self, nums):
		print(nums)
		used = [False for i in range(len(nums))]
		results = []

		self.dfs(nums, used, [], results)
		return results

	def dfs(self, nums, used, items, results):
		if len(items) == len(nums):
			results.append(list(items))
			return

		for i in range(len(nums)):
			if not used[i]:
				used[i] = True
				items.append(nums[i])
				self.dfs(nums, used, items, results)
				used[i] = False
				items.pop()


nums = [1, 2, 3]
solution = Solution()
solution.permute(nums)