class Solution(object):
	"""docstring for Solution"""
	def twoSum(self, nums, target):

		oldnums = list(nums)

		index1 = 0
		index2 = len(nums)-1

		nums.sort()

		# print(oldnums, nums)
		while index1 < index2:
			tmpSum = nums[index1] + nums[index2]
			if tmpSum == target:
				result1 = -1
				result2 = -1
				
				# print(index1, index2)

				for i in range(len(nums)):
					if oldnums[i] == nums[index1]:
						result1 = i
						break
				# print(result1)
				for i in range(len(nums)):
					if oldnums[i] == nums[index2]:
						if nums[index1] == nums[index2]:
							if i > result1:
								result2 = i
								break
						else:
							result2 = i
							break
				# print(result2)
				results = [result1+1, result2+1]
				results.sort()
				return results

			elif tmpSum < target:
				index1 += 1
			else:
				index2 -= 1




nums = [0,4,3,0]
target = 0

solution = Solution()
result = solution.twoSum(nums, target)
print(result)