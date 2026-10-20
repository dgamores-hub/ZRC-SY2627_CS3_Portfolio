SINGLE INHERITANCE
```python
class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def speak(self):
        print(self.__name, "makes a sound")

class Dog(Animal):
    def bark(self):
        print(self.get_name(), "says woof!")

dog1 = Dog("Buddy")
dog1.speak()
dog1.bark()

dog1.set_name("Max")
dog2 = Dog("Charlie")

print("updated name:", dog1.get_name())
dog2.bark()
```

MULTILEVEL INHERITANCE
```python
class LivingThing:
    def breathe(self):
        print("I can breathe.")

class Animal(LivingThing):
    def move(self):
        print("I can move.")

class Bird(Animal):
    def fly(self):
        print("I can fly!")

bird1 = Bird()
bird1.breathe()
bird1.move()
bird1.fly()

bird2 = Bird()
bird2.fly()
```

HIERARCHICAL INHERITANCE
```python
class Vehicle:
    def __init__(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

class Car(Vehicle):
    def drive(self):
        print(self.get_brand(), "is driving.")

class Motorcycle(Vehicle):
    def ride(self):
        print(self.get_brand(), "is riding.")

car1 = Car("Toyota")
bike1 = Motorcycle("Honda")

car1.drive()
bike1.ride()

car1.set_brand("Ford")
car2 = Car("Tesla")

print("Updated brand:", car1.get_brand())
car2.drive()
```

