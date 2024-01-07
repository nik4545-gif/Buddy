import webbrowser
import time
import os
one = input("Привет, я чатбот Buddy, что пожелаете?: ")
if one == "Открой Яндекс":
   webbrowser.open('http://ya.ru', new=3)
   print('Открываю Яндекс')
   time.sleep(2)
   exit()
if one == "Открой Сайт":
	bebra = input("Введите адрес сайта: ")
	webbrowser.open(bebra, new=2)
	print("Открываю")
	time.sleep(2)
	exit()
if one == "Калькулятор":
   os.system('cls')
   ll1 = int(input("Введите первое число: "))
   ll2 = int(input("Введите второе число: "))
   ll3 = input("Введите знак: ")
   if ll3 == "+":
      result = ll1 + ll2
      print(result)
   if ll3 == "-":
      result = ll1 - ll2
      print(result)
   if ll3 == "*":
      result = ll1 * ll2
      print(result)
   if ll3 == "/":
      result = ll1 / ll2
      print(result)
   time.sleep(2)
   exit()
if one == "О тебе":
	   print("Меня зовут Buddy и меня создает один человек")
	   time.sleep(3)
	   exit()
else:
	print("Я вас не понимаю")
	time.sleep(2)
	exit()
