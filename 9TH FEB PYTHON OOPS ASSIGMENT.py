#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>
Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed 
and average_of_vehicleSure, here's an example of how you could create a Python class called Vehicle with the specified instance variables and an __init__ method:
# In[5]:


class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

# Creating an instance of the Vehicle class
car = Vehicle("vande bhart", 180, 40)
print(car.name_of_vehicle)
print(car.max_speed) 
print(car.average_of_vehicle)

In this example, the __init__ method initializes the instance variables name_of_vehicle, max_speed, and average_of_vehicle with the values passed as arguments when creating an instance of the class. You can then access these instance variables using dot notation, like car.name_of_vehicle, car.max_speed, and car.average_of_vehicle.Q2.  Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class. 
Create a method named seating_capacity which takes capacity as an argument and returns the name of 
the vehicle and its seating capacity.
# Certainly! Here's how you can create a child class Car that inherits from the Vehicle class and add the seating_capacity method:

# In[6]:


class Car(Vehicle):
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        super().__init__(name_of_vehicle, max_speed, average_of_vehicle)

    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} has a seating capacity of {capacity} people"

# Creating an instance of the Car class
car_instance = Car("Sedan", 180, 25)

# Calling the seating_capacity method
capacity_info = car_instance.seating_capacity(5)
print(capacity_info)  # Output: Sedan has a seating capacity of 5 people

In this example, the Car class inherits the Vehicle class, and the seating_capacity method is added to the Car class. The method takes a capacity argument and returns a formatted string containing the name of the vehicle and its seating capacity. When you create an instance of the Car class and call the seating_capacity method, it will provide the desired output.Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.Multiple inheritance is a feature in object-oriented programming languages, including Python, where a class can inherit attributes and methods from more than one parent class. This means that a child class can inherit behaviors and attributes from multiple base classes. However, multiple inheritance can lead to complex inheritance hierarchies and potential conflicts, so it should be used carefully.

Here's an example of multiple inheritance in Python:
# In[8]:


# Parent class 1
class Parent1:
    def method1(self):
        print("Method from Parent1")

# Parent class 2
class Parent2:
    def method2(self):
        print("Method from Parent2")

# Child class inheriting from both Parent1 and Parent2
class Child(Parent1, Parent2):
    def method3(self):
        print("Method in Child")

# Creating an instance of Child class
child_obj = Child()

# Calling methods from all parent classes and child class
child_obj.method1()  # Output: Method from Parent1
child_obj.method2()  # Output: Method from Parent2inheritance
child_obj.method3()  # Output: Method in Child

In this example, the Child class inherits from both Parent1 and Parent2 classes using multiple inheritance. It can access methods from both parent classes as well as define its own methods. Keep in mind that if there are methods with the same name in both parent classes, the method from the class mentioned first in the base class list will take precedence.

Remember, while multiple inheritance can be powerful, it can also lead to issues like the "diamond problem" where ambiguity arises if two parent classes have the same method name. It's essential to design your class hierarchy carefully and avoid situations that might lead to confusion or conflicts.
# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this 
# class
In Python, getter and setter methods are used to control the access and modification of class attributes (instance variables). They are used to encapsulate the attributes, providing a way to read and modify them while also allowing you to add additional logic or validation if needed.

Here's how you can create a class with getter and setter methods:
# In[9]:


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for name
    def set_name(self, name):
        self._name = name

    # Getter method for age
    def get_age(self):
        return self._age

    # Setter method for age
    def set_age(self, age):
        if age >= 0:  # Adding a basic validation
            self._age = age
        else:
            print("Age cannot be negative")

# Creating an instance of the Person class
person = Person("Alice", 25)

# Using getter and setter methods
print("Initial name:", person.get_name())  # Output: Initial name: Alice
person.set_name("Bob")
print("Updated name:", person.get_name())  # Output: Updated name: Bob

print("Initial age:", person.get_age())    # Output: Initial age: 25
person.set_age(30)
print("Updated age:", person.get_age())    # Output: Updated age: 30

person.set_age(-5)  # Trying to set a negative age

In this example, the Person class has getter and setter methods for both the name and age attributes. The getter methods (get_name() and get_age()) allow you to retrieve the values of the attributes, while the setter methods (set_name() and set_age()) allow you to set new values after potential validation checks.

Note that by convention, attributes that should not be accessed directly are prefixed with an underscore (e.g., _name and _age). This is not enforced by the language itself but serves as a visual cue for other programmers to treat these attributes as internal to the class and use the getter and setter methods instead.
# Q5.What is method overriding in python? Write a python code to demonstrate method overriding.
Method overriding is a concept in object-oriented programming where a subclass provides a specific implementation for a method that is already defined in its superclass. This allows the subclass to customize the behavior of the inherited method without changing the method name or signature.

Here's an example of method overriding in Python:
# In[10]:


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating instances of subclasses
dog = Dog()
cat = Cat()

# Calling the overridden methods
dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows

In this example, we have a base class Animal with a method speak(). Both Dog and Cat are subclasses of Animal. They override the speak() method with their own implementations. When you call the speak() method on instances of these subclasses, the overridden methods in the respective subclasses are executed.

Method overriding is a powerful way to provide different behaviors for inherited methods, allowing you to create specialized behavior for subclasses while still retaining the structure and interface defined in the superclass.
# #  <P style="color:GREEN"> Thank You ,That's All </p>
