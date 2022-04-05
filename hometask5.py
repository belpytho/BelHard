print("Чтобы остановить калькулятор наберите СТОП")
i=0
while True:
     x = ((input('Введите первое число: ')))
     if x == ("СТОП"):
         break
     b = (input('Введите знак: '))
     if b == ("СТОП"):
         break
     c = ((input('Введите второе число: ')))
     if c == ("СТОП"):
         break

     try:
         x = float(x)
         c = float(c)
         i+=1
         if b == "+":
             print(f"{i}. {x}+{c}=", x + c)
         elif b == "-":
             print(f"{i}. {x}-{c}=", x - c)
         elif b == "/":
             print(f"{i}. {x}/{c}=", x / c)
         elif b == "*":
             print(f"{i}. {x}*{c}=", x * c)
         else:
             print("Неверный знак")

     except ZeroDivisionError:
         print("Ошибка: деление на нуль.")
     except :
         print("Ошибка")














