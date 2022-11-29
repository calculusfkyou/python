"""
字典:

字典結構與串列類似，其元素是以 鍵-值 對方式儲存，照樣就可使用 鍵 來取得 值 。
#第一種方式，將元素置於 {} 中
#語法為: 字典名稱 = {鍵1:值1, 鍵2:值2, ...}
字串、浮點數、整數都可做為 鍵 ，但以字串做為 鍵 的情況最多。
ex:
dict = {"香蕉":20, "蘋果":50, "橘子":30}

#第二種方法是使用dict函式，再將 鍵-值 對置於 [] 中
#語法為: 字典名稱 = dict([[鍵1,值1], [鍵2,值2],...])
ex:
dict = dict([["香蕉",20], ["蘋果",50], ["橘子",30]])

#第三種方法也是使用dict函式，只要將鍵與值已等號連接起來即可
#語法為: 字典名稱 = dict(鍵1=值1, 鍵2=值2, ...)
#第三種語法的 鍵 不能使用數值，否則執行會產生錯誤

字典取值:
基本取值方式
#字典名稱[鍵]
ex: 
dict = {"香蕉":20, "蘋果":50, "橘子":30}    
print(dict["蘋果"])    # 50

當字典的鍵重複時:
ex: 
dict = {"香蕉":20, "蘋果":50, "橘子":30, "香蕉":25}
print(dict["香蕉"])     #25 ("香蕉":20被覆蓋)

當字典的鍵不存在時:
ex: 
dict = {"香蕉":20, "蘋果":50, "橘子":30}
print(dict[0])  #錯誤 (不能以位置數值作為索引)
print(dict["鳳梨"])     #錯誤 (不存在的鍵)

python提供了get方法可以取的字典元素值，即使鍵不存在也不會產生錯誤。
語法為: 字典名稱.get(鍵[, 預設值])
    沒有傳入預設值:鍵存在:返回鍵對應的值
    沒有傳入預設值:鍵不存在:返回none
    有傳入預設值:鍵存在:返回鍵對應的值
    有傳入預設值:鍵不存在:返回預設值
ex:
dict = {"香蕉":20, "蘋果":50, "橘子":30}
print(dict.get("蘋果"))     #50
print(dict.get("鳳梨"))     #none
print(dict.get("蘋果", 80))     #50
print(dict.get("鳳梨", 80))     #80

修改字典:
#語法為:字典名稱[鍵] = 值
ex1:
dict = {"香蕉":20, "蘋果":50, "橘子":30}
dict["橘子"] = 60
print(dict["橘子"])    #60
ex2:
dict = {"香蕉":20, "蘋果":50, "橘子":30}
dict = ["鳳梨"] = 40
print(dict)     #{"香蕉":20, "蘋果":50, "橘子":30, "鳳梨" : 40}

刪除字典:
第一種是刪除字典中特定元素
#語法為: del 字典名稱[鍵]

第二種使刪除字典中所有元素
#語法為: 字典名稱.clear()
dict = {"香蕉":20, "蘋果":50, "橘子":30}
del dict["蘋果"]    #刪除 "蘋果":50 元素
print(dict)    #{"香蕉":20, "橘子":30}
dict.clear()    #刪除所有元素
print()       #{}  #空字典

第三種是刪除字典，字典刪除後該字典就不存在
#語法為: del 字典名稱
dict = {"香蕉":20, "蘋果":50, "橘子":30}
del dict    #刪除dict字典
print(dict)  #產生錯誤，dict字典不存在

#字典進階用法:(dict = {"joe":5,"mary":8})
取得字典元素個數: len(dict)
ex:
n = len(dict)  
n = 2

複製字典: dict.copy()
ex:
dict2 = dict.copy()
dict2 = {"joe":5,"mary":8}

檢查 鍵 是否存在: 鍵 in dict
ex:
b = "joe" in dict
b = True

取得以 鍵-值 組為元素的組合: dict.items()
ex:
item = dict.items()
item = [("joe":5),("mary":8)]

取得以 鍵 為元素的組合: dict.keys()
ex:
key = dict.keys()
key = ["joe","mary"]

與get()類似，若 鍵 不存在就以參數的 鍵-值 建立新元素: dict.setdefault(鍵,值)
n = dict.setdefault("joe")
n = 5

取得以 值 為元素的組合: dict.values()
value = dict.values()
value = [5,8]

in 功能:
in 功能會檢查字典中的 鍵 是否存在，如果 鍵 存在 就傳回True ，鍵 不存在就傳回 False
#語法為: 鍵 in 字典名稱
ex:
dict = {"香蕉":20, "蘋果":50, "橘子":30}
print("香蕉" in dict)    #True
print("鳳梨" in dict)    #False

EXERCISE:
dict = {"電視":15000, "冰箱":23000, "冷氣":28000}
device = input("輸入電器名稱:")
if device in dict:
    print(device,"的價格為",str(dict[device]))
else: 
    price = input("輸入電器價格:")
    dict[device] = price
    print("字典內容",str(dict)) 

keys()功能可以取得字典中所有 鍵  ，資料型態為dict_keys
ex:
dict = {"香蕉":20, "蘋果":50, "橘子":30}
key = dict.keys()
print(key)    #dict_keys(['香蕉', '蘋果', '橘子'])
雖然dict_keys資料型看起來像串列，但它不能以索引方式取的元素值:
dict = {"香蕉":20, "蘋果":50, "橘子":30}
key = dict.keys()
print(key[0])      #產生錯誤，不能以索引方式取得元素值
必須將dict_keys資料型態以list函式轉換為串列才能取得元素值:
dict = {"香蕉":20, "蘋果":50, "橘子":30}
key = list(dict.keys())
print(key[0])   #香蕉

values()功能可取的字典中所有的 值 ，資料型態為dict_values。用法和keys()完全相同，不再贅述。

items()功能可同時取的 鍵-值 組成的組合，資料型態為dict_items。

setdefault 功能:
與get雷同，但get功能不會改變字典內容；setdefault可能改變字典內容。
#語法為:字典名稱.setdefault(鍵[,預設值]
    沒有傳入預設值， 鍵 存在，返回鍵對應的值，字典沒有改變
    沒有傳入預設值， 鍵 不存在，返回None，字典加入元素 鍵:None
    有傳入預設值， 鍵 存在，返回鍵對應的值，字典沒有改變
    有傳入預設值， 鍵 不存在，返回鍵預設值，字典加入元素 鍵:預設值
ex:
dict={"香蕉":20, "蘋果":50, "橘子":30}
n=dict.setdefault("蘋果")    #n=50, dict未改變
n=dict.setdefault("蘋果", 100)   #n=50, dict未改變
n=dict.setdefault("鳳梨")    #n=None, dict={"香蕉":20, "蘋果":50, "橘子":30ㄝ, "鳳梨":None}
n=dict.setdefault("鳳梨", 100)    #n=None, dict={"香蕉":20, "蘋果":50, "橘子":30, "鳳梨":100}
"""