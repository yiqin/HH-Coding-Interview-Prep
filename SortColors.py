class Solution(object):
	"""docstring for Solution"""
	def sortColors(self, nums):
		redPointer = -1
		whitePointer = -1
		bluePointer = -1 

		if len(nums) == 0:
			return []

		for i in range(len(nums)):
			if nums[i] == 0:
				redPointer += 1
				whitePointer += 1
				bluePointer += 1

			elif nums[i] == 1:
				whitePointer += 1
				bluePointer += 1

			elif nums[i] == 2:
				bluePointer +=1

		# print(redPointer)
		# print(whitePointer)
		# print(bluePointer)

		# results = [-1 for i in range(len(nums))]
		for i in range(redPointer+1):
			nums[i] = 0
		for i in range(redPointer+1, whitePointer+1):
			nums[i] = 1
		for i in range(whitePointer+1, bluePointer+1):
			nums[i] = 2
		


nums = [1, 0]
solution = Solution()
solution.sortColors(nums)