def main():
    n = int(input())  # 讀取音軌的數量
    permutation = list(map(int, input().split()))  # 讀取給定的排列
    
    # 根據排列建立新的文件名序列
    filenames = [0] * n
    for i, p in enumerate(permutation):
        filenames[i] = p

    # 輸出新的文件名序列
    print(" ".join(map(str, filenames)))

if __name__ == "__main__":
    main()
