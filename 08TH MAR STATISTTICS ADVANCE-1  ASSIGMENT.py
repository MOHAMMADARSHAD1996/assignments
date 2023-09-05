#!/usr/bin/env python
# coding: utf-8

# #  <P style="color:brown"> MD. ARSHAD </p>
# ###  <P style="color:skyblue"> ALISHARMEEN02@GMAIL.COM  </p>

# #  <P style="color:purple"> STATISTTICS ADVANCE-1 </p>

# Q1. What is the Probability density function?

The Probability Density Function (PDF) is a fundamental concept in probability theory and statistics. It is a mathematical function that describes the likelihood of a continuous random variable taking on a specific value or falling within a particular range of values. In other words, the PDF provides a way to quantify the probability of different outcomes for continuous random variables.

The key properties of a Probability Density Function are as follows:

Non-Negative Values: The PDF must be non-negative for all possible values of the random variable. That is, for any value "x," the PDF must satisfy the condition: 
�
(
�
)
≥
0
f(x)≥0.

Area Under the Curve: The area under the curve of the PDF over the entire range of possible values must be equal to 1. In mathematical terms, this is expressed as: 
∫
−
∞
∞
�
(
�
)
�
�
=
1
∫ 
−∞
∞
​
 f(x)dx=1, where the integral symbol (
∫
∫) represents the area under the curve.

Probability within an Interval: The probability that the random variable falls within a specific interval 
[
�
,
�
]
[a,b] is given by the integral of the PDF over that interval: 
∫
�
�
�
(
�
)
�
�
∫ 
a
b
​
 f(x)dx.

Notation: The PDF is typically denoted as 
�
(
�
)
f(x), where 
�
x is the random variable. The probability of 
�
x falling within an interval 
[
�
,
�
]
[a,b] is denoted as 
�
(
�
≤
�
≤
�
)
P(a≤x≤b) and is calculated using the PDF.

In summary, the Probability Density Function provides a way to describe the probability distribution of a continuous random variable by assigning probabilities to different values or intervals. It is an essential concept in statistics and is used to analyze and model a wide range of real-world phenomena, including measurements, uncertainties, and random processes.
# In[ ]:





# Q2. What are the types of Probability distribution?
There are several types of probability distributions in statistics, each with its own characteristics and applications. The choice of which distribution to use depends on the nature of the data and the specific problem you are trying to solve. Here are some common types of probability distributions:

Uniform Distribution: In a uniform distribution, all outcomes are equally likely. It's often represented as a flat horizontal line, and it's commonly used when every outcome has the same probability.

Bernoulli Distribution: The Bernoulli distribution models a single trial with two possible outcomes, typically labeled as "success" and "failure." It's useful for modeling binary events like coin flips or yes/no experiments.

Binomial Distribution: The binomial distribution describes the number of successes in a fixed number of independent Bernoulli trials. It's used when you have a binary outcome (success/failure) and you want to know the probability of getting a specific number of successes in a fixed number of trials.

Poisson Distribution: The Poisson distribution models the number of events that occur in a fixed interval of time or space. It's often used to describe rare events or count data, such as the number of phone calls received at a call center in an hour.

Normal (Gaussian) Distribution: The normal distribution is characterized by its bell-shaped curve. It's widely used to model continuous data in many real-world situations, as it describes the distribution of data when many random factors contribute to an outcome.

Exponential Distribution: The exponential distribution is often used to model the time between events in a Poisson process. It's commonly applied in reliability analysis and queueing theory.

Geometric Distribution: The geometric distribution models the number of trials required for the first success in a sequence of independent Bernoulli trials. It's used when you want to know the probability of achieving success for the first time after a certain number of trials.

Gamma Distribution: The gamma distribution is a versatile distribution that generalizes the exponential distribution and is used to model the waiting time for a Poisson process with a non-integer mean.

Log-Normal Distribution: The log-normal distribution describes data that follows a normal distribution after taking the natural logarithm. It's commonly used for modeling data that is positively skewed, such as income or stock prices.

Beta Distribution: The beta distribution is a continuous probability distribution defined on the interval [0, 1]. It's often used as a probability distribution for random variables that represent probabilities themselves.

Chi-Square Distribution: The chi-square distribution arises in various statistical tests, including hypothesis testing for the variance of a normally distributed population and goodness-of-fit tests.

Student's t-Distribution: The t-distribution is used in hypothesis testing when the sample size is small, and the population standard deviation is unknown. It's similar in shape to the normal distribution but has heavier tails.

