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


# <2> 関数-------------------------

# def profile(x,y=20):
#   print("私の名前は" + x + "で" + str(y) + "歳です")
  
# profile("たけし")