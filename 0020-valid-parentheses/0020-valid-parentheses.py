class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        p={'(': ')','{': '}','[': ']'}
        for bracket in s:
            if bracket in p:
                stack.append(bracket)
            elif len(stack)==0 or bracket!=p[stack.pop()]:
                return False
        return len(stack)==0