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

#finditer関数（全ての一致箇所を取得2）
#finditer関数は、指定した正規表現に一致するiterableオブジェクトを返却
# これをfor文でループすることで、全ての結果オブジェクトを得ることができる

# # 1行で利用する場合
# # re.finditer(pattern, string, flags=0)
# iter = re.finditer("\d{3}", "123-4567")
# for match in iter:
#     print(match)
# # => <_sre.SRE_Match object; span=(0, 3), match='123'>
# # => <_sre.SRE_Match object; span=(4, 7), match='456'>

# # 正規表現オブジェクトから利用する場合
# # regex.finditer(string[, pos[, endpos]])
# pattern = re.compile("\d{3}")
# iter = pattern.finditer("123-4567")
# for match in iter:
#     print(match)
# # => <_sre.SRE_Match object; span=(0, 3), match='123'>
# # => <_sre.SRE_Match object; span=(4, 7), match='456'>


#sub関数（文字列の置換）
#正規表現に一致する部分を、指定した文字列に置き換え

# # 1行で利用する場合
# # re.sub(pattern, repl, string, count=0, flags=0)
# re.sub("\d{3}", "***", "credit:123-AA-456-78")
# # => 'credit:***-AA-***-78'
# re.sub("\d{3}", "***", "credit:123-AA-456-78", count=1)
# # => 'credit:***-AA-456-78'
# re.sub("\d{3}", "***", "credit:123-AA-456-78", count=2)
# # => 'credit:***-AA-***-78'

# # 正規表現オブジェクトから利用する場合
# # regex.sub(repl, string, count=0)
# pattern = re.compile("\d{3}")
# pattern.sub("***", "credit:123-AA-456-78", count=1)
# # => 'credit:***-AA-456-78'


#MatchObjectオブジェクト
#正規表現の検索結果を保持するオブジェクト

#match.start, match.end（一致の開始位置と終了位置）
#一致した開始位置、終了位置を取得することができる

# # match.start([group])
# # match.end([group])
# m = re.match("(\d+)\.(\d+)", "24.1632")
# m.start(1)
# # => 0
# m.end(1)
# # => 2
# m.start(2)
# # => 3
# m.end(2)
# # => 7


#match.span（一致の範囲）
#一致した範囲を取得することができる match.startとmatch.endをまとめて取得できる感じ

# # match.span([group])
# m = re.match("(\d+)\.(\d+)", "24.1632")
# m.span(1)
# # => (0, 2)


#match.group（一致したグループ）
#一致した結果から、グループを取得することができます

# match.group([group1, ...])
# match = re.search("(\d{3})-(\d{4})", "123-4567")
# match.group(0)
# # => '123-4567'
# match.group(1)
# # => '123'
# match.group(2)
# # => '4567'
# match.group(1,2)
# # => ('123', '4567')

# # また、グループに名前をつけることもできます
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# m.group("first_name")
# # => 'Malcolm'
# m.group("last_name")
# # => 'Reynolds'
# m.group(1)
# # => 'Malcolm'
# m.group(2)
# # => 'Reynolds'


#match.groups（一致した全てのグループ）
#取得できたグループ一覧を得ることができる

# # match.groups(default=None)
# m = re.match("(\d+)\.(\d+)", "24.1632")
# m.groups()
# # => ('24', '1632')
# m = re.match("(\d+)\.?(\d+)?", "24")
# m.groups()
# # => ('24', None)
# m.groups(default=0)
# # => ('24', 0)

#match.groupdict（グループを辞書形式で取得）
#取得できたグループを辞書形式で取得できる

# # match.groupdict(default=None)
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# m.groupdict()
# # => {'first_name': 'Malcolm', 'last_name': 'Reynolds'}
