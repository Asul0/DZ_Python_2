# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N


num = int(input('Введдите число: '))

count = 0
while 2**count < num:
   print(2**count, end=" ")
   count =count+1
   

