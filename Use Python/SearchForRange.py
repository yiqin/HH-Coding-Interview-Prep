class Solution(object):
	"""docstring for Solution"""
	def searchRange(self, nums, target):
		start = 0
		end = len(nums)-1

		while start <= end:
			mid = (end-start)/2



nums = [5, 7, 7, 8, 8, 10]
target = 8
solution = Solution()
solution.searchRange(nums, target)