#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# Q1. What is an Exception in python? Write the difference between Exceptions and syntex errors
In Python, an exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions. When an exceptional condition arises, an exception is raised, which can be caught and handled using appropriate exception-handling mechanisms.

Exceptions can occur for various reasons, such as attempting to divide by zero, accessing an index that doesn't exist in a list, or trying to open a file that doesn't exist. They can also be raised explicitly using the raise statement to signal that an error condition has occurred.

Differences between Exceptions and Syntax Errors:

Nature of Occurrence:

Exception: Occurs during runtime when an unexpected condition or error arises while executing the program. These are runtime errors that can potentially be handled.
Syntax Error: Occurs during the parsing of the code, before the program starts running. These errors are due to invalid syntax and prevent the program from even starting.
Handling:

Exception: Can be caught and handled using try, except, else, and finally blocks, allowing the program to recover from the error and continue running.
Syntax Error: Can't be caught and handled within the program. They need to be fixed in the source code before running the program.
Examples:

Exception Examples: ZeroDivisionError, IndexError, ValueError, FileNotFoundError, etc.
Syntax Error Example: Missing a colon in an if statement, forgetting to close parentheses, etc.
When Detected:

Exception: Detected when the program is running and trying to execute certain statements or operations.
Syntax Error: Detected by the Python interpreter during the parsing phase before execution begins.
Cause:

Exception: Caused by issues such as invalid user input, unexpected conditions, or external factors like unavailable files.
Syntax Error: Caused by incorrect or malformed code that doesn't follow Python's grammar rules.
Impact:

Exception: Can be handled, allowing the program to gracefully recover or provide meaningful feedback to the user.
Syntax Error: Requires fixing the code in the source file before it can be executed.
In summary, exceptions are runtime errors that occur during program execution and can be caught and handled, while syntax errors are errors that occur before the program even starts running due to invalid code syntax.Q2. What happens when an exception is not handled? Explin with an exampleWhen an exception is not handled, it leads to what's known as an "unhandled exception" or "uncaught exception." In Python, if an exception is raised but not caught and handled using appropriate exception-handling mechanisms, the program's normal flow is disrupted, and the program terminates abruptly, printing an error message indicating the type of exception and the line where it occurred.

Here's an example to illustrate what happens when an exception is not handled:
# In[10]:


def divide(a, b):
    return a / b

num1 = 10
num2 = 0

result = divide(num1, num2)
print("Result:", result)

In this example, the divide function attempts to perform division. However, when num2 is set to 0, a ZeroDivisionError is raised because division by zero is not allowed. Since we haven't provided any exception-handling code for this error, the program will terminate with an error message like this:
# In[12]:


# Traceback (most recent call last):
#   File "example.py", line 6, in <module>
#     result = divide(num1, num2)
#   File "example.py", line 2, in divide
#     return a / b
# ZeroDivisionError: division by zero

When an exception is not handled, it leads to what's known as an "unhandled exception" or "uncaught exception." In Python, if an exception is raised but not caught and handled using appropriate exception-handling mechanisms, the program's normal flow is disrupted, and the program terminates abruptly, printing an error message indicating the type of exception and the line where it occurred.

Here's an example to illustrate what happens when an exception is not handled:

python
Copy code
def divide(a, b):
    return a / b

num1 = 10
num2 = 0

result = divide(num1, num2)
print("Result:", result)
In this example, the divide function attempts to perform division. However, when num2 is set to 0, a ZeroDivisionError is raised because division by zero is not allowed. Since we haven't provided any exception-handling code for this error, the program will terminate with an error message like this:

arduino
Copy code
Traceback (most recent call last):
  File "example.py", line 6, in <module>
    result = divide(num1, num2)
  File "example.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
As you can see, the traceback shows the sequence of function calls that led to the unhandled exception. The error message indicates the type of exception (ZeroDivisionError) and provides additional information about the exception's cause (division by zero). The program terminates at this point, and any code that was supposed to be executed after the exception occurred is not executed.
To handle this situation, you can use a try and except block to catch the exception and provide appropriate handling or recovery mechanisms. If you don't handle exceptions, your program's stability and user experience may be compromised, especially in production environments.Q3. Which Python statements are used to catch and handle exceptions? Explain with an exampleIn Python, the statements used to catch and handle exceptions are try, except, else, and finally. These statements allow you to create a structured approach to handle exceptions and control the flow of your program when errors occur.

Here's how each of these statements works with an example:

try: The try block is used to enclose the code that might raise an exception. If an exception occurs within the try block, the program will immediately jump to the appropriate except block.

except: The except block is used to catch and handle exceptions. It follows the try block and specifies the type of exception(s) it can catch. If an exception of the specified type occurs in the try block, the code within the except block will be executed.

else: The else block is executed if no exceptions occur in the try block. It is placed after all the except blocks. This can be useful for separating normal code execution from exception handling.

finally: The finally block contains code that is executed regardless of whether an exception occurred or not. It is placed after all except and else blocks. This is often used for cleanup operations like closing files or releasing resources.

