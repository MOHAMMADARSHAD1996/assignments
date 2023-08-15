#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>
Q1. What is Abstraction in OOps? Explain with an example.Abstraction in object-oriented programming (OOP) is a fundamental concept that focuses on hiding complex implementation details and showing only the necessary features of an object to the outside world. It allows you to create models or representations of real-world entities in your code that capture their essential characteristics without exposing the internal workings.

At its core, abstraction involves defining a clear interface for interacting with an object while keeping the internal details hidden. This enables you to work with high-level concepts and manipulate objects without needing to understand all the intricate details of how those objects are implemented.

Here's an example to illustrate abstraction:

Let's consider a real-world scenario of a "Vehicle." Vehicles can include cars, motorcycles, buses, and so on. Each type of vehicle has common attributes like speed, fuel capacity, and a method to start the engine. However, the internal mechanisms of these vehicles can be quite different.
# In[1]:


class Vehicle:
    def __init__(self, speed, fuel_capacity):
        self.speed = speed
        self.fuel_capacity = fuel_capacity
        self.engine_started = False
    
    def start_engine(self):
        self.engine_started = True
        print("Engine started")

# Concrete Car class
class Car(Vehicle):
    def __init__(self, speed, fuel_capacity, brand):
        super().__init__(speed, fuel_capacity)
        self.brand = brand

# Concrete Motorcycle class
class Motorcycle(Vehicle):
    def __init__(self, speed, fuel_capacity, has_sidecar):
        super().__init__(speed, fuel_capacity)
        self.has_sidecar = has_sidecar

# Create instances of concrete classes
my_car = Car(speed=160, fuel_capacity=60, brand="Toyota")
my_motorcycle = Motorcycle(speed=120, fuel_capacity=15, has_sidecar=False)

# Using abstraction to start engines
my_car.start_engine()
my_motorcycle.start_engine()

In this example, the Vehicle class serves as an abstraction. It defines a common interface with attributes and a method to start the engine. The Car and Motorcycle classes inherit from the Vehicle class, inheriting the attributes and method. However, each concrete class can have its own unique attributes and methods.

By using abstraction, you can interact with instances of Car and Motorcycle without worrying about the intricate details of how their engines start or how they store fuel. This separation of concerns makes your code more maintainable, scalable, and easier to understand.Q2. Differentiate between Abstraction and Encapsulation. Explain with an example.Abstraction and encapsulation are two important concepts in object-oriented programming (OOP) that help manage complexity and create more modular and maintainable code. While they are related, they serve distinct purposes.
Abstraction:
Abstraction is the process of simplifying complex reality by modeling classes based on essential properties and behaviors. It involves creating a simplified representation of an object by focusing on its high-level characteristics and hiding the irrelevant implementation details. Abstraction defines what an object does without necessarily specifying how it does it.
Encapsulation:
Encapsulation is the practice of bundling data (attributes) and methods (functions) that operate on the data into a single unit, called a class. It restricts direct access to some of the object's components from the outside, allowing controlled access through well-defined interfaces. Encapsulation ensures data integrity and helps prevent unintended interference or manipulation of an object's internal state.
Here's an example to illustrate the difference between abstraction and encapsulation:

# In[2]:


# Abstraction and Encapsulation Example

# Abstraction: Defining a basic abstract class
class Shape:
    def area(self):
        pass

# Encapsulation: Creating specific classes that encapsulate data and behavior
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Using the classes
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

# Abstraction in action: The "area" method is abstracted; we know what it does without knowing how.
print("Circle area:", circle.area())       # Abstraction: We don't need to know the formula for the area.

# Encapsulation in action: Data (attributes) and behavior (methods) are encapsulated within the classes.
print("Rectangle area:", rectangle.area()) # Encapsulation: We access the area through the encapsulated method.

In this example, the Shape class is an abstraction, defining a common interface for calculating the area of different shapes without specifying how the area calculation is done. The Circle and Rectangle classes encapsulate the data (radius, width, height) and behavior (area calculation) relevant to their respective shapes.

