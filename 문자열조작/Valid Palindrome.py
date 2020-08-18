import sys

class Solution:
    def isPalindrome(self, s):
        self.s = s
        res = ''.join(filter(lambda x : x.isalnum(), s)).lower()
        return res == res[::-1]

s = sys.stdin.readline()

print(Solution().isPalindrome(s))