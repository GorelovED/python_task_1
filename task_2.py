# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите значения X="))
y = int(input("Введите значения У="))
z = int(input("Введите значени Z="))

a = x*y*z
b = x+y+z

if a > 0:
    a = 0
elif a > 1:
    a = 1
if b > 0:
    b = 0
elif b > 1:
      b = 1

leftSide = not (x or y or z)
rightSide = not x and not y and not z
result = leftSide == rightSide

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
