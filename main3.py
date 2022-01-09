# <4> その他

#-------位置引数のタプル化---------

# *を使って位置引数をタプルとして受け取れる
# def print_args(*args):
#     print("Positional arguments tuple:", args)

#以下のように引数をいくつでも指定することができる

# 引数なしで呼び出した
# print_args()
# Positional arguments tuple: ()

# 引数を3つ指定して呼び出した
# print_args("a", "b", "c")
# Positional arguments tuple: ('a', 'b', 'c')


#Pythonの関数の引数には2種類ある 「位置引数」と「キーワード引数」
# def do_something(arg1, arg2, arg3):
#     print(arg1, arg2, arg3)

# 位置引数を用いて関数を呼び出す
# do_something("a", "b", "c")
# a b c

# キーワード引数を用いて関数を呼び出す
# do_something(arg1="a", arg2="b", arg3="c")
# a b c


# *を用いた位置引数のタプル化は、必須の引数と組み合わせても使うことができる

# 必須引数と位置引数の組み合わせ
# def print_more(required1, required2, *args):
#     print("required1:", required1)
#     print("required2:", required2)
#     print("other:", args)


# 引数2個の場合
# print_more(1, 2)

# required1: 1
# required2: 2
# other: ()

# 引数3個の場合
# print_more(1, 2, 3)

# required1: 1
# required2: 2
# other: (3,)

# 引数5個の場合
# print_more(1, 2, 3, 4, 5)

# required1: 1
# required2: 2
# other: (3, 4, 5)

# 必須引数が足りなければエラー
# print_more(1)

# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# TypeError: print_more() missing 1 required positional argument: 'required2'

#タプルを用いて位置引数を関数に渡すこともできる

# 位置引数が2つの関数
# def say_hello(name, age):
#     print("Hi, my name is %s, %d years old" % (name, age))


# 関数に渡したい値をタプルで用意して、タプルで渡す
# user = ("Yohei", 30)
# say_hello(*user)
# Hi, my name is Yohei, 30 years old


#------キーワード引数の辞書化-------------

# **によるキーワード引数の辞書化
# def print_kwargs(**kwargs):
#     print("Keyword arguments:", kwargs)

# 引数を指定しない場合
# print_kwargs()
# Keyword arguments: {}

# キーワード引数を2つ指定した場合
# print_kwargs(num=1, text="aaa")
# Keyword arguments: {'num': 1, 'text': 'aaa'}

# 位置引数を指定したらエラー
# print_kwargs(1)
# Traceback(most recent call last):
#   File "<stdin>", line 1, in <module >
# TypeError: print_kwargs() takes 0 positional arguments but 1 was given


# *argsと**kwargsとの併用
# def print_args(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# 引数を指定しない場合
# print_args()
# Positional arguments: ()
# Keyword arguments: {}

# 位置引数のみ指定した場合
# print_args(1, 2, 3)
# Positional arguments: (1, 2, 3)
# Keyword arguments: {}

# キーワード引数のみ指定した場合
# print_args(name="Yohei", age=30)
# Positional arguments: ()
# Keyword arguments: {'name': 'Yohei', 'age': 30}

# 位置引数とキーワード引数を共に指定した場合
# print_args(1, 2, 3, name="Yohei", age=30)
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Yohei', 'age': 30}

# 引数が2つの関数
# def say_hello(name, age):
#     print("Hi, my name is %s, %d years old" % (name, age))

# 位置引数で指定できますし、
# say_hello("Yohei", 30)
# Hi, my name is Yohei, 30 years old

# キーワード引数でも指定できますし、
# say_hello(name="Yohei", age=30)
# Hi, my name is Yohei, 30 years old

# そしてなんと、辞書でも指定できます。
# user = {"name": "Yohei", "age": 30}
# say_hello(**user)
# Hi, my name is Yohei, 30 years old


#----リストのいろいろ------------------------------

#空のリストを作る
# list01 = list()
# list01 = []

#初期値を指定する
# list01 = ["a","b","c"]

#タプルからリストを作る
# aTapple = (1,2)
# list01 = list(aTapple)
# print(list01)  # =>[1, 2]

# セットからリストを作る
# aSet = set([1,2,3,4,5])
# list01 = list(aSet)  # =>[1, 2, 3, 4, 5]
# print(list01)

# 文字列から作る
# list01 = list("abcde") #=> ['a', 'b', 'c', 'd', 'e']
# print(list01)

# 文字列から作る
# list01 = "1,2,3,4,5".split(",") # => ['1', '2', '3', '4', '5']
# print(list01)

# レンジから作る
list01 = range(0,10) # => [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(list01))

# レンジで数値が小さくなるように作る
list01 = range(10, 1, -1) # => [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(list01))



###コーディング規約
###デコレーター
###演算子の定義
###ラムダ式
