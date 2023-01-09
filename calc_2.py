info = ''
sert = ''
operat = input('Выберите операцию: ')
while True: 
  if operat in '+-*/':
    break
  print('такой операции не существует')
  operat = input('Выберите операцию: ')
if operat == '+':
  count = 0
else:
  count = 1
numbers = int(input('Сколько чисел будете вводить? '))
for i in range(1,numbers+1):
  print('Введите число',i,':', end='')
  variable = input()
  info += (variable + operat)
  if operat == '+':
    result = count + float(variable)
    count = result
  elif operat == '-':
      if i == 1:
        result = float(variable)
      else:
        result -= float(variable)
  elif operat == '*':
    result = count * float(variable)
    count = result
  elif operat == '/':
      if i == 1:
        result = float(variable)
      else:
        result -= float(variable)  
print('Результат: ',info[:-1],'=', result)
  
