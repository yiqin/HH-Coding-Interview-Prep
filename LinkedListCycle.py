class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None
		

class Solution(object):
	def hasCycle(self, head):
		if head == None:
			return False

		faster = head
		dummy = ListNode(0)
		dummy.next = head
		slower = dummy

		while True:
			if faster.next != None and faster.next.next != None:
				faster = faster.next.next
				slower = slower.next
				if faster.val == slower.val:
					return True
			else:
				return False



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

node4.next = node2


solution = Solution()
result = solution.hasCycle(node1)
print(result)