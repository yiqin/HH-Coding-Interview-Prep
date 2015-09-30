# merge = [[1.1, 2.5, 1], [2.5, 3.3, 2], [3.3, 4, 3], [4, 5, 2], [5, 6, 1]]
# lines = [2.5, 4]

def method(merge, lines):

	i = 0
	j = 0
	result = 0

	while True:
		if merge[i][0] <= lines[j] and lines[j] < merge[i][1]:
			print(lines[j])
			result += merge[i][2]
			j += 1
			
		elif merge[i][0] > lines[j]:
			j += 1
		elif lines[j] >= merge[i][1]:
			i += 1

		if i == len(merge) or j == len(lines):
			break

	print(result)
	return result


merge = [[1.1, 2.5, 1], [2.5, 3.3, 2], [3.3, 4, 3], [4, 5, 2], [5, 6, 1]]
lines = [2.5, 4]

method(merge, lines)