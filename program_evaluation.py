# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:17:52 2020

@author: skans
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import os
import matplotlib as mpl


# Step 1: Data Preprocessing
pd.set_option('display.max_rows',None)
evaluation_data = pd.read_csv("Datasets/Program_evaluation.csv")
evaluation_data.drop(['Unnamed: 0','index','home_precinct','date_six_months_ago','date_two_years_ago','date_after_one_year','arrest_id','bdate'],axis = 1, inplace = True)
print(evaluation_data.columns)
print("\n Complete Post Implementation Data:")
print(evaluation_data.info())
evaluation_data['gender'] = evaluation_data['gender'].replace(to_replace = 'female', value = 'F')
evaluation_data['gender'] = evaluation_data['gender'].replace(to_replace = 'male', value = 'M')


# Step 2: Dividing the data between the treatment and the control group
treatment_data = evaluation_data[evaluation_data['treatment_status'] == 'treatment']
print("\n Treatment Data:")
print(treatment_data.info())

control_data = evaluation_data[evaluation_data['treatment_status'] == 'control']
print("\n Control Data:")
print(control_data.info())

#%%

#Step 3: Count Plot to check the observations in the treatment and control group 
sns.countplot(x='treatment_status', data=evaluation_data)
plt.savefig("plots/countplot.png")
#%%

#Step 4 : Crime type comparison between the treatment and the control group
law_code_counts = pd.crosstab(evaluation_data.law_code,evaluation_data.treatment_status )
law_code_counts.plot(kind = 'bar', stacked=True)
plt.xlabel("Law Code")
plt.ylabel("Count")
plt.title("Trial Group (Treatment and Control")
plt.savefig("plots/crime_type_and_treatmentstatus.png")

#%%

