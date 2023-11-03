import os

# os.path.abspath(path)： 將相對路徑轉換為絕對路徑。給定一個路徑 path，這個函數返回它的絕對路徑。
print(os.path.abspath("os_path.py"))

# os.path.basename(path)： 返回路徑 path 的基本名稱部分，即路徑中的檔案名或目錄名。
print(os.path.basename("os_path.py"))
print(os.path.basename("python_module"))

# os.path.exists(path)： 檢查路徑 path 所指向的檔案或目錄是否存在，如果存在則返回 True，否則返回 False。
print(os.path.exists("../test.pyi"))
print(os.path.exists("../NTTU_SVPCC"))

# os.path.getsize(path)： 返回指定檔案的大小（位元組數）。
print(os.path.getsize("os_path.py"))

# os.path.split(path)： 將路徑 path 分割為目錄部分和檔案名部分，並返回一個元組，其中第一個元素是目錄部分，第二個元素是檔案名部分。
print(os.path.split("os_path.py"))
print(os.path.split("../datastructure/BFS.py"))

# os.path.join(path1, path2, ...)： 將多個路徑組合成一個。這個函數接受多個參數，每個參數是一個路徑，它們會被連接在一起形成一個完整的路徑。
current_directory = os.getcwd()
print(os.path.join("Os.py", "os_path.py"))
print(os.path.join(current_directory, "os_path.py"))

# os.walk(path) 會遍歷這個目錄，若有子目錄會接續遍歷直到全部檔案遍歷過一次 (從外到內遍歷)
# 設定要遍歷的目錄路徑
root_folder = "C:\GitHub\python\python_module"

for foldername, subfolders, filenames in os.walk(root_folder):
    print(f"目錄：{foldername}")
    # print(filenames)

    # 列出子目錄
    for subfolder in subfolders:
        print(f"子目錄：{subfolder}")

    # 列出檔案
    for filename in filenames:
        print(f"檔案：{filename}")
