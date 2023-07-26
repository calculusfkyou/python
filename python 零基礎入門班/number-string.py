# 數字運算
#   x = 2+3
#   print(x)
#   x//=1   # x = x+1   # 將變數中的字 +1
#   print(x)
# 字串運算  # \ = 跳脫 = Hell"o
   #s = "Hell\"o"
   #print(s)
#一個空白也能串接字串
  #x = "hello" "world"
  #print(x)
#\n  #"""Hello\nworld"""   表換行
   #y = "Hello\nworld"
   #print(y)
#* 重複
   #z = "Hello"*3+"world"
   #print(z)

# 字串會對內部的字元編號(索引)，從 0 開始算起
a = "hello"
print(a[1:4])   
# 包含開頭不包含結尾，得 ell
b = "hello"
print(b[1:])    
# 包含開頭的全部到結尾，得 ello
c = "hello"
print(c[:4])    
# 開頭的全部到結尾前一個，得 hell
