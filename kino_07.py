"""
a = ('sato', 'suzuki', 'kato') #タプルはリストと違い、()で囲う 要素の追加、削除、変更不可
print(a)
print(a[1]) #要素にアクセス
"""
"""
a = (0, 1, 2, 3, 4, 5)
print(a[1:4]) #開始位置と終了位置の取得(1は含まれ4は含まれない)
print(a[2:]) #(2は含まれ最後まで)
print(a[:2]) #(最初から2は含まれず)
print(a[::2]) #ステップして取得(0,2,4)
print(a[::-2]) #後ろからステップして取得(5,3,1)
"""
"""
a = (('aka', 'ao'), ('midori', 'kiiro')) #タプルの中にタプルを入れる
print(a[0][0]) #要素にアクセス
print(a[0][1])
print(a[1][0])
print(a[1][1])
"""
"""
a = ('sato', 'suzuki', 'kato')
b = a + ('tanaka', 'sato') #タプルの足し算
print(b)

a = ('sato', 'suzuki', 'kato') * 2 #タプルの掛け算
print(a)
"""
"""
a = ('sato', 'suzuki', 'kato')
print(a.index('sato')) #指定した要素が何番目にあるか調べる
print(a.index('tanaka')) #存在しないのでエラー
"""
"""
a = ('sato', 'suzuki', 'kato', 'sato')
print(a.count('sato')) #タプル内に指定した要素が幾つあるか取得
"""
"""
a = ('sato', 'suzuki', 'kato')
print('sato' in a) #タプル内に指定された要素が存在するか調べる(true)
print('tanaka' in a) #(false)
"""
"""
a = (8, 3, 5, 1, 2)
print(sorted(a)) #小さい順に並び替え
a = sorted(a, reverse = True) #大きい順に並び替え
print(a)
print(max(a)) #タプルの最大値の取得
print(min(a)) #タプルの最小値の取得
"""
"""
l = ['a', 'b', 'c']
a = tuple(l) #リスト型からタプル型へ変換
print(a)
print(type(a)) #型が変換されているか調べる
"""

s = 'python'
a = tuple(s) #文字列をタプル型へ変換('p', 'y', 't', 'h', 'o', 'n')
print(a)
print(type(a)) #型が変換されているか調べる
