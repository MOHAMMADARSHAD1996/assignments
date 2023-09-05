#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# #  <P style="color:purple"> STATISTTICS BASIC-2 </p>

# Q1. What are the three measures of central tendency?
The three measures of central tendency are:

Mean: The mean is the average of a set of values. It is calculated by adding up all the values in the data set and then dividing by the number of values.

Median: The median is the middle value in a data set when the values are arranged in ascending or descending order. If there is an even number of values, the median is the average of the two middle values.

Mode: The mode is the value that occurs most frequently in a data set. A data set can have one mode (unimodal), more than one mode (multimodal), or no mode at all if all values occur with the same frequency.

These measures help describe the central or typical value of a data set.
# In[ ]:





# Q2. What is the difference between the mean, median, and mode? How are they used to measure the
# central tendency of a dataset?
Mean, median, and mode are three common measures of central tendency used to describe the typical or central value of a dataset. Each of these statistics provides a different way of summarizing the data, and they can help you understand the distribution of values within a dataset.

Mean:

The mean is also known as the average.
To calculate the mean, you add up all the values in the dataset and then divide by the total number of values.
Formula: Mean = (Sum of all values) / (Number of values)
The mean is sensitive to outliers or extreme values because it considers all data points equally.
It is widely used when you have a dataset with interval or ratio scale data, and it provides a measure of the central point that minimizes the sum of squared differences from each data point to the mean.
Median:

The median is the middle value of a dataset when the values are arranged in ascending or descending order.
If there is an even number of data points, the median is the average of the two middle values.
The median is less affected by outliers than the mean because it is based on the position of values rather than their actual numerical values.
It is useful when you have data with outliers or a skewed distribution.
Mode:

The mode is the most frequently occurring value(s) in a dataset.
A dataset can have one mode (unimodal), more than one mode (multimodal), or no mode at all (no repeating values).
The mode is particularly useful for nominal or categorical data but can also be used for other types of data.
Unlike the mean and median, the mode does not provide a measure of central tendency on a numerical scale but identifies the most common category or value.
In summary:

The mean provides an average value and is suitable for data with interval or ratio scales.
The median identifies the middle value and is useful when dealing with skewed distributions or data with outliers.
The mode indicates the most common value(s) and is mainly used for categorical data.
It's essential to choose the appropriate measure of central tendency based on the characteristics of your data and the specific research or analysis goals. In some cases, you may use a combination of these measures to gain a more comprehensive understanding of your dataset's central tendency. 
# In[ ]:





# Q3. Measure the three measures of central tendency for the given height data:
# 
#  [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
To measure the three measures of central tendency (mean, median, and mode) for the given height data, you can follow these steps:

Mean (Average):

To calculate the mean, sum up all the values and then divide by the total number of values.
Sum of the heights: 178 + 177 + 176 + 177 + 178.2 + 178 + 175 + 179 + 180 + 175 + 178.9 + 176.2 + 177 + 172.5 + 178 + 176.5 = 2762.3
Number of values: 16
Mean = Sum / Number of values
Mean = 2762.3 / 16 ≈ 172.64 (rounded to two decimal places)
Median:

To find the median, first arrange the data in ascending order.
Sorted data: [172.5, 175, 175, 176, 176, 176.2, 177, 177, 178, 178, 178, 178, 178.2, 178.9, 179, 180]
Since there are 16 data points (an even number), the median is the average of the two middle values, which are the 8th and 9th values in the sorted list.
Median = (177 + 178) / 2 = 177.5
Mode:

The mode is the value(s) that appear most frequently in the dataset.
In this dataset, there are two modes: 178 and 176, both occurring three times.
So, the modes are 178 and 176.
To summarize, for the given height data:

Mean (Average) ≈ 172.64
Median = 177.5
Mode = 178 and 176
# Q4. Find the standard deviation for the given data:
# 
# [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
To calculate the standard deviation for the given data set, you can follow these steps:

Calculate the mean (average), which we found to be approximately 172.64 in a previous response.

Find the squared difference between each data point and the mean:

(178 - 172.64)^2 = 31.74
(177 - 172.64)^2 = 19.22
(176 - 172.64)^2 = 11.20
(177 - 172.64)^2 = 19.22
(178.2 - 172.64)^2 = 31.41
(178 - 172.64)^2 = 31.74
(175 - 172.64)^2 = 5.52
(179 - 172.64)^2 = 39.88
(180 - 172.64)^2 = 54.26
(175 - 172.64)^2 = 5.52
(178.9 - 172.64)^2 = 39.43
(176.2 - 172.64)^2 = 12.69
(177 - 172.64)^2 = 19.22
(172.5 - 172.64)^2 = 0.02
(178 - 172.64)^2 = 31.74
(176.5 - 172.64)^2 = 14.11
Calculate the mean of these squared differences:

