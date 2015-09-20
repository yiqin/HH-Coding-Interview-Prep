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
			return None

		level = 1
		n = 0

		queue = list()
		queue.append(root)

		array = list()
		array.append(root.val)

		while len(queue) != 0:
			item = queue[0]
			queue = queue[1:len(queue)]
			if n == 0:
				# empty array
				print("end", array)
				for i in range(len(array)/2):
					if array[i] != array[n-1-i]:
						print(array[n-1-i])
						return False
				#
				array = list()
				level = level * 2
				n = level
				print(n)

			if item.left != None:
				queue.append(item.left)
				array.append(item.left.val)
				n -= 1
			if item.right != None:
				queue.append(item.right)
				array.append(item.right.val)
				n -= 1

		return True





node1 = TreeNode(1)
node2 = TreeNode(2)
node22 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node44 = TreeNode(4)
node33 = TreeNode(3)

node1.left = node2
node1.right = node22

node2.left = node3
node2.right = node4

node22.left = node44
node22.right = node33

solution = Solution()
result = solution.isSymmetric(node1)
		
print(result)
		