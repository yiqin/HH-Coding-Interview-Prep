class Solution(object):
	"""docstring for Solution"""
	def summaryRanges(self, nums):

		if len(nums) == 0 or nums == None:
			return []

		# Make sure we have at least one elements

		results = []

		n = len(nums)
		
		p1 = nums[0]
		p2 = nums[0]

		for i in range(1, n):
			if nums[i] == p2 + 1:
				p2 = nums[i]
			else:
				if p1 == p2:
					results.append(str(p1))
				else:
					results.append(str(p1)+"->"+str(p2))

				p1 = nums[i]
				p2 = nums[i]

		if p1 == p2:
			results.append(str(p1))
		else:
			results.append(str(p1)+"->"+str(p2))

		# print(results)

		return results

nums = [0, 1, 2, 4, 5, 7]
solution = Solution()
solution.summaryRanges(nums)
		