class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	"""docstring for Solution"""
	def isSymmetric(self, root):

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
		