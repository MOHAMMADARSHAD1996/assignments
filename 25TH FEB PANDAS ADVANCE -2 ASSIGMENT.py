#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# import pandas as pd
# course_name = [‘Data Science’, ‘Machine Learning’, ‘Big Data’, ‘Data Engineer’]
# duration = [2,3,6,4]
# df = pd.DataFrame(data = {‘course_name’ : course_name, ‘duration’ : duration})
# Q1. Write a code to print the data present in the second row of the dataframe, df.

# In[1]:


import pandas as pd

course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]

df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})

# Print the data present in the second row
second_row_data = df.iloc[1]
print(second_row_data)


# Q2. What is the difference between the functions loc and iloc in pandas.DataFrame?
In pandas, both loc and iloc are used to access and manipulate data in a DataFrame, but they have different ways of referencing and selecting data.
loc stands for "location" and is primarily label-based indexing. It is used to access data by referring to the row and column labels. This means you use actual row and column labels to extract data.
iloc stands for "integer location" and is integer-based indexing. It is used to access data by using integer indices for rows and columns. This is similar to the way you would use indices in a typical list or array.
Here's a breakdown of their differences:

loc:

Uses label-based indexing for both rows and columns.
You provide row and column labels to access data.
The syntax is df.loc[row_label, column_label].
iloc:

Uses integer-based indexing for both rows and columns.
You provide integer indices to access data.
The syntax is df.iloc[row_index, column_index].
Here are some examples to illustrate the differences:

Assume you have a DataFrame like this:

css
Copy code
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
# Accessing a specific element
value = df.loc[1, 'B']  # Returns 5

# Accessing a row
row_data = df.loc[0]  # Returns the entire first row as a Series

# Accessing a column
column_data = df.loc[:, 'C']  # Returns the entire 'C' column as a Series
# Accessing a specific element
value = df.iloc[1, 2]  # Returns 8

# Accessing a row
row_data = df.iloc[0]  # Returns the entire first row as a Series

# Accessing a column
column_data = df.iloc[:, 2]  # Returns the entire third column as a Series
#In summary, loc uses label-based indexing, and iloc uses integer-based indexing to access data in a pandas DataFrame. 
#The choice between them depends on whether you want to access data using labels or integer indices.
# In[ ]:





# Q3. Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df
# then find the output for both new_df.loc[2] and new_df.iloc[2].
# Did you observe any difference in both the outputs? If so then explain it.
# Consider the below code to answer further questions:
# import numpy as np
# columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
# indices = [1,2,3,4,5,6]
# #Creating a dataframe:
# df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)
It seems like you're referring to a DataFrame manipulation task in Python using the pandas library. Let's break down the steps you've provided and then answer your questions:

You have a DataFrame called df1 created using random values and specified columns and indices.
You want to reindex this DataFrame using the list reindex = [3, 0, 1, 2] and store the result in a new variable called new_df.
You want to analyze the outputs of new_df.loc[2] and new_df.iloc[2].
Here's the code to perform these tasks:

python
Copy code
import pandas as pd
import numpy as np

columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1, 2, 3, 4, 5, 6]

# Creating a DataFrame:
df1 = pd.DataFrame(np.random.rand(6, 6), columns=columns, index=indices)

reindex = [3, 0, 1, 2]
new_df = df1.reindex(reindex)

output_loc = new_df.loc[2]
output_iloc = new_df.iloc[2]
Now, let's discuss the outputs and any differences between .loc and .iloc:

new_df.loc[2]:
This will return the row with the label/index 2 from the new_df DataFrame. Since the new indices are [3, 0, 1, 2], and the label 2 corresponds to the last index, it will return the row with the index 2 from the original df1 DataFrame, but with the new indexing.

new_df.iloc[2]:
This will return the row located at the integer position 2 from the new_df DataFrame. Since the new indices are [3, 0, 1, 2], the row at integer position 2 in new_df will correspond to the row that originally had index 1 in the df1 DataFrame.

In summary, the key difference between .loc and .iloc is that .loc uses labels/indices, while .iloc uses integer positions to access rows and columns. In this specific case, due to the reindexing, you'll observe a difference in the outputs of new_df.loc[2] and new_df.iloc[2] because they refer to different rows from the original df1 DataFrame.





# Q4. Write a code to find the following statistical measurements for the above dataframe df1:
# (i) mean of each and every column present in the dataframe.
# (ii) standard deviation of column, ‘column_2’

# Certainly! You can use the pandas library to calculate these statistical measurements for the DataFrame df1. Here's the code to find the mean of each column and the standard deviation of the column named 'column_2':

# In[3]:


import numpy as np

columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1, 2, 3, 4, 5, 6]

# Creating a DataFrame:
df1 = pd.DataFrame(np.random.rand(6, 6), columns=columns, index=indices)

# (i) Mean of each column
column_means = df1.mean()
print("Mean of each column:")
print(column_means)

# (ii) Standard deviation of column 'column_2'
std_dev_column_2 = df1['column_2'].std()
print("\nStandard deviation of column 'column_2':")
print(std_dev_column_2)