Mean of squared differences = (31.74 + 19.22 + 11.20 + 19.22 + 31.41 + 31.74 + 5.52 + 39.88 + 54.26 + 5.52 + 39.43 + 12.69 + 19.22 + 0.02 + 31.74 + 14.11) / 16 ≈ 21.71
Calculate the square root of the mean of squared differences to find the standard deviation:

Standard deviation = √(21.71) ≈ 4.66 (rounded to two decimal places)
So, the standard deviation for the given data set is approximately 4.66.
# In[ ]:





# In[ ]:





# Q5. How are measures of dispersion such as range, variance, and standard deviation used to describe 
# the spread of a dataset? Provide an example.
Measures of dispersion, including range, variance, and standard deviation, are used to describe how data points in a dataset are spread out or dispersed from the central tendency (e.g., mean or median). These measures provide valuable information about the variability or spread of the data, helping statisticians and data analysts understand the distribution of the values within a dataset. Let's explore these measures and provide an example:

Range:

The range is the simplest measure of dispersion and represents the difference between the maximum and minimum values in a dataset.
Range = Maximum value - Minimum value.
It gives a basic idea of the spread but is sensitive to outliers.
Example: Suppose we have a dataset of exam scores for a class: [60, 70, 75, 80, 95]. The range would be 95 - 60 = 35.
Variance:

Variance measures the average squared deviation from the mean.
It provides a more comprehensive understanding of the data's spread.
The formula for sample variance is:
�
2
=
1
�
−
1
∑
�
=
1
�
(
�
�
−
�
ˉ
)
2
s 
2
 = 
n−1
1
​
 ∑ 
i=1
n
​
 (x 
i
​
 − 
x
ˉ
 ) 
2
 
where 
�
�
x 
i
​
  are individual data points, 
�
ˉ
x
ˉ
  is the sample mean, and 
�
n is the number of data points.
Example: Consider the dataset of exam scores [60, 70, 75, 80, 95]. The sample variance would be calculated as:
�
2
=
1
5
−
1
[
(
60
−
76
)
2
+
(
70
−
76
)
2
+
(
75
−
76
)
2
+
(
80
−
76
)
2
+
(
95
−
76
)
2
]
=
135
s 
2
 = 
5−1
1
​
 [(60−76) 
2
 +(70−76) 
2
 +(75−76) 
2
 +(80−76) 
2
 +(95−76) 
2
 ]=135
So, the variance is 135.
Standard Deviation:

The standard deviation is the square root of the variance.
It is used to quantify the dispersion in the same units as the data.
The formula for sample standard deviation is:
�
=
�
2
s= 
s 
2
 
​
 
where 
�
2
s 
2
  is the sample variance.
Example: For the dataset with a variance of 135, the standard deviation would be 
135
≈
11.61
135
​
 ≈11.61.
In summary, the range provides a basic idea of how spread out the data is, but it doesn't take into account the distribution of values. Variance and standard deviation provide more detailed information about the spread, with standard deviation being the most commonly used measure as it is in the same units as the original data. These measures help analysts assess the variability and make comparisons between datasets or different sets of observations.
# In[ ]:





# In[ ]:





# Q6. What is a Venn diagram?
A Venn diagram is a visual representation of the relationships between sets, groups, or categories of objects or elements. It is named after the British mathematician and philosopher John Venn, who introduced the concept in the late 19th century. Venn diagrams use overlapping circles or other shapes to illustrate the commonalities and differences between various sets or groups.

The key components of a Venn diagram include:

Sets: Each circle or shape in a Venn diagram represents a set, group, or category of items. The items within a set share a common characteristic or attribute.

Overlapping Regions: The overlapping parts of the circles or shapes indicate the elements that are shared between the sets. These elements satisfy the criteria of multiple sets simultaneously.

Non-overlapping Regions: The non-overlapping areas within each circle represent elements that are unique to that specific set and do not belong to any other sets.

Venn diagrams are commonly used to visually represent concepts in various fields, including mathematics, logic, statistics, and data analysis. They help illustrate the intersection and differences between sets, making complex relationships easier to understand. Venn diagrams can have multiple circles to represent more than two sets and can be used for various purposes, such as solving logic puzzles, representing data relationships, and demonstrating set theory concepts.
# In[ ]:





# In[ ]:





