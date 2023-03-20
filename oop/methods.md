# class/static/instance methods
>**instance method** - методы, которые первым аргументом принимают обьект от класса (instance, self). исппользуются для работы с обьектом и его аттрибутами 

```py
class A:
    def instance_method(self):
        print("метод обьекта")
        print("self", self)

obj = A()
obj.instance_method()
```

>**class methods** - методы, которые первым аргументом принимают класса (class). исппользуются для работы с классом и его аттрибутами 


```py
lass A:
    @classmethod
    def class_method(cls):
        print("метод класса")
        print("cls", cls)

A.class_method()
# метод класса
# cls <class '__main__.A'>

obj = A()
obj.class_method()
# метод класса
# cls <class '__main__.A'>
```

> для создании class метода, нужно использовать декоратор 'classmethod'


> **static method** - методы, которые не взаимодйствуют с обьектом и классом, но находятся внутри класса (по принципу)