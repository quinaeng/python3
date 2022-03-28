animal = 'fruitbat'

def change_local():
  animal = 'wombat'
  print('inside change_local:', animal, id(animal))

change_local()
print('inside change_local:', animal, id(animal))

