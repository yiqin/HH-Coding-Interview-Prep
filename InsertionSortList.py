class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):

	def insertionSortList(self, head):

		print(head.val)
		self.swap(None, head, head.next)
		return

	def swap(self, previous, node1, node2):
		if node1 != None and node2 != None:
			previous.next = node2
			node2.next = node1
			node1.next = node2.next
		return 



node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(6)
node4 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
solution.insertionSortList(node1)

