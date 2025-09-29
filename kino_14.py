"""
a = 2
b = 0
try: #try~except文 実行したい処理
    print("start")
    print(a / b)
except: #例外処理
    print("0除算エラー")
"""
"""
a = 2
b = 1
try: #try~except文 実行したい処理
    print("start")
    print(a / b)
except: #例外処理
    print("0除算エラー")
else: #エラーが発生しなかった場合に実行
    print("エラー発生しなかった")
"""
"""
a = 2
b = 0
try: #try~except文 実行したい処理
    print("start")
    print(a / b)
except: #例外処理
    print("0除算エラー")
else: #エラーが発生しなかった場合に実行
    print("エラー発生しなかった")
finally: #エラー発生の有無に関わらず実行される
    print("finish")
"""
"""
a = 2
b = "2"
try:
    print("start")
    print(a / b)
except ZeroDivisionError: #exceptの後にエラー名を記述すると各エラーで場合分けしてくれる
    print("0除算エラー")
except TypeError:
    print("データ型エラー")
"""

a = 2
b = 0
try:
    print("start")
    print(a / b)
except Exception as e: #エラー名の出力
    print(e)
finally:
    print("finish")
