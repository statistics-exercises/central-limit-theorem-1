# Histogram for sample mean

In previous weeks we have established that the expectation and variance of a sample mean computed from multiple random variables:

![](https://render.githubusercontent.com/render/math?math=\overline{X}=\frac{1}{n}\sum_{i=1}^{n}X_i)

are

![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(\overline{X})=\mathbb{E}(X)\qquad\textrm{and}\qquad\textrm{var}(\overline{X})=\frac{\textrm{var}(X)}{n})

where ![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(X)) and ![](https://render.githubusercontent.com/render/math?math=\textrm{var}(X)) are the expectation and variance for the random variable, ![](https://render.githubusercontent.com/render/math?math=X_i) that were added together to generate the mean.  What we have not answered, however, is what distribution we are sampling when we compute a sample mean.  __In this exercise, we are thus going to investigate the distribution that is sampled when we compute a sample mean by computing a histogram from a series of sample means.__  To complete the exercise you will need to do the following:

1. Write a function called `sample_mean` that takes a parameter `n`.  This function should return a sample mean that is calculated from a sample of `n` uniform (continuous) random variables that lie between -4 and +4.
2. Write a loop that generates 500 of these sample means using your `sample_mean` function.  Each of the sample means you compute should be from a sample of 20 uniform (continuous) random variables that lie between -4 and +4
3. Use the list called `counts` to count how many of each of these random variables fall into each of the 20 bins that we have divided the line segment between -4 and +4 into.
4. Write a loop that normalises the histogram in `counts`.  By the time you exit this loop the integral of the pdf you have estimated over the whole x axis should be one.

As I did in the last exercise I have calculated the x-coordinates at which to plot each of the y-values in counts for you.  I have also written code to draw the probability density function for a normal random variable with expectation 0 and variance 4/15 in red.  These two values are the expectation and variance for a sample mean calculated from 20 uniform random variables that lie between -4 and +4 that are obtained when you use the expressions above.