In summary, abstraction focuses on the essential characteristics of an object while hiding the implementation details, and encapsulation bundles data and methods together while controlling their access. Together, these concepts contribute to writing modular and maintainable code in object-oriented programming.Q3. What is abc module in python? Why is it used?
# The abc module in Python stands for "Abstract Base Classes." It provides a way to create abstract classes and interfaces, which can help enforce certain rules and structures in your code. Abstract classes are classes that cannot be instantiated directly and are meant to be subclassed by concrete classes.
# 
# The primary purpose of the abc module is to encourage and facilitate a form of design by contract, where you define the expected behavior that subclasses must adhere to. It helps in achieving better code organization, maintainability, and compatibility between different parts of your codebase.
# 
# Here's why the abc module is used:
# 
# Defining Abstract Base Classes: The abc module allows you to create abstract base classes using the ABC class. An abstract base class defines a common interface that its subclasses should implement. It can also provide default implementations for certain methods.
# 
# Forcing Subclasses to Implement Methods: By using the @abstractmethod decorator from the abc module, you can mark methods as abstract within your abstract base class. This enforces that any concrete subclass must implement these methods, ensuring consistent behavior throughout the inheritance hierarchy.
# 
# Structuring Code: Abstract base classes help structure your code by clearly defining a contract for subclasses. This makes your code more organized and easier to understand, especially in larger projects where multiple developers might be working on different parts.
# 
# Polymorphism: Abstract base classes enable polymorphism by providing a common interface for objects of different subclasses. This allows you to write more generic code that can work with various implementations without needing to know the specific details of each class.
# 
# Here's a simple example demonstrating the usage of the abc module:

# In[3]:


from abc import ABC, abstractmethod

# Defining an abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete subclasses of Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Creating instances and using them
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())

In this example, the Shape class is an abstract base class, and the Circle and Rectangle classes are its concrete subclasses. The abstractmethod decorator in the Shape class enforces that any subclass must implement the area method, ensuring a consistent behavior among different shapes.Q4. How can we achieve data abstraction?Data abstraction is a key concept in object-oriented programming that allows you to hide the complex implementation details of data while providing a simplified and controlled interface for interacting with that data. In other words, data abstraction focuses on exposing only the essential attributes and operations of an object, while keeping the internal workings hidden.

You can achieve data abstraction through a combination of techniques:

Encapsulation: Encapsulation is the practice of bundling data (attributes) and methods (functions) that operate on the data into a single unit, usually a class. By encapsulating data within a class, you control how the data is accessed and modified from the outside, ensuring that the internal state remains consistent and protected.

Private and Protected Attributes: In many programming languages, including Python, you can use access modifiers like private and protected to control the visibility of attributes within a class. Private attributes are typically indicated by using a naming convention (e.g., _attribute_name), and they are not meant to be accessed directly from outside the class.

Getters and Setters: Instead of directly accessing attributes, you can define getter and setter methods to retrieve and modify the attributes. This allows you to add validation, computation, or other logic before accessing or modifying the data.

Abstract Base Classes: In Python, you can use the abc module to define abstract base classes that enforce a certain structure and interface for subclasses. This helps in achieving data abstraction by defining the expected behavior that subclasses should follow.

Here's a simplified example of achieving data abstraction in Python:
# In[4]:


class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    
    def get_account_number(self):
        return self._account_number
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance")

# Creating an instance of the BankAccount class
account = BankAccount(account_number="12345", balance=1000)

# Using abstraction to access the data through methods
print("Account Number:", account.get_account_number())
print("Initial Balance:", account.get_balance())

account.deposit(500)
print("Balance after Deposit:", account.get_balance())

account.withdraw(300)
print("Balance after Withdrawal:", account.get_balance())

In this example, the BankAccount class encapsulates the data (account number, balance) and provides methods to interact with that data. The use of the _account_number and _balance attributes with the single leading underscore indicates that they are intended to be protected, discouraging direct access from outside the class.

By using getter and setter methods and controlling access to attributes, you achieve data abstraction, as the internal details of the class are hidden from the outside world, and the external interface provides a controlled and simplified way to work with the data.Q5. Can we create an instance of an abstract class? Explain your answer.No, you cannot create an instance of an abstract class in most programming languages, including Python. An abstract class is meant to be a blueprint for other classes and is not intended to be instantiated directly. Instead, you create concrete subclasses that inherit from the abstract class and provide implementations for its abstract methods.

In Python, you can use the abc module to define abstract base classes and enforce this behavior. Abstract base classes are created by subclassing the ABC class from the abc module, and you can mark methods within the abstract base class as abstract using the @abstractmethod decorator. These abstract methods must be implemented by concrete subclasses before they can be instantiated.

Here's an example to illustrate this:
# In[5]:


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Trying to create an instance of the abstract class will raise an error
# shape = Shape()  # This will result in a TypeError

# Creating an instance of the concrete subclass
circle = Circle(radius=5)
print("Circle area:", circle.area())

In this example, the Shape class is an abstract base class with an abstract method area. It cannot be instantiated directly. However, the Circle class is a concrete subclass that inherits from Shape and provides an implementation for the area method. You can create instances of Circle and use them as intended.

Remember that the purpose of abstract classes is to provide a common interface and structure for subclasses. They ensure that certain methods must be implemented by subclasses, promoting consistency and enforcing a contract.
# #  <P style="color:GREEN"> Thank You ,That's All </p>
