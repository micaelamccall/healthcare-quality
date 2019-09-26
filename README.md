# Exploring patient satisfaction, readmission, and indices of medical underservice
## I

*python | API queries | *

## Background

Working in a hospital has given me an appreciation of the complexity of the systems at play and the diversity of interested parties. his complexity is reflected in the numerous outcomes measures that are used to assess the quality of healthcare facilities.

Readmission rate is a crucial outcome measure because unplanned readmissions are very costly and often preventable. This outcome measure is often used by entities such as CMS to evaluate a facility. Certain interventions can reduce unplanned readmissions, such as:
 - medication reconciliation
 - follow-up phone calls
 - handoff to PCPs promptly after surgery

Another another outcome measure is patient satisfaction, as reflected in patient reported outcome measures (PRAMs) such as the Consumer Assessment of Healthcare Providers and Systems (CAHPS). 

 Sometimes, these outcome measures can come into conflict with each other. For instance, swift handoff can make patients feel like they aren't being given attention. So, patient satisfaction can be used as a balance measure for interventions aiming to affect another outcome measure.


## Goals

CMS (data.medicare.gov) has large datasets on readmissions, by hospital, and CAHPS outcomes by hospital. I was interested in exploring these data sets and the relatioships between readmission rates and CAHPS outcomes.

Additionally, tasks such as follow-up calls and medication reconciliation require large staff investments. CMS also identifies and rates Medically Underserved Areas (MUAs) and a number of related measures. I wanted to explore the relationship between these measures and the outcome measures listed above.


Can facilities in underserved areas achieve high levels of patient satisfaction and reasonable readmission rates?
