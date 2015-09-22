class MinStack(object):
	"""docstring for MinStack"""
	def __init__(self):
		self.regularStack = list()
		self.minStack = list()

	def push(self, x):
		# minStack first
		if len(self.minStack) == 0:
			self.minStack.append(x)
		else:
			last = self.minStack[len(self.minStack)-1]
			if last < x:
				self.minStack.append(last)
			else:
				self.minStack.append(x)

		self.regularStack.append(x)

	def pop(self):
		if len(self.regularStack) == 0:
			pass
		else:
			del self.regularStack[len(self.regularStack)-1]
			del self.minStack[len(self.minStack)-1]

	def top(self):
		if len(self.regularStack) == 0:
			return None
		else:
			return self.regularStack[len(self.regularStack)-1]

	def getMin(self):
		if len(self.regularStack) == 0:
			return None
		else:
			return self.minStack[len(self.minStack)-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-1)

print(minStack.getMin())
print(minStack.top())
print(minStack.pop())
print(minStack.getMin())
		