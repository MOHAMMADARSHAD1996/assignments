#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# Q1. List any five functions of the pandas library with execution.

# In[3]:


#read_csv(): This function is used to read a comma-separated values (CSV) file into a DataFrame.
import pandas as pd

# Read a CSV file into a DataFrame
data = pd.read_csv("C:\\Users\\MOHD. ARSHAD\\Downloads\\data.csv")
print(data.head())
# head(): This function returns the first n rows of a DataFrame. By default, it returns the first 5 rows.
# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 30, 22, 28, 35]}

df = pd.DataFrame(data)

# Display the first 3 rows
print(df.head(3))


# In[5]:


# groupby(): This function is used to group the data in a DataFrame based on specified columns,
# and then you can apply various aggregation functions on the groups.
# Create a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 15, 8, 12, 9]}

df = pd.DataFrame(data)

# Group by 'Category' and calculate the mean value for each group
grouped = df.groupby('Category')['Value'].mean()
print(grouped)


# In[6]:


# merge(): This function is used to combine two or more DataFrames based on a common column or index.
# Create two sample DataFrames
data1 = {'ID': [1, 2, 3],
         'Name': ['Alice', 'Bob', 'Charlie']}
df1 = pd.DataFrame(data1)

data2 = {'ID': [2, 3, 4],
         'Age': [25, 30, 22]}
df2 = pd.DataFrame(data2)

# Merge DataFrames based on 'ID'
merged_df = pd.merge(df1, df2, on='ID')
print(merged_df)


# In[8]:


#pivot_table(): This function creates a pivot table that summarizes data 
# from a DataFrame by aggregating values according to specified rows and columns.
# Create a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 15, 8, 12, 9]}

df = pd.DataFrame(data)

# Create a pivot table
pivot_table = df.pivot_table(index='Category', values='Value', aggfunc='mean')
print(pivot_table)
# Remember to replace 'data.csv' with the actual path to your CSV file in the first example 
# and adjust the data in the other examples according to your needs.


# In[ ]:





# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
# DataFrame with a new index that starts from 1 and increments by 2 for each row.
# 

# In[9]:


"""Certainly! You can achieve this by using the set_index() function in combination with a custom index that starts from 1 and increments by 2 for each row. Here's a Python function that does that:"""
def reindex_with_custom_index(df):
    new_index = pd.Index(range(1, len(df) * 2 + 1, 2), name='NewIndex')
    new_df = df.set_index(new_index)
    return new_df

# Sample DataFrame
data = {'A': [10, 20, 30, 40],
        'B': [5, 15, 25, 35],
        'C': [1, 2, 3, 4]}
df = pd.DataFrame(data)

# Reindex the DataFrame
new_df = reindex_with_custom_index(df)
print(new_df)
"""In this example, the reindex_with_custom_index() function takes a DataFrame df as an argument, creates a new index using pd.Index() with the desired start and increment values, and then sets the new index to the DataFrame using set_index(). The resulting DataFrame new_df will have the new custom index as specified."""


# In[ ]:





# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.
# For example, if the 'Values' column of df contains the values [10, 20, 30, 40, 50], your function should
# calculate and print the sum of the first three values, which is 60.

# In[10]:


#Certainly! You can use the iterrows() function to iterate over the DataFrame rows and 
#calculate the sum of the first three values in the 'Values' column. Here's a Python function that does that:
def calculate_sum_first_three(df):
    total_sum = 0
    for index, row in df.iterrows():
        if index < 3:  # Only consider the first three rows
            total_sum += row['Values']
    print("Sum of the first three values:", total_sum)

