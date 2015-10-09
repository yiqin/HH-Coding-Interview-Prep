class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		firstNumber = 0
		# sort
		results = []

		# set the first number

		for i in range(len(nums)-2):

			sum = 0
			if i == 0:
				firstNumber = nums[i]
			else:
				if nums[i-1] == nums[i]:
					continue
				else:
					firstNumber = nums[i]

			# sum of two numbers
			starting = i+1
			ending = len(nums)-1

			# update starting and ending
			while starting < ending:
				sum = firstNumber + nums[starting] + nums[ending]
				if sum == 0:
					results.append([firstNumber, nums[starting], nums[ending]])
					while nums[starting-1] == nums[starting]:
						starting += 1
					starting += 1
				elif sum < 0:
					while nums[starting-1] == nums[starting]:
						starting += 1
					starting += 1
				else:
					while ending+1 < len(nums) and nums[ending] == nums[ending+1]:
						ending -= 1
					ending -= 1


		return results


S = [-1, 0, 1, 2, -1, -4]

solution = Solution()
result = solution.threeSum(S)
print(result)