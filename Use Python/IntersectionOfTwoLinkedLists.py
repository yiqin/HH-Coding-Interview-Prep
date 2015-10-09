class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	"""docstring for Solution"""
	def getIntersectionNode(self, headA, headB):
		if headA == None or headB == None:
			return None

		lengthA = 0

		nodeA = headA
		while nodeA.next != None:
			nodeA = nodeA.next
			lengthA += 1

		lengthB = 0

		nodeB = headB
		while nodeB.next != None:
			nodeB = nodeB.next
			lengthB += 1

		# reset 
		nodeA = headA
		nodeB = headB

		# move steps first
		if lengthA >= lengthB:
			diff = lengthA-lengthB
			for i in range(diff):
				nodeA = nodeA.next
		else:
			diff = lengthB-lengthA
			for i in range(diff):
				nodeB = nodeB.next
		
		print(nodeA.val, nodeB.val)

		while nodeA != None and nodeB != None:
			if nodeA.val == nodeB.val:
				return nodeA

			nodeA = nodeA.next
			nodeB = nodeB.next

		return None


a1 = ListNode(1)
a2 = ListNode(2)

b1 = ListNode(3)
b2 = ListNode(4)
b3 = ListNode(5)

c1 = ListNode(6)
c2 = ListNode(7)
c3 = ListNode(8)

a1.next = a2
a2.next = c1

b1.next = b2
b2.next = b3
b3.next = c1

c1.next = c2
c2.next = c3

solution = Solution()
result = solution.getIntersectionNode(a1, b1)

print(result.val)






