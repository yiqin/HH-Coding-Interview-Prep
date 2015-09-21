class Solution(object):
	"""docstring for Solution"""
	def searchInsert(self, nums, target):
		print(nums)

		starting = 0
		ending = len(nums)-1

		while starting <= ending:

			mid = (ending+starting)/2
			print(starting, mid, ending)

			# luck
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				starting = mid + 1
			elif nums[mid] > target:
				ending = mid - 1

		print(mid)
		return starting






nums = [1, 3, 5, 6]

solution = Solution()
solution.searchInsert(nums, 0)

