# Полиморфизм
> принцип ООП, в котором методы в разных классах называются одинаково. (один интерфейс - разная реализация)

```py
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
    ```