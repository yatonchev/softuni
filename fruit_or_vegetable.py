#Плод или зеленчук
#Да се напише програма, която чете име на продукт, 
# въведено от потребителя, и проверява дали е плод или зеленчук.

product = input()

if product in ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']:
  print("fruit")
elif product in ['tomato', 'cucumber', 'pepper', 'carrot']:
  print("vegetable")
else:
    print("unknown")