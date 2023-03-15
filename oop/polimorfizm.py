class Dog:
    def speak(self):
        print("gav-gav")

class Cat:
    def speak(self):
        print("myaw-myaw") 

class Frog:
    def speak(self):
        print("kwa-kwa")               

animals = [Cat(), Frog(), Dog(), Cat(), Frog()]
for animal in animals:
    animal.speak()


list1 = [1,2,3,4,5]
dict1 = {"a":1, "b":2}

list1.pop(0)   # удаление по индексу
dict1.pop("a") # удаление по ключу


1 + 3
"a" + "b"

# __add__      прибавление 
a = 4
b = 5
print(a+b)              #9
print(a.__add__(b))     #9
a = [1,2,3]
b = [4,5,6]
print(a.__add__(b))     # [1, 2, 3, 4, 5, 6]

# __len__      считать символы 
a = 'abc'
print(len(a))       #3
print(a.__len__())  #3

b = [1,2,3,[4,5,6]]  
print(len(b))           # 4
print(b.__len__())      # 4