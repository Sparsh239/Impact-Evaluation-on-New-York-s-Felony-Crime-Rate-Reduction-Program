# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:44:23 2020

@author: skans
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:40:25 2020

@author: skans
"""
import datetime
import pandas as pd
from dateutil.relativedelta import *
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 500)
pd.set_option('expand_frame_repr', False)

#  Step 1) Read the Dataset 

arrests = pd.read_csv('Datasets/arrests.csv')  # Reading the arrest data
#print("Arrests Dataset Information: \n", arrests.info())
print("Arrests:\n",arrests.head(5))
print("\n")
demo = pd.read_csv('Datasets/demo.csv')  # Reading the demogeaphic data
#print("Demographic Dataset Information: \n", demo.info())
print("Demographic:\n",demo.head(5))
print("\n")
treatment = pd.read_csv('Datasets/treatment_assignment.csv') # Reading the treatment data 
#print("Treatment Status Dataset Information: \n", treatment.info())
print("Treatment Status:\n",treatment.head(5))
print("\n")


# Step 2: Create columns with dates
arrests['arrest_date'] = pd.to_datetime(arrests['arrest_date'],format='%Y/%m/%d') # Converts the arrest date into a date time format 
arrests['date_six_months_ago'] = arrests['arrest_date'].apply(lambda x:x - relativedelta(months = 6)) # Calculates date six months ago
arrests['date_two_years_ago'] = arrests['arrest_date'].apply(lambda x:x - relativedelta(years = 2)) # Calculate date 2 years ago
arrests['date_after_one_year'] = arrests['arrest_date'].apply(lambda x:x + relativedelta(years = 1)) # Caculate date 1 year later

print("Arrests with new columns:\n",treatment.head(5))
print("\n")

# Step 3: Calculate the number of cases after January 2010
arrests_post_implementation = arrests[arrests['arrest_date'] > datetime.datetime(2010,1,1)] # Data Post Implementation subset the orignal arrest dataframe
print("\n Arrests Post Implementation:")
print(arrests_post_implementation.info())

# Step 4: Calculate the covariates representing number of crimes and outcome variable
# Number of Prior Misdemeanor Arrests (in the last 2 years)
# Number of Prior Felony Arrests (in the last 2 years)
# Number of Prior Misdemecor Arrests (in the last 6 months)
# Number of Prior Felony Arrests (in the last 6 months)

for index,row in arrests_post_implementation.iterrows():
    person_id = getattr(row, 'person_id') # Person_is of the particular row
    arrest_id = getattr(row,'arrest_id')  # Arrest id of the row 
    current_arrest_date = getattr(row,'arrest_date') # Current Arrest Date
    date_past_6_months = getattr(row, 'date_six_months_ago') # Date Six Months Ago from the current date
    date_past_2_years = getattr(row, 'date_two_years_ago') # Date 2 years ago from the current date
    date_after_one_year = getattr(row,'date_after_one_year') # Date after one year
    cases = arrests[arrests['person_id'] == person_id] # Number of cases with each person id 
    misdemeanor_past_6_months = cases[(cases['law_code'] == 'misdemeanor') & ((
        date_past_6_months < cases['arrest_date']) & (cases['arrest_date'] <= current_arrest_date))]
    # Total number of misdemeanor cases in the last 6 months
    arrests_post_implementation.loc[index, 'misdemeanor_past_6_months'] = len(misdemeanor_past_6_months)
    misdemeanor_past_2_years = cases[(cases['law_code'] == 'misdemeanor') & ((
        date_past_2_years < cases['arrest_date']) & (cases['arrest_date'] <= current_arrest_date))]
    # Total number of misdemeanor cases in the last 2 years
    arrests_post_implementation.loc[index, 'misdemeanor_past_2_years'] = len(misdemeanor_past_2_years)
    felony_past_6_months = cases[(cases['law_code'] == 'felony') & ((
        date_past_6_months < cases['arrest_date']) & (cases['arrest_date'] <= current_arrest_date))]
    # Total number of felony cases in the last 6 months
    arrests_post_implementation.loc[index, 'felony_past_6_months'] = len(felony_past_6_months)
    felony_past_2_years = cases[(cases['law_code'] == 'felony') & ((
        date_past_2_years <= cases['arrest_date']) & (cases['arrest_date'] <= current_arrest_date))]
    # Total number of felony cases in the last 2 years
    arrests_post_implementation.loc[index, 'felony_past_2_years'] = len(felony_past_2_years)
    felony_next_one_year = cases[(cases['law_code'] == 'felony') & ((
        current_arrest_date < cases['arrest_date']) & (cases['arrest_date'] <= date_after_one_year))]
    # Total number of felony cases in the  next year
    if len(felony_next_one_year) > 0: # If the felony cases are more than one
        arrests_post_implementation.loc[index, 'felony_in_one_year'] = 1
    else:
        arrests_post_implementation.loc[index, 'felony_in_one_year'] = 0

print("\n Arrests Post Implementation with New Variables: \n")
print(arrests_post_implementation.info())    
print("\n")
print(arrests_post_implementation.head(3))    


# Step 5: Merge Demographic Dataset with the arrests_post_implementation dataset
merged_post_data = pd.merge(arrests_post_implementation,demo,on ='person_id')
merged_post_data['bdate'] = pd.to_datetime(merged_post_data['bdate'],format='%Y/%m/%d')
merged_post_data['age'] = ((merged_post_data['arrest_date'] - merged_post_data['bdate']).dt.days / 365.25).astype(int) 

# Step 6: Merge the dataset calculated above with treatment status dataset
policy_post_data = pd.merge(merged_post_data,treatment,left_on ='home_precinct', right_on = 'precinct')

# Step 7: 
unique_person_id = policy_post_data['person_id'].unique()
program_evaluation = []
for person_id in unique_person_id:
    cases_person_id = policy_post_data[policy_post_data['person_id'] == person_id]
    cases_person_id = cases_person_id.reset_index().sort_values(['arrest_date'],ascending = True)
    program_evaluation.append(cases_person_id.iloc[0]) # Takes the first case post implementation 

post_program_evaluation_dataframe = pd.DataFrame(program_evaluation)
post_program_evaluation_dataframe.to_csv("Datasets/Program_evaluation.csv")

