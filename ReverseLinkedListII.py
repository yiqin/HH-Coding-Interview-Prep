class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def reverseBetween(self, head, m, n):
		print(head.val)


	def revsereTwoNodes(self, node1, node2):




node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
solution.reverseBetween(node1, 2, 4)