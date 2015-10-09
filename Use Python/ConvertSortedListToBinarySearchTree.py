class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):

	globvar = ListNode(0)

	def sortedListToBST(self, head):
		self.globvar = head
		count = 0
		temp = head
		while temp != None:
			temp = temp.next
			count += 1
		return self.bst(0, count) 

	def bst(self, starting, ending):
		# print(globvar.val)
		if starting > ending or self.globvar == None:
			return None
		print(self.globvar.val)

		mid = starting + (ending - starting)/2
		left = self.bst(starting, mid - 1)
		root = TreeNode(self.globvar.val)
		
		# why this? 
		self.globvar = self.globvar.next

		right = self.bst(mid + 1, ending)
		
		root.left = left
		root.right = right

		return root


		
# http://yucoding.blogspot.com/2012/12/leetcode-question-24-convert-sorted.html
		
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(8)
node5 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
result = solution.sortedListToBST(node1)
print(result.val)
