class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	"""docstring for Solution"""
	def removeElements(self, head, val):
		if head == None:
			return None

		p1 = head

		while True:
			if p1 == None:
				return None
			if p1.val == val:
				p1 = p1.next
			else:
				break

		# print(p1.val)

		p2 = p1.next
		newHead = p1

		while True:
			if p2 == None:
				break

			if p2.val == val:
				# print(p1.val)
				tmp = p2.next
				p1.next = tmp
				p2 = tmp
			else:
				tmp = p2.next
				p1 = p2
				p2 = tmp

		# print(newHead.val)
		return newHead

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

solution = Solution()
solution.removeElements(node1, 1)		
		