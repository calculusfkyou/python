def h1(A):
    # 計算 A1 ⊕ A2
    A1 = bin(A)[2:]
    A2 = A1[-len(A1)//2:]
    A1 = A1[:len(A1)//2]
    A1_xor_A2 = int(A1, 2) ^ int(A2, 2)

    # 取中間 q 個位元
    q = len(bin(A1_xor_A2)[2:]) // 2
    middle_bits = (A1_xor_A2 >> (len(bin(A1_xor_A2)[2:]) - q)) & ((1 << q) - 1)

    return middle_bits

def h2(A):
    # 計算 B1 ⊕ B3 ⊕ B2
    B1 = bin(A)[2:]
    B2 = B1[-len(B1)//3:]
    B3 = B1[-2*len(B1)//3:-len(B1)//3]
    B1 = B1[:2*len(B1)//3]
    B1_xor_B3_xor_B2 = int(B1, 2) ^ int(B3, 2) ^ int(B2, 2)

    # 取中間 q 個位元
    q = len(bin(B1_xor_B3_xor_B2)[2:]) // 2
    middle_bits = (B1_xor_B3_xor_B2 >> (len(bin(B1_xor_B3_xor_B2)[2:]) - q)) & ((1 << q) - 1)

    return middle_bits

while True:
    try:
        A = int(input())
        print(h1(A), h2(A))
    except:
        break

