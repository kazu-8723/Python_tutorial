"""
f = open("test.txt", "w") #ファイルの作成 ファイル名"test.txt writeモード
f.write("test") #テキストの書き込み
f.close() #ファイルの作成完了
"""
"""
with open("test.txt", "w") as f: #close無し
    f.write("overwrite") #上書きされる
"""
"""
text = '''\
apple
grape
orange
banana
'''
#改行

with open("test2.txt", "w") as f:
    f.write(text)
"""
"""
with open("test2.txt", "a") as f: #"a" 追加
    f.write("peach\n")
"""
"""
with open("test2.txt", "r") as f: #ファイルの読み込み
    print(f.read())
"""
"""
with open("test2.txt", "r") as f:
    for i in range(3):
        print(f.readline(), end = "") #1行ずつファイルの読み込み
"""
"""
with open("test2.txt", "r+") as f: #"r+"ファイルの読み込み+書き込み
    print(f.read())
    f.write("melon\n")
"""
"""
with open("test2.txt", "r+") as f: #readメソッドを使用しなかったため、テキストの最初から書き込まれる
    f.write("melon\n")
"""
"""
with open("test2.txt", "r+") as f:
    f.seek(6) #テキストの途中から書き込む
    f.write("melon\n")
"""
"""
text = '''\
apple
grape
orange
banana
'''

with open("test3.txt", "w+") as f: #"w+"ファイルの読み込み+書き込み
    f.write(text)
    f.seek(0)
    print(f.read())
"""

with open("test3.txt", "a+") as f: #"a+"ファイルの末尾にテキスト追加+読み込み
    f.write("peach\n")
    f.seek(0)
    print(f.read())
