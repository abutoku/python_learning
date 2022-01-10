###デコレーター

#デコレーターとは関数に@xxxをつけるものを指す

# デコレーター用の関数
# 引数に、デコレータ対象の関数を受け取る
# def document_it(func):
#     # """デコレータ対象の関数について、関数名 / 引数の内容 / 実行結果を表示する"""
#     def new_function(*args, **kwargs):
#         # デコレータ付与先の関数名
#         print("Runnning function:", func.__name__)
#         # デコレータ付与先の関数が受け取る位置引数の一覧
#         print("Positional arguments:", args)
#         # デコレータ付与先の関数が受け取るキーワード引数の一覧
#         print("Keyword arguments:", kwargs)
#         # 実行する
#         result = func(*args, **kwargs)
#         # デコレータ付与先の関数の結果を表示する
#         print("Result:", result)
#         # デコレータ付与先の関数の結果を返却する
#         return result
#     return new_function
  

# 上記の関数を以下のようにデコレーターとして設定
# @document_it
# def add_ints(a, b):
#     return a + b

#実行
# add_ints(1, 2)

# Runnning function: add_ints
# Positional arguments: (1, 2)
# Keyword arguments: {}
# Result: 3
# 3

#付与対象の関数の結果を変化させることもできる

# デコレート対象の関数の結果を二乗する
# def square_it(func):
#     def square_it_new_function(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return square_it_new_function

# @square_it
# def add_ints(a, b):
#     return a + b

# # 実行結果が二乗される
# print(add_ints(1, 2)) # 9

#複数のデコレーターを付与した場合の実行順序
#関数に最も近いデコレーターから実行される

# 実行順を見える化するために、printを各所に追加
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print("document_it starts")
#         print("Runnning function:", func.__name__)
#         print("Positional arguments:", args)
#         print("Keyword arguments:", kwargs)
#         result = func(*args, **kwargs)
#         print("Result:", result)
#         print("document_it ends")
#         return result
#     return new_function

# 同じく、printを追加
# def square_it(func):
#     # 関数名もdocument_itを変えています
#     def square_it_new_function(*args, **kwargs):
#         print("square_it starts")
#         result = func(*args, **kwargs)
#         print("square_it ends")
#         return result * result
#     return square_it_new_function
  
# デコレーターを2つ付与
# @document_it
# @square_it
# def add_ints(a, b):
#     return a + b


# 実行した結果は以下の通り
# print(add_ints(1, 2))

# document_it starts
# # document_itが受け取る関数は、square_it_new_functionとなっている
# Runnning function: square_it_new_function
# Positional arguments: (1, 2)
# Keyword arguments: {}
# # 関数の処理としては、squre_itから実行される
# square_it starts
# square_it ends
# Result: 9
# document_it ends
# 9

# デコレーターを逆順にしてみると、実行順序が変わる
# @square_it
# @document_it
# def add_ints(a, b):
#     return a + b


# 実行した結果は、以下
# add_ints(1, 2)

# square_it starts
# document_it starts
# # 今回の場合は、document_itデコレーターはadd_intsを関数として受け取っている
# Runnning function: add_ints
# Positional arguments: (1, 2)
# Keyword arguments: {}
# Result: 3
# document_it ends
# square_it ends
# 9



###演算子の定義

#__init__()メソッド
# 自作のクラスに __init__() メソッドを定義しておけば、
# インスタンスの生成時に __init__() が自動で呼び出される

#__add__()メソッド
# + 演算子に対応した特殊メソッド

# class Array(object):
#     def __init__(self, values):
#         """インスタンス生成時に呼び出されるメソッド
#            values には数字を格納したリストを渡す
#         """
#         self.values = values

#     def __add__()(self, other):
#         """+ 演算子を定義するメソッド
#            values 内の要素同士を足し合わせた新しい Array インスタンスを返す """
#         return Array(list(map(lambda x, y: x + y,
#                           self.values,
#                           other.values)))


# m1 = Array([3, 5])
# m2 = Array([10, 11])

# m3 = m1 + m2
# print(m3.values)

# => [13, 16]
# `` __add__() `` メソッドで定義したとおりの結果となっている


#__mul__()メソッド
# * 演算子に対応したメソッドです。 mul というのは multiply ・ multiplication の略

# class Array(object):
#     # ここに __init__ などの定義
#     # ...

#     def __mul__()(self, other):
#         """* 演算子を定義するメソッド
#            values 内の要素同士をかけ合わせた新しい Array インスタンスを返す """
#         return Array(list(map(lambda x, y: x * y,
#                           self.values,
#                           other.values)))


# m1 = Array([3, 5])
# m2 = Array([10, 11])

# m4 = m1 * m2
# print(m4.values)
# => [30, 55]
# __mul__() メソッドで定義したとおりの結果となっている
#__add__() と同様の結果が得られている

# __lshift__()メソッド
# << 演算子に対応したメソッド

# class Array(object):
#     # ここに __init__ などの定義
#     # ...

#     def __lshift__()(self, new_element):
#         """<< 演算子を定義するメソッド
#            新しいオブジェクトは生成せず values の末尾に要素を append する（破壊的メソッド） """
#         self.values.append(new_element)
#         return self


# m1 = Array([3, 5])

# m1 << 10
# print(m1.values)
# => [3, 5, 10]
# こちらも __lshift__() で定義したとおりの結果となっている


#__iadd__()メソッド
#+= 演算子に対応したメソッド

# class Array(object):
#     # ここに __init__ などの定義
#     # ...

#     def __iadd__()(self, element):
#         """+= 演算子を定義するメソッド
#           values の各要素に渡された値を加算する """
#         self.values = list(map(lambda x: x + element, self.values))
#         return self


# m1 = Array([3, 5])

# m1 += 1
# print(m1.values)
# => [4, 6]

# こちらも __iadd__() で定義したとおりの結果
# オブジェクト id も不変
# 戻り値はレシーバ自身にしないと（ return self としておかないと）うまく動いてくれません


###ラムダ式
#--- lambda 引数:返り値

##Pythonではlambda式を使って無名関数を作ることができる
##無名関数は、一度だけしか使われない使い捨ての関数のこと
##一度きり使うだけなので、名前をつける必要がない

# num = (lambda x, y: x + y)(3, 4)
# print (num )  # 7


## lambdaは式なので、defと異なり関数をプログラムの様々なところで作ることができる

# 引数を2乗するpow()の定義
# def pow(x):
#     return x * x

# map()でリストの各要素にpow()を適用
# print (list(map (pow, [2,3,4])))  # [4, 9, 16]

#ambdaを使った無名関数
# print (list(map(lambda x:x * x, [2,3,4])))  # [4, 9, 16]
