# <1 > 写経してみよう

# ----function 関数--------------------------

###Basic

# def add(a,b):
#   return a + b

# result = add(10,20)
# print(result)

### Argument default value

# def pow(a,b=2):
#   return a ** b

# result = pow(10)
# print(result)

###keyword arguments

# def create_date(
#   year=0,month=0,date=0):
#   return str(year) + "/" + str(month) + "/" + str(date)

# print(create_date(year=2017,date=10))

###Multiple return

# def get_user():
#   return 'Yohei',30

# name,age = get_user()

# print(name)
# print(age)


# ----read / write a file ファイルの読み書き-------------------------

### Wtire a file.

# f = open("python.txt","w")
# f.write("Hello")
# f.close

###Read a file.

# f = open("python.txt")
# txt = f.read()
# print(txt)
# f.close

###Append a file.(追加書き込み)

# f = open("python.txt","a")
# f.write("Hi")
# f.close()

###using With

# with open ("python.txt") as f:
#   txt = f.read()
#   print(txt)

# ----class クラスの使い方-------------------------

##Class and Constructor.

# class User:
#   def __init__(self,name):
#     self.name = name
    
#   #Method
#   def say(self,name):
#     print("Hello" + self.name)
    
# ##Instance.
# user = User("Yohei")
# print(user.name)

# # Use method.
# user = User()
# user.say("Yohei")


# <2> 関数--------------------------------------

# def profile(x,y=20):
#   print("私の名前は" + x + "で" + str(y) + "歳です")
#   print("私の名前は%sで%d歳です " % (x, y))
  
# profile("たけし")

# <3> Python のクラスをさらに学ぼう---------------

#-----クラスの基礎----------

##クラスの定義
# class MyClass(object):
#   pass

##クラスからインスタンスを作成
# me = MyClass()
# print(me) # => <__main__.MyClass object at 0x100799b00>

#-----

## 何も要素を持たないクラス
# class EmptyClass(object):
#     pass

## 要素を好きなように定義できるので、複数の変数をまとめた入れ物として扱える
# holder = EmptyClass()
# holder.name = "Yohei"
# holder.age = 30
# print(holder.name, holder.age)  # => Yohei 30

#-----インスタンス変数とインスタンスメソッド

# class MyClass(object):
# クラス直下に定義した変数はクラス変数
# インスタンス変数ではない
# some_field = "aaa"

# インスタンス生成時に、値を渡すことができる
# def __init__(self, name, age):
#     # 「self.xxx」でインスタンス変数の参照/代入ができる
#     self.name = name
#     self.age = age

# インスタンスメソッドの定義
# def introduce(self):
#     print("My name is %s, %d years old." % (self.name, self.age))

# インスタンス化
# me = MyClass('Yohei', 30)
# me.introduce()  # => My name is Yohei, 30 years old.

# 直接値を代入することもできる
# me.name = "Taro"
# me.age = 25
# me.introduce()  # => My name is Taro, 25 years old.


#-----クラス変数とクラスメソッドとスタティックメソッド

# class MyClass(object):
#     # クラス直下に定義すると、クラス変数になる
#     primary_key = "id"

#     # クラスメソッドは「@classmethod」を付与して定義する
#     @classmethod
#     def show_primary_key(cls):
#         print("PrimayKey is %s" % cls.primary_key)


# クラス変数やクラスメソッドへのアクセスは、インスタンス化する必要ない
# print(MyClass.primary_key)  # => id
# MyClass.show_primary_key()  # => PrimayKey is id

#------スタティックメソッド

# class MyClass(object):
#     primary_key = "id"

#     @classmethod
#     def show1(cls):
#         print(cls.primary_key)

#     # スタティックメソッドは「@staticmethod」を付与して関数を定義します
#     @staticmethod
#     def show2():
#         print(MyClass.primary_key)


# MyClass.show1()  # => id
# MyClass.show2()  # => id

#-----クラスメソッドとスタティックメソッドでは、継承した場合に挙動が変わる

# class MySubClass(MyClass):
#     primary_key = "subid"

# MySubClass.show1()  # => subid MySubClass.primary_keyを取得
# MySubClass.show2()  # => id MyClass.primary_keyを取得

#-----クラスの継承

# 人を表すクラス（親クラス）
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sayHi(self):
#         print("Hi, my name is %s, %d years old." % (self.name, self.age))

#  %s → 文字列
#  %d → 整数

# 仕事人を表すクラス（子クラス）
# class Worker(Person):
#     def __init__(self, name, age, skills):
#         # 親クラスの関数を使う場合には、super()を使う
#         super().__init__(name, age)
#         self.skills = skills

#     def show_skills(self):
#         # 親クラスの変数も参照できる
#         print("%s's skills are %s" % (self.name, self.skills))

# インスタンス化
# w = Worker("Yohei", 30, ["html", "js", "css"])
# # 親クラスのメソッドも呼び出せる
# w.sayHi()
# w.show_skills()


### インスタンス変数、インスタンスメソッド、クラス変数、クラスメソッド、スタティックメソッド、継承の使い分け


