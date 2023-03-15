# dunder (double underscore) - методы у которых 2 __ в начале и в конце
# магия в том, что мы их не вызываем на прямую

class A:
    def __new__(cls):
        print("__NEW__")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("__INIT__")

A()
# __NEW__
# __INIT__

# __new__,__init__ - вызываются при создании обьекта 

print(dir(object))

# __eq__ ==
#__ge__ >=
# __gt__ >
# __le__ <=
# __lt__ <
# __ne__ !=
# __sub__ -
# __floordiv__ /
# __truediv__ //
# __add__ +


class A:
    pass
# __str__ str, print

print(A())
# <__main__.A object at 0x105058bd0>

class A:
    def __str__(self) -> str:
        return "Hello"
    
print(A())    
# Hello


class A:
    def __init__(self, number) -> None:
        self.number = number 

    def __eq__(self, other) -> bool:
        return self.number == other.number

obj1 = A(5)
obj2 = A(5)

print(obj1 == obj2)
print(obj1.__eq__(obj2))

print("hello") # hello
print(repr("hello")) # 'hello' .    str == repr 

class A:
    def __str__(self) -> str:
        return "A __STR__"
    
    def __repr__(self) -> str:
        return "A__REPR__"
    
print(A())
print(repr(A))    