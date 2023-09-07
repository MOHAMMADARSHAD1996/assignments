#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# #  <P style="color:purple"> STATISTICS ADVANCE-5   </p>

# Q1. Calculate the 95% confidence interval for a sample of data with a mean of 50 and a standard deviation 
# of 5 using Python. Interpret the results.

# In[1]:


#To calculate the 95% confidence interval for a sample with a mean of 50 and 
#a standard deviation of 5 using Python, you can use the scipy.stats library. Here's how you can do it:
import scipy.stats as stats

# Sample statistics
mean = 50
std_dev = 5

# Sample size
sample_size = 100  # You'll need to specify the actual sample size

# Confidence level
confidence_level = 0.95

# Calculate the margin of error
margin_of_error = stats.norm.ppf((1 + confidence_level) / 2) * (std_dev / (sample_size ** 0.5))

# Calculate the confidence interval
confidence_interval = (mean - margin_of_error, mean + margin_of_error)

print("95% Confidence Interval:", confidence_interval)
#Replace sample_size with the actual size of your sample. 
#The code above calculates the margin of error using the z-score corresponding to a 95% confidence level for 
#a two-tailed test. It then calculates the confidence interval by subtracting and
#adding the margin of error from the sample mean.
#The 95% confidence interval for the population mean based on this sample data is [lower bound, upper bound]. 
# It means that we can be 95% confident that the true population mean falls within this interval.
# In your case, if you replace sample_size with your actual sample size and run the code, 
# you will get the specific interval for your data.


# In[ ]:





# Q2. Conduct a chi-square goodness of fit test to determine if the distribution of colors of M&Ms in a bag 
# matches the expected distribution of 20% blue, 20% orange, 20% green, 10% yellow, 10% red, and 20% 
# brown. Use Python to perform the test with a significance level of 0.05.
# To conduct a chi-square goodness of fit test in Python to determine 
# if the distribution of colors of M&Ms in a bag matches the expected distribution, 
# you can use the scipy.stats library.
# Here's how you can do it:
import numpy as np
from scipy.stats import chi2_contingency

# Observed frequencies (counts) of each color in the bag
observed_frequencies = np.array([35, 15, 22, 10, 11, 22])  # Replace with your actual counts

# Expected frequencies based on the expected distribution
expected_frequencies = np.array([0.2, 0.2, 0.2, 0.1, 0.1, 0.2]) * np.sum(observed_frequencies)

# Perform the chi-square goodness of fit test
chi2_stat, p_value = chi2_contingency(observed_frequencies)

# Degrees of freedom (number of categories - 1)
degrees_of_freedom = len(observed_frequencies) - 1

# Significance level
alpha = 0.05

# Compare p-value to alpha
if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
print(f"Chi-square statistic: {chi2_stat}")
print(f"P-value: {p_value}")
# Replace observed_frequencies with the actual counts of each color you observed in the M&M bag. 
# The code calculates the expected frequencies based on the expected distribution and
# then performs the chi-square goodness of fit test. It compares the p-value to the significance level (alpha = 0.05) 
# to determine whether to reject or fail to reject the null hypothesis.
# If the p-value is less than 0.05 (or your chosen significance level), you would reject the null hypothesis.
# This suggests that there is a significant difference between the observed and
# expected distributions of M&M colors in the bag.
# If the p-value is greater than or equal to 0.05, you would fail to reject the null hypothesis. 
# This suggests that there is no significant difference between the observed and expected distributions, 
# and the distribution of colors in the bag matches the expected distribution.
# In[ ]:





# Q3. Use Python to calculate the chi-square statistic and p-value for a contingency table with the following 
# data:
# Outcome 1 20 15
# Outcome 2 10 25
# Outcome 3 15 20

# In[3]:


#To calculate the chi-square statistic and p-value for the given contingency table data using Python,
#you can use the scipy.stats library. Here's how you can do it:
from scipy.stats import chi2_contingency

# Create the contingency table (replace with your actual data)
contingency_table = np.array([[20, 15],
                               [10, 25],
                               [15, 20]])

