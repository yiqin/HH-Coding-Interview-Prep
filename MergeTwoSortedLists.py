class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	"""docstring for Solution"""
	def mergeTwoLists(self, l1, l2):
		if l1 == None:
			return l2
		if l2 == None:
			return l1

		# print("here")
		# init
		head = ListNode(0)

		if l1.val < l2.val:
			head = l1
			l1 = l1.next
		else:
			head = l2
			l2 = l2.next
		newHead = head

		# print(newHead.val)

		while not (l1 == None and l2 == None):
			# print("loop")
			if l1 == None:
				# print("loop")
				newHead.next = l2
				newHead = newHead.next
				l2 = l2.next
				# print("loop", newHead.val)
				continue

			if l2 == None:
				newHead.next = l1
				newHead = newHead.next
				l1 = l1.next
				continue
			
			if l1.val < l2.val:
				newHead.next = l1
				newHead = newHead.next
				l1 = l1.next
			else:
				newHead.next = l2
				newHead = newHead.next
				l2 = l2.next

		print(head.next.val)
		return head


node1 = ListNode(1)
node2 = ListNode(2)

solution = Solution()
solution.mergeTwoLists(node1, node2)


