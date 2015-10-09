class Solution(object):
	def evalRPN(self, tokens):
		numStack = list()

		for i in range(len(tokens)):

			c = tokens[i]

			if self.isOperator(c):
				num2 = int(numStack.pop())
				num1 = int(numStack.pop())
				print(num1, c, num2)
				result = 0
				if c == "+":
					result = num1 + num2
				elif c == "-":
					result = num1 - num2
				elif c == "*":
					result = num1 * num2
				elif c == "/":
					if num1 * num2 < 0:
						result = - (abs(num1)/abs(num2))
					else:
						result = num1 / num2

				numStack.append(str(int(result)))
			else:
				numStack.append(c)

		return int(numStack.pop())


	def isOperator(self, str):
		if str == "+" or str == "-" or str == "*" or str == "/":
			return True
		else:
			return False




tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution()
result = solution.evalRPN(tokens)
print(result)