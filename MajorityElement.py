class Solution(object):
	"""docstring for Solution"""
	def majorityElement(self, nums):

		result = nums[0]
		count = 1
		
		for i in range(1, len(nums)):
			if count == 0:
				result = nums[i]
				count += 1
			else:
				if result == nums[i]:
					count += 1
				elif result != nums[i]:
					count -= 1

		# print(count)
		return result







nums = [10,9,9,9,10]
solution = Solution()
result = solution.majorityElement(nums)
print("result ",result)
		