These are some of the fundamental probability distributions used in statistics and probability theory. Choosing the appropriate distribution for a given problem is crucial for accurate modeling and analysis.
# In[ ]:





# Q3. Write a Python function to calculate the probability density function of a normal distribution with 
# given mean and standard deviation at a given point.

# In[6]:


#You can calculate the probability density function (PDF) of a normal distribution at a given point using 
#Python's scipy.stats.norm module. Here's a Python function to do that:
import scipy.stats as stats

def normal_pdf(mean, std_dev, x):
    """
    Calculate the probability density function (PDF) of a normal distribution at a given point.

    Parameters:
    mean (float): Mean (average) of the normal distribution.
    std_dev (float): Standard deviation of the normal distribution.
    x (float): The point at which to calculate the PDF.

    Returns:
    float: The PDF of the normal distribution at the given point.
    """
    pdf = stats.norm.pdf(x, loc=mean, scale=std_dev)
    return pdf

# Example usage:
mean = 0  # Mean of the normal distribution
std_dev = 1  # Standard deviation of the normal distribution
x = 1.5  # Point at which to calculate the PDF

pdf_value = normal_pdf(mean, std_dev, x)
print(f"The PDF at x={x} is {pdf_value}")
# In this code:
# We import the scipy.stats module as stats, which provides functions for working with probability distributions.
# The normal_pdf function takes three arguments: mean, std_dev, and x.
# It calculates the PDF of a normal distribution with the given mean and std_dev at the point x using stats.norm.pdf().
# You can replace the values of mean, std_dev, and x in the example usage section with your desired values to calculate 
#the PDF at a specific point for a normal distribution with the given mean and standard deviation.


# In[ ]:





# Q4. What are the properties of Binomial distribution? Give two examples of events where binomial 
# distribution can be applied.
The Binomial distribution is a discrete probability distribution that describes the number of successes (usually denoted as "k") in a fixed number of independent Bernoulli trials (experiments), where each trial has only two possible outcomes: success (usually denoted as "S") or failure (usually denoted as "F"). The properties of the Binomial distribution are as follows:

Fixed Number of Trials (n): The number of trials or experiments, denoted as "n," is predetermined and remains constant throughout the process.

Two Possible Outcomes: Each trial results in one of two mutually exclusive and exhaustive outcomes, typically labeled as success (S) and failure (F).

Constant Probability of Success (p): The probability of success (P(S)) is the same for each trial. It is denoted as "p."

Independent Trials: The trials are assumed to be independent of each other, meaning the outcome of one trial does not affect the outcome of any other trial.

Discrete Data: The random variable, which represents the number of successes, is a discrete variable, taking on non-negative integer values (0, 1, 2, ...).

Probability Mass Function (PMF): The probability mass function of the Binomial distribution, denoted as P(X=k), gives the probability of getting exactly k successes in n trials, and it is calculated using the binomial coefficient formula:

P(X=k) = C(n, k) * p^k * (1-p)^(n-k)

Where C(n, k) is the binomial coefficient, given by C(n, k) = n! / (k!(n-k)!), and "!" denotes factorial.

Two examples of events where the Binomial distribution can be applied are:

Coin Flips: When you flip a fair coin (with a 50% chance of getting heads and a 50% chance of getting tails) a fixed number of times, say 10 times, the number of heads you get follows a Binomial distribution. You can use the Binomial distribution to calculate the probability of getting a specific number of heads (e.g., 5 heads) in 10 coin flips.

Quality Control: In manufacturing, you might have a process where each item produced has a certain probability of being defective (e.g., 5% chance of being defective). If you inspect a fixed number of items (e.g., 100 items), you can use the Binomial distribution to model the number of defective items you'll find during the inspection. This is useful for quality control purposes.

In both of these examples, you have a fixed number of trials (coin flips or inspections), two possible outcomes (success or failure), a constant probability of success (probability of getting heads or probability of an item being defective), independent trials, and a discrete random variable representing the number of successes.
# In[ ]:





# In[ ]:





# Q5. Generate a random sample of size 1000 from a binomial distribution with probability of success 0.4 
# and plot a histogram of the results using matplotlib.

# In[5]:


#To generate a random sample of size 1000 from a binomial distribution with a probability of success of 0.4 and 
#plot a histogram of the results using Matplotlib in Python, you can use the following code:
import numpy as np
import matplotlib.pyplot as plt

# Parameters
probability_of_success = 0.4
sample_size = 1000

