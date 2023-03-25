# while True:
#     try:
#         tokens=list(input())
#         stack,temp=[],[]
#         for i in tokens:
#             if i.isdight():
#                 temp.append(i)
            
#             if tokens[0]=="(" or tokens[0]==")" or tokens[0]=="(" or tokens[0]=="+" or tokens[0]=="-" or tokens[0]=="*" or tokens[0]=="/":
#                 stack.append(tokens[0])
#                 tokens.pop(0)
            
#     except EOFError:
#         break 

stack = []
output = []
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

expression = "8-(3+2*6)/5+4"

for char in expression:
    if char.isdigit():
        output.append(char)
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            output.append(stack.pop())
        stack.pop() # remove '('
    else:
        while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[char]:
            output.append(stack.pop())
        stack.append(char)

while stack:
    output.append(stack.pop())

print(" ".join(output))