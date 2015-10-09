class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isValidBST(self, root):

		def dsf(root, min, max):
			if root == None:
				return True
			if root.val <= min or root.val >= max:
				return False
			return dsf(root.left, min, root.val) and dsf(root.right, root.val, max)

		return dsf(root, float("-infinity"),  float("infinity"))
		

node1 = TreeNode(8)
node2 = TreeNode(3)
node3 = TreeNode(10)
node4 = TreeNode(1)
node5 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5


solution = Solution()
result = solution.isValidBST(node1)
print(result)
		