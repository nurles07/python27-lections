'===============Встроенные функции==============='
# enumerate 

string = 'hello'
enum = enumerate(string)
print(enum)
# <enumerate object at 0x1011a1440>
print(list(enum))
# [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

string = 'world'
enum = enumerate(string, 5)
print(list(enum))
#[(5, 'w'), (6, 'o'), (7, 'r'), (8, 'l'), (9, 'd')]

list1 = [1,4,78,3,7,0,4,2,7]

for ind in range(len(list1)):
   element = list1[ind]
   if ind % 2: # ind % 2 != 0 
      list1[ind] = element * 2
      if ind % 3 == 0:
         list1[ind] = element * 3

print(list1)
  # [1, 8, 78, 9, 7, 0, 4, 4, 7]



list1 = [1,4,78,3,7,0,4,2,7]  
for ind, element in enumerate(list1):
   if ind % 2:
      list1[ind] = element * 3     # [1, 8, 78, 9, 7, 0, 4, 4, 7]

string = 'abcd'
print(dict(enumerate(string, 1))) # 1: 'a', 2: 'b', 3: 'c'}



# zip 
list1 = [1,2,3,4,5]
list2 = 'abcdefg'
list3 = [0.5, 0.3,0.6]

print(list(zip(list1,list2,list3)))
# [(1, 'a', 0.5), (2, 'b', 0.3), (3, 'c', 0.6)]





"======================Функция высшего порядка====================="
# это функция , которая:
# принимает в аргументы другую функицию
# возвращает функцию 
# создает внутри функцию 
# вызывает внутри функцию

# map - принимает в аргументы функций и итерируемый обьект, возврощает генератор, в котором все элементы - результат принимаемой функций,
# в которую передали элементы последовательности

mapped = map(int, ['1', '2', '3'])
print(list(mapped))  # [1, 2, 3]


list1 = [1,2,3,4]

print(list(map(lambda i: i+1, list1))) #[2, 3, 4, 5]



# filter - принимает в аргументы функций и итерируемый обьект, возврощает генератор, в котором элементы из последовательности
# прошедшие фильтр (функция вернула True)

list1 = [-3,7,0,34,-23,435,10]

def is_positive(i):
    return i > 0

print(list(filter(is_positive, list1))) 
# [7, 34, 435, 10]

print(list(filter(lambda i: i > 0, list1)))  #[7, 34, 435, 10]    вариант с lambda



list1 = [ 'Hello', 'wORLD', 'MAKERS']
print(list(filter(lambda i: i[0].isupper(), list1))) # ['Hello', 'MAKERS']




# reduce - функция которая импортируется из functools.
# тоже принимает функцию и итерируемый обьект.
# возврощает 1 результат

from functools import reduce
list1 = [2,4,6,3,65,8]

def mul(x,y):
   return x*y

res = reduce(mul, list1)
print(res)
#74880 = 2*4*6*3*65*8

string = 'nurles'
print(reduce(lambda x,y: x+'$'+y, string)) 
#n$u$r$l$e$s



str1 = ['hello', 'world', 'bootcamp']
print(reduce(lambda x,y: x if len(x) >  len(y) else y, str1))
# bootcamp
