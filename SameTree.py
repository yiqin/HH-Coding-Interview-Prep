class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	"""docstring for Solution"""
	def isSameTree(self, p, q):
		if p == None:
			if q != None:
				return False
			else:
				return True

		if q == None:
			if p != None:
				return False
			else:
				return True


		queueP = list()
		queueP.append(p)

		queueQ = list()
		queueQ.append(q)

		while len(queueP) != 0:
			tmp1 = queueP[0]
			queueP = queueP[1:len(queueP)]

			tmp2 = queueQ[0]
			queueQ = queueQ[1:len(queueQ)]

			if tmp1 == None and tmp2 == None:
				break
			if (tmp1 != None and tmp2 == None) or (tmp1 == None and tmp2 == None):
				return False

			if  tmp1.val != tmp2.val:
				return False

			if (tmp1.left != None and tmp2.left != None and tmp1.left.val == tmp2.left.val) or (tmp1.left == None and tmp2.left == None):
				queueP.append(tmp1.left)
				queueQ.append(tmp2.left)
			else:
				return False

			if (tmp1.right != None and tmp2.right != None and tmp1.right.val == tmp2.right.val) or (tmp1.right == None and tmp2.right == None):
				queueP.append(tmp1.right)
				queueQ.append(tmp2.right)
			else:
				return False

		return True


solution = Solution()


		