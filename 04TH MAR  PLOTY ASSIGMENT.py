#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# #  <P style="color:purple"> PLOTY </p>

# Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
# scatter plot for age and fare columns in the titanic dataset.

# In[2]:


import seaborn as sns
import plotly.express as px


# In[3]:


# Load the "titanic" dataset using Seaborn
titanic_data = sns.load_dataset("titanic")

# Create a scatter plot using Plotly Express
fig = px.scatter(titanic_data, x="age", y="fare", title="Scatter Plot of Age vs. Fare (Titanic Dataset)")

# Show the plot
fig.show()


# Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express.
df = px.data.tips

# Create a box plot using Plotly Express
fig = px.box(df, x="day", y="total_bill", title="Box Plot of Total Bill by Day")

# Show the plot
fig.show()


# In[ ]:





# Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
# the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
# column with the color parameter.
import plotly.express as px

# Load the "tips" dataset from Plotly Express
df = px.data.tips

# Create a grouped bar chart using Plotly Express
fig = px.bar(
    df,
    x="sex",
    y="total_bill",
    color="day",
    facet_col="smoker",
    title="Grouped Bar Chart of Total Bill by Sex (with Day Color and Smoker Facet)",
)

# Show the plot
fig.show()
# Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
# the color parameter.
# Note: Use "sepal_length", "sepal_width", "petal_length", "petal_width" columns only with the
# dimensions parameter.

# In[11]:


import plotly.express as px

# Load the "iris" dataset from Plotly Express
df = px.data.iris()

# Create a scatter matrix plot with color differentiation by species
fig = px.scatter_matrix(
    df,
    dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
    color="species",
    title="Scatter Matrix Plot of Iris Dataset by Species",
)

# Show the plot
fig.show()


# Q5. What is Distplot? Using Plotly express, plot a distplot.

# In[12]:


# Sample data (replace this with your own dataset)
data = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]

# Create a distplot using Plotly Express
fig = px.histogram(data, nbins=10, title="Distplot of Sample Data")

# Show the plot
fig.show()


# #  <P style="color:GREEN"> Thank You ,That's All </p>
