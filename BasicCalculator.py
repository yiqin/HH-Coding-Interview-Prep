class Solution(object):
	"""docstring for Solution"""
	def calculate(self, s):
		n = len(s)

		stack = list()
		totalSum = 0
		i = 0

		isInStack = False

		while i < n:
			c = s[i]
			if c == ' ':
				pass
			elif c == '(':
				isInStack = True
				stack.append(c)
			elif c == ')':
				tmp = 0
				while True:	
					print(stack)			
					num = int(stack[len(stack)-1])
					del stack[len(stack)-1]
					operator = stack[len(stack)-1]
					del stack[len(stack)-1]
					
					if operator == "-":
						num = -num
					elif operator == "(":
						break
					tmp += num

				totalSum += tmp
			elif isInStack:
				stack.append(c)
			

			i += 1

		print(stack)
				


solution = Solution()
result = solution.calculate("(1+(4+5+2 )-3)+ (6+ 8) ")
# 23