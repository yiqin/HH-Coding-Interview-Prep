class Solution(object):
	"""docstring for Solution"""
	def moveZeroes(self, nums):
		i = 0
		# ready to swap, but not 
		pointer2 = -1
		if len(nums) == 0:
			return nums

		while i < len(nums):
			if nums[i] == 0 and pointer2 < 0:
				pointer2 = i
			elif nums[i] != 0 and pointer2 >= 0:				
				tmp = nums[pointer2]
				nums[pointer2] = nums[i]
				nums[i] = tmp
				pointer2 += 1
			elif nums[i] == 0:
				i += 1
			else:
				i += 1



nums = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(nums)

		