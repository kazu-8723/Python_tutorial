"""
age = 22

if age >= 20: #if文
    print("adult")
"""
"""
age = 18

if age >= 20: #if~else文
    print("adult")
else:
    print("child")
"""
"""
age = 0

if age >= 20: #if~else文
    print("adult")
elif age == 0: #elif文
    print("baby")
else:
    print("child")
"""
"""
number = 21

if number % 2 == 0 and number % 3 == 0: # 変数を2と3で割ったそれぞれの余りが0
    print("6の倍数です")
elif number % 2 == 0 and number % 3 != 0: # 3で割り切れない場合
    print("2の倍数です")
elif number % 2 != 0 and number % 3 == 0: # 2で割り切れない場合
    print("3の倍数です")
else:
    print("2と3の倍数ではありません")
"""

fruit = "apple"
"""
if fruit == "apple":
    print("リンゴ")
elif fruit == "orange":
    print("オレンジ")
elif fruit == "grape":
    print("ブドウ")
elif fruit == "peach":
    print("モモ")
else:
    print("その他の果物")
"""
"""
match fruit: #match文 Python3.10から実装 上と同義
    case "apple":
        print("リンゴ")
    case "orange":
        print("オレンジ")
    case "grape":
        print("ブドウ")
    case "peach":
        print("モモ")
    case _:
        print("その他の果物")
"""
"""
age = 18

if age >= 20: #if~else文
    print("adult")
else:
    pass #何もしない 可読性を上げる
"""
"""
age = 18

if age >= 20: #if~else文
    print("adult")
else:
    print("child")


print("adult" if age >= 20 else "child") #三項演算子 上と同義
"""