# Q7. For the two given sets A = (2,3,4,5,6,7) & B = (0,2,6,8,10). Find:
# 
# (i) 	A B
# 
# (ii)	A ⋃ B

# Let's find the intersection and union of the two sets A and B:
# 
# (i) The intersection of two sets A and B, denoted as A ∩ B, consists of all elements that are common to both sets.
# 
# A = {2, 3, 4, 5, 6, 7}
# B = {0, 2, 6, 8, 10}
# 
# A ∩ B = {2, 6}
# 
# So, the intersection of sets A and B is {2, 6}.
# 
# (ii) The union of two sets A and B, denoted as A ∪ B, consists of all elements that belong to either set A or set B or both.
# 
# A = {2, 3, 4, 5, 6, 7}
# B = {0, 2, 6, 8, 10}
# 
# A ∪ B = {0, 2, 3, 4, 5, 6, 7, 8, 10}
# 
# So, the union of sets A and B is {0, 2, 3, 4, 5, 6, 7, 8, 10}.

# In[ ]:





# In[ ]:





# In[ ]:





# Q8. What do you understand about skewness in data?
# Skewness is a statistical measure that describes the asymmetry or lack of symmetry in a dataset's distribution. It provides insights into the shape of the data's probability distribution curve. Skewness indicates whether the data is skewed to the left (negatively skewed), skewed to the right (positively skewed), or approximately symmetric.

Here are the key points to understand about skewness in data:

Negative Skewness (Left Skew):

In a negatively skewed distribution, the tail on the left side of the distribution curve is longer or fatter than the right side.
The majority of data points tend to be concentrated on the right side, while a few smaller values are stretched towards the left.
The mean (average) is typically less than the median, as the lower values pull the mean in that direction.
Positive Skewness (Right Skew):

In a positively skewed distribution, the tail on the right side of the distribution curve is longer or fatter than the left side.
The majority of data points are concentrated on the left side, while a few larger values are stretched towards the right.
The mean is typically greater than the median because the higher values pull the mean in that direction.
Zero Skewness (Symmetric):

In a symmetric distribution, the data is evenly distributed on both sides of the mean, resulting in a balanced or symmetric shape.
The mean and median are equal in a perfectly symmetric distribution.
Skewness is quantified using a statistical measure known as the skewness coefficient or skewness index. A positive skewness coefficient indicates positive skew (right-skewed), a negative coefficient indicates negative skew (left-skewed), and a coefficient close to zero suggests that the data is approximately symmetric.

Skewness is essential in data analysis and modeling because it helps analysts and data scientists understand the nature of the data's distribution. It can also influence decisions about which statistical techniques and models are appropriate for analyzing the data. For instance, in finance, understanding the skewness of returns is crucial for risk assessment and portfolio management.
# In[ ]:





# In[ ]:





# Q9. If a data is right skewed then what will be the position of median with respect to mean?
# In a right-skewed (positively skewed) distribution, the median will be positioned to the left of the mean. Here's why:

Right-Skewed Distribution:

In a right-skewed distribution, the tail on the right side of the distribution curve is longer or fatter than the left side.
The majority of data points are concentrated on the left side, with progressively fewer data points as you move to the right.
The presence of a few larger values on the right side "pulls" the mean in that direction.
Position of the Median:

The median is the middle value of a dataset when it is ordered from smallest to largest.
Since the right tail of the distribution contains relatively few but larger values, the median, which lies at the midpoint, is influenced less by these larger values than the mean.
Therefore, the median tends to be less affected by extreme outliers or large values in the right tail, and it is positioned to the left of the mean.
In summary, in a right-skewed distribution, the median is typically less than the mean because the rightward tail of the distribution contains larger values that exert a greater influence on the mean, pulling it to the right. The median, being less sensitive to extreme values, remains relatively closer to the center of the distribution.
# In[ ]:





# In[ ]:





# Q10. Explain the difference between covariance and correlation. How are these measures used in 
# statistical analysis?
Covariance and correlation are both statistical measures used to describe the relationship between two variables in a dataset, but they serve slightly different purposes and have different scales of measurement. Here's an explanation of the key differences between covariance and correlation and how they are used in statistical analysis:

1. Covariance:

