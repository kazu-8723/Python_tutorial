"""
for i in [0, 1, 2, 3, 4]: #5回同じ処理を繰り返す
    print(i)
"""
"""
for i in range(5): #5回同じ処理を繰り返す
    print(i)
"""
"""
for i in range(5):
    if i == 3:
        break #break文 3で繰り返しを終了0~2まで表示
    print(i)
"""
"""
for i in range(5):
    if i == 3:
        continue #continue文 3のときに処理をスキップ 0~2,4が表示される
    print(i)
"""
"""
for i in range(3):
    for j in range(3): # for文のネスト(同じものの中に同じものをいれること) 外側が1周する間に内側が全周、その繰り返し
        print(i, j, sep = "-")
"""
"""
string = ["Tokyo", "Osaka", "Nagoya"]
for i in string: #リストの中身が変数に1つずつ格納される
    print(i)
"""
"""
arr = [2, 4, 6, 8, 10]
sum = 0
for i in arr:
    sum += i #リスト内の数字を順に足し上げる
print(sum)
"""
"""
i = 0
while i < 5:
    print(i)
    i += 1 # i<5の間、iを表示(1ずつiに加算)
"""
"""
i = 1
while i < 100:
    print(i)
    i *= 2 # i<100の間、iを表示(2ずつiに乗算)
print("finish")
"""

i = 200
while True: # 無限ループ
    print(i)
    i *= 2
    if i >= 100:
        break
print("finish")
