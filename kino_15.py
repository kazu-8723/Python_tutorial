"""
l1 = [] #空のリスト
for i in range(5): #for文で作成
    l1.append(i) #リストにカウンタ変数を加えていく

l2 = [i for i in range(5)] #内包表記
l3 = [i / 2 for i in range(5)] #forの前のカウンタ変数を計算式にすることも可能

print(l1)
print(l2)
print(l3)
"""
"""
s = {i for i in range(5)} #集合内包表記
s = {i / 2 for i in range(5)}
print(s)
"""
"""
d = {i : i * 2 for i in range(5)} #辞書内包表記　キー:値

print(d)
"""
"""
l = [i for i in range(10) if i % 2 == 0] #条件付き内包表記(i%2=0のときのみリストに追加)

print(l)
"""
"""
d = {i : "even" if i % 2 ==0 else "odd" for i in range(10)} #偶数:even、奇数:oddの辞書 forが最後

print(d)
"""

l1 = []
for i in (10, 100, 1000):
    for j in (1, 2, 3):
        l1.append(i + j)

l2 = [i + j for i in (10, 100, 1000) for j in (1, 2, 3)] #内包表記のネスト

print(l1)
print(l2)
