"""
s = {0, 2, 1, 2, 3, 0, 1 ,1} #集合の作成 {0, 1, 2, 3}
print(s)
print(type(s)) #データ型の確認 <class 'set'>
"""
"""
s = {123, 1.23, (1, 2, 3), 123, 1.23} #異なるデータ型でも1つの集合として作成可能(int,floot,tuple) {1.23, 123, (1, 2, 3)}
print(s)

s = {123, 1.23, [1, 2, 3], 123, 1.23} #要素にリストや辞書といった更新のできるミュータブルなオブジェクトを含むことはできない
print(s)
"""
"""
a = [0, 2, 1, 2, 3, 0, 1 ,1]
s = set(a) #set関数を用いた集合の作成(set関数の引数には集合に変換したいオブジェクトを指定)
print(s)
"""
"""
s1 = set() #set関数を用いて空集合作成 <class 'set'>
s2 = {} #要素を持たない{}=辞書 <class 'dict'>
print(type(s1))
print(type(s2))
"""
"""
s = {0, 1, 2}
s.add(3) #集合に要素を追加
print(s)
"""
"""
s = {0, 1, 2}
s.remove(1) #集合の要素を削除
print(s)
"""
"""
s = {0, 1, 2}
s.clear() #集合の要素を全削除 set()
print(s)
"""
"""
a = [0, 2, 1, 1, 2, 3, 1]
s = frozenset(a) #要素の変更不可なfrozenset関数の作成 frozenset({0, 1, 2, 3})
#s.add(4) #エラー発生
#s.clear() #エラー発生
print(s)
"""
"""
s1 = {0, 1, 2}
s2 = {1, 2, 3}

s3 = s1 | s2 #|を用いた和集合の作成 {0, 1, 2, 3}
print(s3)

s4 = s1.union(s2) #union関数を用いた和集合の作成 {0, 1, 2, 3}
print(s4)
"""
"""
s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

s4 = s1 & s2 & s3 #&を用いた積集合の作成 {2}
print(s4)

s5 = s1.intersection(s2, s3) #intersection関数を用いた積集合の作成 {2}
print(s5)
"""
"""
s1 = {0, 1, 2}
s2 = {1, 2, 3}

s3 = s1 - s2 #-を用いた差集合の作成(含まれる集合を先、含まれない集合を後に記述) {0}
print(s3)

s4 = s1.difference(s2) #difference関数を用いた差集合の作成(含まれる集合のdifferenceメソッドを記述し、引数に含まれない集合を記述) {0}
print(s4)
"""
"""
s1 = {0, 1, 2}
s2 = {1, 2, 3}

s3 = s1 ^ s2 #^を用いた対称差集合の作成(片方にのみ含まれる要素) {0, 3}
print(s3)

s4 = s1.symmetric_difference(s2) #symmetric_difference関数を用いた対称差集合の作成 {0, 3}
print(s4)
"""
"""
s1 = {0, 1, 2}
s2 = {0, 1, 2, 3, 4}

print(s1 <= s2) #<=を用いたs1がs2の部分集合であるかの判定 (true)
print(s1.issubset(s2)) #issubset関数を用いたs1がs2の部分集合であるかの判定 (true)
"""
"""
s1 = {0, 1, 2}
s2 = {0, 1, 2, 3, 4}
s3 = {2, 1, 0}

print(s1 == s2) #==を用いた集合が等しいかどうかの判定(false)
print(s1 == s3) #順番は影響しない(true)
"""
"""
s1 = {0, 1, 2}
s2 = {0, 1, 2, 3, 4}
s3 = {2, 1, 0}

print(s1 < s2) #<を用いたs1がs2の真部分集合(部分集合かつ等しくない)かどうかの判定(true)
print(s1 < s3) #部分集合かつ等しいのでNG(false)
"""
"""
s1 = {0, 1, 2}
s2 = {3, 4, 5}
s3 = {2, 3, 4}

print(s1.isdisjoint(s2)) #isdisjoint関数を用いた互いに素であるかの判定(true)
print(s1.isdisjoint(s3)) #(false)
"""
"""
s = {1, 2, 3, 4, 5}

print(1 in s) #要素の存在確認(true)
print(0 in s) #要素の存在確認(false)
"""
"""
s = {4, 3, 2, 1}
for i in s: #要素の順番がないためインデックスは使えない。for文の使用、取り出す順番は要素の並び順とは限らない。
    print(i)
"""
"""
s = {1, 2, 3, 4}
l = list(s) #集合をリスト化して指定した要素を取り出す

print(l[0])
"""
