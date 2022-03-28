# 辞書

# キーと値の組み合わせのデータ

score = {"Japanese":80,"English":75,"Sience":90}
print(score["Japanese"])
print("検索結果")
print(score.get("Japaneses"))

# 書き換えが可能(ミュータブル)
score["Japanese"] = 100
print(score["Japanese"])

print("キーを取得")
for key in score.keys():
  print(key)

print("値を取得")
for value in score.values():
  print(value)

print("アイテムを取得")
for item in score.items():
  print(item)
