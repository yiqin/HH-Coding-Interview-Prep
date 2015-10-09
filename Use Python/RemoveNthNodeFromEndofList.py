class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	"""docstring for Solution"""
	def removeNthFromEnd(self, head, n):
	    p = head
	    for i in xrange(1, n):
	        p = p.next
	    dummy = ListNode(0)
	    dummy.next = head
	    pp = dummy
	    while p.next:
	        p = p.next
	        pp = pp.next
	    if pp.next:
	        pp.next = pp.next.next
	    else:
	        pp.next = None
	    return dummy.next


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
solution.removeNthFromEnd(node1, 2)
		