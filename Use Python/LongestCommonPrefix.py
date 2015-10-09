class Solution(object):
	def longestCommonPrefix(self, strs):
		if len(strs) == 0:
			return ""

		prefix = strs[0]

		for i in range(1, len(strs)):
			string = strs[i]
			
			#print(prefix)
			hasBreak = False
			for j in range(0, min(len(string), len(prefix))):
				if string[j] != prefix[j]:
					if j == 0:
						return ""
					else:
						prefix = prefix[:j]
						hasBreak = True
						break
			if not hasBreak and len(string) < len(prefix):
				prefix = string

		return prefix



strs = ["flower","flow","flight"] # ["hello", "hele", "hewwo"]

solution = Solution()
result = solution.longestCommonPrefix(strs)

print(result)
		