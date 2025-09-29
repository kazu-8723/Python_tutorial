"""
def say_hello(): #関数の定義(引数無し)
    print("Hello World")

say_hello()
"""
"""
def say_hello(greeting): #関数の定義(引数有り)
    print(greeting)

say_hello("Hello World")
"""
"""
def say_hello(greeting):
    print(greeting)

hello = say_hello #関数を変数に代入
hello("Hello World")
"""
"""
def add(num01, num02): #複数の引数がある関数の定義
    print(num01 + num02)

add(6, 2)
"""
"""
def add(num01, num02):
    return(num01 + num02) #戻り値

# print(add(6, 2))
add_result = add(6, 2) #結果を変数に代入してprint関数で表示
print(add_result)
"""
"""
def show_number(a = 1, b = 2): #デフォルト引数
    print(a)
    print(b)

show_number() #引数を渡すと上書きされる
"""
"""
def show_number(a, b, c):
    print(a)
    print(b)
    print(c)

show_number(a = 1, c = 10, b = 100) #キーワード引数
"""
"""
def show_number(a, b, *args): #可変長位置引数(複数の引数を1つのタプルとして受け取る)
    print(a)
    print(b)
    print(args)
    print(*args) #タプルが展開されて表示
show_number(1, 2, 3, 4, 5)
"""
"""
def show_number(**kwargs): #可変長キーワード引数(複数の引数を1つの辞書として受け取る)
    print(kwargs)

show_number(a =1, b = 2, c = 3)
"""
"""
def outer_func(a, b): #2
    def inner_func(c, d):
        return c - d #4

    x = inner_func(2, 1) #3
    y = inner_func(a, b) #3
    print(x)
    print(y) #5
outer_func(3, 1) #1
"""
"""
def circle_area(pi):
    def calculation(radius): #クロージャー(関数の外で宣言された変数・引数を保持)
        return pi * radius * radius
    return calculation

area1 = circle_area(3.14)
area2 = circle_area(3)

print(area1(2))
print(area2(2))
"""
"""
def info(func):
    def wrapper(a, b):
        print("start")
        func(a, b)
        print("finish")
    return wrapper

@info #デコレーター
def add(a, b):
    print(a + b)

add(1, 2)
add(3, 4)
"""

def info(func):
    def wrapper(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("finish")
    return wrapper

@info #デコレーター
def add(a, b):
    print(a + b)

@info #デコレーター
def add2(c, d, e):
    print(c + d + e)

add(1, 2)
add2(3, 4, 5)
