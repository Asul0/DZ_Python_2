# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
#  вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть


from random import randint as rnd

value_coins = int(input('Введдите кол-во монет: '))

numbers = []
orel = 0
reshka = 0

for i in range(value_coins):
   numbers.append(rnd(0, 1))
print(numbers)

for j in numbers:
   if  j == 0:
      orel +=1
   else:
      reshka +=1
print(f"орел = {orel}, решка = {reshka}")

if orel < reshka:
   print(f"минимальное количество монет, которые нужно перевернуть: {orel}")
else:
   print(f"минимальное количество монет, которые нужно перевернуть: {reshka}")



