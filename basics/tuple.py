'==========кортеж========='
#список - это изменяемый, итерируемый, индексируемый и упорядоченный
# тип данных,предназначенный для хранение элементов в строгом порядке
#(в целом ничем не отличается от списков просто неизменяемый поэтому занимает меньше памяти)
tuple1 = (1,2,3,4)
tuple2 = (5) # int
tuple3 = 1,2,3,4 # tuple
tuple4 = 5, # tuple (5,)
tuple5 = (1, 'hello' [2,3,4])
tuple5[-1].append (5)
# tuple = (1, 'hello', [2,3,4,5])
tuple5 [0] = 5 #TypeError:'tuple' object does not support item assigment
tuple6 = tuple('hello') # ('h','e','l','l','o')

'=========методы tuple=========='
#count - считает  кол-во данного элемента в tuple
tuple1 = (1,2,3,1,2,1,3,4,) 
print(tuple1.count(1)) # 3
print(tuple1.count('hello')) # 0

# index 
tuple1 = ('hello', 'world', 105)
print(tuple1.index('hello')) # 0
print(tuple1 )