# Sample DataFrame
data = {'Values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Calculate and print the sum of the first three values
#calculate_sum_first_three(df)
#In this example, the calculate_sum_first_three() function takes a DataFrame df as
#an argument and iterates over its rows using iterrows(). 
#It checks if the index is less than 3 (to consider the first three rows) and 
#accumulates the 'Values' column values. Finally, it prints the sum to the console.


# Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column 
# 'Word_Count' that contains the number of words in each row of the 'Text' column.
# 

# In[1]:


#Certainly! You can achieve this using the apply 
#function along with a lambda function to count the number of words in each row of the 'Text' column.
#Here's how you can do it:
import pandas as pd

# Sample DataFrame
data = {'Text': ["This is a sample sentence.",
                 "Another example of text.",
                 "Short text."]}
df = pd.DataFrame(data)

# Function to count words in a text
def count_words(text):
    words = text.split()
    return len(words)

# Apply the function to create the 'Word_Count' column
df['Word_Count'] = df['Text'].apply(lambda x: count_words(x))

print(df)
# the sample data with your actual DataFrame.
#The above code will add a new column 'Word_Count' to the DataFrame containing
#the number of words in each row of the 'Text' column.





# Q5. How are DataFrame.size() and DataFrame.shape() different?
In Pandas, both DataFrame.size and DataFrame.shape are attributes used to provide information about the dimensions of a DataFrame, but they serve slightly different purposes:

DataFrame.size:
DataFrame.size returns the total number of elements in the DataFrame, which is calculated by multiplying the number of rows by the number of columns.
It gives you the total count of cells in the DataFrame, including empty or NaN (null) values.
The value returned by DataFrame.size is an integer.
# In[2]:


data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}
df = pd.DataFrame(data)

size = df.size
print(size)  # Output: 6 (2 rows * 3 columns = 6)


DataFrame.shape:
DataFrame.shape returns a tuple representing the dimensions of the DataFrame in the form (rows, columns).
It provides the number of rows and the number of columns in the DataFrame.
The values returned by DataFrame.shape are integers.
# In[3]:


data = {'A': [1, 2, 3],
        'B': [4, 5, 6]}
df = pd.DataFrame(data)

shape = df.shape
print(shape)  # Output: (3, 2) (3 rows, 2 columns)


# In summary, DataFrame.size gives you the total number of elements in the DataFrame, while DataFrame.shape gives you a tuple representing the dimensions of the DataFrame in terms of rows and columns.

# Q6. Which function of pandas do we use to read an excel file?
#To read an Excel file in pandas, you can use the pd.read_excel() function. This function allows you to read data from an #Excel file and create a DataFrame. Here's how you can use it:

# Read an Excel file and create a DataFrame
df = pd.read_excel('file.xlsx')

# Display the DataFrame
print(df)
#Replace 'file.xlsx' with the actual path to your Excel file. By default, pd.read_excel() reads the first sheet of the #Excel file, but you can specify the sheet name or index using the sheet_name parameter.

#Additionally, the pd.read_excel() function provides various optional parameters to customize how the Excel file is read, #such as specifying specific columns, skipping rows, handling headers, etc. You can refer to the pandas documentation for #more information on these parameters: pd.read_excel() documentation.
# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email 
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column 
# 'Username' in df that contains only the username part of each email address.
# 
# The username is the part of the email address that appears before the '@' symbol. For example, if the 
# email address is 'john.doe@example.com', the 'Username' column should contain 'john.doe'. Your 
# function should extract the username from each email address and store it in the new 'Username' 
# column

# In[5]:


#you can achieve this by applying a string manipulation function to extract the username from each email address in the # 'Email' column. You can use the str.split() method along with a lambda function. Here's how you can do it:
# Sample DataFrame
data = {'Email': ['user1@example.com', 'user2@example.com', 'user3@example.com']}
df = pd.DataFrame(data)

# Function to extract username from email
def extract_username(email):
    return email.split('@')[0]

# Apply the function to create the 'Username' column
df['Username'] = df['Email'].apply(lambda x: extract_username(x))

print(df)
#Replace the sample data with your actual DataFrame. The above code will create a new column 'Username' in the DataFrame #containing only the username part of each email address.


# In[6]:


#ertainly! You can use the str.split() method with the @ symbol to split the email addresses and then access the first part #(username) of the split. Here's how you can achieve this:
# Sample DataFrame
data = {'Email': ['user1@example.com', 'user2@example.com', 'user3@example.com']}
df = pd.DataFrame(data)

# Extract username using str.split()
df['Username'] = df['Email'].str.split('@').str[0]

print(df)
#Replace the sample data with your actual DataFrame. The above code will create a new column 'Username' in the DataFrame #containing only the username part of each email address.


# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects 
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The 
# function should return a new DataFrame that contains only the selected rows.
# 
# For example, if df contains the following values:
# 
#    A   B   C
# 
# 0  3   5   1
# 
# 1  8   2   7
# 
# 2  6   9   4
# 
# 3  2   3   5
# 
# 4  9   1   2
# Assignment
# Data Science Masters
# Your function should select the following rows:   A   B   C
# 
# 1  8   2   7
# 
# 4  9   1   2
# 
# The function should return a new DataFrame that contains only the selected rows.

