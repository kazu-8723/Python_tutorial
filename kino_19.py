"""
print("Python", "Ruby", "PHP", sep = "-", end = "~") #sepで引数の間を指定した文字列で埋められる
print("Java")
"""
"""
print(type("Hello")) #str
print(type(10)) #int
print(type([1, 2, 3])) #list
print(type({"Python":1, "Ruby":2, "PHP":3})) #dict

print(type("Hello") is str) #true
print(type("Hello") is int) #false
"""
"""
a = "10.0"

print(float(a))
print(type(float(a)))
"""
"""
print(10 / 3)
print(0.1 * 2 == 0.2)
print(0.1 * 3 == 0.3)
"""
"""
print(round(1.234, 2)) #小数第二位に丸める

print(round(1.5)) #第二引数を省略すると整数に丸められる(四捨五入ではなくより近い整数に)
print(round(2.5))
print(round(2.501))

print(round(1234.56, -2)) #-は正の数　この場合は100の位で丸められる
"""
"""
print(bool(2 > 1))
print(bool(2 < 1))
"""
"""
print(len("Hello")) #要素の数
print(len((1, 2, 3, 4, 5)))
"""
"""
x = [1, 2, 3, 4]
print(sum(x)) #要素の合計値
print(sum(x, 100)) #第二引数も合計される
"""
"""
x = [1, 2, 3, 4]
print(max(x)) #要素の最大値

x = ["Python", "Javascript", "PHP"]
print(max(x)) #1文字目で判断

x = ["Python", "Javascript", "PHP"]
print(max(x, key = len)) #要素の数で判断

x = {"a":3, "b":2, "c":1}
print(max(x)) #辞書を引数に渡すと、キーの最大値が返される
print(max(x.values())) #数字の最大値を得るにはvaluesメソッドを使用
"""
"""
x = [1, 2, 3, 4]
print(min(x)) #要素の最小値

x = ["Python", "Javascript", "PHP"]
print(min(x)) #1文字目で判断

x = ["Python", "Javascript", "PHP"]
print(min(x, key = len)) #要素の数で判断
"""
"""
print(range(5)) #連続した整数値を要素に持つオブジェクト作成
print(type(range(5)))

for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(5, 10, 2):
    print(i)
"""
"""
name = ["Python", "Ruby", "PHP"]
number = [10, 100, 1000]

print(zip(name, number)) #複数のリストやタプルに入った要素をまとめたオブジェクトを作成
print(type(zip(name, number)))

for i in zip(name, number):
    print(i)

for i, j in zip(name, number):
    print(i)
    print(j)
"""

name = ["Python", "Ruby", "PHP"]

print(enumerate(name)) #リストやタプルの要素とインデックスをまとめたオブジェクトを作成
print(type(enumerate(name)))

for i in enumerate(name):
    print(i)

for i, j in enumerate(name):
    print(i)
    print(j)
