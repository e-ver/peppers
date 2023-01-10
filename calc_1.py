print('Умножение деление')
print('Вычитание сложение')
operat = input('Выберите операцию: ')
while True: 
  if operat in '+-*/':
    break
  print('такой операции не существует')
  operat = input('Выберите операцию: ')
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
if operat == '+':
  print(number_1, operat, number_2, '=', number_1 + number_2)
elif operat == '-':
  print(number_1, operat, number_2, '=', number_1 - number_2)
elif operat == '*':
  print(number_1, operat, number_2, '=', number_1 * number_2)
elif operat == '/':
  print(number_1, operat, number_2, '=', number_1 / number_2)
  
