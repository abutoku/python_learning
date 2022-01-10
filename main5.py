###デコレーター
###演算子の定義


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
