#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# #  <P style="color:purple"> STATISTICS ADVANCE-6  </p>

# Q1. Explain the assumptions required to use ANOVA and provide examples of violations that could impact 
# the validity of the results.
Analysis of Variance (ANOVA) is a statistical technique used to compare means among two or more groups or treatments. To use ANOVA effectively and ensure the validity of the results, several assumptions must be met. Violations of these assumptions can impact the validity of ANOVA results. Here are the key assumptions for ANOVA, along with examples of potential violations:

Assumption 1: Independence of Observations

Assumption: Observations in each group or treatment are independent of each other.
Violation Example: In a medical study, if patients within the same family are assigned to different treatment groups, the assumption of independence is violated because family members may share genetic or environmental factors affecting the response variable.
Assumption 2: Homogeneity of Variance (Homoscedasticity)

Assumption: The variances of the groups being compared are roughly equal.
Violation Example: In a study comparing the test scores of students from different schools, if the variance in test scores in one school is much larger than in another school, the assumption of homogeneity of variance is violated.
Assumption 3: Normality of Residuals

Assumption: The residuals (the differences between observed and predicted values) should follow a normal distribution.
Violation Example: In an experiment measuring the time it takes for participants to complete a task, if the residuals (differences between observed times and predicted times) are strongly skewed or exhibit significant outliers, the assumption of normality is violated.
Assumption 4: Independence of Groups

Assumption: Different groups or treatments should not affect each other.
Violation Example: In a manufacturing study comparing the defect rates of products produced on different machines, if the machines are physically close and vibrations from one machine affect the others, the assumption of independence of groups may be violated.
Assumption 5: Equal Sample Sizes (for one-way ANOVA)

Assumption: In one-way ANOVA, all groups should have roughly equal sample sizes.
Violation Example: In a one-way ANOVA comparing the performance of different software versions, if one version has a significantly larger sample size than others, it can lead to an unbalanced design and violate this assumption.
Assumption 6: Random Sampling (for inferential ANOVA)

Assumption: The data should be obtained through random sampling or a properly randomized experiment.
Violation Example: If the data is collected through convenience sampling or non-random methods, the assumption of random sampling may be violated, and the results may not be generalizable.
Assumption 7: No Perfect Multicollinearity (for factorial ANOVA)

Assumption: In factorial ANOVA, there should be no perfect linear relationships between the independent variables.
Violation Example: If two independent variables are perfectly correlated (e.g., height in feet and height in inches), it can lead to multicollinearity issues, making it challenging to interpret the effects of each variable.
It's important to note that ANOVA is robust to some violations, especially when sample sizes are large. However, violations of these assumptions can still affect the validity and interpretability of the results. In cases of severe violations, alternative statistical methods or data transformations may be necessary to obtain reliable conclusions. Data visualization, residual plots, and normality tests can help assess whether these assumptions are met.
# In[ ]:





# Q2. What are the three types of ANOVA, and in what situations would each be used?
Analysis of Variance (ANOVA) is a statistical technique used to compare means among two or more groups or treatments. There are three main types of ANOVA, each designed for specific situations:

One-Way ANOVA (One-Factor ANOVA):

Use: One-way ANOVA is used when you have one categorical independent variable (factor) with more than two levels or groups, and you want to determine whether there are significant differences in the means of a continuous dependent variable across these groups.
Example: You want to compare the average test scores of students from three different schools (School A, School B, and School C) to see if there are statistically significant differences among them.
Two-Way ANOVA (Two-Factor ANOVA):

Use: Two-way ANOVA is used when you have two categorical independent variables (factors) and you want to examine their individual and interactive effects on a continuous dependent variable.
Example: You are studying the effect of both the type of fertilizer (Factor 1: Fertilizer A, Fertilizer B) and the amount of water (Factor 2: Low, Medium, High) on plant growth (dependent variable), and you want to know if either or both factors, as well as their interaction, have significant effects.
Repeated Measures ANOVA (Within-Subjects ANOVA):

