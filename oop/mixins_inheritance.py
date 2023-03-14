""" 
1 Миксины - классы, которые будут использоваться для наледования.
Но от миксинов не создаются обьекты
2 Миксины - классы-примеси, которые служат для расширения функционала класса
"""
# От миксинов нельзя создавать обьекты,
# поскольку миксины - несамостоятельные классы
# При наследовании миксины должны идти в первую очередь



class WalkMixin:
    def walk(self):
        print('я могу ходить')     

class SwimMixin:
    def swim(self):
        print('я могу плавать')    

class FlyMixin:
    def fly(self):
        print('я могу летать')               

class Human(WalkMixin, SwimMixin):
    name = 'Человек'

    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'рыбы'    

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'летучая рыба'

class Duck(WalkMixin, SwimMixin, FlyMixin):
    name = 'утка'

# objects = [Human(), Fish(), Exocoetidae(), Duck()]

# for obj in objects:
#     # print(obj.name)

#     attrs = ['fly', 'swim', 'walk', 'talk']
#     for attr in attrs:
#         if hasattr(obj, attr):     # проверяет если метод у данного класса "hesattr"
#             method = getattr(obj, attr)    # работает через переменные и выводит значение методы " getattr"
#             method()

#я могу плавать
# я могу ходить
# я могу говорить
# я могу плавать
# я могу летать
# я могу плавать
# я могу летать
# я могу плавать
# я могу ходить

obj = Human()
setattr(obj, 'new_attribute', 'hello world')   # создает новый аттрибут и сразу дает ему значение "setattr"
# print(dir(obj))
print(obj.name)
print(obj.new_attribute)


# print(hasattr(obj, 'fly')) -> True
# print(getattr(obj, 'walk'))

# obj.fly()
# obj.swim()
# obj.walk()

# hasattr - функция, которая принимает обьект и называние аттрибута. Возвращает True, если у обьекта есть такой аттрибут (метод) 
# getattr - функция, ко торая принимает обьект и название аттрибута . Возврощает значение аттрибута

# setattr - функция , которая принимает обьект , название аттрибута и значение аттрибута. Добовляетв в обьект новый аттрибут или перезапишет одноименный аттрибут. 
