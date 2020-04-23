# Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program

# **Executive Summary**
Back in January 2010, the NYC District Attorney's office implemented a program designed to reduce the felony re-arrest rates city wide. The individuals arrested after the implementation of the program in certain precincts were provided with on-spot intervention by New York Policy Department. The DA's office hopes providing interventions will reduce the probability of arrested individuals committing a felony crime in the next one year. This repository evaluates the impact of the program developed by NYC District Attorney's office and recommends continuing the program after evaluating its impact on the felony re-arrest rate employing the probit regression model on the provided data.

Data contains information on the crime arrest made from 2008 – 2011, including their crime-type (felony, misdemeanor), arrest-date, treatment group (treatment, control), and demographics (gender, age, precinct). Exploratory data analysis on both crime and demographic-based features offers a graphical and tabular description of the data and its distribution. Further, statistical tests spearman, Mann- Whitney, chi-square and independent t-test, measures the correlation and association between the indicators depending upon their types. Keeping the analytical test results and assumptions in mind, the analysis employs probit regression to find the significant signs influencing the chances of felony re-arrest rate in one year after January 2010. The model demonstrated that individuals in the treatment groups have a 16.7 percent lower probability of committing a felony re-arrest rate in the next year, holding other variables constant. People arrested with a misdemeanor crime when provided with onspot intervention on average have an approximate 23 percent higher chance of felony re-arrest without any other variable influence. Similarly, age, irrespective of other indicators, increases the likelihood of felony re-arrest by 3.5 percent.

# **Instructions**
## **data_preprocessing.csv**
1. ***Read the datasets*** <br>
>There are three datasets required in this analysis. The dataset belong to the Crime and Education Lab at UChicago. They come along with the repository when cloned in the Desktop.
>> *arrest.csv*
>>> *Contains information on the arrests made from 2008 to 2011*
>>>> - **person_id** : Unique identification for each individuals
>>>> - **arrest_date** : Arrest Date
>>>> - **arrest_id** : Arrest ID for each arrest made. Note, there are more than one arrest id for each    >>>>                   person id, if arrested more than once
>>>> - **law_code** : Type of Crime (Misdemeanor and Felony)
<br>
![arrests_csv](https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/arrests_csv.png)

>> *demo.csv*
>>> *Demographic information of the people arrested*
>>>> - **person_id** : Unique identification for each individuals
>>>> - **gender** : Gender of the person arrested
>>>> - **bdate** : Birth Date of the person arrested
>>>> - **home_precinct** : Precinct number of the place where the arrests took place.

>> **treatment_assignment.csv**
>>> *Contains information on the precinct and treatment status (Treatment or Control)*
>>>> - **precinct** : Precinct number of the place where the arrests took place.
>>>> - **Treatment Status** : Treatment Status of the Precinct (Treatment or Control). Certain precincts >>>>                          were provided treatment and others were part of control group





2. ***Calculate the date 6 months ago , 2 years ago and one year later***
>>> We add three columns in the dataset. The first column represents the six month before date for each observation. Similarly the second and third column represent date two years ago and one year later to the current date of the respective observation.
>>> Example Code
>>>> `from dateutil.relativedelta import *` <br>
>>>> `arrests['arrest_date'] = pd.to_datetime(arrests['arrest_date'] ,format='%Y/%m/%d')`
>>>> `arrests['arrest_date_six_months_ago'] = arrests['arrest_date'].apply(lambda x:x relativedelta(months = 6))`
3. ***Subset cases into two datasets: post-implementation (After 1st January 2010) & pre-implementation (Before 1st January 2010)***
>>> Example Code
>>>> `arrests_post_implementation = arrests[arrests['arrest_date'] > datetime.datetime(2010,1,1)]`









4. ***Calculate the following parameters for the people arrested post program implementation***
>>**1)Number of Prior Misdemeanor Arrests (in the last 2 years)**
>>**2)Number of Prior Felony Arrests (in the last 2 years)**
>>**3)Number of Prior Misdemeanor Arrests (in the last 6 months)**
>>**4)Number of Prior Felony Arrests (in the last 6 months)**
>>> Example Code
>>>> `for each_row in arrests_post_implementation.iterrows():
          person_id = getattr(row, 'person_id') # Through getattr, we obtain the person id at a particular row
          arrest_id = getattr(row,'arrest_id')  # Again through getattr, we obtain the arrest id at a particular row
          current_arrest_date = getattr(row,'arrest_date') # Again through getattr, we obtain the current arrest date
          date_past_6_months = getattr(row, 'date_six_months_ago') # Date Six Months Ago from the current date
          date_past_2_years = getattr(row, 'date_two_years_ago') # Date 2 years ago from the current date
          date_after_one_year = getattr(row,'date_after_one_year') # Date after one year
          cases = arrests[arrests['person_id'] == person_id] # Number of cases with each person id in the total dataset
          misdemeanor_past_6_months = cases[(cases['law_code'] == 'misdemeanor') & ((
          date_past_6_months < cases['arrest_date']) & (cases['arrest_date'] <= current_arrest_date))]`
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```
