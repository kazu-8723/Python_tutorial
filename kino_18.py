"""
a = 1

def func():
    b = 2

print(globals()) #名前空間の確認
"""
"""
def func():
    b = 2

print(b) #スコープ 今回の場合、関数内で定義されたbを外から参照することは不可
"""
"""
a = 1 #グローバルスコープ　モジュール内のどこからでも参照可能

def func():
    b = 2
    print(a)

print(a)
func()
"""
"""
def func():
    a = 1 #ローカルスコープ　関数内で参照可能
    print(a)

func()

def func():
    a = 1

print(a) #関数外から参照不可
"""
"""
a = 1 #グローバル変数

def func():
    a = 2 #ローカル変数
    print(a)

func() #関数内の2が表示
print(a) #関数外の1が表示
"""
"""
a = 1

def func():
    print(a)
    a = 2 #グローバル変数よりもローカル変数が優先されるため、この場合エラーになる

func()
"""
"""
a = 1 #グローバルスコープ　モジュール内のどこからでも参照可能

def func():
    a = 2
    print(locals()) #関数を呼び出したスコープの名前空間を取得

func()
print(locals())
"""
"""
a = 1

def func1():
    a = 2

    def func2():
        a = 3
        print(a)

    func2()
    print(a)

func1()
print(a)
"""
"""
a = 1

def func1():
    a = 2

    def func2():
        global a #ローカル変数をグローバル変数として定義
        a = 3
        print(a)

    func2()
    print(a)

func1()
print(a)
"""

a = 1

def func1():
    # nonlocal a　1つ外側がグローバルスコープなので適用されない
    a = 2

    def func2():
        nonlocal a #func1に3が適用される
        a = 3
        print(a)

    func2()
    print(a)

func1()
print(a)
