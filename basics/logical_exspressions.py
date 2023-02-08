'====знак равенства====='
#print (5 == 5) -> true
#print (5 == 4) -> false 

# "=" -> знак присвоение 
# "==" -> знак сравнение 

# print (4 != 5) -> true - это знак неравенство
#print(4 ! = 4) -> false

"знак больше"
#print(5 < 5) -> false
#print(5 < 10) -> true


"больше или равно"
#print (5>= 10) -> false
#print(5 >= 5) -> true


#print(5 <= 3) ->false
#print(5 <= 5) -> true


#print ('5' == 5) -> false
#print ('hello' == 'hello') -> true
#print ('Hello' == 'hello') -> false


"======== AND OR NOT======"
# and - и
# or - или
# not - не

a = 5
b = 6 

# print(a == 5 and b == 6 ) -> true
#print(a == 4 and b == 6) -> false

a = 5
b = 6
#print( a == 4 or b == 3) -> false 
#print(a == 5 or b == 6) -> true

#print(not a == 5) -> false
#print(not a == 5 or not b == 6) -> true
#print(not a == 5 not b == 6) -> false

#print(not true) -> false
#print(not False) -> True


"===========Boolean Type========"
# у булевого типа всего 2 значение: True и False

#print (bool(1)) -> True
#print(bool(0)) -> False
#print(bool(-11)) -> True

#print(bool ('hello')) -> True
#print(bool(' ')) -> True
#print(bool("")) -> False

#print(bool([])) -> False
#print(bool([[]])) -> True



"=========None Type======"
#None - неизменяемый тип данных с одним значением None,
# который используется для обозначение пустоты 
#print(bool(None)) -> False
#print(bool('None')) -> True


"===========Условные операторы========="

# условные операторы - конструкция, которая используется для того,
# чтобы при разных входных данных код работал по разному (в зависимости от условия )
#if условие1:
  #  тело1
    #  тело1 будет выполняться только если условие1 верно

#if условие1:
  #  тело1
 #  тело1 будет выполняться только если условие1 верно
#else:
  #  тело2
    #тело2 будет выполняться во всех других случаях


 #if условие1:
   # тело1
    # тело1 будет выполняться только если условие1 верно
# elif условие2:
   # тело2
    #тело2 будет выполняться только если
    # условие1 не верное и если условие2 верное
#else




    # в одной конструкции мы можем использывать только один if 
    # В одной конструкции мы можем использывать 
    # неограниченное количество elif или не использывать вообще
    # в одной конструкции мы можем испоьзывать только один else или не использывть вообще



#num = int(input('ведите число: '))

#if num > 0:
#    print(f' число{num} - положительное')
#elif num == 0:
#    print(f'число {num} - это 0')
#else:
#    print(f'число {num} - отрицательное')



#password = input('придумайте свой пароль: ')
#first_let = password[0].upper()
#print(first_let)
#if not len(password) >= 8:
#    print('ваш пароль меньше 8 символов')
#elif password.startswith(first_let.upper()):
#    print('ваш пароль не начинается с большой буквы')

#else:
#    print('успешно создан пароль')




'=============тернарные операторы========'
# тернарные операторы - условие в одну строку 
#тело1 if условие else тело2

#num = int(input())

# res = 'Hello' if num == 5 else 'Bye'
#  print(res)

'===========FizzBuzz========='

num = int(input())

if num % 3 ==0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
elif num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
else:
    print(num)
