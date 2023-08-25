#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>
Q1. Explain why we have to use the Exception class while creating a Custom Exception.

Note: Here Exception class refers to the base class for all the exceptions.# Using the Exception class as the base class when creating custom exceptions is a common practice in many programming languages, including Python. The Exception class provides a foundational structure and behavior that is essential for creating meaningful and consistent custom exceptions. Here are the reasons why we use the Exception class as the base class for custom exceptions:

Consistency and Familiarity: By inheriting from the Exception class, your custom exception will follow the same patterns and conventions as built-in exceptions in the language. This consistency makes it easier for developers to understand how to work with your custom exception and handle it appropriately.

Exception Hierarchy: The Exception class is often at the top of the exception hierarchy in programming languages. This hierarchy provides a structured way to organize different types of exceptions. By inheriting from Exception, you're placing your custom exception within this hierarchy, which helps in categorizing and handling exceptions effectively.

Common Functionality: The Exception class typically provides common methods and properties that are useful for exception handling, such as the ability to provide an error message, stack trace, and other relevant information. By inheriting from Exception, your custom exception can automatically inherit these features, making it consistent with standard exceptions.

Catching and Handling: When you use your custom exception in a try...catch block, you can catch it in the same way you would catch any other exception. This simplifies the error-handling process and ensures that your custom exception can be treated in the same manner as built-in exceptions.

Customization: While inheriting from Exception, you can also add additional properties or methods that are specific to your custom exception's context. This allows you to extend the base behavior to suit your needs.

Documentation and Clarity: When other developers encounter your custom exception, they will immediately recognize it as an exception due to its inheritance from the Exception class. This promotes clarity in your codebase and reduces confusion.

Here's an example in Python of how you might create a custom exception class by inheriting from the Exception class:
# In[2]:


class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.custom_property = "Additional custom information"

In this example, CustomError is a custom exception that inherits from the built-in Exception class. It retains all the benefits and characteristics of an exception while allowing you to add your own custom behavior and attributes.
In summary, using the Exception class as the base class for custom exceptions is a best practice that ensures consistency, proper functionality, and familiarity in the world of exception handling.
Q2. Write a python program to print Python Exception Hierarchy.
# In[3]:


def print_exception_hierarchy(exception_class, indent=0):
    print(" " * indent + str(exception_class))
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 2)

print_exception_hierarchy(BaseException)

This program defines a function print_exception_hierarchy that takes an exception class and an optional indent parameter. It prints the name of the current exception class and then recursively calls itself on each of the subclasses of the given exception class, increasing the indentation each time.
In the main part of the program, it starts the printing from the BaseException class, which is the top-level class in the Python exception hierarchy. You can run this program to see the entire exception hierarchy printed out in an indented manner. Please note that the exception hierarchy might be quite extensive, so the output could be lengthy.Q3. What errors are defined in the ArithmeticError class? Explain any two with an example.The ArithmeticError class in Python is a base class for exceptions that occur during arithmetic operations. It serves as a parent class for various arithmetic-related exception classes. Here are two specific errors defined within the ArithmeticError class:
ZeroDivisionError:
This error occurs when you try to divide a number by zero.
Example:
# In[4]:


try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
    


# In[7]:


# OverflowError:
# This error occurs when a calculation exceeds the maximum limit that a data type can represent.
# Example:
import sys

try:
    big_number = sys.maxsize + 1
except OverflowError as e:
    print("Error:", e)
    
#Error: cannot convert float infinity to integer    

In the first example, attempting to divide by zero triggers a ZeroDivisionError. In the second example, adding 1 to the maximum value that sys.maxsize can represent triggers an OverflowError due to the value exceeding the limit of the data type.
Both of these errors are subclasses of ArithmeticError, which itself is a subclass of Exception. They are categorized as arithmetic-related errors because they typically occur during arithmetic operations and calculations.Q4. Why LookupError class is used? Explain with an example KeyError and IndexError.The LookupError class in Python is a base class for exceptions that occur when a lookup or indexing operation fails. It serves as a parent class for exceptions related to looking up values in sequences, containers, and dictionaries. The primary purpose of LookupError and its subclasses is to handle situations where you are trying to access an element or value in a data structure, but the access is invalid due to an out-of-bounds index or a missing key.

Here are two specific errors derived from LookupError:

KeyError:
This error occurs when you try to access a dictionary using a key that doesn't exist in the dictionary.

Example:
# In[8]:


my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['x']
except KeyError as e:
    print("Error:", e)


