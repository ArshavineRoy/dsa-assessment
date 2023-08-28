from collections import deque

def is_balanced(expression):
    stack = deque()  # Create an empty stack
    brackets = {
        "(": ")",    # Map opening brackets to their corresponding closing brackets
        "{": "}",
        "[": "]"
    }

    for char in expression:
        if char in brackets.keys():  # If the character is an opening bracket, ({[ 
            stack.append(char)       # Push it onto the stack
            
        elif char in brackets.values():  # If the character is a closing bracket, )}]
            if not stack or brackets[stack.pop()] != char:  # Check if the stack is empty or mismatched
                return False
    
    return not stack  # If the stack is empty, the expression is balanced

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # True
print(is_balanced(expression2))  # False