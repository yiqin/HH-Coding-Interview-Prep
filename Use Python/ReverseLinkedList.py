class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	"""docstring for Solution"""
	def reverseList(self, head):
		if head == None:
			return None

		p1 = head
		p2 = head.next
		if p2 == None:
			return p1

		while True:
			new = p2.next
			p2.next = p1

			# update
			p1 = p2
			p2 = new

			if p2 == None:
				return p1




node1 = ListNode(1)
node2 = ListNode(2)

node1.next = node2

solution = Solution()
result = solution.reverseList(node1)
		
print(result.val)