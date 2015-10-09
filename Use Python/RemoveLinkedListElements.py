class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	"""docstring for Solution"""
	def removeElements(self, head, val):
		newHead = head
		while head != None and head.val == val:
			newHead = head.next
			head = head.next

		tmpNode = newHead

		while head != None:
			print(head.val)
			if head.val != val:
				tmpNode.next = head

			head = head.next

		print(newHead.next.val)
		return newHead


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
solution.removeElements(node1, 1)
