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

#####リストを生成する######

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
# list01 = range(0,10) # => [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(list01))

# レンジで数値が小さくなるように作る
# list01 = range(10, 1, -1) # => [10, 9, 8, 7, 6, 5, 4, 3, 2]
# print(list(list01))


#####値を追加する######

# list01 = ["a","b","c"]

# 後ろに追加
# list01.append("d")
# print(list01)

# 前に追加
# list01.insert(0, "z")
# print(list01)

# 任意の場所に追加
# list01.insert(2, "hoge")
# print(list01)

# 配列に配列を追加
# list01.extend([10, 20, 30, 10, 20, 30])
# print(list01)
# list02 = list01 + [1, 2, 3, 4, 5]
# print(list02)


#####値を削除する######

# 要素の削除（複数存在する場合は1つ目のみ）
# list01.remove("c")
# print(list01)

# 要素の削除（複数存在するものを全部）
# list01 = [item for item in list01 if item is not "c"]
# print(list01)

# list01 = filter(lambda a: a != "c", list01)
# print(list(list01))

# 位置を指定して削除（1件）
# del list01[0]
# print(list01)

# 位置を指定して削除（複数件）
# del list01[1:2]
# print(list01)

# 位置を指定して削除（全部）
# del list01[:]
# print(list01)

#####値の取得、出現回数、サイズ######

# list01 = [1, 2, 3, 4, 5]

# 範囲指定で取り出す
# 要素0〜1
# print (list01[0:2])

# 要素1〜後ろから2つ目まで
#print (list01[0:-1])

# 要素0〜2まで
# print (list01[:3])

# 要素3〜最後まで
# print (list01[3:])

# 2つ置きに取得する
# print(list01[::2]) # =>[1, 3, 5]

# 逆順に取得する
# print(list01[::-1]) # =>[5, 4, 3, 2, 1]

# 逆順に2つ置きに取得する
# print(list01[::-2])  # => [5, 3, 1]


# 指定した要素の位置を取得する
# index = list01.index(1)
# print(index)

# 最後の要素を取得して同時に削除する
# item = list01.pop()
# print(item)
# print(list01)

# 指定した位置の要素を取得して同時に削除する
# item = list01.pop(1)
# print(item)
# print(list01)


# 指定した要素の出現回数を取得する
# count = list01.count(2)
# print(count)

# サイズを確認する
# print(len(list01))

# 要素の存在確認
# list01 = [1, 2, 3, 4, 5]
# print (2 in list01)
# =>True
# print (6 in list01)
# =>False

#####値を変更する######

# list01 = ["a", "b", "c", "d"]

# 要素3の値を変更する
# list01[3] = "D"  # => ['a', 'b', 'c', 'D']
# print(list01)

# 要素0〜2を変更する
# list01[:3] = ["A", "B", "C"]  #=> ['A', 'B', 'C', 'D']
# print(list01)

# 一番後ろ〜の値を変更する（追加要素が多い場合は末尾に追加される）
# list01[-1:] = ["E", "F"] #=> ['A', 'B', 'C', 'E', 'F']
# print(list01)

#####ソートする######

# list01 = [2,5,3,1,8,6,7,4]

# ソートする（元のリスト自体をソートする）
# list01.sort()
# print(list01)

# ソートする（元のリストは変更しない）
# list02 = sorted(list01)
# print(list01)
# print(list02)

# ソート条件を指定する（cmp） ※ Python2系の場合
# >>> list01.sort(cmp=lambda x, y: x < y)
# >>> list01 = sorted(list01, cmp=lambda x, y: x < y)

# ソート条件を指定する（key） ※ Python3系の場合
# list01.sort(key=lambda x: x)
# print(list01)
# list01 = sorted(list01, key=lambda x: x)
# print(list01)

# ソートの前処理を指定する
# ["a", "AA", "Ab", "ac"].sort(key=str.lower)

# 逆順にソートする（元のリスト自体をソートする）
# list01.sort(reverse=True)
# print(list01)

# または（元のリストは変更しない）
# list02 = list(reversed(list01))
# print(list02)

#####リストをスタックとして使う######

# stuck = [3, 4, 5]

# stuck.append(6)
#=>[3, 4, 5, 6]

# stuck.pop() #=> 6
# print(stuck)  # => [3, 4, 5]

#####リストをキューとして使う######

# リストのappendとpop(0)で実現できるが、
# pop(0)を行うと全要素の位置を変更するため処理が遅い
# 代わりに以下の実装を利用すると高速

# from collections import deque

# queue = deque(["A", "B", "C"])
# =>deque(['A', 'B', 'C'])

# queue.append("D")
# => deque(['A', 'B', 'C', 'D'])
# print(queue)

# queue.popleft()
# =>'A'
# print(queue)

# queue
# => deque(['B', 'C', 'D'])


#####関数プログラミング（filter、map、reduce)######


#####リスト内包表記######
# list01 = range(1, 6) # =>[1, 2, 3, 4, 5]
# print(list(list01))

# list01 = [i * 2 for i in list01] #=>[2, 4, 6, 8, 10]
# print(list(list01))

# print ([i * 2 for i in range(10)])
# print ([i * 2 for i in range(10) if i % 2 is 1])

# 異なる組み合わせを全て抽出
# print ([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

#####ループ処理######

# list01 = list("abcde")

# 1件ずつ処理する
# for item in list01:
#   print(item)

# ループ処理（indexも一緒に取得したい）
# for i, v in enumerate(list01):
#   print (i, v)

# ループ処理（2つの配列を同時に処理する）
# firstNames = ["a", "b", "c"]
# lastNames = ["A", "B", "C"]
# for f, l in zip(firstNames, lastNames):
#   print (f, l)

# ループ中に、ループ対象のリストを処理する
# list01 = list(range(10))

# for i in list01[:]:
#   if i % 3 is 0:
#     list01.append(i)
    
# print(list(list01))




