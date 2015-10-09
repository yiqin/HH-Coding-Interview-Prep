class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s, sub, ips, ip):
        	if sub == 4:
        		if s == '':
        			print(ip)
        			ips.append(ip[1:])
        		return
        	for i in range(1, 4):
        		if i <= len(s):
        			if int(s[:i]) <= 255:
        				print(int(s[:i]))
        				dfs(s[i:], sub+1, ips, ip+'.'+s[:i])
        			if s[0] == '0': break

        ips = []
        dfs(s, 0, ips, '')
        return ips


solution = Solution()
result = solution.restoreIpAddresses("25525511135")
print(result)