Definition: Covariance measures the degree to which two variables change together. It indicates whether an increase in one variable corresponds to an increase or decrease in another variable.
Scale: The scale of covariance is not standardized, meaning it can take any value, including positive, negative, or zero. Therefore, the magnitude of covariance depends on the scales of the two variables being measured.
Interpretation: Positive covariance indicates a positive relationship, meaning that as one variable increases, the other tends to increase as well. Negative covariance indicates a negative relationship, implying that as one variable increases, the other tends to decrease. A covariance of zero suggests no linear relationship.
Formula: The formula for covariance between two variables X and Y in a dataset is given by:
Cov(X, Y) = Σ((Xᵢ - μₓ) * (Yᵢ - μᵧ)) / (n - 1)
where Xᵢ and Yᵢ are individual data points, μₓ and μᵧ are the means of X and Y, respectively, and n is the number of data points.
2. Correlation:

Definition: Correlation is a standardized measure that quantifies the strength and direction of the linear relationship between two variables. It provides a more interpretable value that is independent of the scales of the variables.
Scale: Correlation coefficients range from -1 to 1. A correlation of 1 indicates a perfect positive linear relationship, -1 indicates a perfect negative linear relationship, and 0 indicates no linear relationship.
Interpretation: A positive correlation coefficient (e.g., +0.8) implies a strong positive linear relationship, meaning that as one variable increases, the other tends to increase linearly. A negative correlation coefficient (e.g., -0.6) indicates a strong negative linear relationship, where an increase in one variable corresponds to a decrease in the other. A correlation coefficient of 0 suggests no linear relationship.
Formula: The most common formula for the Pearson correlation coefficient (r) between two variables X and Y is given by:
r = Σ((Xᵢ - μₓ) * (Yᵢ - μᵧ)) / (σₓ * σᵧ)
where Xᵢ and Yᵢ are individual data points, μₓ and μᵧ are the means of X and Y, respectively, and σₓ and σᵧ are the standard deviations of X and Y, respectively.
Usage in Statistical Analysis:

Covariance: Covariance is used primarily to understand the direction of the relationship between two variables and whether they tend to move together or in opposite directions. However, the magnitude of covariance is not easily interpretable because it depends on the scales of the variables. Therefore, it is often used as a preliminary step in analyzing relationships and is typically followed by standardization to calculate correlation coefficients.

Correlation: Correlation is widely used in statistical analysis because it provides a standardized measure that is easier to interpret. It is valuable for:

Assessing the strength and direction of linear relationships between variables.
Comparing relationships between different pairs of variables, regardless of their scales.
Identifying associations and making predictions in various fields, including finance, social sciences, and natural sciences.
Detecting outliers and influential data points that may affect relationships.
Guiding decision-making and modeling processes in data analysis, such as in regression analysis.
In summary, while covariance and correlation both capture the relationship between two variables, correlation is preferred in many situations due to its standardized scale and easier interpretability. Covariance can be useful for an initial assessment of relationships but is often followed by the calculation of correlation coefficients for a more comprehensive analysis.
# In[ ]:





# Q11. What is the formula for calculating the sample mean? Provide an example calculation for a 
# dataset.
The formula for calculating the sample mean (also known as the sample average) is quite straightforward. To find the sample mean for a dataset, you sum all the values in the dataset and then divide by the number of data points. Here's the formula:

Sample Mean (x̄) = (Σx) / n

Where:

x̄ represents the sample mean.
Σx denotes the sum of all individual data points.
n is the number of data points in the sample.
Let's illustrate this with an example calculation for a dataset. Suppose you have the following dataset of 5 exam scores:

Dataset: 80, 75, 90, 85, 88

First, add up all the values:
Σx = 80 + 75 + 90 + 85 + 88 = 418

Next, determine the number of data points in the sample, which is 5 in this case:
n = 5

Now, use the formula to calculate the sample mean:
x̄ = Σx / n
x̄ = 418 / 5
x̄ = 83.6

So, the sample mean of the dataset is 83.6. This means that, on average, the exam scores in this sample are approximately 83.6. The sample mean is a central measure of location and is often used as a representative value for the dataset when discussing its typical or average value.
# In[ ]:





# Q12. For a normal distribution data what is the relationship between its measure of central tendency?
In a normal distribution, also known as a Gaussian distribution or bell curve, there is a specific relationship between its measures of central tendency, which are the mean, median, and mode. Here's how they relate to each other:

Mean (μ): The mean of a normally distributed dataset is equal to the median and the mode. In other words, in a perfect normal distribution, the mean is located exactly at the center of the distribution, and it is also the point of highest probability (mode). This relationship holds true for idealized normal distributions.

Median: The median is equal to the mean in a perfectly symmetrical normal distribution. This is because the normal distribution is symmetric, and the mean is the point that divides it into two equal halves. Therefore, if you were to draw a vertical line at the mean on a normal distribution histogram, it would cut the distribution into two equal areas.

