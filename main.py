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

price = [str(i) + '円' for i in range(0,101)]
print(price)


