# Stroop Effect

<h2>Background Information</h2>
<p>In a Stroop task, participants are presented with a list of words, with each word displayed in a color of ink. The participant’s task is to say out loud the color of the ink in which the word is printed. The task has two conditions: a congruent words condition, and an incongruent words condition. In the congruent words condition, the words being displayed are color words whose names match the colors in which they are printed: for example RED, BLUE. In the incongruent words condition, the words displayed are color words whose names do not match the colors in which they are printed: for example PURPLE, ORANGE. In each case, we measure the time it takes to name the ink colors in equally-sized lists. Each participant will go through and record a time from each condition.</p>

<h2>Questions For Investigation</h2>
<h3>As a general note, be sure to keep a record of any resources that you use or refer to in the creation of your project. You will need to report your sources as part of the project submission.</h3>
<p>
1.	What is our independent variable? What is our dependent variable?
<ul>
a.	Independent variable: conditions of the words.
</ul>
<ul>
b.	Dependent variable: the time it took for the participant to recognize the color of the words.
</ul>
</p>

<p>
2.	What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.

a.	Hypothesis in words:
<ul>
<li>H0: The conditions does not affect how the participants recognize the color of the words.</li>
<li>H1: It takes longer for participants to recognize color in noncongruent conditions than for congruent.</li>
</ul>
<ul>Hypothesis in mathematical terms:
<li>H0=Mu1 = Mu2</li>
<li>Ha= Mu1>Mu2</li>
Mu1 is for population average time it takes for noncongruent participants to recognize the color.
Mu2 is for population average time it takes for congruent particpants to recognize the color.
</ul>
        
b.	I expect to perform dependent t-test because t-test is for comparing two means and that the population mean, standard deviation are unknown. I chose dependent t-test because the test compares the means of two related groups to determine whether there is a statistically significant difference between these means. The groups are related because both participants are present in the two groups. This is a one-tail test. Moreover, due to the small sample size (n<25) t- test is more suitable. 
</p>
<p>
3. Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability.
<ul>
<li>There are 24 samples. </li>
<li><b> SHOWN IN TABLE BELOW</b>
Central tendacy: sample mean time for <b>congruent</b> condition is 14.051125 seconds, for <b>noncongruent</b> sample mean is 22.015917. <i>Sample mean differences is 7.964792</i> and <i>sample standard deviation of the differences is 4.864827</i>. The standard deviation for each condition is 3.559358 and 4.797057, respectively. </li>

<br>![Preview](https://github.com/jtsou/Statistics-Stroop-Effect/blob/master/table.png)<br>

</ul>
</p>
<p>  
4. Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

<br>![Preview](https://github.com/jtsou/Statistics-Stroop-Effect/blob/master/congruent.png)<br>

<br>![Preview](https://github.com/jtsou/Statistics-Stroop-Effect/blob/master/non%20congruent.png)<br>

<br>![Preview](https://github.com/jtsou/Statistics-Stroop-Effect/blob/master/time%20diff.png)<br>

<ul>I created histograms for each condition, and for the difference in the conditions. I noticed that they are not normal Congruent condition is slight skewed to the right; the incongruent condition indicates that most participants was able to recognize the color within 27 seconds, with a outlier of 35 seconds. </ul>
</p>
<p>
5. Now, perform the statistical test and report your results. What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?
<ul>
My confidence interval is 0.95 and the critical statistics value is 1.7138. the t statistics is -8.02070694411. Also we test the p value at alpha=0.05, and p-value we calculated is at 4.10300058571e-08. We reject null hypothesis and come to the conclusion that participants take longer to recognize color in noncongruent conditions. The results match up with my expections.
</ul>
</p>

<p>
Q6: Hypotheses regarding the reasons for the effect observed are presented. An extension or related experiment to the performed Stroop task is provided, that may produce similar effects.
<ul>
After some research, the similar effects are: Warped words, Emotional, Spatial, Numerical, etc..
</ul>
</p>
