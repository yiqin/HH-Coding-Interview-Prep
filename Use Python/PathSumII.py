class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):


	def pathSum(self, root, sum):
		results = []
		self.treeSum(root, [], 0, sum, results)
		print(results)
		return results

	def treeSum(self, root, items, tmpSum, targetSum, results):
			if root == None:
				return
			else:
				items.append(root.val)
				tmpSum += root.val
				
				if root.left == None and root.right == None:
					# print("end")
					if tmpSum == targetSum:
						results.append(list(items))
					return

				

				if root.left != None:
					self.treeSum(root.left, items, tmpSum, targetSum, results)
					
				if root.right != None:
					self.treeSum(root.right, items, tmpSum, targetSum, results)
					

				# items.pop()
				# tmpSum -= root.val




node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)

node4 = TreeNode(11)
node5 = TreeNode(13)

node6 = TreeNode(4)

node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(5)

node10 = TreeNode(1)


node1.left = node2
node1.right = node3

node2.left = node4
node4.left = node7
node4.right = node8

node3.left = node5
node3.right = node6

node6.left = node9
node6.right = node10


solution = Solution()
solution.pathSum(node1,22)
		