# In[7]:


#Certainly! Here's how you can create a Python function that selects rows from the DataFrame based on the specified #conditions and returns a new DataFrame containing only the selected rows:
import pandas as pd

# Sample DataFrame
data = {'A': [3, 8, 6, 2, 9],
        'B': [5, 2, 9, 3, 1],
        'C': [1, 7, 4, 5, 2]}
df = pd.DataFrame(data)

# Function to select rows based on conditions
def select_rows(df):
    selected_rows = df[(df['A'] > 5) & (df['B'] < 10)]
    return selected_rows

selected_df = select_rows(df)
print(selected_df)
#The function uses boolean indexing to filter the rows where the value in column 'A' is greater than 5 and the value in #column 'B' is less than 10, resulting in a new DataFrame containing only the selected rows.

Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to 
create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days 
for each row in the DataFrame. The moving average should be calculated using a window of size 7 and 
should include the current day
# In[8]:


data = {'Date': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05', '2023-08-06', '2023-08-07'],
        'Sales': [100, 150, 200, 130, 170, 190, 210]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime

# Function to calculate moving average
def calculate_moving_average(df, window_size=7):
    df['MovingAverage'] = df['Sales'].rolling(window=window_size, min_periods=1).mean()
    return df

df_with_moving_average = calculate_moving_average(df)
print(df_with_moving_average)


# In[9]:


# Replace the sample data with your actual DataFrame. 
#The above code will calculate the moving average of the 'Sales' column using a window of size 7 for each row,
#including the current day. The resulting DataFrame will have the 'MovingAverage' column added.
# Note that min_periods=1 is used in the rolling() function to ensure that
# even if there are fewer than 7 days of data available, the moving average is calculated.
# The output will show the DataFrame with the 'MovingAverage' column containing the calculated moving averages.


# Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new 
# column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g. 
# Monday, Tuesday) corresponding to each date in the 'Date' column.
# 
# For example, if df contains the following values:
# 
#          Date
# 
# 0  2023-01-01
# 
# 1  2023-01-02
# 
# 2  2023-01-03
# 
# 3  2023-01-04
# 
# 4  2023-01-05
# 
# Your function should create the following DataFrame:
# 
# 
#          Date    Weekday
# 
# 0  2023-01-01    Sunday
# 
# 1  2023-01-02     Monday
# 
# 2  2023-01-03    Tuesday
# 
# 3  2023-01-04    Wednesday
# 
# 4  2023-01-05    Thursday
# 
# The function should return the modified DataFrame

# In[10]:


data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime

# Function to add weekday column
def add_weekday_column(df):
    df['Weekday'] = df['Date'].dt.strftime('%A')
    return df

df_with_weekday = add_weekday_column(df)
print(df_with_weekday)


# Replace the sample data with your actual DataFrame. The above code will extract the weekday name corresponding to each date in the 'Date' column and add the 'Weekday' column to the DataFrame.
# 
# The %A format specifier in the strftime() function is used to represent the full weekday name. The output will show the DataFrame with the 'Weekday' column added, containing the weekday names corresponding to the dates in the 'Date' column.

# Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python 
# function to select all rows where the date is between '2023-01-01' and '2023-01-31'.

# In[11]:


#You can achieve this by using boolean indexing to filter the rows based on the specified date range. 
#Here's how you can create a function that selects rows where the date is between '2023-01-01' and '2023-01-31':
data = {'Date': ['2023-01-01', '2023-01-15', '2023-02-10', '2023-01-05', '2023-01-25']}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime

# Function to select rows within date range
def select_rows_in_date_range(df, start_date, end_date):
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    selected_rows = df[mask]
    return selected_rows

start_date = '2023-01-01'
end_date = '2023-01-31'
selected_df = select_rows_in_date_range(df, start_date, end_date)
print(selected_df)
#Replace the sample data with your actual DataFrame. The above code will filter the rows in the DataFrame where 
#the 'Date' column falls within the specified date range.
#The output will show the DataFrame containing only the rows with dates between '2023-01-01' and '2023-01-31'.


# Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to 
# be imported

# import pandas as pd
# By convention, pandas is often imported as pd, which makes it easier to reference its functions and classes throughout your code. Once you've imported pandas, you can use its various data manipulation and analysis capabilities to work with DataFrames and Series.

# In[ ]:





# #  <P style="color:GREEN"> Thank You ,That's All </p>