Mode: In a normal distribution, the mode is also equal to the mean and the median. It represents the most frequently occurring value in the dataset, and in a perfect normal distribution, there is only one mode, which is located at the mean.

It's important to note that in real-world data, distributions may not be perfectly normal, and there could be slight variations between the mean, median, and mode. However, for a true normal distribution, these three measures of central tendency are equal.





# In[ ]:





# Q13. How is covariance different from correlation?
Covariance and correlation are both measures of the relationship between two variables in statistics, but they serve slightly different purposes and have different scales of measurement.

Covariance:

Covariance measures the degree to which two variables change together. If the covariance is positive, it indicates that when one variable increases, the other tends to increase as well, and when one decreases, the other tends to decrease. If the covariance is negative, it suggests that when one variable increases, the other tends to decrease and vice versa.
Covariance is not standardized and is expressed in the units of the two variables being analyzed. Therefore, its magnitude is not easily interpretable, and it can be affected by the scale of the variables.
The formula for the covariance between two variables X and Y is:
Cov(X, Y) = Σ[(X_i - X̄)(Y_i - Ȳ)] / (n - 1), where X̄ is the mean of X, Ȳ is the mean of Y, and n is the number of data points.
Correlation:

Correlation, on the other hand, standardizes the covariance to a scale of -1 to 1, making it easier to interpret. It measures both the strength and direction of the linear relationship between two variables.
A correlation coefficient of +1 indicates a perfect positive linear relationship, -1 indicates a perfect negative linear relationship, and 0 indicates no linear relationship.
The most commonly used measure of correlation is the Pearson correlation coefficient (r), which is calculated as follows:
r = Cov(X, Y) / (σX * σY), where σX and σY are the standard deviations of X and Y, respectively.
In summary, the main differences between covariance and correlation are:

Covariance is not standardized and is in the units of the original variables, while correlation is standardized and falls within the range of -1 to 1.
Covariance measures the linear relationship between two variables but does not provide information about the strength or direction of the relationship. Correlation provides both the strength and direction of the linear relationship.
Correlation is a more interpretable measure of association between variables and is widely used in statistics and data analysis.
# In[ ]:





# Q14. How do outliers affect measures of central tendency and dispersion? Provide an example.
Outliers can significantly impact measures of central tendency (e.g., mean, median, mode) and measures of dispersion (e.g., range, variance, standard deviation) in statistical analysis. An outlier is an observation that lies far away from the majority of the data points in a dataset. They can distort the overall summary statistics and provide a skewed or inaccurate representation of the data. Here's how outliers affect these measures:

Measures of Central Tendency:

Mean: Outliers can have a substantial effect on the mean (average) because it takes into account the value of each data point. If there are outliers with very large or very small values, they can pull the mean in their direction. For example, consider the dataset: 1, 2, 3, 4, 100. The mean is (1+2+3+4+100) / 5 = 22, which is heavily influenced by the outlier 100.
Median: The median is less affected by outliers compared to the mean. It represents the middle value when the data is ordered. In the example above, the median would be 3, which is less influenced by the outlier.
Measures of Dispersion:

Range: The range is the difference between the maximum and minimum values in a dataset. Outliers can significantly expand the range, making it larger than it would be without outliers. In the example, the range is 100 - 1 = 99 due to the outlier.
Variance and Standard Deviation: Outliers can increase the variance and standard deviation because they introduce additional variability. These measures are sensitive to the distance between each data point and the mean. When there are outliers far from the mean, the spread of the data is exaggerated. In the example, the variance and standard deviation would be larger because of the outlier.
Example:
Consider a dataset of salaries for a small company:

$40,000, $45,000, $42,000, $41,000, $43,000, $1,000,000

Without the outlier ($1,000,000), the measures of central tendency and dispersion would be:

Mean: ($40,000 + $45,000 + $42,000 + $41,000 + $43,000) / 5 = $42,200
Median: $42,000
Range: $1,000,000 - $40,000 = $960,000
Variance and Standard Deviation: These would be computed with respect to the mean, so they would be relatively small compared to the presence of the outlier.
With the outlier, the mean is heavily influenced, and the range, variance, and standard deviation are significantly larger. The median remains relatively unaffected.

In situations where outliers may be the result of errors or anomalies, it's often advisable to identify and handle them appropriately, such as through data preprocessing techniques like winsorization, trimming, or excluding them if they are found to be erroneous. The choice depends on the context and the impact of the outliers on the analysis.





# In[ ]:





# #  <P style="color:GREEN"> Thank You ,That's All </p>
