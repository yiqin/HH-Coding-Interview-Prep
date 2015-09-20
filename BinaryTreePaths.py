class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		

class Solution(object):
	"""docstring for Solution"""

	def binaryTreePaths(self, root):
		if root == None:
			return []

		results = []
		self.dfs(root, "", results)
		return results


	def dfs(self, root, srtItems, results):
		if len(srtItems) == 0:
			srtItems = str(root.val)
		else:
			srtItems = srtItems + "->" + str(root.val)

		if root.left == None and root.right == None:
			# print(srtItems)
			results.append(srtItems)
			return

		if root.left != None:
			self.dfs(root.left, srtItems, results)

		if root.right != None:
			self.dfs(root.right, srtItems, results)






node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)

node1.left = node2
# node1.right = node3
# node2.right = node4


solution = Solution()
result = solution.binaryTreePaths(node1)
print(result)
		