Use: Repeated Measures ANOVA is used when you have a within-subjects or repeated-measures design, where the same subjects are measured under different conditions or at different time points.
Example: You are conducting a clinical trial to assess the effect of a new drug on patients' blood pressure. You measure each patient's blood pressure at baseline (before treatment), after one week of treatment, and after four weeks of treatment. Repeated Measures ANOVA helps you analyze the changes in blood pressure over time within the same group of patients.
These three types of ANOVA address different experimental designs and research questions:

One-Way ANOVA is used for comparing multiple independent groups or treatments.
Two-Way ANOVA extends the analysis to two independent variables and assesses their main effects and interaction effects.
Repeated Measures ANOVA is used when you have repeated measurements on the same subjects or units and you want to investigate changes over time or under different conditions within those subjects.
Choosing the appropriate type of ANOVA depends on your research design and the nature of your data. It's important to select the ANOVA method that aligns with your specific experimental setup to obtain meaningful and valid results.
# In[ ]:





# Q3. What is the partitioning of variance in ANOVA, and why is it important to understand this concept?
The partitioning of variance in Analysis of Variance (ANOVA) refers to the process of decomposing the total variance in a dataset into different components that can be attributed to various sources or factors. Understanding this concept is crucial in ANOVA because it helps researchers identify and quantify the sources of variability in their data, which in turn allows them to make informed statistical inferences about group differences and the significance of independent variables. The key components of variance partitioning in ANOVA are:

Total Variance (Total Sum of Squares, SST):

This represents the total variability in the data, regardless of the groups or treatments. It is calculated as the sum of the squared differences between each data point and the overall mean.
Between-Groups Variance (Between-Groups Sum of Squares, SSB):

This component of variance measures the variability among group means. It quantifies how much the means of different groups or treatments differ from each other. It is calculated as the sum of the squared differences between each group mean and the overall mean, weighted by the number of observations in each group.
Within-Groups Variance (Within-Groups Sum of Squares, SSW):

This component of variance represents the variability within each group or treatment. It measures the differences between individual data points and their respective group means. It is calculated as the sum of the squared differences within each group.
The partitioning of variance is typically expressed as follows:

�
�
�
=
�
�
�
+
�
�
�
SST=SSB+SSW

Here's why understanding this concept is important:

Hypothesis Testing: ANOVA is used to test whether there are statistically significant differences among group means. Partitioning the variance allows researchers to quantify the variability that can be attributed to the independent variable(s) (between-groups variance) and the variability due to random fluctuations or error (within-groups variance). This partitioning is essential for hypothesis testing and determining the statistical significance of group differences.

Effect Size: By knowing the proportion of variance explained by the independent variable(s) relative to the total variance, researchers can assess the practical or clinical significance of their findings. This is often expressed as an effect size, such as eta-squared (
�
2
η 
2
 ) or partial eta-squared (
�
�
2
η 
p
2
​
 ), which provide information about the magnitude of the effect.

Model Assessment: Variance partitioning helps researchers assess the goodness of fit of their ANOVA model. A model that explains a large portion of the variance is preferable, as it indicates that the independent variable(s) have a substantial influence on the dependent variable.

Interpretation: Understanding the partitioning of variance allows researchers to interpret the results of ANOVA more effectively. They can discuss the relative contributions of different factors to the observed differences in group means, helping to formulate hypotheses about why these differences exist.

In summary, the partitioning of variance in ANOVA is a fundamental concept that provides insight into the sources of variability in data and helps researchers draw meaningful conclusions about group differences and the effects of independent variables. It is a critical step in the analysis process, allowing for informed statistical inference and interpretation of results.
# In[ ]:





# Q4. How would you calculate the total sum of squares (SST), explained sum of squares (SSE), and residual 
# sum of squares (SSR) in a one-way ANOVA using Python?

# In[1]:


#In a one-way ANOVA, you can calculate the Total Sum of Squares (SST), 
#Explained Sum of Squares (SSE), and Residual Sum of Squares (SSR) using Python. You typically use a library like NumPy to perform the necessary calculations. Here's how you can calculate these values:
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Sample data as a pandas DataFrame
data = pd.DataFrame({'Group A': [25, 30, 35, 40],
                     'Group B': [20, 22, 25, 30],
                     'Group C': [15, 18, 20, 22]})

