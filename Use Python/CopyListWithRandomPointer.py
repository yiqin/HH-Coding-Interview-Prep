class RandomListNode(object):
	"""docstring for RandomListNode"""
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution(object):
	"""docstring for Solution"""
	def copyRandomList(self, head):
		newHead = head
		newPointer = 
		if head == None:
			return None

		p1 = head
		p2 = head.next

		while p2 != None:
			new1 = RandomListNode(p1.label)
			new2 = RandomListNode(p2.label)

			new1.next = new2

			p1 = p2
			p2 = p2.next






node1 = RandomListNode(1)
node2 = RandomListNode(2)
node3= RandomListNode(3)
node4 = RandomListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

node1.random = node3
node2.random = node1
node3.random = node4
node4.random = node1

solution = Solution()
solution.copyRandomList(node1)
