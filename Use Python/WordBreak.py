class Solution(object):
	"""docstring for Solution"""
	def wordBreak(self, s, wordDict):
		n = len(s)
		matrix = [False for i in range(len(s))]

		for i in range(n):
			# print(s[i:i+1])
			for j in range(i+1):
				subString = s[j:i+1]
				if subString in wordDict:
					if j == 0:
						matrix[i] = True
						break
					else:
						#print("break")
						if matrix[j-1]:
							matrix[i] = True
							break

		return matrix[len(s)-1]




wordDict = ["leet", "code"]
s = "leetcode"



solution = Solution()
solution.wordBreak(s, wordDict)