# **Summary**
This memo recommends continuing the program implemented by NYC District Attorney’s (DA’s) Oﬃce after evaluating its impact on the felony re-arrest rate employing the probit regression model on the provided data. Data contained information on the crime arrest made from 2008 – 2011, including their crime-type (felony, misdemeanor), arrest-date, treatment group (treatment, control), and demographics (gender, age, precinct). Exploratory data analysis on both crime and demographic-based features offers a graphical and tabular description of the data and its distribution. Further, statistical tests spearman, Mann- Whitney, chi-square and independent t-test, measures the correlation and association between the indicators depending upon their types. Keeping the analytical test results and assumptions in mind, I employed probit regression to find the significant signs influencing the chances of felony re-arrest rate in one year after January 2010. The model demonstrated that individuals in the treatment groups have a 16.7 percent lower probability of committing a felony re-arrest rate in the next year, holding other variables constant. People arrested with a misdemeanor crime when provided with onspot intervention on average have an approximate 23 percent higher chance of felony re-arrest without any other variable influence. Similarly, age, irrespective of other indicators, increases the likelihood of felony re-arrest by 3.5 percent.

# **Exploratory Data Analysis**
The post-implementation data considers 3662 observations (one observation for each person) further divided into treatment(1450) and control (2212) categories. Among the arrests made after January 2010, individuals with age spanned out between 8 years to 66 years had one past misdemeanor crime on average. Importantly, past misdemeanor crimes per person ranked up to 7 arrests in the past two years, while the felony crimes reached a maximum of four.  Generally, males crime rate is above the female crime rate irrespective of the treatment group and time of arrest.

<img src="https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/Exploratory_data_analysis.png" alt="drawing" width="700" height = "400"/>

# **Statistical Analysis**
>> *Correlations and Association Analysis**

Each of the treatment group and the control group must have certain conditions validated before moving into the statistical evaluation. Since numerical variables are discrete except age, it is reasonable to calculate the correlation between them through the “Spearman” correlation coefficient. The test doesn’t show any critical relationship except the same crimes committed in the past six months, and the past two years have a 0.50 correlation.

<img src="https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/correlation_plot.png" alt="drawing" width="800" height = "400"/>

In summary, there is no significant relationship between the covariates and the treatment type. I applied three different tests to measure the significance of the associations—first, the chi-square test to calculate the association between two nominal categorical variables. Second, the Mann-Whitney test to discover correlations between a nominal input and an ordinal qualitative or discrete quantitative output variable. Third, an independent t-test to figure out differences in distribution among the experimentation groups on continuous numerical indicators. Tests with p-values above 0.05 signifies no relationship between the variables. Table 2 shows the summarized results of all the statistical tests, along with the test name.

<img src="https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/Association_table.png" alt="drawing" width="1000" height = "400"/>

>> *Program Evaluation*

Felony re-arrest is an ordinal categorical variable evaluated using the probit regression model mentioned below. Y with a value 1 represents committing a felony crime again while 0 denotes disengaging in felony crime again in the next one year.

<img src="https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/regression_equation.png" alt="drawing" width="700" height = "200"/>

**Column a**. On average, a person given an on-spot intervention is associated with a 14.1 percent lower probability of getting arrested for felony again.

**Column b**. Law code decreases the coefficient of treatment status at the same time is significant. A person with a misdemeanor crime has a 21.8 percent higher probability of committing a felony again, holding treatment status constant.

**Column c**.Including age further lowers the probability of an individual in the treatment group of committing a felony crime again. Now, a person given an on spot intervention has a 16.9 percent lower likelihood of still committing a felony crime holding age and law code constant. Alternatively, one unit increase in age is associated with a 3.5 percent increase in the felony re-arrest irrespective of treatment status and law code.

At this point, treatment status(treatment), law code(misdemeanor), and age are the only three significant variables. In conclusion, a person in the control group arrested for a misdemeanor crime with an average age of 29 years has a 3 percent higher probability of committing a felony crime again in comparison to an individual in the treatment group.

**Column d,e,f,g,h**. The coefficient on the treatment status and the age remains unaffected further, including gender, felony crime(  past six months and two years), and misdemeanor crimes( past six months and previous two years). However, the coefficient on the misdemeanor crime increases, but it becomes insignificant. All the subseauently included variables are insignificant.

<img src="https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/regression_model_covariates.png" alt="drawing" width="800" height = "400"/>

# **Validity**

The evaluation might have a history threat and instrumentation threat affecting the effect of program intervention. The person arrested post-implementation has become more mature with time. However, the model s displays an increased age-associated with a higher probability of re-arrest. Accordingly, the program implementation might remain uninfluenced from the maturation threat. There is a selection bias with DA’s Oﬃces decision to consider certain precincts as participants for on-spot intervention. Despite selection, bias precincts show no relationship with the felony-re-arrest.

# **Conclusion**

In conclusion, the memo explores the data through descriptive statistics, associations between variables, and finally evaluates the effect of program intervention on the probability of committing a felony re-arrest. Treatment status has no significant relationship with the other covariates. Individuals in the treatment groups have a 16.7 percent lower likelihood of committing a felony re-arrest rate in the next year, holding other variables constant. While a one-unit increase in age increases the probability of felony re-arrest by 3.5 percent.
