print('Таблица умножения')
while True:
  number = int(input('\nВведите число от 1 до 9: '))
  if number == 0:
    print('Программа завершена')
    break
  else:
    for i in range(1,10):
      numb =i*number
      print('\n',number,'*',i,'=',numb)
   	
