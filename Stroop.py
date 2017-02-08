
# coding: utf-8

# # Statistics: The Science of Decisions
#     Stroop

# Background Information
# In a Stroop task, participants are presented with a list of words, with each word displayed in a color of ink. The participant’s task is to say out loud the color of the ink in which the word is printed. The task has two conditions: a congruent words condition, and an incongruent words condition. In the congruent words condition, the words being displayed are color words whose names match the colors in which they are printed: for example RED, BLUE. In the incongruent words condition, the words displayed are color words whose names do not match the colors in which they are printed: for example PURPLE, ORANGE. In each case, we measure the time it takes to name the ink colors in equally-sized lists. Each participant will go through and record a time from each condition.
# 
# Questions For Investigation
# As a general note, be sure to keep a record of any resources that you use or refer to in the creation of your project. You will need to report your sources as part of the project submission.
# 1.	What is our independent variable? What is our dependent variable?
#     a.	Independent variable: conditions of the words.
#     b.	Dependent variable: the time it took for the participant to recognize the color of the words.
# 2.	What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.
#     a.	Hypothesis in words: 
#         H0: The conditions does not affect how the participants recognize the color of the words.
#         H1: It takes longer for participants to recognize color in noncongruent conditions than for congruent.
#         Hypothesis in mathematical terms:
#         H0=X_bar1 = X_bar2
#         Ha= X_bar1>X_bar2
#         
#         X_bar1 is for average time it takes for noncongruent participants to recognize the color.
#         X_bar2 is for average time it takes for congruent particpants to recognize the color.
#         
#     b.	I expect to perform dependent t-test because t-test is for comparing two means and that the population mean, standard deviation are unknown. I chose dependent t-test because the test compares the means of two related groups to determine whether there is a statistically significant difference between these means. The groups are related because both participants are present in the two groups. This is a one-tail test. Moreover, due to the small sample size (n<25) t- test is more suitable. 
# 
# 3. Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability.
#     a. There are 24 samples. 
#     Central tendacy: sample mean time for congruent condition is 14.051125 seconds, for noncongruent sample mean is 22.015917. Sample mean differences is 7.964792 and sample standard deviation of the differences is 4.864827. The standard deviation for each condition is 3.559358 and 4.797057, respectively. 
#   
# 4. Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.
#     a. I created histograms for each condition, and for the difference in the conditions. I noticed that they are not normal Congruent condition is slight skewed to the right; the incongruent condition indicates that most participants was able to recognize the color within 27 seconds, with a outlier of 35 seconds. 
#     
#     5. Now, perform the statistical test and report your results. What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?
#     a. My confidence level is 0.95 and the critical statistics value is 1.7138. the t statistics is -8.02070694411. Also we test the p value at alpha=0.05, and p-value we calculated is at 4.10300058571e-08. We reject null hypothesis and come to the conclusion that participants take longer to recognize color in noncongruent conditions. The results match up with my expections.
# 
#  
# Q6: Hypotheses regarding the reasons for the effect observed are presented. An extension or related experiment to the performed Stroop task is provided, that may produce similar effects.
# 
# After some research, the similar effects are: Warped words, Emotional, Spatial, Numerical, etc..

# In[2]:

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import math


# In[7]:

congruent=[12.079,16.791,9.564,8.63,14.669,12.238,14.692,8.987,9.401,14.48,22.328,15.298,15.073,16.929,18.2,12.13,18.495,10.639,11.344,12.369,12.944,
14.233,19.71,16.004]
noncongruent=[19.278,18.741,21.214,15.687,22.803,20.878,24.572,17.394,20.762,26.282,24.524,18.644,17.51,20.33,35.255,22.158,25.139,20.429,17.425
              ,34.288,23.894,17.96,22.058,21.157]
plt.hist(congruent)
plt.xlabel("Seconds")
plt.ylabel("frequency")
plt.title("Performance on Congruent")
plt.show()


plt.hist(noncongruent)
plt.xlabel("Seconds")
plt.ylabel("frequency")
plt.title("Performance on Noncongruent")
plt.show()

difference=np_noncongruent-np_congruent

plt.hist(difference)
plt.xlabel("Seconds")
plt.ylabel("frequency")
plt.title("Time difference between the two conditions")
plt.show()


# In[4]:

np_congruent=np.array(congruent)
print('The mean of congruent result is ',np.mean(np_congruent))
np_noncongruent=np.array(noncongruent)
print('The mean of noncongruent result is ',np.mean(np_noncongruent))

print('Number of Participants for congruents: ',len(congruent))
print('Number of Participants for noncongruents: ',len(noncongruent))


# In[5]:

df = pd.DataFrame({"congruent":np_congruent,
                          "noncongruent":np_noncongruent,
                          "difference":np_noncongruent-np_congruent})
df.describe()


# In[8]:

stats.ttest_rel(a = congruent,
                b = noncongruent)  
std=difference.std(ddof = 1)
print('sample std: ', std)


# In[11]:

from scipy import stats

t_stat, p_val = stats.ttest_rel(congruent, noncongruent)

print 'Test-statistic: ', t_stat
print 'P-value: ', p_val

