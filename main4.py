###コーディング規約

#------インデント------------------

#-----行を継続する場合は、折り返された要素を縦に揃える

# 開きカッコで揃える（関数呼び出しの例）
# foo = long_function_name(var_one, var_two,
#                          var_three, var_four)

# if文の条件が長い場合には、以下のようにインデントを取る
# if (this_is_one_thing and
#         that_is_another_thing):
#     do_something()

# ただし、上記if文の場合には後続の行との違いがわからないので、以下にしてもOK
# 継続された行の条件をさらに深くインデントする
# if (this_is_one_thing
#         and that_is_another_thing):
#     do_something()

# NG：折り返された要素を縦に揃えていない
# foo = long_function_name(var_one, var_two,
#                          var_three, var_four)

#----- この行とそれ以外を区別するために、インデントを深くする
# インデントを深くする（関数定義の例）
# def long_function_name(
#         var_one, var_two, var_three,
#         var_four):
#     print(var_one)

# インデントを深くする（関数呼び出しの例）
# foo = long_function_name(
#     var_one, var_two,
#     var_three, var_four)

# NG：折り返したところのインデントが深くなく、他の行と区別できない
# def long_function_name(
#         var_one, var_two, var_three,
#         var_four):
#     print(var_one)


#-----行を継続して波カッコ/ブランケット/カッコを閉じる

# パターン1：改行後のインデントに合わせる場合
# my_list = [
#     1, 2, 3,
#     4, 5, 6
# ]

# result = some_function_that_takes_arguments(
#     'a', 'b', 'c',
#     'd', 'e', 'f'
# )

# パターン2：最初の行のインデントに合わせる
# my_list = [
#     1, 2, 3,
#     4, 5, 6
# ]

# result = some_function_that_takes_arguments(
#     'a', 'b', 'c',
#     'd', 'e', 'f'
# )


#-----1行の長さは79文字、72文字--------------------
# 行の長さは、 最大79文字以内に制限します。また、docstringやコメントのように構造制限が少ないものは、72文字以内に制限します。
# ただし、チームで合意できればそれより長くてもOK

#-----演算子の位置----------------------------------

# # 2項演算子は前に揃える
# income = (gross_wages
#           + taxable_interest
#           + (dividends - qualified_dividends)
#           - ira_deduction
#           - student_loan_interest)

#-----空行のルール----------------------------------

# トップレベルの関数やクラスは、2行ずつ空けて定義する
# クラス内部では、1行ずつ空けてメソッドを定義する
# 関連する関数のグループを分けるために、2行以上開けてもOK（ただし控えめに）

#-----import文のルール----------------------------------

###importはモジュールごとに行を分ける

# 良い例
# import os
# import sys

# 悪い例
# import os sys

#同じパッケージから複数のモジュールをインポートする場合には、列挙する書き方が推奨
# 同パッケージから異なるモジュールをインポート
# from subprocess import Popen, PIPE

###絶対importを推奨する
# 絶対importを推奨
# import mypkg.sibling
# from mypkg import sibling
# from mypkg.sibling import example


# 絶対importを使うと不必要に冗長になる複雑なパッケージレイアウトの時は、相対インポートの利用もOK
# from . import sibling
# from .sibling import example

###ワイルドカードを使ったインポートは絶対に避けたい

#ワイルドカードを使って、すべてのモジュールをインポートできますが、これはバグを生みやすいため、避けるべき

# どの名前が名前空間に存在しているかわかりにくく、
# 名前の上書きをしてしまった場合に、デバッグが非常にしづらい
# 悪い例：
# from somemodule import *

#-----式や文中の空白文字----------------------------------

###カッコ/ブランケット/波カッコの前後には空白を入れない
# 良い
# spam(ham[1], {eggs: 2})

# 悪い
# spam(ham[1], {eggs: 2})

###カンマ/セミコロン/コロンの直後に空白を入れる
# 良い
# if x == 4 print x, y; x, y = y, x

# 悪い
# if x == 4 print x , y ; x , y = y , x


# 良い
# ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
# ham[lower:upper], ham[lower:upper:], ham[lower:upper:step]
# ham[: upper_fn(x): step_fn(x)], ham[:: step_fn(x)]
# ham[lower + offset: upper + offset]

# 悪い
# ham[lower + offset:upper + offset]
# ham[1: 9], ham[1:9], ham[1:9:3]
# ham[lower:: upper]
# ham[: upper]

###関数呼び出しの引数リストを始める開きかっこの直前は無駄な余白を入れない

# 良い
# spam(1)

# 悪い
# spam (1)

#インデックスやスライスの開きかっこ直前も不要
# 良い
# dct["key"] = lst[index]

# 悪い
# dct ["key"] = lst [index]

#代入演算子を揃えるための、無駄な余白はダメ

# 良い
# x = 1
# y = 2
# long_variable = 3

# # 悪い
# x = 1
# y = 2
# long_variable = 3

#二項演算子は、両側に常に1つだけスペースを入れる
# 代入演算子（=）
# 拡張代入演算子（+=, -=）
# 比較演算子（ == , < , > , != , <> , <= , >= , in , not in , is , is not）
# ブール演算子（and , or , not）

# 良い例
# val1 = val2 + val3
# val4 = val4 and val5

#優先度の異なる演算子を複数使う場合には、余白を活用して優先度を見える化する

# 良い
# x = x*2 - 1
# hypot2 = x*x + y*x
# c = (a+b) * (a-b)

# 悪い
# submitted += 1
# x = x * 2 - 1
# hypot2 = x * x + y * y
# c = (a + b) * (a - b)

#キーワード引数やデフォルトパラメータの「=」は余白なし
# 良い
# def complet(real, imag=0.0):
#     return magic(r=real, i=imag)

# 悪い
# def complex(real, imag = 0.0):
#     return magic(r = real, i = imag)

#関数アノテーションの「:」と「->」の余白

#関数アノテーションは、コロンに関する通常のルール（コロンの前には余計なスペースを入れない）を守りつつ、->演算子がある場合は、その両側には常にスペースを入れる

# 良い
# def munge(input: AnyStr): ...
# def munge() -> AnyStr: ...

# 悪い
# def munge(input:AnyStr): ...
# def munge()->PosInt: ...


#-----命名規則----------------------------------


##前アンダースコア
# _から始まる変数は、内部だけで使うことを示す

##後ろアンダースコア
# _を付ける場合には、Pythonのキーワードと衝突するのを避けるために使われる

##前アンダースコア2つ
#__とアンダースコアを2つ付ける方法は、クラスの属性に名前を付ける時に、名前のマングリング機構を呼び出します（クラスFoobarの__booという名前は、_FooBar__booになる


