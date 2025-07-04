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

class Factory:
    def __init__(self, material,zips):
        self.material = material
        self.zips = zips

class Fact(Factory):
    def __init__(self, material,zips,color):
        super.__init__(material,zips)
        self.color = color

class Factor(Fact):
    def __init__(self, material,zips,color,pockets):
        super.__init__(material,zips,color)
        self.pockets = pockets

obj = Factor