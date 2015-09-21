class Solution(object):
	def removeDuplicates(self, nums):
		numsSet = set()

		if len(nums) == 0:
			return 0

		i = 0

		while True:
			if i > len(nums)-1:
				break

			if nums[i] in numsSet:
				del nums[i]
				# print(nums)
			else:
				numsSet.add(nums[i])
				i += 1
			

		# print(nums)
		return len(nums)



nums = [1, 1, 2]
solution = Solution()
solution.removeDuplicates(nums)