# Generate the random sample from a binomial distribution
random_sample = np.random.binomial(1, probability_of_success, sample_size)

# Plot a histogram
plt.hist(random_sample, bins=2, edgecolor='black')
plt.title('Binomial Distribution (n=1, p=0.4)')
plt.xlabel('Success (1) / Failure (0)')
plt.ylabel('Frequency')
plt.xticks([0, 1], ['Failure (0)', 'Success (1)'])

# Show the plot
plt.show()
# In this code:
# We import the necessary libraries, including numpy as np and matplotlib.pyplot as plt.
# We specify the probability of success as probability_of_success (0.4) and the desired sample size as sample_size (1000).
# We generate a random sample of size 1000 from a binomial distribution using
# np.random.binomial(1, probability_of_success, sample_size). Here, we use 1 as the number of trials (n) because we
# are interested in individual successes or failures (Bernoulli trials).
# We plot a histogram of the random sample using plt.hist().
# We specify the number of bins as bins=2 since there are two possible outcomes (success or failure), and 
# we label the x-axis accordingly.
# Finally, we use plt.show() to display the histogram.
# This code will generate a histogram that visually represents the random sample of Bernoulli trials with
#a probability of success of 0.4.The histogram will show the frequency of successes (1) and failures (0) in the sample.


# In[ ]:





# Q6. Write a Python function to calculate the cumulative distribution function of a Poisson distribution 
# with given mean at a given point.

# In[3]:


#You can calculate the cumulative distribution function (CDF) of a Poisson distribution with 
#a given mean at a given point using the following Python function. We'll use the scipy.stats library,
#which provides a convenient way to work with various probability distributions, including the Poisson distribution:

import scipy.stats as stats

def poisson_cdf(mean, k):
    """
    Calculate the cumulative distribution function (CDF) of a Poisson distribution.

    Args:
        mean (float): The mean of the Poisson distribution.
        k (int): The point at which to evaluate the CDF.

    Returns:
        float: The CDF value at the given point.
    """
    cdf_value = stats.poisson.cdf(k, mu=mean)
    return cdf_value

# Example usage:
mean = 3.5  # Mean of the Poisson distribution
k = 2       # Point at which to calculate the CDF

cdf_result = poisson_cdf(mean, k)
print(f"CDF at {k} for Poisson(mean={mean}): {cdf_result:.4f}")
# In this code:
# We import the scipy.stats library as stats.
# The poisson_cdf function takes two arguments: mean (the mean of the Poisson distribution) and 
# k (the point at which you want to calculate the CDF).
# Inside the function, we use stats.poisson.cdf(k, mu=mean) to calculate the CDF of the Poisson distribution at 
# the given point k with the specified mean mu.
# The function returns the CDF value at the given point.
# You can change the mean and k values in the example usage section to calculate
# the CDF at different points for a Poisson distribution with a different mean.


# In[ ]:





# Q7. How Binomial distribution different from Poisson distribution?
The Binomial distribution and the Poisson distribution are two different probability distributions that are used to model different types of random events. Here are the key differences between the Binomial distribution and the Poisson distribution:

Nature of Events:

Binomial Distribution: The Binomial distribution is used to model a fixed number of independent Bernoulli trials, where each trial can result in one of two possible outcomes (usually denoted as success and failure). Examples of Binomial distributions include the number of heads obtained when flipping a coin a fixed number of times or the number of defective items in a batch of products.

Poisson Distribution: The Poisson distribution is used to model the number of events that occur in a fixed interval of time or space when these events happen randomly and independently of the time since the last event. Examples include the number of customer arrivals at a store in an hour or the number of emails received in an hour.

Number of Trials:

Binomial Distribution: In a Binomial distribution, the number of trials (n) is fixed and known in advance. You are interested in counting the number of successful outcomes in these fixed trials.

Poisson Distribution: In a Poisson distribution, there is no fixed number of trials. Events occur randomly over time or space, and you are interested in counting how many events occur within a fixed interval.

Parameters:

Binomial Distribution: The Binomial distribution is parameterized by two values: the probability of success on each trial (p) and the number of trials (n).

Poisson Distribution: The Poisson distribution is parameterized by a single value: the average rate of event occurrences (lambda, λ) in the fixed interval.

Shape:

Binomial Distribution: The Binomial distribution is typically symmetric when the number of trials (n) is large, and the probability of success (p) is not too extreme (not too close to 0 or 1). It can take on a range of discrete values between 0 and n.