Here's an example that demonstrates the use of these statements:
# In[13]:


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Please provide valid numeric inputs.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The result is: {result}")
    finally:
        print("This will always execute, regardless of exceptions.")

# Example usage
divide(10, 2)    # This will print "The result is: 5.0" and the "finally" block
divide(10, 0)    # This will print "Error: Division by zero is not allowed." and the "finally" block
divide(10, '2')  # This will print "Error: Please provide valid numeric inputs." and the "finally" block

In the above example:

The try block contains code that might raise exceptions. In this case, it's attempting division.
The except blocks catch specific types of exceptions. If a ZeroDivisionError or TypeError occurs, the appropriate error message is printed.
The Exception catch-all block will handle any other exceptions that aren't explicitly caught by the previous except blocks.
The else block is executed if no exceptions were raised within the try block. It's used to specify code that should run when no exceptions occur.
The finally block contains code that will always execute, regardless of whether an exception occurred or not. It's often used for cleanup tasks.
Keep in mind that using a broad except block (like except Exception:) might make it harder to identify specific issues in your code, so it's generally better to catch specific exception types whenever possible.Q4. Explain with an example:
-> try and else 
-> finally
-> raise   1. try and else:
The try block is used to enclose a section of code that might raise an exception. The else block is executed when no exception occurs within the try block. This allows you to separate the normal code execution from the exception handling.
# In[5]:


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print("You entered:", num)

In this example, the user is prompted to enter a number. If they enter a non-integer value, a ValueError is raised and the message "Invalid input. Please enter a valid number." is printed. If they enter a valid integer, the else block is executed, and the entered number is displayed.2. finally:
The finally block is used to specify code that should be executed regardless of whether an exception was raised or not. This is often used for tasks like cleanup or releasing resources.
# In[8]:


try:
    file = open("arshad.txt", "w")
    file = open("arshad.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File content:", content)
finally:
    file.close()
    print("File closed.")

In this example, we attempt to open a file for reading. If the file is not found, a FileNotFoundError is caught and an appropriate message is printed. If the file is successfully opened, its content is printed. The finally block ensures that the file is closed, regardless of whether an exception occurred or not.3. raise:
The raise keyword is used to manually raise an exception. This is particularly useful when you want to handle specific situations by raising your own custom exceptions.
# In[9]:


def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        raise ValueError("Must be at least 18 years old")
    else:
        print("Age is valid")

try:
    user_age = int(input("Enter your age: "))
    validate_age(user_age)
except ValueError as ve:
    print("Invalid age:", ve)

In this example, a function validate_age is defined to validate the age entered by the user. If the age is negative or less than 18, a ValueError is raised with an appropriate message. In the try block, the user's age is obtained, and the validate_age function is called. If an exception occurs, the error message is caught and displayed.

These examples showcase how try, else, finally, and raise work in Python's exception handling mechanism.Q5. What are Custom Excptions in python? Why do we need Custom Exceptions? Explain with an exampleIn Python, custom exceptions are user-defined exception classes that allow you to create your own specific exception types. While Python provides a set of built-in exceptions to handle various errors, there might be situations where these built-in exceptions don't fully capture the nature of the error you want to handle. This is where custom exceptions come in.

Custom exceptions are useful for the following reasons:

Better Error Handling: By creating custom exceptions, you can provide more meaningful error messages that are specific to your application. This helps in understanding what went wrong and where, which is especially important when debugging.

Semantic Clarity: Custom exceptions can make your code more self-explanatory and maintainable. They can provide a clearer indication of the type of error being raised, enhancing the readability of your codebase.

Hierarchical Organization: You can create a hierarchy of custom exceptions, making it easier to categorize and handle different types of errors in a structured manner.

Modularity: Custom exceptions allow you to encapsulate error handling logic within your application's domain, making it easier to change and manage the error-handling behavior without affecting the rest of the code.

Here's an example to illustrate the concept:

Suppose you're building a banking application, and you want to handle specific errors related to insufficient funds during a transaction. Instead of relying solely on the built-in ValueError or Exception for all cases, you can create a custom exception class called InsufficientFundsError:
# In[4]:


class InsufficientFundsError(Exception):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.message = f"Insufficient funds in account {account}. Needed {amount}."

def perform_transaction(account_balance, amount):
    if account_balance < amount:
        raise InsufficientFundsError(account_balance, amount)
    else:
        # Perform the transaction logic here
        pass

try:
    account_balance = 100
    withdrawal_amount = 150
    perform_transaction(account_balance, withdrawal_amount)
except InsufficientFundsError as ife:
    print("Error:", ife.message)

Q6.  Create custom exception class. Use this class to handle an exception
# In[2]:


class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def custom_function(number):
    if number < 0:
        raise CustomException("Number cannot be negative")

try:
    user_input = int(input("Enter a number: "))
    custom_function(user_input)
except CustomException as ce:
    print("Custom Exception:", ce)
except ValueError:
    print("Invalid input. Please enter a valid number.")


# #  <P style="color:GREEN"> Thank You ,That's All </p>