# Flatten the data into a 1-D array
values = data.values.flatten()

# Create a grouping variable
groups = np.repeat(['Group A', 'Group B', 'Group C'], 4)

# Create a one-way ANOVA model
model = ols('values ~ groups', data={'values': values, 'groups': groups}).fit()

# Calculate the Total Sum of Squares (SST)
sst = np.sum((values - np.mean(values))**2)

# Calculate the Explained Sum of Squares (SSE)
sse = np.sum((model.fittedvalues - np.mean(values))**2)

# Calculate the Residual Sum of Squares (SSR)
ssr = np.sum((values - model.fittedvalues)**2)

print("Total Sum of Squares (SST):", sst)
print("Explained Sum of Squares (SSE):", sse)
print("Residual Sum of Squares (SSR):", ssr)
# In the code above:
# We import the necessary libraries, including NumPy for numerical operations and the statsmodels library to perform the one-way ANOVA analysis.
# We create a sample dataset using a pandas DataFrame. Each column represents a different group (e.g., Group A, Group B, Group C).
# We flatten the data into a 1-D array and create a grouping variable to specify the groups for the ANOVA model.
# We create a one-way ANOVA model using the ols function from statsmodels.
# We calculate the Total Sum of Squares (SST), Explained Sum of Squares (SSE), and Residual Sum of Squares (SSR) using the appropriate formulas. SST is the total variance in the data, SSE is the variance explained by the model (between-groups variance), and SSR is the unexplained variance (within-groups variance).
# Finally, we print out the calculated values for SST, SSE, and SSR.
# You can replace the sample data with your own dataset and adapt the code accordingly to perform a one-way ANOVA analysis and calculate these sum of squares values for your specific data.


# In[ ]:





# Q5. In a two-way ANOVA, how would you calculate the main effects and interaction effects using Python?

# In[2]:


#In a two-way ANOVA, you can calculate the main effects and interaction effects using Python by leveraging libraries such as NumPy and statsmodels. To illustrate this, I'll provide an example and show you how to calculate the main effects and interaction effects:
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a sample dataset as a pandas DataFrame
data = pd.DataFrame({
    'Factor1': ['A', 'A', 'B', 'B', 'A', 'A', 'B', 'B'],
    'Factor2': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value': [10, 12, 15, 14, 20, 22, 25, 24]
})

# Create a two-way ANOVA model
formula = 'Value ~ Factor1 * Factor2'
model = ols(formula, data=data).fit()

# Calculate main effects and interaction effect
main_effect_factor1 = model.params['Factor1[T.B]']
main_effect_factor2 = model.params['Factor2[T.Y]']
interaction_effect = model.params['Factor1[T.B]:Factor2[T.Y]']

print("Main Effect of Factor 1:", main_effect_factor1)
print("Main Effect of Factor 2:", main_effect_factor2)
print("Interaction Effect:", interaction_effect)
# In this example:
# We import the necessary libraries, including NumPy for numerical operations, pandas for handling data, and statsmodels for statistical analysis.
# We create a sample dataset as a pandas DataFrame. The dataset includes two categorical factors (Factor1 and Factor2) and a continuous dependent variable (Value).
# We create a two-way ANOVA model using the ols function from statsmodels. The formula 'Value ~ Factor1 * Factor2' specifies that we want to examine the main effects of Factor1 and Factor2, as well as their interaction effect
# We fit the model to the data using the .fit() method.
# We calculate the main effects and interaction effect by accessing the model's parameters. The main effects for Factor1 and Factor2 are represented as 'Factor1[T.B]' and 'Factor2[T.Y]' in the model parameters. The interaction effect is represented as 'Factor1[T.B]:Factor2[T.Y]'.
# Finally, we print out the calculated main effects and interaction effect.
# You can replace the sample data and adapt the code for your specific dataset and research questions. This example demonstrates how to calculate these effects in a two-way ANOVA using Python and the statsmodels library.


# In[ ]:





