#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# #  <P style="color:purple"> BOKEH </p>

# Q1. How can you create a Bokeh plot using Python code?

# In[1]:


from bokeh.plotting import figure, show


# In[2]:


x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 17, 8]
p = figure(title="My Bokeh Plot", x_axis_label="X-axis", y_axis_label="Y-axis")
p.line(x, y, legend_label="Line", line_width=2, line_color="blue")
show(p)


# In[ ]:





# Q2. What are glyphs in Bokeh, and how can you add them to a Bokeh plot? Explain with an example.

# In[4]:


# In Bokeh, glyphs are visual markers that represent data points on a plot. Glyphs can be used to create various types of visualizations, such as scatter plots, line charts, bar charts, and more. Bokeh provides a wide range of glyphs that you can use to customize the appearance of your data points.
# To add glyphs to a Bokeh plot, you typically follow these steps:
# Import the necessary modules from Bokeh.
# Create a figure using the figure function, specifying the plot's attributes like title, axis labels, and more.
# Use one of Bokeh's glyph functions (e.g., circle, line, square, triangle, etc.) to add data points or lines to the plot.
# Customize the appearance of the glyphs by setting various attributes such as size, color, line width, and more.
# Show the plot using the show function.
# Here's an example of how to add glyphs to a Bokeh plot:

from bokeh.plotting import figure, show

# Data
x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 17, 8]

# Create a figure
p = figure(title="Bokeh Glyph Example", x_axis_label="X-axis", y_axis_label="Y-axis")

# Add a circle glyph
p.circle(x, y, size=10, color="blue", alpha=0.5, legend_label="Circle Glyph")

# Add a line glyph
p.line(x, y, line_width=2, line_color="red", legend_label="Line Glyph")

# Show the plot
show(p)
#In this example:

# We import the necessary Bokeh modules.
# We create a figure with a title and axis labels using figure.
# We add a circle glyph using circle to represent data points. We customize the size, color, and transparency (alpha) of the circles.
# We add a line glyph using line to connect data points. We customize the line width and color.
# Finally, we display the plot using show.
# This example demonstrates how to add both circle and line glyphs to a Bokeh plot. You can explore other glyph functions and customize the appearance to create various types of visualizations.


# In[ ]:





# Q3. How can you customize the appearance of a Bokeh plot, including the axes, title, and legend?
To customize the appearance of a Bokeh plot, including the axes, title, and legend, you can use various methods and attributes provided by Bokeh. Here's how you can customize different aspects of a Bokeh plot:

Title and Labels:

Customize the plot's title using the title attribute of the figure object.
Set labels for the x-axis and y-axis using the x_axis_label and y_axis_label attributes.

p = figure(title="Customized Bokeh Plot", x_axis_label="X-axis", y_axis_label="Y-axis")
Axis Ticks and Labels:

Customize axis ticks and labels using the axis_label_text_font, axis_label_text_font_size, and axis_label_text_font_style attributes.

p.xaxis.axis_label_text_font = "Arial"
p.xaxis.axis_label_text_font_size = "14pt"
p.yaxis.axis_label_text_font_style = "italic"
Axis Ranges:

Set the range of the x-axis and y-axis using the x_range and y_range attributes.

p.x_range = (0, 10)  # Customize the x-axis range
p.y_range = (0, 20)  # Customize the y-axis range
Legend:

Customize the legend by setting the legend attribute of the glyphs and specifying legend labels.

p.circle(x, y, size=10, color="blue", alpha=0.5, legend_label="Data Points")
p.line(x, y, line_width=2, line_color="red", legend_label="Line")
p.legend.title = "Legend Title"
Grid Lines and Background:

Customize grid lines and background using attributes like grid.grid_line_color, background_fill_color, and background_fill_alpha.

p.grid.grid_line_color = "gray"
p.background_fill_color = "lightgray"
p.background_fill_alpha = 0.2
Plot Size:

Set the size of the plot using the plot_width and plot_height attributes of the figure object.

p.plot_width = 600
p.plot_height = 400
Plot Outline:

Customize the outline of the plot using attributes like outline_line_color and outline_line_width.

p.outline_line_color = "black"
p.outline_line_width = 2
Text and Font:

Customize text properties such as font, size, and style for the title, labels, and legend using attributes like title.text_font, title.text_font_size, and legend.label_text_font_style.

p.title.text_font = "Arial"
p.title.text_font_size = "16pt"
p.xaxis.axis_label_text_font_size = "12pt"
p.legend.label_text_font_style = "bold"
Text Location:

Customize the location of title and labels using attributes like title_location, title_text_align, and xaxis.axis_label_standoff.
p.title_location = "above"
p.title_text_align = "center"
p.xaxis.axis_label_standoff = 20
By applying these customization techniques, you can tailor the appearance of your Bokeh plot to match your specific requirements and design preferences.
# In[ ]:




Q4. What is a Bokeh server, and how can you use it to create interactive plots that can be updated in
real time?A Bokeh server is a key feature of the Bokeh library that allows you to create interactive web applications with real-time updates. With a Bokeh server, you can build dynamic and interactive plots, dashboards, and data applications that respond to user input and data changes without the need to regenerate or reload the entire web page.

