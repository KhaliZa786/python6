a=int(input("Первое число: "))
b=int(input("Второе число: "))
for i in range(a,b+1):
  if i % 7 == 0:
      print(i)

      a = int(input("Введите 1 число: "))
      b = int(input("Введите 2 число: "))
      for i in range(a, b):
          print(i, end=' ')
      print()
      for i in range(b - 1, a - 1, -1):
          print(i, end=' ')
      print()
      for i in range(a, b):
          if i % 7 == 0:
              print(i, end=' ')
      print()
      for i in range(a, b):
          if i % 5 == 0:
              print(i, end=' ')

range_min = float(input())
range_max = float(input())
number = range_min
while number < range_max:
  if number % 3 == 0 and number % 5 == 0:
     print("fizz buzz")
  elif number % 3 == 0:
     print("fizz")
  elif number % 5 == 0:
     print("buzz")
  number += 1
