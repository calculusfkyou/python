import os

# os.getcwd()
# 用於獲取當前工作目錄（Current Working Directory，CWD）。它返回一個表示當前工作目錄的字串。當您需要確定程序當前所在的目錄時，這個函數非常有用。
current_directory = os.getcwd()
print("當前工作目錄：", current_directory)

# os.remove(filename)
# 用於刪除指定的文件。它需要文件名作為參數，並將該文件刪除。
# file_to_delete = "tt.py"
# os.remove(file_to_delete)
# print(f"文件 '{file_to_delete}' 已刪除")

# os.mkdir(directory)
# 用於創建新的目錄。它需要一個目錄名作為參數，並創建一個新的目錄，名稱由參數指定。
new_directory = "new_folder"
os.mkdir(new_directory)
print(f"已創建新目錄 '{new_directory}'")

# os.rmdir(directory)
# 用於刪除指定的目錄。它需要一個目錄名作為參數，並刪除該目錄。請注意，目錄必須是空的才能成功刪除。
directory_to_remove = "new_folder"
os.rmdir(directory_to_remove)
print(f"目錄 '{directory_to_remove}' 已刪除")

# os.path.exists
# 用於檢查指定路徑的文件或目錄是否存在。這個函數會回傳一布林值，如果路徑存在則為 True，否則為 False。
print(os.path.exists("new_folder"))

# os.makedirs(name, mode=0o777, exist_ok=False)
# 用於創建多層目錄，包括所有中間目錄。它需要一個目錄名作為參數。您可以使用 mode 參數指定創建目錄的權限，exist_ok 參數用於確定如果目錄已經存在時是否引發異常。
# nested_directory = "parent/child/grandchild"
# os.makedirs(nested_directory, exist_ok=True)
# print(f"已創建多層目錄 '{nested_directory}'")

import shutil

# rmtree
# 這個函數允許您刪除整個目錄，包括它的所有子目錄和文件。
# 刪除指定目錄(非空目錄)
# shutil.rmtree("parent/child/grandchild")
# shutil.rmtree("parent/child")
# shutil.rmtree("parent")
