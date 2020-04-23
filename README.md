# Impact-Evaluation-on-New-York-s-Felony-Crime-Rate-Reduction-Program
Back in January 2010, the NYC District Attorney;s office implemented a program designed to reduce the felony re-arrest rates city wide. The individuals arrested after the implementation of the program in certain precincts were provided with on-spot intervention by New York Policy Department. The DA's office hopes providing interventions will reduce the probability of arrested individuals committing a felony crime in the next one year. This repository evaluates the impact of the program developed by NYC District Attorney's office.

There are three datasets required in this analysis:
>> **arrest.csv**
>>> *Contains information on the arrests made from 2008 to 2011*
>>>> - **person_id** : Unique identification for each individuals
>>>> - **arrest_date** : Arrest Date
>>>> - **arrest_id** : Arrest ID for each arrest made. Note, there are more than one arrest id for each    >>>>                   person id, if arrested more than once
>>>> - **law_code** : Type of Crime (Misdemeanor and Felony)

>> **demo.csv**
>>> *Demographic information of the people arrested*
>>>> - **person_id** : Unique identification for each individuals
>>>> - **gender** : Gender of the person arrested
>>>> - **bdate** : Birth Date of the person arrested
>>>> - **home_precinct** : Precinct number of the place where the arrests took place.

>> **treatment_assignment.csv**
>>> *Contains information on the precinct and treatment status (Treatment or Control)*
>>>> - **precinct** : Precinct number of the place where the arrests took place.
>>>> - **Treatment Status** : Treatment Status of the Precinct (Treatment or Control). Certain precincts >>>>                          were provided treatment and others were part of control group



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
