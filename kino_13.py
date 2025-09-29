"""
a = 'abcde'
b = "あいうえお"
c = str(12345)

print(a, type(a), a[0]) #文字列の表示、型表示、0番目の表示
print(b, type(b), b[0])
print(c, type(c), c[0])
"""
"""
x = "aaa" + "bbb" #文字列の結合
print(x)
"""
"""
x = "abc" * 3 #3回文字列の結合を繰り返す
print(x)
"""
"""
x = "-".join(["a", "b", "c"]) #joinメソッド(区切り文字-を用いて結合)
print(x)
"""
"""
x = "I study Python"
a = x.split() #splitメソッド(半角スペースを区切り文字として文字列を分割)
print(a)
"""
"""
x = "I-study-Python"
a = x.split(sep = "-") #-を区切り文字として文字列を分割
print(a)
"""
"""
x = "I study Python"
print("s" in x) #文字列の検索(xの中にsが含まれているか) T
print("study" in x) #T
print("python" in x) #F
"""
"""
x = "I study Python"
a = x.find("s") #findメソッド(指定した文字のインデックス番号を取得 スペースも1文字カウント)
a1 = x.find("study") #最小のインデックス番号が返ってくる 2
a2 = x.find("python") #存在しないので-1が返ってくる
print(a)
print(a1)
print(a2)
"""
"""
x = "I study Python"
a = x.replace("Python", "Ruby") #replaceメソッド(置換したいものと置換後に組み込むものを入れる)
print(a)
"""
"""
x = "I study Python"
a = x.replace(" ","") #半角スペースを空白ナシに置換
print(a)
"""
"""
x = 3
print("1 + 2 = {}".format(x)) #formatメソッド(文字列の中に変数を入れ込む)
"""
"""
print("1 + 2 = {}".format(1 + 2)) #引数に計算式なども指定可能
"""
"""
x = 1
y = 2
print("{} + {} = {}".format(x, y, x + y)) #{}複数使用可能
"""
"""
x = 1
y = 2
print("{1} + {0} = {2}".format(x, y, x + y)) #{}内に数値を書くことで呼び出す順番を指定可能
"""
"""
x = 1
y = 2
print("{B} + {A} = {result}".format(A = x, B = y, result = x + y)) #キーワード引数
"""
"""
x = 1
y = 2
print("{} ÷ {} = {:.2f}".format(x, y, x / y)) #書式の指定(小数点以下第二位まで表示)
"""

x = 1
y = 2
print(f"{x} ÷ {y} = {x / y :.2f}") #format済み文字列
