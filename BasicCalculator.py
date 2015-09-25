class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
    	stack = list()
    	num = 0
    	sign = 1
    	result = 0

    	for i in range(len(s)):
    		c = s[i]
    		if c >= '0' and c <= '9':
    			num = num * 10 + int(c)
    		elif c == '+':
    			result = result + sign * num
    			sign = 1
    			num = 0
    		elif c == '-':
    			result = result + sign * num
    			sign = -1
    			num =0
    		elif c == '(':
    			stack.append(result)
    			stack.append(sign)
    			sign = 1
    			result = 0
    		elif c == ')':
				result = result + sign * num
				sign = stack.pop()
				result = sign*result + stack.pop()
				num = 0

    	if num != 0:
    		result = result + sign * num


    	return result





				


solution = Solution()
# "(1+(4+5+2 )-3)+ (6+ 8) "
result = solution.calculate("(1+(4+5+2 )-3)+ (6+ 8) ")
print(result)
# 23