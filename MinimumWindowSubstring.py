class Solution(object):
	def minWindow(self, s, t):
		hashset = set()
		for i in range(len(t)):
			hashset.add(t[i])

		countSet = set()

		minLength = -1

		minStarting = 0
		minEnding = 0

		currentStarting = 0
		currentEnding = 0

		while currentStarting <= currentEnding:

			if len(countSet) == len(hashset):
				if minLength > currentEnding-currentStarting:
					minStarting = currentStarting
					minEnding = currentEnding
				countSet.remove(s[currentStarting])
				currentStarting += 1

			else:
				currentEnding += 1
				if currentEnding == len(s):
					break
				if s[currentEnding] in hashset:
					countSet.add(s[currentEnding])

			print(countSet)
			print(currentStarting)
			print(currentEnding)

		print("result")
		print(s[minStarting: minEnding])


s = "ADOBECODEBANC"
t = "ABC"

print(s[0:0])

solution = Solution()
solution.minWindow(s, t)
		