# 78.39% speed, 5.7% memory
# valid parantheses

class Solution:
    def isValid(self, s: str) -> bool:
        op_par = ('[', '(', '{')
        validation = []
        for i in s:
            if i in op_par:
                if i == '(':
                    validation.append(')')
                elif i == '[':
                    validation.append(']')
                if i == '{':
                    validation.append('}')
            else:
                if len(validation) == 0:
                    return False
                if i != validation.pop():
                    return False
        if validation:
            return False
        else:
            return True