Poisson Distribution: The Poisson distribution is a discrete distribution that is often skewed to the right. It represents rare events occurring in a fixed interval, so it tends to have a long tail on the right side.

Relationship Between Mean and Variance:

Binomial Distribution: The variance of a Binomial distribution is determined by both the number of trials (n) and the probability of success (p), and it is given by σ^2 = n * p * (1 - p).

Poisson Distribution: The variance of a Poisson distribution is equal to its mean, which is determined by the average rate of event occurrences (λ). Therefore, the variance of a Poisson distribution is σ^2 = λ.

In summary, the Binomial distribution is used when you have a fixed number of trials with two possible outcomes, while the Poisson distribution is used to model the number of rare events occurring randomly over time or space. Their parameterization, shape, and relationship between mean and variance differ accordingly.
# In[ ]:





# Q8. Generate a random sample of size 1000 from a Poisson distribution with mean 5 and calculate the 
# sample mean and variance.

# In[2]:


#To generate a random sample of size 1000 from a Poisson distribution with a mean of 5 and calculate the sample mean and variance, you can use a programming language like Python. Here's how you can do it using Python and its numpy library:

import numpy as np

# Parameters
mean = 5
sample_size = 1000

# Generate the random sample
random_sample = np.random.poisson(mean, sample_size)

# Calculate the sample mean and variance
sample_mean = np.mean(random_sample)
sample_variance = np.var(random_sample)

print("Sample Mean:", sample_mean)
print("Sample Variance:", sample_variance)
#In this code:

# We import the numpy library as np.
# We specify the mean of the Poisson distribution (lambda) as mean and the desired sample size as sample_size.
# We generate a random sample of size 1000 from a Poisson distribution with a mean of 5 using np.random.poisson(mean, sample_size).
# We calculate the sample mean using np.mean() and the sample variance using np.var().
# Running this code will give you the sample mean and variance based on the generated random sample. Please note that the values may vary each time you run the code since they are based on random sampling.


# In[ ]:





# Q9. How mean and variance are related in Binomial distribution and Poisson distribution?
The mean and variance are related differently in the Binomial distribution and the Poisson distribution.

Binomial Distribution:
In a Binomial distribution, which models the number of successes (usually denoted as "x") in a fixed number of independent Bernoulli trials (experiments with two possible outcomes, often referred to as success and failure), the mean (μ) and variance (σ^2) are related as follows:

Mean (μ): For a Binomial distribution, the mean is given by μ = n * p, where "n" is the number of trials and "p" is the probability of success on each trial.

Variance (σ^2): The variance of a Binomial distribution is given by σ^2 = n * p * (1 - p), where "n" is the number of trials and "p" is the probability of success on each trial.

So, in the Binomial distribution, the variance is directly related to both the number of trials and the probability of success.

Poisson Distribution:
In a Poisson distribution, which models the number of events that occur in a fixed interval of time or space, the mean (μ) and variance (σ^2) are related as follows:

Mean (μ): For a Poisson distribution, the mean is given by μ = λ, where "λ" (lambda) represents the average rate of event occurrences in the given interval.

Variance (σ^2): The variance of a Poisson distribution is also given by σ^2 = λ, which means that the variance is equal to the mean.

In the Poisson distribution, the variance is equal to the mean, and it is solely determined by the average rate of event occurrences, lambda (λ). This is a unique property of the Poisson distribution, where the spread of the data is directly related to the mean, and it doesn't depend on any other parameters like in the Binomial distribution.

In summary, in the Binomial distribution, the variance depends on both the number of trials and the probability of success, while in the Poisson distribution, the variance is equal to the mean and is solely determined by the average rate of event occurrences.
# In[ ]:





# Q10. In normal distribution with respect to mean position, where does the least frequent data appear?
In a normal distribution (also known as a Gaussian distribution), the data is symmetrically distributed around the mean, which is also the point of highest frequency or peak of the distribution. The least frequent data appears in the tails of the distribution, which are the regions farthest away from the mean on both sides.

Specifically, the data in the tails of a normal distribution is less frequent because it represents values that are further from the mean and are less likely to occur. The farther you move away from the mean in either direction, the less frequent the data points become. The tails of the distribution extend indefinitely in both directions, but in practice, most of the data falls within a few standard deviations of the mean, and the data becomes increasingly rare as you move further into the tails.
# In[ ]:





# #  <P style="color:GREEN"> THNAK YOU, THAT'S ALL </p>
