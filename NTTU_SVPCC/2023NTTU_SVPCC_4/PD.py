# 互動式題目練習
import sys
while True:
    text=sys.stdin.readline()  # 自帶換行符號，所以最後一個元素是換行符，可以不寫strip("\n")取-2
    if text=="I quacked the code!":
        break
    if text[-2]=="?":
        sys.stdout.write('Quack!\n')
    else:
        sys.stdout.write('*Nod*\n')
    sys.stdout.flush()