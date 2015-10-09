class Solution(object):
	"""docstring for Solution"""
	def combinationSum3(self, k, n):
		results = []


		self.help(k, n, 0, [], results)
		print(results)
		return results

	def help(self, k, n, sum, items, results):
		if len(items) == k and sum == n:
			results.append(list(items))
			

		startingIndex = 1
		if len(items) != 0:
			startingIndex = items[len(items)-1]+1

		for i in range(startingIndex, 10):
			items.append(i)
			sum += i
			self.help(k, n, sum, items, results)
			sum -= i
			items.pop()






solution = Solution()
solution.combinationSum3(3, 15)