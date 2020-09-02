import sys
class Solution:
    def mostCommonWord(self, paragraph, banned):
        self.paragraph = paragraph
        self.banned = banned
        # import re
        # paragraph = re.sub(r'[-=+,#/;\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', paragraph)
        # words = paragraph.lower().split()
        paragraph = ''.join([' '.join(map(lambda x : x if x.isalnum() | x.isspace() else ' ', word)) for word in list(paragraph)])
        words = paragraph.lower().replace('  ',' ').split()
        count = {}
        for word in words:
            if word in banned:
                continue
            count[word] = count.get(word, 0) + 1
        
        res = sorted(count.items(), key = lambda item: item[1], reverse = True)[0][0]
        return res


paragraph = sys.stdin.readline()
banned = sys.stdin.readline()

print(Solution().mostCommonWord(paragraph, banned))