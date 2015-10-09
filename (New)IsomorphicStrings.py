class Solution(object):
	"""docstring for Solution"""
	def isIsomorphic(self, s, t):
		dictS = dict()
		dictT = dict()

		for i in range(len(s)):
			if s[i] in dictS:
				tmp = dictS[s[i]]
				tmp.append(i)
			else:
				tmp = [i]
				dictS[s[i]] = tmp

		print(dictS)


		for i in range(len(t)):
			if t[i] in dictT:
				tmp = dictT[t[i]]
				tmp.append(i)
			else:
				tmp = [i]
				dictT[t[i]] = tmp

		print(dictT)

		for i in range(len(dictS.values())):
			tmp = dictS.values()[i]

		if dictS.values() == dictT.values():
			return True
		else:
			return False


solution = Solution()
s = "ab"
t = "ca"
result = solution.isIsomorphic(s, t)
print(result)