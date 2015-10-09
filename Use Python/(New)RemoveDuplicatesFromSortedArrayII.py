class Solution(object):
	"""docstring for Solution"""
	def removeDuplicates(self, nums):
		count = 0
		appearsTime = 0

		for i in range(len(nums)):
			if i == 0:
				appearsTime = 1
				count = 1
			else:
				if nums[i] == nums[i-1]:
					appearsTime += 1
					if appearsTime > 2:
						pass
					else:
						count += 1

				else:
					appearsTime = 1
					count += 1
		return count

nums = [1,1,1,2,2,3]

solution = Solution()
result = solution.removeDuplicates(nums)
print(result)