class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dict = {")": "(", "}": "{", "]": "["} 
        for item in s:
            if item in parentheses_dict:
                if stack and stack[-1] == parentheses_dict.get(item):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)         
        if not stack:
            return True
        else:
            return False