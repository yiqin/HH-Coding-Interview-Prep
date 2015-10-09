def missingNumber(nums):
	hasN = False
	hasZero = False
	for idx, val in enumerate(nums):
		if val == len(nums):
			hasN = True
		elif val == 0:
			hasZero = True
		else:
			nums[idx] = -val

	if hasN and hasZero:
		for idx, val in enumerate(nums):
			if val > 0:
				return idx
	elif hasZero is False:
		return 0
	else:
		# print("Doesn't hasN")
		return len(nums)


nums = [0]
print(missingNumber(nums))

