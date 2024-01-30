class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index1 = 0
        index2 = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ' and ( i == 0 or s[i-1] == ' '):
                index1 = i
                break
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                index2 = i
                break
        return index2 - index1 + 1
        