# 短い関数を作成するよりもラムダのほうが良い

def edit_story(words,func):
  for word in words:
    print(func(word))

stairs = ['thud','meow','thud','hiss']

def enliven(word):
  return word.capitalize() + '!'

edit_story(stairs,enliven)
print("↓ラムダ")
edit_story(stairs,lambda word: word.capitalize() + '!')
