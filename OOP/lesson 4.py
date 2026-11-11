"""
Полиморфизм

"""
# 1
# class Animal:
#     def name(self):
#         pass
#
# class Dog(Animal):
#     def name(self):
#         print('REks')
#
# b = Dog()
# b.name()

# 2
# class Phone:
#      def brand(self):
#          print('Brand ')
#
#
#
# class SmartPhone(Phone):
#     def brand(self):
#         print('Apple')
#
# a = SmartPhone()
# a.brand()


# 3
# class School:
#     def name(self):
#         print('name of school: A.Jumabaev')
#
# class Student(School):
#     def name(self):
#         print('name of student: Asan')
#
# a = School()
# a.name()
# b = Student()
# b.name()


# 4
# class Vehicle:
#     def color(self):
#         pass
#
#
# class Car(Vehicle):
#     def color(self):
#         print('red')
#
# a = Car()
# a.color()

# 5
# class Employee:
#     def name(self):
#         pass
#
# class Teacher(Employee):
#     def name(self):
#         print('Maksat ')
#
# a = Teacher()
# a.name()

# 6
# class Computer:
#     def brand(self):
#         pass
#
# class Laptop(Computer):
#     def brand(self):
#         print('ASUS')
#
# a = Laptop()
# a.brand()


# 7
# class Animal:
#     def age(self):
#         pass
#
#
# class Cat(Animal):
#     def age(self):
#         print("bobi")
#
# a = Cat()
# a.age()


# 8
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print('Арр-Арр')

class Cat(Animal):
    def sound(self):
        print('Мяуу-Мяууу')

d = Dog()
d.sound()
c = Cat()
c.sound()


