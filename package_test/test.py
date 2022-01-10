# import gscommon
# text = gscommon.my_module.get_genius()
# print(text)

##↑のコードはなぜかエラー、解決せず


# from gscommon import my_module
# text = my_module.get_genius()
# print(text)

# from gscommon import my_module as mm
# text = mm.get_genius()
# print(text)

from gscommon import my_special
my_special.greet()