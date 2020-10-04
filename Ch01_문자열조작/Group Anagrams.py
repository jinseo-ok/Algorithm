timport sys

class Solution:
    def __init__(self, strs):
        self.strs = strs

    def groupAnagrams(self):
        words = list(map(lambda x : ''.join(sorted(x)), strs))
        
        res = []
        for word in set(words):
            ls = []
            for i in range(len(words)):
                if word == words[i]:
                    ls.append(strs[i])
            res.append(ls)
            
        return res


strs = sys.stdin.readline().split()

print(Solution(strs).groupAnagrams())