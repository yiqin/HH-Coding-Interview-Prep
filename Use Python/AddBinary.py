class Solution(object):
	"""docstring for Solution"""
	def addBinary(self, a, b):
		returnStr = ""

		adder = 0

		p1 = 0
		p2 = 0

		while (p1 < len(a) or p2 < len(b)):

			aNum = 0
			if p1 < len(a):
				aNum = int(a[len(a)-1-p1])
			
			bNum = 0
			if p2 < len(b):
				bNum = int(b[len(b)-1-p2])

			result = aNum + bNum + adder

			# print(result)

			if result == 0 or result == 1:
				adder = 0
			elif result == 2:
				result = 0
				adder = 1
			elif result == 3:
				result = 1
				adder = 1

			returnStr = str(result)+returnStr

			p1 += 1
			p2 += 1

		if adder == 1:
			returnStr = str(adder) + returnStr

		return returnStr


a = "0"
b = "0"

solution = Solution()
result = solution.addBinary(a, b)
print(result)