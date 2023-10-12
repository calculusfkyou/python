# 檔案處理

# 資料檔案的儲存：open()函式
# 語法
"""
    with open(檔案名稱[, 模式][, 編碼]) as f:
        f.檔案處理函式()
"""

# 檔案名稱：設定檔案的名稱，它是字串型態。
# 模式：設定檔案開啟的模式，省略將預設為讀取模式。
#  r： 讀取模式，此為預設模式。
#  a： 附加模式，若檔案已存在，內容會被附加至檔案尾。
#  w： 寫入模式，若檔案已存在，內容將會被覆蓋。
#  b： 二進位模式
# 編碼：指定檔案的編碼模式，一般可設定`cp950`或`UTF-8` (大小寫都可以)。

# 檔案處理函式
# read()： 讀取檔案內容為文字。
# readline()： 讀取檔案內容的第一行文字。
# readlines()： 讀取檔案內容，以行為元素儲存為串列。
# write()： 寫入檔案。
# close()： 關閉檔案。 一定要關檔案，不然會有未知錯誤。

# 文字檔案讀寫的範例
f = open('file.txt', 'w')
f.write('abc')
f.close()

f = open('file.txt', 'a')
f.write('123')
f.close()

f = open('file.txt', 'r')
print(f.read())
f.close()

f = open('file1.txt', 'a')
f.write('123')
f.write('abc')
# f.close() 未關檔案，有未知錯誤

with open('file2.txt', 'a') as f:  # 這種寫法可以不用close，不會有錯誤
    f.write('123')
    f.write('abc')
