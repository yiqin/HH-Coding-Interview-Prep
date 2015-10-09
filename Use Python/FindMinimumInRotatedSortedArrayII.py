class Solution(object):
	"""docstring for Solution"""
	def findMin(self, nums):
		n = len(nums)

		if n == 0:
			return None
		elif n == 1:
			return nums[0]
		elif n == 2:
			return min(nums[0], nums[1])

		left = 0
		right = n-1

		last = nums[n-1]

		while left <= right:
			mid = (left+right)/2

			# print(mid)

			if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
				return nums[mid]
			elif nums[mid] > last:
				left = mid+1
			else:
				right = mid-1




nums = [1, 2, 1]
solution = Solution()
solution.findMin(nums)

