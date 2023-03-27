def digit(digit):
    if digit in "+-*/()":
        return False
    else:
        return True
    
while True:
    try:
        stack = []
        output = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        # expression = "8-(3+2*6)/5+4"
        expression=str(input())
        # expression="(3+4)*5/(2-3)"
        # expression="(2+4)*(3-1)"
        
        check=""
        # for char in range(len(expression)):
        #     if expression[char].isdigit():
        #         output.append(expression[char])
        #     elif expression[char] == '(':
        #         stack.append(expression[char])
        #     elif expression[char] == ')':
        #         while stack and stack[-1] != '(':
        #             output.append(stack.pop())
        #         stack.pop() # remove '('
        #     else:
        #         while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[expression[char]]:
        #             output.append(stack.pop())
        #         stack.append(expression[char])
        for i in range(len(expression)):
            if expression[i].isdigit():
                check=check+expression[i]
                if i == len(expression)-1 or not expression[i+1].isdigit():
                    output.append(check)
                    check = ""
            else:
                if expression[i] in "+-*/":
                    while len(stack)>0 and stack[-1]!='(' and precedence[expression[i]]<= precedence[stack[-1]]:
                        output.append(stack.pop())
                    stack.append(expression[i])
                elif expression[i]=="(":
                    stack.append(expression[i])
                elif expression[i]==")":
                    while stack[-1]!="(":
                        output.append(stack.pop())
                    stack.pop()
        while stack:
            output.append(stack.pop())

        print(" ".join(output))

        output=list(output)

        while len(output)!=1:
            # for i in range(len(output)-1, -1, -1):
            #     try:
            #         if output[i]=="+" or output[i]=="-" or output[i]=="*" or output[i]=="/":
            #             if output[i]=="+":
            #                 if digit(output[i-1]) and digit(output[i-2]):
            #                     output[i]=str(int(output[i-1])+int(output[i-2]))
            #                     output.pop(i-1)
            #                     output.pop(i-2)
            #                     print(" ".join(output))
            #             elif output[i]=="-":
            #                 if digit(output[i-1]) and digit(output[i-2]):
            #                     output[i]=str(int(output[i-2])-int(output[i-1]))
            #                     output.pop(i-1)
            #                     output.pop(i-2)
            #                     print(" ".join(output))
            #             elif output[i]=="*":
            #                 if digit(output[i-1]) and digit(output[i-2]):
            #                     output[i]=str(int(output[i-1])*int(output[i-2]))                    
            #                     output.pop(i-1)
            #                     output.pop(i-2)
            #                     print(" ".join(output))
            #             elif output[i]=="/":
            #                 if digit(output[i-1]) and digit(output[i-2]):
            #                     output[i]=str(int(int(output[i-2])/int(output[i-1])))
            #                     output.pop(i-1)
            #                     output.pop(i-2)
            #                     print(" ".join(output))
            #     except:
            #         break
            for i in range(0,len(output)):
                try:
                    if digit(output[i]) and digit(output[i+1]):
                        if output[i+2]=="+":
                            output[i+2]=str(int(output[i])+int(output[i+1]))
                            output.pop(i)
                            output.pop(i)
                            print(" ".join(output))
                        elif output[i+2]=="-":
                            output[i+2]=str(int(output[i])-int(output[i+1]))
                            output.pop(i)
                            output.pop(i)
                            print(" ".join(output))
                        elif output[i+2]=="*":
                            output[i+2]=str(int(output[i])*int(output[i+1]))
                            output.pop(i)
                            output.pop(i)
                            print(" ".join(output))
                        elif output[i+2]=="/":
                            output[i+2]=str(int(int(output[i])/int(output[i+1])))
                            output.pop(i)
                            output.pop(i)
                            print(" ".join(output))
                except:
                    break
    except EOFError:
        break