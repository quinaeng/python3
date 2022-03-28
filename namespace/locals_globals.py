animal = 'fruitbat'
def change_local():
  animal = 'wombat' # ローカル変数
  print('locals:', locals())

print(animal)
change_local()
