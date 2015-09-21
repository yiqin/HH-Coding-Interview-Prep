class Solution(object):
	"""docstring for Solution"""
	def countAndSay(self, n):
		if n == None:
			return None

		numsDict = dict()

		while True:
			i = n%10

			if i in numsDict:
				oldCount = numsDict[i]
				oldCount += 1
				numsDict[i] = oldCount
			else:
				numsDict[i] = 1

			n = n/10
			if n == 0:
				break

		result = ""

		numsKey = numsDict.keys()
		numsKey.sort()
		for i in range(len(numsKey)):
			key = numsKey[n-1-i]
			val = numsDict[key]
			if val == 1:
				result += str(key)
			else:
				result += str(val) + str(key)

		# print(result)
		return result



solution = Solution()
solution.countAndSay(1)