In the above code:
(i) The .mean() function is used to calculate the mean of each column in the DataFrame. It returns a Series containing the mean value for each column.
(ii) The .std() function is used to calculate the standard deviation of the specified column 'column_2'. It returns a single value representing the standard deviation of the column.
Just replace the creation of the df1 DataFrame with your own DataFrame if you're working with an existing DataFrame.
# In[ ]:





# Q5. Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
# mean of column, column_2.
# If you are getting errors in executing it then explain why.
# [Hint: To replace the data use df1.loc[] and equate this to string data of your choice.]
#Replacing numerical data with a string in a numeric column will likely result in errors, 
#as pandas DataFrames are designed to hold data of a consistent data type within a column. 
#Mixing data types within a single column can lead to unexpected behavior and errors when performing calculations.
#Here's the code you've provided, along with explanations of potential errors:
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1, 2, 3, 4, 5, 6]

# Creating a DataFrame:
df1 = pd.DataFrame(np.random.rand(6, 6), columns=columns, index=indices)

# Replace data in the second row of 'column_2' with a string
df1.loc[2, 'column_2'] = 'string_data'  # Replacing with a string

# Calculate the mean of column 'column_2'
mean_column_2 = df1['column_2'].mean()
print("Mean of column 'column_2':", mean_column_2)
#Explanation:
#In the code provided, you're attempting to replace the data in the second row of the 'column_2' with a string using df1.loc[2, 'column_2'] = 'string_data'.
#However, this will likely raise a TypeError because you're trying to assign a string to a column that was originally created with numerical data. Pandas DataFrames are designed to hold data of a consistent data type within a column. When you try to mix data types, it can result in errors.
#As a result of the TypeError, you might not be able to proceed to calculate the mean of 'column_2' using df1['column_2'].mean().
#If you need to replace data in the DataFrame with a different data type, it's generally better to create a new column for that purpose or consider using a more suitable data structure for your needs.
# In[ ]:





# Q6. What do you understand about the windows function in pandas and list the types of windows
# functions?
n pandas, a window function is a powerful tool used for performing calculations on a specific subset of data within a defined "window" or range. This window slides or expands over the dataset, allowing you to compute various operations on a window of neighboring rows. Window functions are typically used in conjunction with the groupby operation to work within specific groups of data.

Window functions in pandas are implemented using the .rolling() and .expanding() methods. The main types of window functions are:

Rolling Window Functions (rolling()): These functions create a rolling window of a fixed size that moves across the data. The window includes a specified number of preceding rows along with the current row. Common rolling window functions include:

mean(): Calculate the mean of values in the window.
sum(): Compute the sum of values in the window.
min(): Find the minimum value in the window.
max(): Find the maximum value in the window.
std(): Calculate the standard deviation of values in the window.
Expanding Window Functions (expanding()): These functions create an expanding window that grows over time, including all previous rows up to the current row. Common expanding window functions include:

mean(): Compute the mean of all values up to the current row.
sum(): Calculate the sum of all values up to the current row.
min(): Find the minimum value encountered up to the current row.
max(): Find the maximum value encountered up to the current row.
std(): Compute the standard deviation of all values up to the current row.
Other Window Functions: These functions involve more complex operations, often using data from neighboring rows. Examples include:

rank(): Assign a rank to each element within the window.
shift(): Shift values within the window by a specified number of positions.
diff(): Compute the difference between consecutive values within the window.
pct_change(): Calculate the percentage change between consecutive values.
Window functions are particularly useful for time-series analysis, rolling statistics, and other scenarios where you need to consider the relationships between data points within a certain context. They allow you to efficiently perform calculations without resorting to explicit looping constructs.
# In[ ]:





# Q7. Write a code to print only the current month and year at the time of answering this question.
# 
# [Hint: Use pandas.datetime function]

# In[7]:


# Get the current date and time
current_datetime = pd.to_datetime('now')

# Extract the current month and year
current_month = current_datetime.month
current_year = current_datetime.year

# Print the current month and year
print("Current Month:", current_month)
print("Current Year:", current_year)

When you run this code, it will use the pd.to_datetime('now') function to get the current date and time, and then extract the month and year components using the .month and .year attributes. The printed output will show the current month and year at the time of running the code.
# In[ ]:





# Q8. Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and
# calculates the difference between them in days, hours, and minutes using Pandas time delta. The
# program should prompt the user to enter the dates and display the result.

# Sure, here's a Python program that takes two dates as input and calculates the difference between them in days, hours, and minutes using Pandas' Timedelta:

# In[9]:


# Function to calculate the difference between two dates
def calculate_time_difference(start_date, end_date):
    start_datetime = pd.to_datetime(start_date)
    end_datetime = pd.to_datetime(end_date)
    
    time_difference = end_datetime - start_datetime
    
    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds // 60) % 60
    
    return days, hours, minutes

# Prompt the user for input
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Calculate the time difference
days, hours, minutes = calculate_time_difference(start_date, end_date)

# Display the result
print("Time Difference:")
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")

