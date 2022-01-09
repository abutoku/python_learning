# <1> 写経してみよう

# -----loop-----------------------------------

# for i in range(10):
#   print(i)

# for item in ["a","b","c"]:
#   print(item)

# my_life = 5
# while my_life:
#   print(my_life)
#   my_life -= 1

# idx = 0
# while True:
#   if idx > 5:
#     break
#   print(idx)
#   idx += 1


# ----variables 変数--------------------------

###Define

# my_name = "Yohei"
# age = 20
# is_good = True
# unittest = 1

###Check type

# print(type(my_name)) データ型の確認

###Concat

# print(my_name + age) =>Error
# print(my_name + str(age))

# ----list リスト型 (配列形式）---------------

###Create

# users = [
#   "Yo","Ken","Nao","Shin","Lee"
# ]

###index access

# print(users[0])
# print(users[0:2])
# print(users[1:])
# print(users[::2])
# print(users[::-1])

###Add

# users.append("Miu")
# print(users)

###Delete

# users.remove("Nao")
# print(users)

# ----list comprehension リスト内包表記--------

# users = ["Yo","Ken","Nao","Shin","Lee"]
# users = [u.lower() for u in users if u.find("e") != -1] #lower小文字にする

# print(users)

# ----dictionary 辞書型 key-valueで値を保持-----

###Create
# user_dict = {
#   "Yohei":30,
#   "John":35
# }

####Get 
# print(user_dict["Yohei"])
# print(user_dict.get("Nao",20)) #値がなかった場合の初期値

###Get all
# for k,v in user_dict.items():
#   print(k,v)

### Update / Delete

# user_dict["Yohei"] = 31
# print(user_dict["Yohei"])

# del user_dict["John"]
# print(user_dict)

# ---set セット型 重複がなく、順序を持たないデータの集合-------

#インデックス番号は使えない

###Create

# set_ = {
#   "Tennis","Ramen","Programming"
# }

###Get

# set_[0] # =>Error!!

# for s in set_:
#   print(s)


###Add / Delete

# set_.add("Gs")
# print(set_)

# set_.remove("Ramen")
# print(set_)

###Calc

#set()でも発行できる
#集合演算子

# set1 = set([1,2,3,4,5,])
# set2 = set([3,4,5,])
# print(set1 - set2)

# ---tuple イミュータブル（変更できない）リスト構造----

###Create

# nums = "One","Two","Three"
# nums = ("One","Two","Three")


###Get

# print(nums[0])

# for n in nums:
#   print(n)

###Immutable
#変更しようとするとエラー

#nums[0] = "Zero" # =>Error!

###Assign 

# a,b,c = nums
# print(a,b,c)

#<2> 文字列とインデックスアクセス

# sample = "じこーだすまあさかんでのみしーゅっみてはたなのんしだいろな"

##奇数
# odd = (sample[::2]) 
# print(odd)

##偶数
# even = (sample[1::2])
# print(even)


#<3> Setの練習

# set_ = set('「ではみなさんは、そ
# 

# <4 > リスト内包表記

# price = [str(i) + '円' for i in range(0,101)]
# print(price)


# -----クラスを学ぼう---------------------------------

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


