def is_balanced(expression):
    brackets = {
        ")":"(",
        "}": "{",
        "]": "["
        }
    
    stack =[]
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack 
             
expression1 = '([]{})'
expression2 = '([))'

print(is_balanced(expression2))