# Perform the chi-square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-square statistic: {chi2_stat}")
print(f"P-value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print("Expected frequencies:")
print(expected)
# Replace the contingency_table variable with your actual contingency table data.
# The code calculates the chi-square statistic, p-value, degrees of freedom, and
# expected frequencies for the contingency table.
# This will give you the chi-square statistic and p-value for testing the independence
# of the two categorical variables represented by the contingency table.


# In[ ]:





# Q4. A study of the prevalence of smoking in a population of 500 individuals found that 60 individuals 
# smoked. Use Python to calculate the 95% confidence interval for the true proportion of individuals in the 
# population who smoke.

# In[4]:


# To calculate the 95% confidence interval for the true proportion of individuals in the population who smoke, 
# you can use the formula for the confidence interval for a proportion. In Python, you can use 
# the scipy.stats library to calculate this. Here's how you can do it:
from scipy.stats import norm

# Sample size
n = 500

# Number of individuals who smoke
x = 60

# Calculate the sample proportion
p = x / n

# Confidence level
confidence_level = 0.95

# Calculate the standard error
standard_error = np.sqrt((p * (1 - p)) / n)

# Calculate the margin of error
z = norm.ppf((1 + confidence_level) / 2)
margin_of_error = z * standard_error

# Calculate the confidence interval
confidence_interval = (p - margin_of_error, p + margin_of_error)

print(f"95% Confidence Interval: ({confidence_interval[0]:.4f}, {confidence_interval[1]:.4f})")
# This code calculates the confidence interval for the true proportion of individuals who
# smoke in the population based on the given sample size and the number of individuals who smoke.
# The 95% confidence interval for the true proportion of individuals who smoke in the population is given as
# (lower bound, upper bound). 
# This interval provides a range within which we can be 95% confident that the true population proportion lies.


# In[ ]:





# Q5. Calculate the 90% confidence interval for a sample of data with a mean of 75 and a standard deviation 
# of 12 using Python. Interpret the results.

# In[5]:


#To calculate the 90% confidence interval for a sample with a mean of 75 and a standard deviation of 12 using Python, 
#you can use the scipy.stats library. Here's how you can do it:
import scipy.stats as stats

# Sample statistics
mean = 75
std_dev = 12

# Sample size
sample_size = 100  # You'll need to specify the actual sample size

# Confidence level
confidence_level = 0.90

# Calculate the margin of error
margin_of_error = stats.norm.ppf((1 + confidence_level) / 2) * (std_dev / (sample_size ** 0.5))

# Calculate the confidence interval
confidence_interval = (mean - margin_of_error, mean + margin_of_error)

print(f"90% Confidence Interval: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
# Replace sample_size with the actual size of your sample. The code calculates the margin of error using
# the z-score corresponding to a 90% confidence level for a two-tailed test. It then calculates the confidence interval
# by subtracting and adding the margin of error from the sample mean.
# The 90% confidence interval for the population mean based on this sample data is given as (lower bound, upper bound).
# It means that we can be 90% confident that the true population mean falls within this interval.
# In your case, if you replace sample_size with your actual sample size and run the code,
# you will get the specific interval for your data.


# In[ ]:





# Q6. Use Python to plot the chi-square distribution with 10 degrees of freedom. Label the axes and shade the 
# area corresponding to a chi-square statistic of 15.

# In[7]:


# To plot the chi-square distribution with 10 degrees of freedom in Python,
# you can use the scipy.stats library and matplotlib for visualization.
# Here's how you can do it and shade the area corresponding to a chi-square statistic of 15:
# Degrees of freedom
import matplotlib.pyplot as plt
df = 10

# Create a range of chi-square values
x = np.linspace(0, 30, 1000)

# Calculate the chi-square probability density function
pdf = stats.chi2.pdf(x, df)

# Plot the chi-square distribution
plt.plot(x, pdf, label=f'Chi-square with {df} DF')

# Shade the area corresponding to a chi-square statistic of 15
plt.fill_between(x, pdf, where=(x >= 15), alpha=0.5, color='red', label='Chi-square >= 15')

# Label the axes and add a legend
plt.xlabel('Chi-square Value')
plt.ylabel('Probability Density')
plt.legend()

# Show the plot
plt.title('Chi-square Distribution')
plt.grid(True)
plt.show()

# In this code, we first create a range of chi-square values (x) and 
# then calculate the probability density function (PDF) of the chi-square distribution with 10 degrees of freedom. 
# We plot the distribution and shade the area under the curve where the chi-square statistic is greater than or equal to 15.
# Finally, we label the axes, add a legend, and display the plot.
# Make sure you have the matplotlib library installed in your Python environment to run this code.


# In[ ]:





# Q7. A random sample of 1000 people was asked if they preferred Coke or Pepsi. Of the sample, 520 
# preferred Coke. Calculate a 99% confidence interval for the true proportion of people in the population who 
# prefer Coke.

# In[8]:


# Sample size
n = 1000

# Number of people who prefer Coke
x = 520

# Calculate the sample proportion
p = x / n

# Confidence level
confidence_level = 0.99

# Calculate the standard error
standard_error = np.sqrt((p * (1 - p)) / n)

# Calculate the margin of error
z = norm.ppf((1 + confidence_level) / 2)
margin_of_error = z * standard_error

# Calculate the confidence interval
confidence_interval = (p - margin_of_error, p + margin_of_error)

print(f"99% Confidence Interval: ({confidence_interval[0]:.4f}, {confidence_interval[1]:.4f})")
# This code calculates the margin of error using the z-score corresponding to a 99% confidence level for a two-tailed test and 
# then calculates the confidence interval by subtracting and adding the margin of error from the sample proportion.
# The 99% confidence interval for the true proportion of people in the population who prefer Coke is given 
# as (lower bound, upper bound). It means that we can be 99% confident that the true population proportion falls within this
# interval. In your case, the interval is calculated based on a sample of 1000 people, where 520 preferred Coke.


# In[ ]:





# Q8. A researcher hypothesizes that a coin is biased towards tails. They flip the coin 100 times and observe 
# 45 tails. Conduct a chi-square goodness of fit test to determine if the observed frequencies match the 
# expected frequencies of a fair coin. Use a significance level of 0.05.
# Observed frequencies (tails and heads)
observed_frequencies = np.array([45, 55])  # 45 tails, 55 heads

# Expected frequencies for a fair coin
expected_frequencies = np.array([50, 50])  # 50% tails, 50% heads

# Perform the chi-square goodness of fit test
chi2_stat, p_value = chi2_contingency(observed_frequencies)

# Degrees of freedom (number of categories - 1)
degrees_of_freedom = len(observed_frequencies) - 1

# Significance level
alpha = 0.05

# Compare p-value to alpha
if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

print(f"Chi-square statistic: {chi2_stat}")
print(f"P-value: {p_value}")
# We specify the observed frequencies, where 45 tails and 55 heads were observed in 100 coin flips.
# We specify the expected frequencies for a fair coin, where we expect 50 tails and 50 heads.
# We perform the chi-square goodness of fit test using chi2_contingency from scipy.stats,
# which calculates the chi-square statistic and the associated p-value.
# We define the degrees of freedom (1 for a two-category test) and the significance level (0.05).
# We compare the p-value to the significance level. If the p-value is less than 0.05, 
# we reject the null hypothesis, indicating that the observed frequencies do not match the expected frequencies of a
# fair coin. If the p-value is greater than or equal to 0.05, we fail to reject the null hypothesis, 
# suggesting that there is no significant difference between the observed and expected frequencies.
# This code will help you determine whether the coin is biased toward tails or if 
# the observed frequencies match those expected from a fair coin.
# In[ ]:





# Q9. A study was conducted to determine if there is an association between smoking status (smoker or 
# non-smoker) and lung cancer diagnosis (yes or no). The results are shown in the contingency table below. 
# Conduct a chi-square test for independence to determine if there is a significant association between 
# smoking status and lung cancer diagnosis.
# Smoker 60 140
# Non-smoker 30 170

# In[10]:


# Create the contingency table
contingency_table = np.array([[60, 140],
                               [30, 170]])

# Perform the chi-square test for independence
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-square statistic: {chi2_stat}")
print(f"P-value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print("Expected frequencies:")
print(expected)
# This code creates the contingency table based on the provided data and then performs the chi-square test for 
# independence using chi2_contingency from scipy.stats. 
# It calculates the chi-square statistic, the associated p-value, degrees of freedom, and expected frequencies
# If the p-value is less than the chosen significance level (e.g., 0.05), you would reject the null hypothesis,
# indicating a significant association between smoking status and lung cancer diagnosis.
# If the p-value is greater than or equal to the significance level, you would fail to reject the null hypothesis, 
# suggesting no significant association between the two variables.
# This test will help you determine whether there is a significant relationship between smoking status and lung cancer diagnosis in the study data.


# In[ ]:





# Q10. A study was conducted to determine if the proportion of people who prefer milk chocolate, dark 
# chocolate, or white chocolate is different in the U.S. versus the U.K. A random sample of 500 people from 
# the U.S. and a random sample of 500 people from the U.K. were surveyed. The results are shown in the 
# contingency table below. Conduct a chi-square test for independence to determine if there is a significant 
# association between chocolate preference and country of origin.
# Use a significance level of 0.01

# In[11]:


# Create the contingency table
contingency_table = np.array([[150, 200, 150],
                               [100, 250, 150]])

# Perform the chi-square test for independence
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-square statistic: {chi2_stat}")
print(f"P-value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print("Expected frequencies:")
print(expected)
# In this code:
# We create the contingency table based on the provided data, where rows represent the country of origin (U.S. and U.K.), and columns represent the chocolate preferences (milk chocolate, dark chocolate, white chocolate).
# We perform the chi-square test for independence using chi2_contingency from scipy.stats. This calculates the chi-square statistic, the associated p-value, degrees of freedom, and expected frequencies.
# We print out the results, including the chi-square statistic, p-value, degrees of freedom, and expected frequencies.
# If the p-value is less than the chosen significance level (0.01 in this case), you would reject the null hypothesis, indicating a significant association between chocolate preference and country of origin.
# If the p-value is greater than or equal to 0.01, you would fail to reject the null hypothesis, suggesting no significant association between the two variables.
# This test will help you determine whether there is a significant relationship between chocolate preference and the country of origin (U.S. or U.K.) based on the survey data.


# In[ ]:





# Q11. A random sample of 30 people was selected from a population with an unknown mean and standard 
# deviation. The sample mean was found to be 72 and the sample standard deviation was found to be 10. 
# Conduct a hypothesis test to determine if the population mean is significantly different from 70. Use a 
# significance level of 0.05
# Sample statistics
sample_mean = 72
sample_std_dev = 10

# Sample size
sample_size = 30

# Null hypothesis (H0) - Population mean is equal to 70
# Alternative hypothesis (H1) - Population mean is not equal to 70

# Significance level
alpha = 0.05

# Calculate the t-statistic and p-value
t_statistic, p_value = ttest_1samp(np.random.normal(sample_mean, sample_std_dev, sample_size), 70)

# Compare the p-value to the significance level
if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

print(f"t-statistic: {t_statistic}")
print(f"P-value: {p_value}")
# We specify the sample statistics, including the sample mean (sample_mean), sample standard deviation (sample_std_dev), and sample size (sample_size).
# We set up the null hypothesis (H0) and alternative hypothesis (H1). In this case, H0 states that the population mean is equal to 70, while H1 states that the population mean is not equal to 70.
# We define the significance level (alpha) as 0.05, which corresponds to a 95% confidence level.
# We calculate the t-statistic and p-value using ttest_1samp from scipy.stats. This function performs a one-sample t-test.
# We compare the p-value to the significance level. If the p-value is less than 0.05, we reject the null hypothesis, indicating that the population mean is significantly different from 70. If the p-value is greater than or equal to 0.05, we fail to reject the null hypothesis.
# This test will help you determine whether the population mean is significantly different from 70 based on the sample data and the chosen significance level.
# In[ ]:





# #  <P style="color:GREEN"> THNAK YOU, THAT'S ALL </p>
