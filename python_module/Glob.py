import glob

# 取得目錄中的想取得的檔案。
files = glob.glob("*.py") + glob.glob("../datastructure/*.py")
print(files)
