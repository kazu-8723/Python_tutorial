"""
a = ['sato', 'suzuki', 'kato'] #リスト作成
print(a) #表示

a[1] = 'tanaka' #要素変更
print(a)
"""
"""
a = [['sato', 'suzuki'], ['tanaka', 'hoshino']] #リストのネスト
print(a[0][0])
print(a[1][1])
print(a[0][1])
print(a[1][0])
"""
"""
a = ['sato', 'suzuki', 'kato'] #リストの足し算
a = a + ['hoshino', 'takanashi']
print(a)

a = ['sato', 'suzuki', 'kato'] * 2 #リストの掛け算
print(a)
"""
"""
a = ['sato', 'suzuki', 'kato']
a.append('tanaka') #末尾に要素の追加
a.append(['hoshino', 'takanashi']) #リストがそのまま末尾に追加
print(a)
"""
"""
a = ['sato', 'suzuki', 'kato']
a.extend(['hoshino', 'takanashi']) #リスト内の要素を分解して末尾に追加
print(a)
"""
"""
a = ['sato', 'suzuki', 'kato']
a.insert(0, 'yamane') #リストの指定した位置に要素を追加
print(a)
"""
"""
a = ['sato', 'suzuki', 'kato']
del a[1] #リストの指定した要素の削除
print(a)
"""
"""
a = ['sato', 'suzuki', 'kato']
print(a.pop(1)) #リストの指定した要素の削除と削除した要素の表示
print(a)
"""
"""
a = ['sato', 'suzuki', 'kato']
a.remove('suzuki') #リストの指定した要素を検索し削除
print(a)
"""
"""
a = ['sato', 'suzuki', 'kato']
a.clear() #リストの全要素の削除
print(a)
"""
"""
a = ['sato', 'suzuki', 'kato']
print('sato' in a) #リストに指定した要素が含まれているか検索(true)
print('tanaka' in a) #(false)
"""
"""
a = ['sato', 'suzuki', 'kato', 'sato']
print(a.count('sato')) #リストに何個指定した要素が含まれているか検索(2)
print(a.count('tanaka')) #(0)
"""
"""
a = ['sato', 'suzuki', 'kato']
print(a.index('sato')) #指定した要素が何番目にあるか取得(0)
print(a.index('tanaka')) #存在しないのでエラーが出る
"""
"""
a = [8, 3, 1, 7, 4]
a.sort() #リストの並び替え(小さい順)
print(a)
a.sort(reverse = True)
print(a) #大きい順
"""
"""
a = ['sato', 'suzuki', 'kato']
a.reverse() #リストの要素を逆転
print(a)
"""
"""
a = [8, 3, 1, 7, 4]
print(max(a)) #要素の最大値の取得
print(min(a)) #要素の最小値の取得
print(a.index(max(a))) #要素の最大値のインデックス(位置)の取得
"""
"""
a = ['sato', 'suzuki', 'kato']
print(len(a)) #リストの要素数の取得
"""
