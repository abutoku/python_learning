import re

# search関数（任意の箇所で一致）

#searchでは文字列から正規表現に一致する部分を見つけることができる

# # 1行で使う場合
# # re.search(pattern, string, flags=0)
# re.search("\d{3}-\d{4}", "123-3322")
# # => <_sre.SRE_Match object; span=(0, 8), match='123-3322'>
# re.search("\d{3}-\d{4}", "a123-3322")
# # => <_sre.SRE_Match object; span=(1, 9), match='123-3322'>

# # 正規表現オブジェクトから利用する場合
# # regex.search(string[, pos[, endpos]])
# pattern = re.compile("d")
# pattern.search("dog")
# # -> <_sre.SRE_Match object; span=(0, 1), match='d'>
# pattern.search("dog", 1)
# # => None

#match関数（先頭から一致）

# # 1行で使う場合
# # re.match(pattern, string, flags=0)
# re.match("\d{3}-\d{4}", "123-3322")
# # => <_sre.SRE_Match object; span=(0, 8), match='123-3322'>
# re.match("\d{3}-\d{4}", "a123-3322")
# # => None

# # 正規表現オブジェクトから利用する場合
# # regex.match(string[, pos[, endpos]])
# pattern = re.compile("o")
# pattern.match("dog")
# # => None
# pattern.match("dog", 1)
# # => <_sre.SRE_Match object; span=(1, 2), match='o'>

#fullmatch関数（文字列の完全一致）

# # 1行で利用する場合
# # re.fullmatch(pattern, string, flags=0)
# re.fullmatch("\d{3}-\d{4}", "123-3322")
# # => <_sre.SRE_Match object; span=(0, 8), match='123-3322'>
# re.fullmatch("\d{3}-\d{4}", "a123-3322")
# # => None
# re.fullmatch("\d{3}-\d{4}", "123-3322a")
# # => None

# # 正規表現オブジェクトから利用する場合
# # regex.fullmatch(string[, pos[, endpos]])
# pattern = re.compile("\d{3}-\d{4}")
# pattern.match("123-4567")
# # => <_sre.SRE_Match object; span=(0, 8), match='123-4567'>

#split関数（文字列の分割）

# # 1行で利用する場合
# # re.split(pattern, string, maxsplit=0, flags=0)
# re.split("\W+", "Words, words, words.")
# # => ['Words', 'words', 'words', '']
# re.split("\W+", "Words, words, words.", 1)
# # => ['Words', 'words, words.']

# # 正規表現オブジェクトから利用する場合
# # regex.split(string, maxsplit=0)
# pattern = re.compile("\W+")
# pattern.split("Words, words, words.")
# # => ['Words', 'words', 'words', '']


#findall関数（全ての一致箇所を取得）

# # 1行で利用する場合
# # re.findall(pattern, string, flags=0)
# re.search("\d{3}", "123-4567")
# # => <_sre.SRE_Match object; span=(0, 3), match='123'>
# re.findall("\d{3}", "123-4567")
# # => ['123', '456']
# text = """
# name:Yohei,age:30,
# name:Ryusuke,age:24,
# name:Junji,age:32
# """
# re.findall("name:(\w+?),", text)
# # => ['Yohei', 'Ryusuke', 'junji']

# # 正規表現オブジェクトから利用する場合
# # regex.findall(string[, pos[, endpos]])
# pattern = re.compile("\d{3}")
# pattern.findall("123-4567")
# # => ['123', '456']