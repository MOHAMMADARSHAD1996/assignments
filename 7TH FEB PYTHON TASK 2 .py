#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# Q1. You are writing code for a company. The requirement of the company is that you create a python 
# function that will check whether the password entered by the user is correct or not. The function should 
# take the password as input and return the string “Valid Password” if the entered password follows the 
# below-given password guidelines else it should return “Invalid Password”.
# Note: 
# 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
# 2. The Password should contain at least a number and three special characters.
# 3. The length of the password should be 10 characters long.

# In[1]:


import re

def check_password(password):
    # Check length of password
    if len(password) != 10:
        return "Invalid Password"
    
    # Count uppercase and lowercase letters
    uppercase_count = sum(1 for char in password if char.isupper())
    lowercase_count = sum(1 for char in password if char.islower())
    
    # Count digits and special characters
    digit_count = sum(1 for char in password if char.isdigit())
    special_count = sum(1 for char in password if re.match(r'[!@#$%^&*(),.?":{}|<>]', char))
    
    # Check conditions
    if uppercase_count >= 2 and lowercase_count >= 2 and digit_count >= 1 and special_count >= 3:
        return "Valid Password"
    else:
        return "Invalid Password"

# Test the function
password = input("Enter password: ")
result = check_password(password)
print(result)

Q2. Solve the below-given questions using at least one of the following: 

1. Lambda function
2. Filter function
3. Zap function
4. List ComprehensionCheck if the string starts with a particular letter
# In[36]:


starts_with = lambda s, letter: s.startswith(letter)

test_strings = ["apple", "banana", "cherry", "grape"]

target_letter = "b"

for s in test_strings:
    if starts_with(s, target_letter):
        print(f"{s} starts with {target_letter}")
    else:
        print(f"{s} does not start with {target_letter}")


# Check if the string is numeric

# In[35]:


is_numeric = lambda s: s.isdigit()

test_strings = ["123", "abc", "456", "789"]

for s in test_strings:
    if is_numeric(s):
        print(f"{s} is numeric")
    else:
        print(f"{s} is not numeric")

 Sort a list of tuples having fruit names and their quantity. 
   [("mango",99),("orange",80),("grapes", 1000)] 
# In[34]:


fruits = [("mango", 99), ("orange", 80), ("grapes", 1000)]

sorted_fruits = sorted(fruits, key=lambda x: x[1])

for fruit, quantity in sorted_fruits:
    print(f"Fruit: {fruit}, Quantity: {quantity}")


# Find the squares of numbers from 1 to 10

# In[33]:


x = list(map(lambda p:p**2,range(11)))
print(x)


# Find the cube root of numbers from 1 to 10

# In[32]:


x = list(map(lambda p:p**.33,range(11)))
print(x)


# Check if a given number is even

# In[30]:


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_flags = list(map(lambda x: x % 2 == 0, input_list))

for i, is_even in enumerate(even_flags):
    if is_even:
        print(f"{input_list[i]} is even" ,end= ",")
    else:
        print(f"{input_list[i]} is not even")


# Filter odd numbers from the given list.
#    [1,2,3,4,5,6,7,8,9,10]

# In[27]:


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda x: x % 2 != 0, input_list))

print("Odd numbers:", odd_numbers)


#  Sort a list of integers into positive and negative integers lists.
#    [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]

# In[26]:


input_list = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, 0]

positive = list(filter(lambda x: x > 0, input_list))
negative = list(filter(lambda x: x < 0, input_list))

print("Positive numbers:", positive)
print("Negative numbers:", negative)


# #  <P style="color:GREEN"> Thank You ,That's All </p>