# In[9]:


# IndexError:
# This error occurs when you try to access a sequence (like a list or tuple) using an index that is out of its valid range.
# Example:
my_list = [10, 20, 30]

try:
    value = my_list[5]
except IndexError as e:
    print("Error:", e)

In the first example, attempting to access a non-existent key in the dictionary results in a KeyError. In the second example, trying to access an element at an index beyond the valid range of the list causes an IndexError.

By catching these specific exceptions, you can gracefully handle cases where lookup operations fail due to missing keys or invalid indices, preventing your program from crashing unexpectedly. These errors are derived from the more general LookupError class, which provides a common interface to handle lookup-related exceptions.Q5. Explain ImportError. What is ModuleNotFoundError?ImportError and ModuleNotFoundError are both exceptions in Python that are related to importing and using modules. Let's take a closer look at each of them:

ImportError:
ImportError is a base class for exceptions that occur when there's an issue with importing a module or package. It can be raised for various reasons, such as when the module does not exist, there's an issue with the module's content, or there are circular dependencies.

Example:
Let's say you have a module named my_module that doesn't exist in your current working directory or any of the paths in your Python environment:
# In[10]:


try:
    import my_module
except ImportError as e:
    print("Error:", e)

ModuleNotFoundError:
ModuleNotFoundError is a subclass of ImportError that specifically occurs when a module or package cannot be found during the import process. This error was introduced in Python 3.6 to provide a more precise error message when a module is not found.

Example:
Trying to import a non-existent module named nonexistent_module:
# In[11]:


try:
    import nonexistent_module
except ModuleNotFoundError as e:
    print("Error:", e)

It's important to note that in Python 3.6 and later, when you try to import a module that doesn't exist, you'll get a ModuleNotFoundError instead of a generic ImportError.
In summary, both ImportError and ModuleNotFoundError are exceptions that indicate problems related to module imports. While ImportError is a more general exception class, ModuleNotFoundError is a specific subclass introduced to improve the accuracy of error messages when a module or package is not found.Q6. List down some best practices for exception handling in python.Exception handling is a crucial aspect of writing robust and maintainable Python code. Here are some best practices for effective exception handling in Python:
Be Specific with Exception Types:
Catch only the exceptions you expect and can handle. Avoid using a broad except statement that catches all exceptions, as it can hide unexpected issues and make debugging difficult.
Use Multiple except Blocks:
Use separate except blocks for different types of exceptions. This allows you to handle different exception scenarios in a more targeted manner.
Avoid Silent Failures:
Avoid catching exceptions and doing nothing (silent failures). At the very least, log the exception information so you can diagnose issues later.
Use finally for Cleanup:
Use the finally block to ensure that cleanup code (like closing files or network connections) is executed, regardless of whether an exception occurred.
Keep try Blocks Small:
Place only the code that may raise exceptions inside the try block. This makes it easier to pinpoint the location of exceptions and helps with code readability.
Avoid Catching Exception Globally:
Avoid using a global try...except Exception block that catches all exceptions. This can mask serious issues and hinder debugging efforts.
Use Custom Exceptions:
Define custom exception classes for situations where your code can raise distinct errors. This makes your code more readable and allows for more specific handling.
Use the with Statement:
Use the with statement for resources like files, database connections, and network sockets. It ensures proper resource management and automatic cleanup.
Log Exceptions:
Use logging to record exception details. This information can be immensely helpful in diagnosing issues in production environments.
Handle Exceptions Locally:
Whenever possible, handle exceptions at the point where they are raised or in a nearby context. This makes the code more self-contained and easier to understand.
Use the else Clause:
Use the else clause in try...except blocks to define code that should only run if no exception was raised. This can help separate regular code paths from error handling.
Avoid Bare except Statements:
Avoid using bare except statements without specifying the exception type. This can lead to unexpected behaviors and obscure errors.
Rethrow Exceptions Sparingly:
If you catch an exception and don't intend to handle it, consider re-raising it using raise without arguments. This preserves the original exception's traceback.
Document Exception Behavior:
Document in comments or docstrings the exceptions your functions/methods might raise. This helps other developers understand how to use your code safely.
Test Exception Scenarios:
Include test cases that intentionally trigger exceptions to ensure your code handles them correctly. This is part of ensuring the reliability of your application.
By following these best practices, you can create more robust and maintainable Python code that handles exceptions effectively and provides a better user experience.
# #  <P style="color:GREEN"> Thank You ,That's All </p>
