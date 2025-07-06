# Imperative Approach
# a = 5
# b = 2
# print(a+b) 

# Functional Approach
# def sum(a,b):
#     print(a+b)
# sum(5,4)
# sum(15,24) 

# OOPS Approach
# In OOPS, variables are called attributes and functions are called methods
# class Factory:
#     a = 12 # Attribute
#     def hello(self): # Method
#         print('How are You?')
#     print('I am a Class and I am getting initialized') 

# print(Factory().a)
# Factory().hello()

# class BagFactory:
#     def __init__(self, material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
#     def show(self):
#         print(f'Your Object Details are {self.material}, {self.pockets}, {self.zips}')

# reebok = BagFactory('Cotton', 3, 2)
# nike = BagFactory('Nylon', 3, 3)

# reebok.show()

# class Animal:
#     name = 'Lion' # Class Attribute
#     def __init__(self,age):
#         self.age = age
#     def show(self): # Instance Method
#         print('How are You?')
    
#     @classmethod
#     def hello(cls):
#         print('I am a Class Method')
    
#     @staticmethod
#     def stat():
#         print('I am a Normal Function')

# obj = Animal(12)
# obj.stat()

# Inheritance
# class Factory:
#     a = 'I am an Attribute mentioned in Factory'
#     def hello(self):
#         print('I am a method inside Factory')

# class Fact(Factory):
#     pass

# obj = Fact()

# obj.hello()

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f'Hello, Your name is {self.name}') 

# class Human(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#     def show(self):
#         print(f'Hello, Your name is {self.name}, age is {self.age}') 

# person = Human('SK',21)
# person.show()

# class Animal:
#     def __init__(self,name):
#         pass
#     name1 = 'SK'

# class Human:
#     def __init__(self,name,age):
#         pass
#     name2 = 'Leo'

# class Robots(Human, Animal):
#     name3 = 'charlie'

# obj = Robots('SK', 21)

# class Factory:
#     def __init__(self, material,zips):
#         self.material = material
#         self.zips = zips

# class Fact(Factory):
#     def __init__(self, material,zips,color):
#         super.__init__(material,zips)
#         self.color = color

# class Factor(Fact):
#     def __init__(self, material,zips,color,pockets):
#         super.__init__(material,zips,color)
#         self.pockets = pockets

# obj = Factor()

# Polymorphism

# Method Overriding
# class Animal:
#     def show(self):
#         print('I am in Animal')
# class Human(Animal):
#     def show(self):
#         print('I am in Human')
# obj = Human()
# obj.show()

# Duck Typing
# class Animal:
#     def show(self):
#         print('I am in Animal')

# class Human(Animal):
#     def show(self):
#         print('I am in Human')

# obj = Human()
# obj2 = Animal()
# obj.show()
# obj2.show()

# Encapsulation

# class Fact:
#     _a = 'fact' # Protected Attribute
#     __b = 'fact' # Private Attribute
#     def _show(self):
#         print('I am in Fact')
# class Factory(Fact):
#     def show(self):
#         print(super()._a)

# obj = Factory()
# print(obj._a)
# print(obj.__b) # Throws an error as the attribute is private

# Abstraction
# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side
#     def Perimeter(self):
#         print('Per')
#     def Area(self):
#         print('Ar')

# class Circle(abstract):
#     def __init__(self,rad):
#         self.raf = rad
#     def Perimeter(self):
#         print('Per')
#     def Area(self):
#         print('Ar')

# obj = Circle(6)

# Dunder (Double Underscore) Method 
# class Animal:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
    
#     def __str__(self):
#         return f"Hello, I am {self.name}"
    
#     def __add__(self, other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age
#         return f"Your Sum of Ages are {self.age + sum}"

# obj = Animal("Lion", 12)
# obj2 = Animal("Lion", 12)
# obj3 = Animal("Lion", 12)
# obj4 = Animal("Lion", 12)

# print(obj+ (obj2, obj3, obj4))

# Some Advance Stuff 

# Decorators 
# class Animal:
#     @property 
#     def show(self):
#         print('Hello How are you?')
# obj = Animal()
# obj.show

# Creating a Decorator 
# def decorate(func):
#     def wrapper(a,b):
#         print('The Addition to your numbers are ')
#         func(a,b)
#         print('Thank You')
#     return wrapper
# @decorate
# def add(a,b):
#     print(f'Sum is {a+b}')
# add(5,6)

#  args(*) or arguments and kwargs(**) or keyword arguments
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)

# add(5,6,8,9)

# def info(**kwargs):
#     print('Your Info is:\n')
#     for i in kwargs:
#         print(f'{i}:{kwargs[i]}')
# info(name='SK',age=22)