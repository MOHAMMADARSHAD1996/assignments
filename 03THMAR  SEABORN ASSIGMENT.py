#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# #  <P style="color:purple"> SEABORN </p>

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt


# Que 1: Name any five plots that we can plot using the Seaborn library. Also, state the uses of each plot
Seaborn is a powerful Python data visualization library built on top of Matplotlib. It provides a high-level interface for creating informative and attractive statistical graphics. Here are five commonly used plots in Seaborn along with their uses:

Scatter Plot:

Use: Scatter plots are used to visualize the relationship between two continuous variables. They are helpful in identifying patterns, correlations, and outliers in the data.
Bar Plot:

Use: Bar plots display categorical data with rectangular bars. They are useful for comparing the values of different categories or showing the distribution of a categorical variable.
Histogram:

Use: Histograms represent the distribution of a single variable by dividing the data into bins and displaying the frequency or density of each bin. They are used to understand the data's distribution and identify patterns like skewness or peaks.
Box Plot (Box-and-Whisker Plot):

Use: Box plots are used to display the distribution of a dataset and highlight its central tendency, spread, and potential outliers. They are particularly useful for visualizing the distribution of continuous data and detecting outliers.
Heatmap:

Use: Heatmaps are used to visualize the relationship between two categorical variables by displaying a matrix of colors. They are great for showing patterns, correlations, or associations between variables in a tabular format.
These are just a few examples, and Seaborn offers many other types of plots for various data visualization needs. The choice of plot depends on the specific characteristics of your data and the insights you want to convey.
# In[ ]:





# Que 2: Load the "fmri" dataset using the load_dataset function of seaborn. Plot a line plot using x =
# "timepoint" and y = "signal" for different events and regions.
# Note: timepoint, signal, event, and region are columns in the fmri dataset.
import seaborn as sns
import matplotlib.pyplot as plt

# Load the "fmri" dataset
fmri_data = sns.load_dataset("fmri")

# Create a line plot using Seaborn
sns.set(style="darkgrid")  # Set the style of the plot (optional)

# Create a line plot with different events and regions
plt.figure(figsize=(10, 6))  # Set the figure size (optional)

# Use the sns.lineplot function to create the line plot
sns.lineplot(data=fmri_data, x="timepoint", y="signal", hue="event", style="region")

# Add labels and a title
plt.xlabel("Timepoint")
plt.ylabel("Signal")
plt.title("FMRI Signal Over Time by Event and Region")

# Show the legend
plt.legend(title="Event", loc="upper right")

# Show the plot
plt.show()
# In[ ]:





# Que 3: Load the "titanic" dataset using the load_dataset function of seaborn. Plot two box plots using x =
# 'pclass', y = 'age' and y = 'fare'.
# Note: pclass, age, and fare are columns in the titanic dataset.

# In[4]:


titanic_data = sns.load_dataset("titanic")

# Create a figure with two subplots (one for 'age' and one for 'fare')
plt.figure(figsize=(12, 6))  # Set the figure size (optional)

# Create the first box plot ('pclass' vs. 'age')
plt.subplot(1, 2, 1)
sns.boxplot(data=titanic_data, x="pclass", y="age")
plt.title("Box Plot of Age by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Age")

# Create the second box plot ('pclass' vs. 'fare')
plt.subplot(1, 2, 2)
sns.boxplot(data=titanic_data, x="pclass", y="fare")
plt.title("Box Plot of Fare by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Fare")

# Adjust the layout and display the plots
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# Que 4: Use the "diamonds" dataset from seaborn to plot a histogram for the 'price' column. Use the hue
# parameter for the 'cut' column of the diamonds dataset.
diamonds_data = sns.load_dataset("diamonds")

# Create a histogram with 'price' and use 'cut' for coloring
sns.set(style="whitegrid")  # Set the style of the plot (optional)

# Use the sns.histplot function to create the histogram with hue
plt.figure(figsize=(10, 6))  # Set the figure size (optional)
sns.histplot(data=diamonds_data, x="price", hue="cut", bins=30, kde=True)

# Add labels and a title
plt.xlabel("Price")
plt.ylabel("Count")
plt.title("Histogram of Diamond Prices by Cut")

# Show the legend
plt.legend(title="Cut", loc="upper right")

# Show the plot
plt.show()
# In[ ]:





# Que 5: Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column
# of the iris dataset.
iris_data = sns.load_dataset("iris")

# Create a pair plot with hue for "species"
sns.set(style="ticks")  # Set the style of the plot (optional)

# Use the sns.pairplot function to create the pair plot
sns.pairplot(data=iris_data, hue="species", palette="husl")

# Show the plot
plt.show()

# In[ ]:





# Que 6: Use the "flights" dataset from seaborn to plot a heatmap.
# Load the "flights" dataset
flights_data = sns.load_dataset("flights")

# Pivot the data to create a matrix suitable for a heatmap
flights_pivot = flights_data.pivot("month", "year", "passengers")

# Create a heatmap
plt.figure(figsize=(10, 6))  # Set the figure size (optional)
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")

# Add labels and a title
plt.xlabel("Year")
plt.ylabel("Month")
plt.title("Passenger Count Heatmap (Flights Dataset)")

# Show the plot
plt.show()
# In[ ]:





# #  <P style="color:GREEN"> Thank You ,That's All </p>