Here are the main features and benefits of a Bokeh server:

Real-Time Interactivity: Bokeh servers enable real-time interactivity by maintaining a live connection between the Python server and the client's web browser. This means that changes to the plot or data on the server side can be immediately reflected in the web application without requiring page refreshes.

Responsive User Interfaces: You can create interactive user interfaces (UI) with widgets such as sliders, buttons, dropdowns, and text inputs. These widgets allow users to interact with the data and control the behavior of the plot.

Dynamic Data Updates: Bokeh servers can update data sources in real time. This is particularly useful for live data streams, data streaming from databases, or updates triggered by user actions.

Custom Callbacks: You can define custom Python callbacks that respond to events or changes in the user interface. These callbacks can modify the plot, update data sources, and perform computations in real time.

Scalability: Bokeh servers can be deployed on a variety of platforms, including local development environments, cloud servers, or in containerized environments. This makes it possible to build scalable data applications.

Here's a basic outline of how you can use a Bokeh server to create interactive plots with real-time updates:

Import Required Modules: Import the necessary modules from Bokeh for creating plots, widgets, and the server application.

Create a Plot: Build the initial Bokeh plot with your desired visualizations and add any widgets you want to use.

Define Callbacks: Write Python callback functions that specify how the plot and data should update in response to user interactions or changes in data sources.

Create a Bokeh Application: Define a Bokeh application that includes the plot, widgets, and the callbacks. You can use the bokeh.application module for this purpose.

Run the Bokeh Server: Start the Bokeh server using the bokeh serve command followed by the script name containing your Bokeh application.

Access the Web Application: Access the interactive web application in your web browser by navigating to the specified URL. The application will be hosted by the Bokeh server.

As an example, you might create an interactive dashboard that displays real-time stock price data and allows users to adjust date ranges or select specific stocks. The Bokeh server would continuously update the chart and display new data points as they arrive.

To get started with Bokeh servers, you can refer to the official Bokeh documentation, which provides detailed tutorials and examples for building interactive applications.
# In[ ]:





# Q5. How can you embed a Bokeh plot into a web page or dashboard using Flask or Django?
Embedding a Bokeh plot into a web page or dashboard using Flask or Django involves a few key steps. Below, I'll provide a general guide for both Flask and Django:

Using Flask:

Install Flask: Make sure you have Flask installed. You can install it using pip:

pip install Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
Prepare Bokeh Plot: Create your Bokeh plot and save it as an HTML file.

from bokeh.plotting import figure, output_file, show

# Create a Bokeh plot
p = figure(plot_width=400, plot_height=400)
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 1])

# Save the plot as an HTML file
output_file("bokeh_plot.html")
show(p)
HTML Template: Create an HTML template (e.g., templates/index.html) that includes a placeholder for your Bokeh plot.

<!DOCTYPE html>
<html>
<head>
    <title>Bokeh Plot Embedded in Flask</title>
</head>
<body>
    <h1>My Web Page</h1>
    <!-- Placeholder for Bokeh plot -->
    <div>
        {% include 'bokeh_plot.html' %}
    </div>
</body>
</html>
Run Flask App: Start your Flask application to serve the web page with the embedded Bokeh plot.

if __name__ == "__main__":
    app.run(debug=True)
Access the Web Page: Navigate to http://localhost:5000/ in your web browser to see the Flask web page with the embedded Bokeh plot.

Using Django:

Create a Django Project: Create a Django project and app if you haven't already.

Prepare Bokeh Plot: Create your Bokeh plot and save it as an HTML file, similar to the previous example.

Template Folder: Create a folder for your Django app templates if it doesn't exist. Place the Bokeh plot HTML file inside this folder.

Django View: Define a Django view that renders an HTML template containing the embedded Bokeh plot.

from django.shortcuts import render

def bokeh_plot(request):
    return render(request, "app_name/bokeh_plot_template.html")
URL Configuration: Configure a URL route that maps to the bokeh_plot view in your Django app's urls.py.

from django.urls import path
from . import views

urlpatterns = [
    path("bokeh-plot/", views.bokeh_plot, name="bokeh_plot"),
]
HTML Template: Create an HTML template that includes the Bokeh plot HTML file.

<!DOCTYPE html>
<html>
<head>
    <title>Bokeh Plot Embedded in Django</title>
</head>
<body>
    <h1>My Web Page</h1>
    <!-- Placeholder for Bokeh plot -->
    <div>
        {% include 'app_name/bokeh_plot.html' %}
    </div>
</body>
</html>
Access the Web Page: Run your Django project (python manage.py runserver) and navigate to the appropriate URL (e.g., http://localhost:8000/app_name/bokeh-plot/) to see the Django web page with the embedded Bokeh plot.

These are general steps for embedding a Bokeh plot into web pages in Flask or Django. Depending on your specific project structure and requirements, you may need to adapt these steps accordingly.
# In[ ]:





# #  <P style="color:GREEN"> Thank You ,That's All </p>
