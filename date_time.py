# import datetime  

# datetimeモジュールの中身

# datetime.date
# 日付を表現するクラス。年月日を保持することができる。
# datetime.time
# 時間を表現するクラス。時分秒とマイクロ秒を保持することができる。
# datetime.datetime
# 日付と時間をまとめて扱うことができるクラス。
# datetime.timedelta
# 2つの日付や時間の差を表現するためのクラス。
# datetime.tzinfo
# タイムゾーン情報を表現する基底クラス。
# datetime.timezone
# タイムゾーンについて、UTCからの固定オフセットとして実装するクラス。

### date ----------------datetime.dateクラス

# 引数に年月日を指定する
# aDate = datetime.date(2015, 1, 1)
# print(aDate)

# 引数が範囲を超える場合はエラー（勝手に繰り越しなどはしない）
# datetime.date(2015, 13, 1)

## 当日を取得する
# aDate = datetime.date.today()

## タイムスタンプから日付を取得する
# aDate = datetime.date.fromtimestamp(1442189545)

## 日付の演算
# answer = datetime.date.today() + datetime.timedelta(days=1)

## 日付の演算2
# today = datetime.date.today()
# yesterday = today + datetime.timedelta(days=-1)
# answer = datetime.date.today() - yesterday
# print(answer)

## 日付の演算3
# print(yesterday < today)

## 値の変更
# aDate = datetime.date(2015, 1, 1)
# aDate.replace(year=2026)
# aDate.replace(month=2)
# aDate.replace(day=2)


## 曜日を返す（0:月曜日、6:日曜日）
# aDate.weekday()

## 曜日を返す2（1:月曜日、7:日曜日）
# aDate.isoweekday()

## フォーマット文字列1
# aDate.isoformat()

## フォーマット文字列2
# aDate.strftime("%Y/%m/%d(%A) %H:%M:%S.%f")

## datetimeへ変換する
# datetime.datetime(*(aDate.timetuple()[:6]))


### time-------------datetime.timeクラス

# 生成
# aTime = datetime.time(1, 20, 35, 432)  # 1時20分35秒432マイクロ秒
# print(aTime)

# 値の取得
# aTime.hour
# aTime.minute
# aTime.second
# aTime.microsecond

# 値の変更
# aTime = aTime.replace(hour=2)
# aTime = aTime.replace(minute=50)
# aTime = aTime.replace(second=10)
# aTime = aTime.replace(microsecond=1000)

# 文字列にする
# aTime.strftime("%H:%M:%S.%f")

### datetime---------datetime.datetimeクラス

# 引数に年月日時分秒マイクロ秒を与える
# aDatetime = datetime.datetime(
#     2015, 10, 12, hour=10, minute=20, second=30, microsecond=40)

# print(aDatetime)

# 現在日時
# datetime.datetime.today()
# datetime.datetime.now()

# タイムスタンプから日時を取得する
# datetime.datetime.fromtimestamp(1442189545)

# dateオブジェクトとtimeオブジェクトを合わせる
# aDate = datetime.date.today()
# aTime = datetime.time(12, 30, 59)
# answer = datetime.datetime.combine(aDate, aTime)
# print(answer)

# 文字列からdatetimeへ
# http://docs.python.jp/3.3/library/datetime.html#strftime-strptime-behavior
# datetime.datetime.strptime(
#     "2015-01-01 12:30:59.296195", "%Y-%m-%d %H:%M:%S.%f")

# 値の取得
# aDatetime.year
# aDatetime.month
# aDatetime.day
# aDatetime.hour
# aDatetime.minute
# aDatetime.second
# aDatetime.microsecond
# aDatetime.weekday()
# aDatetime.isoweekday()

# 演算
# datetime.datetime.now() + datetime.timedelta(days=1)
# datetime.datetime.now() - datetime.timedelta(weeks=1)
# datetime.datetime(2015, 1, 1) - datetime.datetime(2015, 1, 2)
# datetime.datetime(2015, 1, 1) < datetime.datetime(2015, 1, 2)

# Dateの取得
# datetime.datetime.now().date()

# Timeの取得
# datetime.datetime.now().time()

# Timestampの取得
# datetime.datetime.now().timestamp()

# 文字列にする
# datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


### timedelta-----------datetime.timedeltaクラス(日付や時間の差を扱うことができる)

# 生成（引数は全てオプション、指定しなければ0）
# aTimedelta = datetime.timedelta(
#     days=1, seconds=2, microseconds=3, milliseconds=4, minutes=10, hours=15, weeks=20)
# print(aTimedelta)

# 生成（負数も指定可能）
# datetime.timedelta(days=-1)

# 演算
# datetime.timedelta(days=10) + datetime.timedelta(days=20)
# datetime.timedelta(days=10) - datetime.timedelta(days=20)
# datetime.timedelta(days=10) * 5
# datetime.timedelta(days=10) * 0.5
# datetime.timedelta(days=10) / 2

# 絶対値を取得する
# abs(datetime.timedelta(days=-10))
