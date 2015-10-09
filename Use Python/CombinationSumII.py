class Solution(object):
	"""docstring for Solution"""

	def combinationSum2(self, candidates, target):
		candidates.sort()
		print(candidates)
		self.used = [False for i in range(len(candidates))]

		results = []
		self.helper(candidates, 0, target, [], 0, results)

		print(results)
		return results

	def helper(self, candidates, sum, target, item, index, results):

		if sum == target:
			results.append(list(item))
			return

		for i in range(index, len(candidates)):
			if (i==index or candidates[i-1]!=candidates[i]) and sum+candidates[i]<=target:
				sum += candidates[i]
				item.append(candidates[i])

				self.helper(candidates, sum, target, item, i+1, results)

				sum -= candidates[i]
				item.pop()


nums = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
solution = Solution()
solution.combinationSum2(nums, 27)
		