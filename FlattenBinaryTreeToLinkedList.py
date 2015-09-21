class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		

class Solution(object):
	"""docstring for Solution"""
	def flatten(self, root):
		# dfs

		# left first

		# put all to the right

	# How...
	def dfs(self, node):

		if node.left == None and node.right = None:
			return node

		if node.left 


		
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.righ = node5

node2.left = node3
node2.right = node4

node5.right = node6


solution = Solution()

solution.flatten(node1)