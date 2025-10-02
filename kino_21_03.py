"""
class Student: #親クラス

    job = "junior nigh school student" #クラス変数

    def __init__(self, name, age): #name,age:インスタンス関数
        self.name = name
        self.age = age

studentA = Student("Yamada", 15)
print(studentA.job)
print(studentA.name)
print(studentA.age)

studentB = Student("Sato", 12)
print(studentB.job)
print(studentB.name)
print(studentB.age)
"""
"""
class Student: #親クラス

    job = "junior nigh school student" #クラス変数
    age = 13

    @classmethod #クラスメソッド
    def add_age(cls):
        cls.age += 1
        return cls.age

    def __init__(self, name, age): #name,age:インスタンス関数
        self.name = name
        self.age = age

studentA = Student("Yamada", 15)
print(Student.add_age())
"""

class Student: #親クラス

    job = "junior nigh school student" #クラス変数
    age = 13

    @classmethod #クラスメソッド
    def add_age(cls):
        cls.age += 1
        return cls.age

    @staticmethod #スタティックメソッド
    def greeting():
        print("hello")
        print(f"I am {Student.age}")

    def __init__(self, name, age): #name,age:インスタンス関数
        self.name = name
        self.age = age

Student.greeting()
