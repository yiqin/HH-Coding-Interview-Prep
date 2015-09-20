class Solution(object):
	def longestConsecutive(self, nums):
		print(nums)
		hashSet = set()
		for i in range(len(nums)):
			hashSet.add(nums[i])

		longestLenght = -1

		for i in range(len(nums)):
			if nums[i] in hashSet:
				tmpLength = 1
				hashSet.remove(nums[i])
				largerNumber = nums[i]+1

				while largerNumber in hashSet:
					tmpLength += 1
					hashSet.remove(largerNumber)
					largerNumber += 1
					# print(largerNumber)

				smallerNumber = nums[i]-1
				while smallerNumber in hashSet:
					tmpLength += 1
					hashSet.remove(smallerNumber)
					smallerNumber -= 1
					# print(smallerNumber)

				if tmpLength > longestLenght:
					longestLenght = tmpLength

		print(longestLenght)
		return longestLenght




nums = [100, 4, 200, 1, 3, 2]

solution = Solution()
solution.longestConsecutive(nums)