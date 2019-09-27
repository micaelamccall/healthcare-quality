# Exploring patient satisfaction and readmission in medically underserved areas

*python | API queries | data mining | data cleaning | data visualization*

# Intro

Working in a hospital has given me an appreciation of the complexity of helthcare outcome measures and the diversity of interested parties. This project aims to explore outcome measures and indices of medical underservice, in order to reveal potential areas for investment. 

## Radmission rate and patient satisfaction 

Unplanned readmissions are very costly and often preventable. The metric of readmission rate is thus used by entities, such as Center for Medicaid Services (CMS), to evaluate a facility. 

Additionally, healthcare is a *service* that can also be evaluated by *patient reported outcome measures* (PRAMs) such as the Consumer Assessment of Healthcare Providers and Systems (CAHPS). 

## Improving outcome measures in medically underserved areas

Tasks such as follow-up calls and medication reconciliation demand resources. Therefore, facilities in medically underserved areas (MUAs)may struggle to achieve high levels of patient satisfaction and decrease readmission rates.

CMS uses a number of measures, such as physicians per 1000 population,and infant mortality rates, to identify MUAs. 

# Project goals

In this project, I aimed to explore the relationships between readmission rates and CAHPS outcomes in MUAs and non-MUAs. I hoped to answer these questions:

- Does readmission rate and patient satisfaction have a positive correlation, or must we make tradeoffs in improvements?
- Are measures used to determine MUA status related to a facility's outcome measures? 
- Should investments aimed at improving outcome measure target MUA measures? 



# Data
I used [CMS's API](https://dev.socrata.com) to combile data 
 on 
 - [readmissions by hospital](https://data.medicare.gov/Hospital-Compare/Unplanned-Hospital-Visits-Hospital/632h-zaca
), 
- [CAHPS outcomes by hospital](https://data.medicare.gov/Hospital-Compare/Outpatient-and-Ambulatory-Surgery-Consumer-Assessm/yizn-abxn
), and 
- [Medically Underserved Areas + measures](https://bhw.hrsa.gov/shortage-designation)


# Setup

If you're using anaconda, clone this repo and create my conda environment from the terminal by running  `conda env create -f environment.yml`

If you're using pip, install packages with `pip install -r requirements.txt`

# Usage

# Findings


