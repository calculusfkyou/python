import time

# time.time() 返回自1970年1月1日午夜（格林威治時間）以來的秒數。通常用於測量代碼執行時間或時間間隔。
print(time.time())

# time.sleep(seconds) 讓程序休眠指定數秒，其中seconds是要休眠的秒數。它通常用於制造時間間隔，例如在兩個操作之間添加延遲。
time.sleep(3)

# time.ctime([seconds])
# 將一個時間戳（秒數）轉換為易讀的時間字符串。如果未提供seconds，則默認為當前時間。例如，time.ctime()會返回當前時間的字符串表示。
print(time.ctime())
print(time.ctime()[-4:])  # 取出西元年

# time.localtime([seconds])
# 將一個時間戳（秒數）轉換為本地時間的struct_time對象。struct_time包含有關年、月、日、小時、分鐘等時間元素的信息。如果未提供seconds，則默認為當前時間。
now = time.localtime()  # 結構時間
# print(now)
# now.tm_year 取得西元年
cyear = int(now.tm_year) - 1911  # 民國年
month = now.tm_mon
day = now.tm_mday
print("中華民國 {}年 {}月 {}日".format(cyear, month, day))
