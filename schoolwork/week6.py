memory=[0 for i in range(254)]      # 記憶體 254 words
register=[0 for i in range(16)]     # 暫存器 16 個
pc=0                                #程式記數器 program counter
ir=0                                #指令暫存器 Instruction Register
noi=input()                         # 讀入指令數 
for i in range(noi):                # load instructions to memeory
   memory[i]=int(input(),16)        # instruction以16進位讀入

while True:                         # machine cycle 機器循環
    ir=memory[pc]                   # 指令抓取 fetch instruction
    opcode=ir>>12                   # 解碼 取得op code 
    Rd=R=(ir<<4)>>8                        # 取得 Rd 目的地暫存器 ,Rs1 來源暫存器1 ,Rs2 來源暫存器2
    Rs1=(ir<<8)>>4
    Rs2=ir<<12
    Md=(ir<<4)>>4                                #      Ms 來源記憶體位址, Md 目的地記憶體位址
    Ms=ir<<12
                                    # pc 指向下一指令所在位址
    if opcode==0:                   # 解碼執行指令碼 (參考指令表)
        break
    elif opcode==1:
        Rd=Ms
    elif opcode==2:
        Rs=ir<<12
        Rd=Rs1+Rs2
    elif opcode==3:
        Rd=Rs1+Rs2
    elif opcode==4:
        Rd=Rs
    elif opcode==5:
        pass
    elif opcode==6:
        pass
    elif opcode==7:
        pass
    elif opcode==8:
        pass
    elif opcode==9:
        pass
    elif opcode==10:
        R+=1
    elif opcode==11:
        R-=1
    elif opcode==12:
        pass
    elif opcode==13:
        pass
    elif opcode==14:
        pass
    elif opcode==15:
        pass
    else:
        break