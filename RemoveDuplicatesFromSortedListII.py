class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	"""docstring for Solution"""
	def deleteDuplicates(self, head):
		if head == None:
			return None

		newHead = None
		previous = head.val

		if head.next != None:

		else:
			return None

		nextVal = head.next.val




node1 = ListNode(1)
node11 = ListNode(1)
node111 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node11
node11.next = node111
node111.next = node2
node2.next = node3

solution = Solution()
solution.deleteDuplicates(node1)		