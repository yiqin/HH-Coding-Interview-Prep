class Solution(object):
	def isValid(self, s):		
		# ()
		stack1 = []

		for i in range(len(s)):

			if s[i] == '(' or s[i] == '[' or s[i] == '{':
				stack1.append(s[i])
			else:
				if not stack1:
					return False
				popVal = stack1.pop()
				if (s[i] == ')' and popVal != '(') or (s[i] == ']' and popVal != '[') or (s[i] == '}' and popVal != '{'):
					return False

		if len(stack1) == 0:
			return True
		else:
			return False


s = "([]())[]"
solution = Solution()
result = solution.isValid(s)
print(result)
