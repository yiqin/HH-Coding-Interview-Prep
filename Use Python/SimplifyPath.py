class Solution(object):
	def simplifyPath(self, path):
		stack = list()

		hasFound = False
		starting = 0
		ending = 0
		for i in range(len(path)):
			c = path[i]
			if c != '/' or i == len(path)-1:
				if not hasFound:
					starting = i
					hasFound = True
			else:
				if hasFound:
					ending = i
					hasFound = False

					subString = path[starting: ending]
					if subString == "..":
						if len(stack) > 0:
							stack.pop()
					else:
						if len(subString) > 0 and subString != '.':
							stack.append(subString)

					starting = i


		if len(stack) == 0:
			return "/"

		print(stack)
		newPath = ""
		for i in range(len(stack)):
			newPath += "/"
			newPath += stack[i]

		return newPath


path = "/abc/.."


solution = Solution()
result = solution.simplifyPath(path)

print("result", result)