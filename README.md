# Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program

# **Executive Summary**
Back in January 2010, the NYC District Attorney's office implemented a program designed to reduce the felony re-arrest rates city wide. The individuals arrested after the implementation of the program in certain precincts were provided with on-spot intervention by New York Policy Department. The DA's office hopes providing interventions will reduce the probability of arrested individuals committing a felony crime in the next one year. This repository evaluates the impact of the program developed by NYC District Attorney's office and recommends continuing the program after evaluating its impact on the felony re-arrest rate employing the probit regression model on the provided data.

Data contains information on the crime arrest made from 2008 – 2011, including their crime-type (felony, misdemeanor), arrest-date, treatment group (treatment, control), and demographics (gender, age, precinct). Exploratory data analysis on both crime and demographic-based features offers a graphical and tabular description of the data and its distribution. Further, statistical tests spearman, Mann- Whitney, chi-square and independent t-test, measures the correlation and association between the indicators depending upon their types. Keeping the analytical test results and assumptions in mind, the analysis employs probit regression to find the significant signs influencing the chances of felony re-arrest rate in one year after January 2010. The model demonstrated that individuals in the treatment groups have a 16.7 percent lower probability of committing a felony re-arrest rate in the next year, holding other variables constant. People arrested with a misdemeanor crime when provided with onspot intervention on average have an approximate 23 percent higher chance of felony re-arrest without any other variable influence. Similarly, age, irrespective of other indicators, increases the likelihood of felony re-arrest by 3.5 percent.

# **Instructions**
## **Script 1: data_preprocessing.csv**
Data preprocessing is the most essential step before getting into exploratory data analysis, statistical analysis and probit modelling. Here, we are taking necessary steps to calculate all the important covariates that have the potential to influence the probability of a person provided intervention after January 2010 to again commit a felony crime apart from just being in the treatment group. Moreover, through data preprocessing, we find our dependent outcome variable. It is a dummy variable ( 0: the arrested person  did not commit a crime in one year after January 2010 , 1: the arrested individual did commit a crime in one year after January 2010 ). After data wrangling and merging along with few other operation we should have the following columns in our dataframe.
> *Covariates*
1. age
2. Gender
3. Home precincts
4. Number of prior misdemeanor arrests (in the last 2 years)
5. Number of prior felony arrests (in the last 2 years)
6. Number of prior misdemeanor arrests (in the last 6 months)
7. Number of prior felony arrests (in the last 6 months)

> *Independent Variable*
1. treatment_status

> *Dependent Variable*
1.  Binary outcome that measures any felony re-arrest in a 1-year period following the arrest


>### **Step 1: Read the datasets** <br>
>>There are three datasets required in this analysis. The dataset belong to the Crime and Education Lab at UChicago. They come along with the repository when cloned in the Desktop.
>> **arrest.csv**
>>> *Contains information on the arrests made from 2008 to 2011*
>>> - **person_id** : Unique identification for each individuals
>>> - **arrest_date** : Arrest Date
>>> - **arrest_id** : Arrest ID for each arrest made. Note, there are more than one arrest id for each person id, if arrested more than once
>>> - **law_code** : Type of Crime (Misdemeanor and Felony)

<img src="https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/arrests_csv.png" alt="drawing" width="300" height = "100"/>

>> *demo.csv*
>>> *Demographic information of the people arrested*
>>> - **person_id** : Unique identification for each individuals
>>> - **gender** : Gender of the person arrested
>>> - **bdate** : Birth Date of the person arrested
>>> - **home_precinct** : Precinct number of the place where the arrests took place.

<img src="https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/demo_csv.png" alt="drawing" width="300" height = "100"/>

>> **treatment_assignment.csv**
>>> *Contains information on the precinct and treatment status (Treatment or Control)*
>>> - **precinct** : Precinct number of the place where the arrests took place.
>>> - **Treatment Status** : Treatment Status of the Precinct (Treatment or Control). Certain precincts >>>>                          were provided treatment and others were part of control group

<img src="https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/treatment_csv.png" alt="drawing" width="300" height = "100"/>

> ###  **Step 2: Create columns with dates**
Here we create three columns representing the following the dates:
1. date_six_months_ago :date six months before the current arrest date
2. date_two_years_ago : date two years before the current arrest date
3. date_after_one_year: date one year after the current arrest date

>>> We convert the date column in the arrests dataset in a date-time format using pandas.to_datetime(column_name,format='%Y/%m/%d')
>>>> `arrests['arrest_date'] = pd.to_datetime(arrests['arrest_date'] ,format='%Y/%m/%d')``
>>> We add three columns in the dataset using relativedelta library. The first column represents the six month before date for each observation. Similarly the second and third column represent date two years ago and one year later to the current date of the respective observation.
>>>> `arrests['arrest_date_six_months_ago'] = arrests['arrest_date'].apply(lambda x:x relativedelta(months = 6))`
>>>> `from dateutil.relativedelta import *` <br>

<img src="https://github.com/Sparsh239/Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program/blob/master/images/arrests_updated.png" alt="drawing" width="300" height = "100"/>


> ###  **Step 3: Calculate the number of cases after January 2010**
We subset the dataset with cases after January 2010. These are the people arrested after the program got implemented.
>>> Example Code
>>>> `arrests_post_implementation = arrests[arrests['arrest_date'] > datetime.datetime(2010,1,1)]`

> ###  **Step 4: Calculate the covariates representing number of crimes and outcome variable**
>>**1)Number of Prior Misdemeanor Arrests (in the last 2 years)**
>>**2)Number of Prior Felony Arrests (in the last 2 years)**
>>**3)Number of Prior Misdemeanor Arrests (in the last 6 months)**
>>**4)Number of Prior Felony Arrests (in the last 6 months)**
>>**5)Binary Variable representing whether person commited felony crime in the next one year after intervention**
>>> Example Code
>>>> `for index,row in arrests_post_implementation.iterrows():
          person_id = getattr(row, 'person_id')
          cases = arrests[arrests['person_id'] == person_id] #Calculate total number of cases of a person id
          # Subset the number of misdemeanor crimes between current arrest date and date six months ago
          misdemeanor_past_6_months = cases[(cases['law_code'] == 'misdemeanor') & ((
          date_past_6_months < cases['arrest_date']) & (cases['arrest_date'] <= current_arrest_date))]`

> ###  **Step 5: Merge Demographic Dataset with the arrests_post_implementation dataset**
Merge the demo.csv file with the arrests_post_implementation on the person_id, a unique identifier for person arrested.
Later we calculate the age of the person by calculating the different between the current arrest date and the date of birth

> ###  **Step 6: Merge the dataset calculated above with treatment status dataset**
Merge the dataset calculated after merging demo.csv and arrests_post_implementation.csv with treatment_status.csv on home precinct.
Dropping all the unnecessary variables we get the final columns in our dataset.

> ###  **Step 7: Selecting the first time the person is arrested after intervention**
To check the efficacy of the program, we will take the first case of each person id after January 2010. This means we are trying to see
when the first time the person is arrested and provided intervention, does he or she commit another felony crime again in the next one year. 



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
