"""
class Student: #クラス定義
    def avg(self): #メソッド定義
        print((80 + 70) / 2)

a001 = Student() #変数にインスタンスを代入
a001.avg()
"""
"""
class Student: #クラス定義

    def __init__(self): #コンストラクタの定義
        self.name = ""

    def avg(self, math, english): #メソッド定義
        print((math + english) / 2)

a001 = Student() #変数にインスタンスを代入
a001.name = "sato" #アトリビュートの定義
print(a001.name)

a002 = Student()
a002.name = "tanaka"
print(a002.name)
"""
"""
class Student: #クラス定義

    def __init__(self, name): #コンストラクタの定義
        self.name = name

    def avg(self, math, english): #メソッド定義
        print((math + english) / 2)

a001 = Student("sato") #変数にインスタンスを代入
print(a001.name)

a002 = Student("tanaka")
print(a002.name)
"""
"""
class Student: #クラス定義

    def __init__(self, name): #コンストラクタの定義
        self.name = name

    def __del__(self): #デストラクタの定義
        print("delete")

person = Student("Yamada") #変数にインスタンスを代入
print(person.name)
del person #personに代入されたオブジェクトの削除
print("------------")
"""
