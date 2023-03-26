while True:
    try:
        stack = []
        output = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        expression = "8-(3+2*6)/5+4"
        expression=str(input())

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

        output=list(output)

        while len(output)!=1:
            for i in range(len(output)-1, -1, -1):
                try:
                    if output[i]=="+" or output[i]=="-" or output[i]=="*" or output[i]=="/":
                        if output[i]=="+":
                            if output[i-1].isdigit() and output[i-2].isdigit():
                                output[i]=str(int(output[i-1])+int(output[i-2]))
                                output.pop(i-1)
                                output.pop(i-2)
                                print(" ".join(output))
                        elif output[i]=="-":
                            if output[i-1].isdigit() and output[i-2].isdigit():
                                output[i]=str(int(output[i-2])-int(output[i-1]))
                                output.pop(i-1)
                                output.pop(i-2)
                                print(" ".join(output))
                        elif output[i]=="*":
                            if output[i-1].isdigit() and output[i-2].isdigit():
                                output[i]=str(int(output[i-1])*int(output[i-2]))                    
                                output.pop(i-1)
                                output.pop(i-2)
                                print(" ".join(output))
                        elif output[i]=="/":
                            if output[i-1].isdigit() and output[i-2].isdigit():
                                output[i]=str(int(output[i-2])//int(output[i-1]))
                                output.pop(i-1)
                                output.pop(i-2)
                                print(" ".join(output))
                except:
                    break
    except EOFError:
        break