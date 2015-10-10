class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	"""docstring for Solution"""
	def isSymmetric(self, root):
		if root == None:
			return True

		depth = 1
		queue1 = list()
		queue2 = list()


		currentQueue = list()
		nextQueue = list()

		currentQueue.append(root)

		while True:
			# clear the next queue
			nextQueue = list()

			for i in range(len(currentQueue)):
				currentNode = currentQueue[i]
				if currentNode != None:
					nextQueue.append(currentNode.left)
					nextQueue.append(currentNode.right)

			currentQueue = nextQueue

			if len(currentQueue) == 0:
				return True

			# print(len(currentQueue), pow(2, depth))
			# process currentQueue
			if len(currentQueue)%2 != 0:
				# print("length")
				return False
			

			# process element
			start = 0
			while start < len(currentQueue) and currentQueue[start] == None:
				start += 1

			end = len(currentQueue)-1
			while end >= 0 and currentQueue[end] == None:
				end -= 1

			while start <= end:
				if currentQueue[start] == None or currentQueue[end] == None:
					return False
				# print(currentQueue[start].val, currentQueue[end].val)
				if currentQueue[start].val != currentQueue[end].val:
					# print("Not equal")
					return False
				start += 1
				end -= 1


		return True





node1 = TreeNode(1)
node2 = TreeNode(2)
node22 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node44 = TreeNode(3)
node33 = TreeNode(3)

node1.left = node2
# node1.right = node22

# node2.left = node3
# node2.right = node4

# node22.left = node44
# node22.right = node33

solution = Solution()
result = solution.isSymmetric(node1)
		
print(result)
		