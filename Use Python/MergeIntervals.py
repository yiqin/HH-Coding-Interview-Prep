class Interval(object):
	"""docstring for Interval"""
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	"""docstring for Solution"""
	def merge(self, intervals):
		intervals.sort(key = lambda x:x.start)
		results = []
		if len(intervals) == 0:
			return []

		tmp = Interval(intervals[0].start, intervals[0].end)
		for i in range(1, len(intervals)):
			next = intervals[i]
			if tmp.end >= next.end:
				pass
			elif tmp.end >= next.start:
				tmp.end = next.end
			elif tmp.end < next.start:
				results.append(Interval(tmp.start, tmp.end))
				# update
				tmp.start = next.start
				tmp.end = next.end
		results.append(tmp)
		print(results[0].start)
		return results



interval1 = Interval(1, 4)
interval2 = Interval(5, 6)
interval3 = Interval(8, 10)
interval4 = Interval(15, 18)

solution = Solution()
results = solution.merge([interval1, interval2])
print(len(results))