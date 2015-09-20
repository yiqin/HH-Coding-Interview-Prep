class Solution(object):
	"""docstring for Solution"""
	def isIsomorphic(self, s, t):
		setS = {}
		for i in range(len(s)):
			if s[i] in setS:
				numSet = setS[s[i]]
				numSet.add(i)
				setS[s[i]] = numSet
			else:
				numSet = set()
				numSet.add(i)
				setS[s[i]] =  numSet
		# print(setS)

		setT = {}
		for i in range(len(t)):
			if t[i] in setT:
				numSet = setT[t[i]]
				numSet.add(i)
				setT[t[i]] = numSet
			else:
				numSet = set()
				numSet.add(i)
				setT[t[i]] = numSet
		# print(setT)
		a = set()
		b = set()

		arrayS = setS.values()
		for i in range(len(arrayS)):
			a.add(arrayS[i])

		arrayT = setT.values()
		for i in range(len(arrayT)):
			b.add(arrayT[i])

		print(arrayS)
		print(arrayT)

		if arrayS == arrayT:
			return True
		else:
			return False


solution = Solution()
result = solution.isIsomorphic("ab","ca")

print(result)