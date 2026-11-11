"""
Абстракция ->
"""



# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         print('Ит урду')
#
# class Cat(Animal):
#     def sound(self):
#         print('Мышык мяу деди')
#
#
# d = Dog()
# c = Cat()
# d.sound()
# c.sound()



# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
# class Car(Transport):
#     def move(self):
#         print('Машина журуп жатат')
#
# class Bike(Transport):
#     def move(self):
#         print('Велосипед журуп жатат')
#
# c = Car()
# b = Bike()
# c.move()
# b.move()



# 1
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         print('Ит урду')
#
# class Cat(Animal):
#     def sound(self):
#         print('Мышык мяу деди')
#
#
# d = Dog()
# c = Cat()
# d.sound()
# c.sound()
#

# 2
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
# class Car(Transport):
#     def move(self):
#         print('Машина журуп жатат')
#
# class Bike(Transport):
#     def move(self):
#         print('Велосипед журуп жатат')
#
# c = Car()
# b = Bike()
# c.move()
# b.move()

# 3
# class Phone(ABC):
#     @abstractmethod
#     def call(self):
#         pass
#
# class Samsung(Phone):
#     def call(self):
#         print('Алоо ')
#
#
# class Iphone(Phone):
#     def call(self):
#         print('Алеее')
#
# s = Samsung()
# i = Iphone()
# s.call()
# i.call()


# 4
# class Employee(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
# class Teacher(Employee):
#     def work(self):
#         print('Мен мугалим болуп эмгектенем')
#
#
# class Programmer(Employee):
#     def work(self):
#         print('Мен программистмин')
#
# t = Teacher()
# p = Programmer()
# t.work()
# p.work()


# 1
class Student:
    def init(self, name, age):
        self.name = name
        self.age = age

    def
