"""
x = 10
y = 3

print(x / y) #割り算 3.3333333333333335
print(x % y) #剰余 1
print(x // y) #商 3
"""
"""
x = 10
y = 3

print(x > y) #関係演算子(true)
print(x < y) #(false)
"""
"""
x = 10
y = 3
z = 10

print(x <= y) #関係演算子(false)
print(x >= z) #(true)
"""
"""
x = 10
y = 3

print(x == y) #等価ではない(false)
print(x != y) #等価(true)
"""
"""
x = 8
y = 3

print(x >= 5 and x <= 10) #論理演算子 "かつ" (true)
print(y >= 5 and y <= 10) #(false)

print(x == 3 or y == 3) #論理演算子 "または" (true)
print(x == 1 or y == 1) #(false)
"""
"""
x = 8
y = 12
z = 20

x += 10 #複合代入演算子 x = x + 10と同義
z -= y # z = z -yと同義

print(x) #18
print(z) #8
"""
"""
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
l3 = l1

print("l1 == l2 :",l1 == l2) #同じ値を持っているのでtrue
print("l1 is l2 :",l1 is l2) #同じ値でも違うオブジェクトなのでfalse
print("l1 == l3 :",l1 == l3) #l3はl1を代入しているため、同じ値かつ同じオブジェクトなのでtrue
print("l1 is l3 :",l1 is l3) #同上のためtrue

print("l1_id :",id(l1)) #l3と同じid=同じオブジェクト
print("l2_id :",id(l2)) #l1と異なるid=違うオブジェクト
print("l3_id :",id(l3)) #l1と同じid=同じオブジェクト
"""
"""
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
l3 = l1

print(l1, id(l1))
l1.append(6)
print(l1, id(l1)) #要素を追加してもidは不変 [1, 2, 3, 4, 5, 6]

print(l2) #l1と異なるオブジェクトのため変更されない [1, 2, 3, 4, 5]
print(l3) #l1と同じオブジェクトのため、変更される [1, 2, 3, 4, 5, 6]
"""
"""
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
l3 = l1

print("    l1 is l2 :",l1 is l2) # 同じ値でも違うオブジェクトなのでfalse
print("l1 is not l2 :",l1 is not l2) #同じ値でも違うオブジェクトなのでtrue
print(".   l1 is l3 :",l1 is l3) #l3はl1を代入しているため、同じ値かつ同じオブジェクトなのでtrue
print("l1 is not l3 :",l1 is not l3) #同じ値かつ同じオブジェクトなのでfalse
"""
"""
l = ['sato', 'tanaka', 'ito']

print("    sato in l :", 'sato' in l) #lの中にsatoが存在するのでtrue
print("sato not in l :", 'sato' not in l) #lの中にsatoが存在するのでfalse
print("    suzuki in l :", 'suzuki' in l) #lの中にsuzukiは存在しないのでfalse
print("suzuki not in l :", 'suzuki' not in l) #lの中にsuzukiは存在しないのでtrue
"""
"""
print(0b10) #0bが2進数表記の目印 2
print(0b100) #4
print(0b1010) #10

print(bin(2)) #bin関数を用いると10進数から2進数に変換可能 0b10
print(bin(4)) #0b100
print(bin(10)) #0b1010
"""
