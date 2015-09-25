class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		

class Solution(object):
	"""docstring for Solution"""
	def invertTree(self, root):
		return self.invert(root)
		

	def invert(self, node):
		if node == None or (node.left == None and node.right == None):
			return node

		left = self.invert(node.left)
		right = self.invert(node.right)

		node.left = right
		node.right = left

		return node