#Step 4 : Gender type comparison between the treatment and the control group
gender_code_counts = pd.crosstab(evaluation_data.gender,evaluation_data.treatment_status)
gender_code_counts.plot(kind = 'bar',stacked=True)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Trial Group (Treatment and Control")
plt.savefig("plots/gender_and_treatmentstatus.png")

#%%

#Step 5 : Felony counts after program implementation comparison between the treatment and the control group
felony_in_one_year_counts = pd.crosstab(evaluation_data.felony_in_one_year,evaluation_data.treatment_status)
felony_in_one_year_counts.plot(kind = 'bar',stacked=True)
print(felony_in_one_year_counts)
plt.xlabel("Felony Re-arrest in one year(post implementation")
plt.ylabel("Count")
plt.title("Trial Group (Treatment and Control")
plt.savefig("plots/rearrest_and_treatmentstatus.png")


#%%
# Step 6 : Treatment and Control Group with age distribution

treatment_data['age'].hist(alpha=0.3, color='k', normed=True)
treatment_data['age'].plot(kind = 'kde',style='k--')
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Treatment")
plt.savefig("plots/age_and_treatment.png")

#%%
# Control Group and Age Distribution
control_data['age'].hist(alpha=0.3, color='k', normed=True)
control_data['age'].plot(kind = 'kde',style='k--')
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Control")
plt.savefig("plots/crime_type_and_control.png")


#%%
# Step 7: Past misdemeanor and felony crimes with the treatment group
fig, axs = plt.subplots(2,2, figsize=(2*4,2*3), squeeze=False)
fig.suptitle('Treatment and Past Crimes')
treatment_misdemeanor_past_2_years= pd.DataFrame(treatment_data['misdemeanor_past_2_years'].value_counts()).reset_index()
print(treatment_misdemeanor_past_2_years)
ax1 = sns.barplot(x='index', y='misdemeanor_past_2_years', data=treatment_misdemeanor_past_2_years, ax = axs[0][0])
ax1.set_ylabel("Count")
ax1.set_xlabel("Misdemeanor(Past 2 Years)")

# # ax2 = fig.add_subplot(122)
treatment_felony_past_2_years= pd.DataFrame(treatment_data['felony_past_2_years'].value_counts()).reset_index()
ax2 = sns.barplot(x='index', y='felony_past_2_years', data=treatment_felony_past_2_years, ax =axs[0][1])
ax2.set_ylabel("Count")
ax2.set_xlabel("Felony( Past 2 Years)")

# ax3 = fig.add_subplot(223)
treatment_misdemeanor_past_6_months= pd.DataFrame(treatment_data['misdemeanor_past_6_months'].value_counts()).reset_index()
ax3 = sns.barplot(x='index', y='misdemeanor_past_6_months', data=treatment_misdemeanor_past_6_months, ax=axs[1][0])
ax3.set_ylabel("Count")
ax3.set_xlabel("Misdemeanor(Past 6 Months)")

# ax4 = fig.add_subplot(224)
treatment_felony_past_6_months= pd.DataFrame(treatment_data['felony_past_6_months'].value_counts()).reset_index()
ax4 = sns.barplot(x='index', y='felony_past_6_months', data=treatment_felony_past_6_months, ax= axs[1][1])
ax4.set_ylabel("Count")
ax4.set_xlabel("Felony( Past 6 Months)")
# fig.tight_layout()
plt.subplots_adjust(wspace=0.5, hspace= 0.5)
plt.savefig("plots/pastcrimes_and_treatment.png")

#%%
# Step 8: Past misdemeanor and felony crimes with the control group
fig, axs = plt.subplots(2,2, figsize=(2*4,2*3), squeeze=False)
fig.suptitle('Control and Past Crimes')
control_misdemeanor_past_2_years= pd.DataFrame(control_data['misdemeanor_past_2_years'].value_counts()).reset_index()
print(control_misdemeanor_past_2_years)
ax1 = sns.barplot(x='index', y='misdemeanor_past_2_years', data=control_misdemeanor_past_2_years, ax = axs[0][0])
ax1.set_ylabel("Count")
ax1.set_xlabel("Misdemeanor(Past 2 Years)")

# # ax2 = fig.add_subplot(122)
control_felony_past_2_years= pd.DataFrame(control_data['felony_past_2_years'].value_counts()).reset_index()
ax2 = sns.barplot(x='index', y='felony_past_2_years', data=control_felony_past_2_years, ax =axs[0][1])
ax2.set_ylabel("Count")
ax2.set_xlabel("Felony( Past 2 Years)")

# ax3 = fig.add_subplot(223)
control_misdemeanor_past_6_months= pd.DataFrame(control_data['misdemeanor_past_6_months'].value_counts()).reset_index()
ax3 = sns.barplot(x='index', y='misdemeanor_past_6_months', data=control_misdemeanor_past_6_months, ax=axs[1][0])
ax3.set_ylabel("Count")
ax3.set_xlabel("Misdemeanor(Past 6 Months)")

# ax4 = fig.add_subplot(224)
control_felony_past_6_months= pd.DataFrame(control_data['felony_past_6_months'].value_counts()).reset_index()
ax4 = sns.barplot(x='index', y='felony_past_6_months', data=control_felony_past_6_months, ax= axs[1][1])
ax4.set_ylabel("Count")
ax4.set_xlabel("Felony( Past 6 Months)")
plt.subplots_adjust(wspace=0.5, hspace= 0.5)
plt.savefig("plots/pastcrimes_and_control.png")

#%%

# Step 9: Descriptive Statistics table 
evaluation_data_numerical = evaluation_data[['misdemeanor_past_6_months',
       'misdemeanor_past_2_years', 'felony_past_6_months',
       'felony_past_2_years','age']]

evaluation_description = evaluation_data_numerical.describe()
evaluation_description.loc['var'] = evaluation_description.var().tolist()
evaluation_description.loc['skew'] = evaluation_description.skew().tolist()
evaluation_description.loc['kurt'] = evaluation_description.kurtosis().tolist()
print(evaluation_description)