In this program, the calculate_time_difference() function takes the start and end dates as input. It converts the dates to Pandas Timestamp objects, calculates the time difference using the Timedelta object, and then extracts the difference in days, hours, and minutes. The user is prompted to enter the dates, and the program displays the calculated time difference.
# Q9. Write a Python program that reads a CSV file containing categorical data and converts a specified
# column to a categorical data type. The program should prompt the user to enter the file path, column
# name, and category order, and then display the sorted data.
#  here's a Python program that reads a CSV file containing categorical data, converts a specified column to a categorical data type, and displays the sorted data based on the specified column:
# Function to convert a column to categorical data type and display sorted data
def convert_and_sort_categorical_column(file_path, column_name, category_order):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Convert the specified column to categorical data type
    df[column_name] = pd.Categorical(df[column_name], categories=category_order, ordered=True)
    
    # Sort the DataFrame based on the categorical column
    sorted_df = df.sort_values(by=[column_name])
    
    return sorted_df

# Prompt the user for input
file_path = input("Enter the file path of the CSV file: ")
column_name = input("Enter the column name to convert to categorical: ")
category_order = input("Enter the category order (comma-separated): ").split(',')

# Call the function to convert and sort the categorical column
sorted_data = convert_and_sort_categorical_column(file_path, column_name, category_order)

# Display the sorted data
print("Sorted Data:")
print(sorted_data)
In this program, the convert_and_sort_categorical_column() function takes the file path, column name, and category order as input. It reads the CSV file using pd.read_csv(), converts the specified column to a categorical data type using the provided category order, and sorts the DataFrame based on the categorical column. The user is prompted to enter the necessary inputs, and the program displays the sorted data.
# In[ ]:





# Q10. Write a Python program that reads a CSV file containing sales data for different products and
# visualizes the data using a stacked bar chart to show the sales of each product category over time. The
# program should prompt the user to enter the file path and display the chart.
To create a Python program that reads a CSV file containing sales data for different products and visualizes the data using a stacked bar chart, you can use the pandas library for data manipulation and the matplotlib library for data visualization. Here's a sample program:
import matplotlib.pyplot as plt

# Function to read CSV file, process data, and create stacked bar chart
def visualize_sales_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Group data by 'Date' and 'Product Category', and sum up the sales
    grouped_data = df.groupby(['Date', 'Product Category'])['Sales'].sum().unstack()
    
    # Plot a stacked bar chart
    plt.figure(figsize=(10, 6))
    grouped_data.plot(kind='bar', stacked=True)
    plt.title('Sales of Product Categories Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend(title='Product Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Prompt the user for input
file_path = input("Enter the file path of the CSV file: ")

# Call the function to visualize sales data using a stacked bar chart
visualize_sales_data(file_path)
In this program, the visualize_sales_data() function reads the CSV file using pd.read_csv(), processes the data by converting the 'Date' column to datetime and grouping it by both 'Date' and 'Product Category'. It then creates a stacked bar chart using the grouped data and matplotlib.

The user is prompted to enter the file path of the CSV file containing sales data, and the program displays the stacked bar chart showing the sales of each product category over time. Make sure you have the pandas and matplotlib libraries installed before running the program. You can install them using the following commands:


# In[ ]:




Q11. You are given a CSV file containing student data that includes the student ID and their test score. Write
a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and
displays the results in a table.
The program should do the followingM
I Prompt the user to enter the file path of the CSV file containing the student dataR
I Read the CSV file into a Pandas DataFrameR
I Calculate the mean, median, and mode of the test scores using Pandas toolsR
I Display the mean, median, and mode in a table.
Assume the CSV file contains the following columnsM
I Student ID: The ID of the studentR
I Test Score: The score of the student's test.
Example usage of the program:
Enter the file path of the CSV file containing the student data: student_data.csv
+-----------+--------+
| Statistic | Value |
+-----------+--------+
| Mean | 79.6 |
| Median | 82 |
| Mode | 85, 90 |
+-----------+--------+
Assume that the CSV file student_data.csv contains the following data:
Student ID,Test Score
1,85
2,90
3,80
4,75
5,85
6,82
7,78
8,85
9,90
10,85
The program should calculate the mean, median, and mode of the test scores and display the results
in a table.from scipy import stats

# Prompt the user to enter the file path
file_path = input("Enter the file path of the CSV file containing the student data: ")

# Read CSV file into a Pandas DataFrame
data = pd.read_csv(file_path)

# Calculate mean, median, and mode
mean_score = data['Test Score'].mean()
median_score = data['Test Score'].median()
mode_scores = stats.mode(data['Test Score'])[0]

# Display the results in a table
result_table = pd.DataFrame({
    'Statistic': ['Mean', 'Median', 'Mode'],
    'Value': [mean_score, median_score, ', '.join(map(str, mode_scores))]
})

print(result_table.to_string(index=False))Make sure to have the student_data.csv file in the same directory as this script or provide the full path to the file when prompted. The program will read the data, calculate the mean, median, and mode of the test scores, and display the results in a table format as shown in your example usage.
# #  <P style="color:GREEN"> Thank You ,That's All </p>
