class Solution(object):
	"""docstring for Solution"""
	def containsNearbyDuplicate(self, nums, k):
		numsDict = dict()

		for i in range(len(nums)):
			if nums[i] in numsDict:
				indexes = numsDict[nums[i]]
				# print(indexes, i)
				for j in range(len(indexes)):
					diff = i - indexes[j]
					# print(diff)
					if diff <= k:
						return True
				indexes.append(i)

			else:
				numsDict[nums[i]] = [i]

		return False


nums = [1, 2, 3, 4, 5, 6, 4]
solution = Solution()
result = solution.containsNearByDuplicate(nums, 5)
print(result)