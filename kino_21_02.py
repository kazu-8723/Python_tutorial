"""
class Student: #親クラス
    def math(self, score):
        print(score)

class Grade1(Student): #子クラス(継承)
    def english(self, score):
        print(score)

studentA = Student()
studentB = Grade1()
studentA.math(50)
studentB.math(60)
studentB.english(70)
"""
"""
class Student: #親クラス
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def math(self, score):
        print(score)

class Grade1(Student): #子クラス(継承)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Name : ", self.name) #オーバーライド
        print(" Age : ", self.age)

    def english(self, score):
        print(score)

studentA = Student("Yamaada", 15)
studentB = Grade1("Sato", 12)
"""
"""
class Student: #親クラス
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def math(self, score):
        print(score)

class Grade1(Student): #子クラス(継承)
    def __init__(self, name, age):
        super().__init__(name, age) #親クラスのメソッドを継承
        print("Name : ", self.name) #オーバーライド
        print(" Age : ", self.age)

    def english(self, score):
        print(score)

studentA = Student("Yamaada", 15)
studentB = Grade1("Sato", 12)
"""
