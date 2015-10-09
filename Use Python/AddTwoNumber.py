class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, x):
		self.val = x
		self.next = None
		
class Solution(object):
	def addTwoNumbers(self, l1, l2):
		# print(l1.val)
		i = 0

		firstRound = True

		head = ListNode(0)
		currentNode = head

		while l1 != None or l2 != None:
			sum = i
			if l1 != None:
				sum += l1.val
				l1 = l1.next
			if l2 != None:
				sum += l2.val
				l2 = l2.next
			if sum >= 10:
				i = 1
				sum -= 10
			else:
				i = 0
			# print(sum)
			if firstRound:
				head = ListNode(sum)
				currentNode = head
				firstRound = False
			else:
				currentNode.next = ListNode(sum)
				currentNode = currentNode.next

		if i > 0:
			currentNode.next = ListNode(1)

		return head


l1 = ListNode(9)
l2 = ListNode(8)
l3 = ListNode(3)

l1.next = l2
# l2.next = l3

l4 = ListNode(1)
l5 = ListNode(6)
l6 = ListNode(4)

# l4.next = l5
l5.next = l6

solution = Solution()
result = solution.addTwoNumbers(l1, l4)

print(result.next.val)