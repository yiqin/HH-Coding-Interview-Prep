class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sortedArrayToBST(self, nums):

		if nums == None or len(nums) == 0:
			return None

		mid = len(nums)/2
		root = TreeNode(nums[mid])
		
		print(root.val)

		return self.findBinary(0, len(nums)-1, nums)


	def findBinary(self, starting, ending, nums):

		if starting > ending:
			return None

		
		mid = starting + (ending - starting) / 2

		currentRoot = TreeNode(nums[mid])

		currentRoot.left = self.findBinary(starting, mid-1, nums)
		currentRoot.right = self.findBinary(mid+1, ending, nums)
		
		return currentRoot
		




nums = [1, 3, 4]

solution = Solution()
result = solution.sortedArrayToBST(nums)

while result.left != None:
	print(result.val)
	result = result.next

# print(result)