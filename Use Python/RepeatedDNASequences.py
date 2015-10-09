class Solution(object):
	def findRepeatedDnaSequences(self, s):
		results = []
		aSet = set()

		for i in range(len(s)-9):
			currentS = s[i:i+10]
			
			if currentS in aSet:
				# print(currentS)
				# result = currentS
				if currentS not in results:
					results.append(currentS)
				# print(results)
			else:
				aSet.add(currentS)
			# print(currentS)
			# print(aSet)
		return results

		
solution = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
results = solution.findRepeatedDnaSequences(s)
print(results)