"=============List=============="
#список - это изменяемый, итерируемый, индексируемый и упорядоченный
# тип данных,предназначенный для хранение элементов в строгом порядке.
list1 = [1, 3.5, 'hello', [1,2,3], (1,2), None, True, False]
list[0] # 10
list1[3] # [1,2,3]
list1[3] [-1] # 3
list1[-1] # False
list1[2][-1] # 'o'


list2 = list('hello')
print(list2) # ['h','e','l','l','o']

list3 = list(range(3,10,2))
print(list3) # [3,5,7,9]
print(list(range(5))) # [0,1,2,3,4,]


'==========изменяемость==========='
string = 'hello'
res = string.upper()
print(string) #'hello'
print(res) # 'HELLO'
list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
print(list1) #[1,2,3]


a = 10 
b = 10
print(id(a))
print(id(b))


'========методы списков=========='
# append - метод который добовляет элемент в конец списка 
list1 = []
list1.append('hello')
list1.append(500)
list1.append([1,2,3])
print(list) # ['hello, 500, [1,2,3]]

#remove - метод который удаляет элемент из списка по назначению ,
# но только первого вхождение этого элемента выдаст ощибку ValueError
# если такого элемента нет в списке

list2 = ['hello', 500, 'world', 1000, 'hello', 500]
list2.remove('hello')
print(list2) #[500, 'world', 1000, 'hello', 500]

# pop - метод который удаляет элемент  из списка по индексу 
# если этого индекса нет выдаст IndexError
list3 = [10, 20, 30, 40, 50]
list3.pop()
print(list3) #[10, 20, 30, 40]
list3.pop(1) #удаление пот индексу 1
print(list3) # [10, 30, 40]
# так же метод pop возвращает удаленный элемент
list4 = [10, 20, 30, 40, 50]
popped = list4.pop(0)
print(list4) #20, 30, 40, 50]
print(popped) # 10

#list5 = []
#list5.pop()

# insert - метод который добовляет элемент в список по индексу
list5 = [1,2,3,4]
list5.insert(0, 'hello')
print(list5)  #['hello', 1, 2, 3, 4]


list6 = [1,2,3,4,5,6,7,8,9,]
list6 = list(range(1,11))
print(list6[::-1]) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# clear - чистит список 
list1 = [1,2,3,]
list1.clear()
print(list1) #[]

# count - считатет количество элемента который передаем в метод в списке 
list1 = [1,2,3,4,1,2,4,1,6,]
list1.count(1) # 3
list1.count(2) # 2
list1.count('hello') # 0

list1 = ['hello', 'hello', 'hello']
list1.count('hello') # 3
list1.count('l') # 0

list1 = [11, 12, 13]
list1.count(1) # 0

# index - возвращает индекс данного элемента
list2 = ['hello', 'world', 'makers']
ind = list2.index('hello')
print(ind) # 0
list2.index('makers') # 2

# sort - метод, который сортирует по возрастанию
# если передать .sort(reverse=True), то сортирует по убыванию
list3 = [34,12,67,12,89,45]
list3.sort()
print(list3) # [12, 12, 34, 45, 67, 89]
list3.sort(reverse=True)
print(list3) # [89, 67, 45, 34, 12, 12]
# list3.sort()
# list3.reverse()

list4 = ['a', 'c', 'b', 'B', 'A']
list4.sort()
print(list4) # ['A', 'B', 'a', 'b', 'c']

list5 = [10, 'b', 3, 'c', 5]
# list5.sort() 
# TypeError: '<' not supported between instances of 'str' and 'int'

# copy - возвращает копию списка
list1 = [1,2,3]
list2 = list1.copy()
list2.append(4)
print(list1)
print(list2)

# extend - расширяет список другим списком
list1 = [1,2,3,4]
list2 = [5,6,7,8]
# list1.append(list2)
# list1  [1,2,3,4, [5,6,7,8]]

list1.extend(list2)
# list1  [1,2,3,4,5,6,7,8]
