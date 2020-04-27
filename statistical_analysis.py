# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:07:09 2020

@author: skans
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import os
import matplotlib as mpl
from patsy import dmatrices
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import wilcoxon, ttest_1samp, mannwhitneyu
# Step 1: Data Preprocessing 
evaluation_data = pd.read_csv("Datasets/Program_evaluation.csv")
evaluation_data.drop(['Unnamed: 0','index','home_precinct','date_six_months_ago','date_two_years_ago','date_after_one_year','arrest_id','bdate'],axis = 1, inplace = True)
print(evaluation_data.columns)
print("\n Complete Post Implementation Data:")
print(evaluation_data.info())
evaluation_data['gender'] = evaluation_data['gender'].replace(to_replace = 'female', value = 'F')
evaluation_data['gender'] = evaluation_data['gender'].replace(to_replace = 'male', value = 'M')
#%%
# Step 2: Correlation Plot between the numerical variables  (Spearman Correlation)
# Age, felony and misdemeanor in the past two years and six montha
evaluation_correlation = evaluation_data[['misdemeanor_past_6_months',
       'misdemeanor_past_2_years', 'felony_past_6_months',
       'felony_past_2_years','age']].corr(method = 'spearman')
ax1 = sns.heatmap(evaluation_correlation,annot=True)
ax1.set_title("plots/Correlation Plot (Spearman)")
print("\n")
#%%
# Step 3: Chi_square Test between Gender and Rearrest 
# HO: There is no relationship between the variables 
# H1: There is a relationship between the variables
male_female = pd.crosstab(evaluation_data.gender, evaluation_data.felony_in_one_year)
V, p, dof, expected = stats.chi2_contingency(male_female) 
print(p)
if p > 0.05:
    print("There is no relationship between gender and felony rearrest")
else:
    print("There is a relationship between gender and felony rearrest")   
print("\n")
#%%   
# Step 4: Chi_square Test between treatment status and Rearrest 
# HO: There is no relationship between the variables 
# H1: There is a relationship between the variables
male_female = pd.crosstab(evaluation_data.treatment_status, evaluation_data.felony_in_one_year)

V, p, dof, expected = stats.chi2_contingency(male_female) 
print(p)
if p > 0.05:
    print("There is no relationship between treatment type and felony rearrest")
else:
    print("There is a relationship between tratment type and felony rearrest")
print("\n")
#%%
# Step 5: Independent T test between treatment status and Age 
eval_treat = evaluation_data.loc[evaluation_data['treatment_status']=='treatment', 'age']
eval_control = evaluation_data.loc[evaluation_data['treatment_status']=='control', 'age']
u_statistic, pVal = stats.ttest_ind(eval_treat, eval_control)
print('Statistics=%.3f, p=%.3f' % (u_statistic, pVal))
# interpret
alpha = 0.05
if pVal > alpha:
	print('Same distribution between age and treatment status (fail to reject H0)')
else:
	print('Different distribution between age and treatment status (reject H0)')
print("\n")
#%%
# Step 6: Chi_square Test between treatment status and Gender  
# HO: There is no relationship between the variables 
# H1: There is a relationship between the variables
male_female = pd.crosstab(evaluation_data.gender, evaluation_data.treatment_status)
V, p, dof, expected = stats.chi2_contingency(male_female) 
print(p)
if p > 0.05:
    print("There is no relationship between gender and treatment status")
else:
    print("There is a relationship between gender and treatment status")    
print("\n")
#%%   
# Step 6: Chi_square Test between treatment status and Law Code (Misdemeanor or Felony)  
# HO: There is no relationship between the variables 
# H1: There is a relationship between the variables
male_female = pd.crosstab(evaluation_data.law_code, evaluation_data.treatment_status)
V, p, dof, expected = stats.chi2_contingency(male_female) 
print(p)
if p > 0.05:
    print("There is no relationship between law code and treatment status")
else:
    print("There is a relationship between law code and treatment status")  
print("\n")    
#%%

# Step 9: Probit Regression Model to find the effect of treatment on the rearrest

columns = ['felony_past_2_years','felony_past_6_months','misdemeanor_past_2_years'
                                   ,'misdemeanor_past_6_months']    
for variable in columns:
    eval_treat = evaluation_data.loc[evaluation_data['treatment_status']=='treatment', variable]
    eval_control = evaluation_data.loc[evaluation_data['treatment_status']=='control', variable]
    u_statistic, pVal = stats.mannwhitneyu(eval_treat,eval_control)
    print('Statistics=%.3f, p=%.3f' % (u_statistic, pVal))
    # interpret
    alpha = 0.05
    if pVal > alpha:
    	print(variable,'and treatment group have same distribution (fail to reject H0) \n')
    else:
    	print(variable,'and treatment group dont have same distribution (reject H0)\n')
    # Thus there is no difference in the average age 
print("\n")
#%%
    
# Step 8: Chi-square between treatment status and precinct
evaluation_data['precinct'] = evaluation_data['precinct'].astype('category')

precinct = pd.crosstab(evaluation_data.precinct, evaluation_data.felony_in_one_year)

V, p, dof, expected = stats.chi2_contingency(precinct) 
if p > 0.05:
    print("There is no relationship between precinct and treatment status")
else:
    print("There is a relationship between precinct and treatment status") 
print("\n")
#%%

# Step 9: Perform logistic regression 

columns = ['treatment_status','law_code','age','gender','felony_past_2_years','felony_past_6_months','misdemeanor_past_2_years','misdemeanor_past_6_months']
#columns = ['treatment_status','law_code']
new_columns = []
list_for_printing = []
for column in columns:
    new_columns.append(column)
    dmatrix = 'felony_in_one_year ~ '
    interation = 0
    for indicators in new_columns:
        if len(new_columns) ==1 :
            dmatrix = dmatrix + indicators
        elif len(new_columns) > 1:
            if interation == (len(new_columns)-1):
                dmatrix = dmatrix + indicators 
                break
            else:
                interation = interation + 1
                dmatrix = dmatrix + indicators +  " + "
    # print(dmatrix)
    print("\n")
    y, X = dmatrices(dmatrix, data=evaluation_data, return_type='dataframe')
    input_data = sm.add_constant(X)
    logit_mod = sm.Probit(y, input_data)
    logit_res = logit_mod.fit()
    # print(logit_res.summary())
    # print(logit_res.params)
    A = np.identity(len(logit_res.params))
    A = A[1:,:]
    list_for_printing.append(logit_res)
    # print(logit_res.f_test(A))
    

from statsmodels.iolib.summary2 import summary_col
dfoutput = summary_col(list_for_printing,stars=True)
print(dfoutput)