# Q6. Suppose you conducted a one-way ANOVA and obtained an F-statistic of 5.23 and a p-value of 0.02. 
# What can you conclude about the differences between the groups, and how would you interpret these 
# results?
In a one-way ANOVA, the F-statistic and its associated p-value are used to assess whether there are statistically significant differences among the means of the groups being compared. When interpreting the results, here's what you can conclude based on the provided F-statistic of 5.23 and a p-value of 0.02:

Significance of the F-statistic:

The F-statistic is a measure of the variation between group means relative to the variation within groups. A larger F-statistic suggests that the means of the groups differ more than would be expected by random chance.
P-value Significance:

The p-value is a measure of the evidence against the null hypothesis. In this case, the null hypothesis (H0) is that there are no significant differences among the group means, meaning all group means are equal.
Interpreting the P-value:

The p-value of 0.02 is less than the common significance level (alpha) of 0.05, which is often used in hypothesis testing. This indicates that there is strong evidence to reject the null hypothesis.
Conclusion:

Based on the provided results, you can conclude that there are statistically significant differences among the groups. In other words, at least one group mean is different from the others.
Follow-Up Analysis:

Since the one-way ANOVA indicates that there are significant differences among the groups, you may want to perform post-hoc tests (e.g., Tukey's HSD, Bonferroni correction, or pairwise t-tests) to identify which specific group(s) differ from each other. These tests can help you pinpoint the source of the differences.
Effect Size:

Additionally, you might want to calculate an effect size measure (e.g., eta-squared or Cohen's d) to quantify the magnitude of the differences among the groups. This can provide information about the practical significance of the observed differences.
In summary, with an F-statistic of 5.23 and a p-value of 0.02, you can conclude that there are statistically significant differences among the groups in your one-way ANOVA. This suggests that the groups are not all equal with respect to the variable you are studying. Further analyses can help you determine which specific group(s) differ from each other.
# In[ ]:





# Q7. In a repeated measures ANOVA, how would you handle missing data, and what are the potential 
# consequences of using different methods to handle missing data?

# Handling missing data in a repeated measures ANOVA is an important consideration, as missing data can impact the validity and reliability of your analysis. There are various methods to handle missing data, each with its own potential consequences. Here's how you can handle missing data in a repeated measures ANOVA and the potential consequences of different methods:
# 
# Listwise Deletion (Complete Case Analysis):
# 
# Method: This approach involves removing cases with missing data entirely, leaving only complete cases for analysis.
# Consequences:
# Pros: Simple to implement.
# Cons: Reduces sample size, potentially leading to reduced statistical power and biased results if data are not missing completely at random (MCAR). It may not be a suitable approach if there is substantial missing data.
# Pairwise Deletion (Available Case Analysis):
# 
# Method: In this approach, you include all available data for each pairwise comparison within the repeated measures factors. As a result, different cases contribute to different comparisons.
# Consequences:
# Pros: Maximizes the use of available data, no case is entirely excluded.
# Cons: Can lead to inefficient use of the data and may produce inflated standard errors and Type I error rates, especially if data are not MCAR.
# Mean Imputation:
# 
# Method: Replace missing values with the mean of the observed values for that variable.
# Consequences:
# Pros: Simple and retains the same sample size.
# Cons: Can introduce bias and underestimate the variability in the data. It assumes that missing values are missing completely at random and that the mean is a good representation of missing values.
# Linear Interpolation or Time-Series Methods:
# 
# Method: If the data have a natural time order (e.g., repeated measures over time), you can use methods like linear interpolation to estimate missing values based on adjacent observations.
# Consequences:
# Pros: Utilizes the temporal structure of the data and may provide better estimates than simple imputation methods.
# Cons: Assumes a linear relationship between adjacent data points, which may not always be appropriate. It can also be computationally intensive.
# Multiple Imputation:
# 
# Method: This is a more advanced technique where multiple imputed datasets are created, each with different imputed values based on a model that takes into account the relationships between variables. These datasets are then analyzed separately, and the results are combined to provide valid parameter estimates and standard errors.
# Consequences:
# Pros: Provides unbiased parameter estimates and valid standard errors when data are missing at random (MAR). It is a robust method for handling missing data.
# Cons: More complex and computationally intensive than other methods. Requires assumptions about the missing data mechanism (MAR).
# The choice of how to handle missing data should be guided by the nature of your data and the reason for the missing values. It's essential to consider the potential consequences of each method, including possible biases and effects on the results. Multiple imputation is often considered the gold standard when missing data are a concern, but it requires a good understanding of the data and appropriate software for implementation. Additionally, reporting the method used for handling missing data and conducting sensitivity analyses can enhance the transparency and robustness of your repeated measures ANOVA results.

# In[ ]:





# Q8. What are some common post-hoc tests used after ANOVA, and when would you use each one? Provide 
# an example of a situation where a post-hoc test might be necessary.
Post-hoc tests are used in the context of Analysis of Variance (ANOVA) when you have conducted an ANOVA and found a significant difference among groups. These tests are designed to make pairwise comparisons between groups to identify which specific groups differ from each other. Some common post-hoc tests used after ANOVA include:

Tukey's Honestly Significant Difference (Tukey HSD):

When to Use: Tukey's HSD is a conservative test that controls the familywise error rate. It is a good choice when you have a relatively large number of groups and you want to identify which specific groups differ from each other without increasing the Type I error rate.
Example: In a one-way ANOVA comparing the exam scores of students from five different schools, you find a significant overall difference. You can use Tukey's HSD to determine which pairs of schools have significantly different means.
Bonferroni Correction:

When to Use: The Bonferroni correction is a simple and conservative method that controls the familywise error rate by adjusting the significance level. It is suitable when you want to make multiple pairwise comparisons while keeping the overall Type I error rate low.
Example: In a study comparing the effectiveness of five different treatments, you perform pairwise comparisons to identify which treatments are significantly different. To maintain a low overall alpha level, you use the Bonferroni correction.
Sidak Correction:

When to Use: Similar to the Bonferroni correction, the Sidak correction adjusts the significance level for multiple comparisons. It is a slightly less conservative alternative to Bonferroni and can be used when you want to control the familywise error rate.
Example: In a repeated measures ANOVA comparing the performance of participants under three different conditions at four time points, you use Sidak correction for pairwise comparisons to assess which conditions and time points are significantly different.
Dunnett's Test:

When to Use: Dunnett's test is used when you have a control group and you want to compare other groups to the control group. It controls the Type I error rate for these specific comparisons.
Example: In a drug trial, you have a control group and three experimental groups receiving different medications. You use Dunnett's test to compare each experimental group to the control group while controlling for familywise error.
Holm-Bonferroni Method:

When to Use: The Holm-Bonferroni method is a stepwise procedure that controls the familywise error rate. It starts with the least significant comparison and progresses to more significant ones.
Example: In a study comparing the sales performance of multiple product categories, you want to identify which pairs of categories have significantly different sales. The Holm-Bonferroni method helps control the overall Type I error rate while prioritizing the most significant comparisons.
Games-Howell Test:

When to Use: The Games-Howell test is a non-parametric post-hoc test used when the assumption of homogeneity of variances is violated. It is appropriate when group variances are unequal.
Example: In a one-way ANOVA comparing the test scores of students from different schools, if Levene's test indicates unequal variances, you can use the Games-Howell test to make pairwise comparisons.
The choice of which post-hoc test to use depends on the specific research question, the number of groups, and the nature of your data. It's important to select a post-hoc test that aligns with your study design and the assumptions of the ANOVA. Additionally, always report which post-hoc test you used, along with the adjusted p-values, to ensure transparency in your statistical analysis.
# In[ ]:





# Q9. A researcher wants to compare the mean weight loss of three diets: A, B, and C. They collect data from 
# 50 participants who were randomly assigned to one of the diets. Conduct a one-way ANOVA using Python 
# to determine if there are any significant differences between the mean weight loss of the three diets. 
# Report the F-statistic and p-value, and interpret the results.

# In[4]:


#To conduct a one-way ANOVA in Python to compare the mean weight loss of three diets (A, B, and C) using randomly collected data from 50 participants assigned to the diets, you can use the SciPy library. Here's how you can perform this analysis and interpret the results:

import scipy.stats as stats

# Sample data for weight loss for each diet
diet_A = [1.5, 2.0, 2.2, 1.8, 1.9, 2.5, 2.8, 2.1, 1.7, 1.2,
          2.3, 2.4, 1.6, 2.2, 1.9, 2.1, 1.8, 2.0, 2.3, 1.4,
          2.5, 2.0, 1.6, 1.8, 2.2, 2.7, 2.3, 1.9, 2.1, 2.4,
          1.7, 2.0, 2.1, 2.5, 2.2, 2.3, 1.8, 1.9, 1.6, 2.0,
          2.2, 2.4, 1.7, 2.1, 2.5, 2.3, 1.8, 1.9]

diet_B = [1.3, 1.9, 2.1, 1.7, 1.6, 2.4, 2.3, 2.0, 1.5, 1.2,
          2.0, 2.2, 1.5, 1.8, 1.6, 2.1, 1.7, 1.9, 1.4, 1.1,
          2.3, 2.1, 1.4, 1.6, 1.8, 2.2, 2.0, 1.9, 1.7, 1.3,
          2.1, 1.8, 1.7, 2.4, 2.0, 2.2, 1.6, 1.4, 1.2, 1.9,
          2.1, 2.3, 1.5, 1.8, 2.2, 2.4, 1.7, 1.9]

diet_C = [0.9, 1.5, 1.8, 1.2, 1.0, 2.1, 2.2, 1.4, 1.1, 0.8,
          2.1, 1.9, 0.7, 1.6, 1.3, 2.0, 1.1, 1.2, 0.9, 0.6,
          2.0, 1.6, 0.8, 1.0, 1.4, 2.0, 1.9, 1.2, 1.3, 1.7,
          1.0, 1.5, 1.4, 2.1, 2.2, 1.8, 1.2, 1.1, 0.7, 1.4,
          1.8, 2.0, 1.0, 1.5, 2.2, 2.1, 1.2, 1.3]

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(diet_A, diet_B, diet_C)

# Interpret the results
alpha = 0.05

print("F-statistic:", f_statistic)
print("p-value:", p_value)

if p_value < alpha:
    print("Reject the null hypothesis: There are significant differences in mean weight loss among the three diets.")
else:
    print("Fail to reject the null hypothesis: There are no significant differences in mean weight loss among the three diets.")
# In this code:
# We have three sets of weight loss data for diets A, B, and C, with each list representing the weight loss for 50 participants assigned to that diet.
# We use the stats.f_oneway function from SciPy to perform a one-way ANOVA on the data. This function calculates the F-statistic and p-value for the ANOVA test.
# We set a significance level (alpha) of 0.05, commonly used in hypothesis testing.
# We interpret the results based on the F-statistic and p-value. If the p-value is less than alpha (0.05 in this case), we reject the null hypothesis and conclude that there are significant differences in mean weight loss among the three diets.
# In this hypothetical example, if the F-statistic is significant (greater than expected by chance) and the p-value is less than 0.05, you would conclude that there are significant differences in mean weight loss among the diets.


# In[ ]:





# Q10. A company wants to know if there are any significant differences in the average time it takes to 
# complete a task using three different software programs: Program A, Program B, and Program C. They 
# randomly assign 30 employees to one of the programs and record the time it takes each employee to 
# complete the task. Conduct a two-way ANOVA using Python to determine if there are any main effects or 
# interaction effects between the software programs and employee experience level (novice vs. 
# experienced). Report the F-statistics and p-values, and interpret the results.
#To conduct a two-way ANOVA in Python to determine if there are any main effects or interaction effects between software programs (Program A, Program B, Program C) and employee experience levels (novice vs. experienced), you can use libraries like SciPy and pandas. Here's how you can perform this analysis and interpret the results:
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a sample dataset as a pandas DataFrame
data = pd.DataFrame({
    'Software': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Experience': ['Novice', 'Novice', 'Novice', 'Novice', 'Novice', 'Novice', 'Novice', 'Novice', 'Novice', 'Novice', 'Novice', 'Novice', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced', 'Experienced'],
    'Time': [15, 16, 14, 16, 17, 15, 13, 14, 16, 14, 15, 15, 12, 13, 11, 13, 14, 12, 15, 16, 15, 14, 15, 15, 13, 14, 12, 16, 15, 14]
})

# Create a two-way ANOVA model
formula = 'Time ~ Software * Experience'
model = ols(formula, data=data).fit()

# Perform the two-way ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)

# Interpret the results
alpha = 0.05

print(anova_table)

main_effect_software_pvalue = anova_table.loc['Software', 'PR(>F)']
main_effect_experience_pvalue = anova_table.loc['Experience', 'PR(>F)']
interaction_pvalue = anova_table.loc['Software:Experience', 'PR(>F)']

print("\nMain Effect of Software - p-value:", main_effect_software_pvalue)
print("Main Effect of Experience - p-value:", main_effect_experience_pvalue)
print("Interaction Effect - p-value:", interaction_pvalue)

if main_effect_software_pvalue < alpha:
    print("Reject the null hypothesis for the main effect of Software.")
else:
    print("Fail to reject the null hypothesis for the main effect of Software.")

if main_effect_experience_pvalue < alpha:
    print("Reject the null hypothesis for the main effect of Experience.")
else:
    print("Fail to reject the null hypothesis for the main effect of Experience.")

if interaction_pvalue < alpha:
    print("Reject the null hypothesis for the Interaction Effect.")
else:
    print("Fail to reject the null hypothesis for the Interaction Effect.")
# In this code:
# We create a sample dataset as a pandas DataFrame with three columns: 'Software,' 'Experience,' and 'Time,' where 'Software' represents the software program used, 'Experience' represents the experience level of the employee, and 'Time' represents the time taken to complete the task.
# We create a two-way ANOVA model using the ols function from statsmodels, specifying the formula 'Time ~ Software * Experience' to account for both main effects and the interaction effect.
# We perform the two-way ANOVA using sm.stats.anova_lm and store the results in the anova_table.
# We interpret the results by examining the p-values for the main effects of Software and Experience, as well as the p-value for the Interaction Effect. We use a significance level (alpha) of 0.05.
# Finally, based on the p-values, we determine whether to reject or fail to reject the null hypotheses for the main effects and the interaction effect.
# Interpretation of the results depends on the p-values. If the p-value is less than alpha (0.05), we reject the null hypothesis, indicating a significant effect. If the p-value is greater than alpha, we fail to reject the null hypothesis, suggesting no significant effect. You should interpret the results in the context of your specific research question and hypotheses.
# In[ ]:





# Q11. An educational researcher is interested in whether a new teaching method improves student test 
# scores. They randomly assign 100 students to either the control group (traditional teaching method) or the 
# experimental group (new teaching method) and administer a test at the end of the semester. Conduct a 
# two-sample t-test using Python to determine if there are any significant differences in test scores 
# between the two groups. If the results are significant, follow up with a post-hoc test to determine which 
# group(s) differ significantly from each other
To determine if there are any significant differences in test scores between the control group (traditional teaching method) and the experimental group (new teaching method), you can conduct a two-sample t-test in Python. If the results are significant, you can follow up with a post-hoc test to identify which group(s) differ significantly from each other. Here's how you can perform these analyses:

Two-Sample t-test:

python
Copy code
import numpy as np
import scipy.stats as stats

# Sample test scores for the control and experimental groups
control_group = [75, 80, 82, 70, 78, 72, 68, 73, 77, 76,
                 79, 74, 71, 69, 75, 76, 72, 78, 80, 70,
                 73, 77, 75, 74, 76, 68, 72, 70, 78, 81]

experimental_group = [82, 87, 89, 75, 80, 79, 76, 84, 88, 85,
                      82, 86, 83, 78, 81, 79, 85, 87, 84, 76,
                      80, 88, 81, 84, 86, 75, 77, 80, 82, 90]

# Perform a two-sample t-test
t_statistic, p_value = stats.ttest_ind(control_group, experimental_group)

# Interpret the results
alpha = 0.05

print("Two-Sample t-test:")
print("t-statistic:", t_statistic)
print("p-value:", p_value)

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in test scores between the two groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in test scores between the two groups.")
In this code:

We have two lists of test scores for the control group and the experimental group.

We use the stats.ttest_ind function from SciPy to perform a two-sample t-test, which calculates the t-statistic and p-value for comparing the means of the two groups.

We set a significance level (alpha) of 0.05 and interpret the results. If the p-value is less than alpha, we reject the null hypothesis and conclude that there is a significant difference in test scores between the two groups.

Post-Hoc Test (if needed):

If the results of the two-sample t-test are significant, suggesting that there is a significant difference between the control and experimental groups, you can perform a post-hoc test to determine which group(s) differ significantly from each other. Common post-hoc tests include Tukey's Honestly Significant Difference (Tukey HSD) or Bonferroni correction. However, since there are only two groups in this case, post-hoc testing may not be necessary as the t-test already provides a direct comparison between the groups.

If you decide to perform post-hoc testing, you can adapt the code accordingly by comparing multiple group means, but remember that for two groups, the t-test is typically sufficient to assess differences.
# In[ ]:





# Q12. A researcher wants to know if there are any significant differences in the average daily sales of three 
# retail stores: Store A, Store B, and Store C. They randomly select 30 days and record the sales for each store 
# on those days. Conduct a repeated measures ANOVA using Python to determine if there are any 
# significant differences in sales between the three stores. If the results are significant, follow up with a posthoc test to determine which store(s) differ significantly from each other
A repeated measures ANOVA is typically used when you have dependent data, such as measurements taken at multiple time points or repeated measurements on the same subjects. In your case, you have daily sales data for three retail stores, and you want to determine if there are significant differences in sales between the three stores. However, a repeated measures ANOVA may not be the most appropriate choice for this scenario, as it is designed for within-subjects or within-groups designs.

For your scenario, where you have independent stores and you want to compare their average daily sales, a regular one-way ANOVA or Kruskal-Wallis test (for non-parametric data) would be more appropriate.

Here's how you can conduct a one-way ANOVA in Python to determine if there are significant differences in daily sales between the three stores:

python
Copy code
import numpy as np
import scipy.stats as stats

# Sample daily sales data for three stores (assuming normally distributed data)
store_A_sales = np.random.normal(500, 50, 30)  # Store A
store_B_sales = np.random.normal(480, 60, 30)  # Store B
store_C_sales = np.random.normal(520, 55, 30)  # Store C

# Combine the sales data into a single array
all_sales_data = np.concatenate([store_A_sales, store_B_sales, store_C_sales])

# Create a grouping variable to indicate the store for each observation
store_labels = ['Store A'] * 30 + ['Store B'] * 30 + ['Store C'] * 30

# Perform a one-way ANOVA
f_statistic, p_value = stats.f_oneway(store_A_sales, store_B_sales, store_C_sales)

# Interpret the results
alpha = 0.05

print("One-Way ANOVA:")
print("F-statistic:", f_statistic)
print("p-value:", p_value)

if p_value < alpha:
    print("Reject the null hypothesis: There are significant differences in daily sales between the three stores.")
else:
    print("Fail to reject the null hypothesis: There are no significant differences in daily sales between the three stores.")
In this code:

We generate random daily sales data for three stores (Store A, Store B, and Store C) using the np.random.normal function to simulate normally distributed data.

We combine the sales data into a single array and create a grouping variable (store_labels) to indicate the store for each observation.

We perform a one-way ANOVA using the stats.f_oneway function to compare the means of the three stores' daily sales.

We interpret the results based on the F-statistic and p-value. If the p-value is less than alpha (0.05), we reject the null hypothesis and conclude that there are significant differences in daily sales between the three stores.

If you find significant differences between the stores, you can follow up with a post-hoc test such as Tukey's HSD or the Bonferroni correction to identify which specific store(s) differ significantly from each other. However, in this example, I've focused on the one-way ANOVA analysis.
# In[ ]:





# #  <P style="color:GREEN"> THNAK YOU, THAT'S ALL </p>
