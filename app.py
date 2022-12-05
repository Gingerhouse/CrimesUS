import altair as alt
import streamlit as st
import pandas as pd
from pycaret.regression import *
from vega_datasets import data


st.set_page_config(layout="wide")
st.title("Crime in the United Sates")

tab1, tab2, tab3, tab4 = st.tabs(["Main", "Crime","Predict Crime", "State"])

@st.cache
def load_crime_data():
   crime_df = pd.read_csv("crimedata.csv")
   crime_corr = pd.read_csv("corr.csv", index_col=0)
   crime_corr = crime_corr.reset_index()
   return crime_df, crime_corr

@st.cache
def non_v_pred_cache(test_data):
   lr_nv_saved = load_model('non_viol_mdl')
   predictions = predict_model(lr_nv_saved, data= test_data)
   return predictions['Label']

@st.cache
def v_pred_cache(test_data):
   lr_v_saved = load_model('viol_mdl')
   predictions = predict_model(lr_v_saved, data= test_data)
   return predictions['Label']

@st.cache
def var_dict(var):
   Data_dict = {'population': 'population for community',
                'householdsize': 'mean people per household',
                'racepctblack': 'percentage of population that is of african american ',
                'racePctWhite': 'percentage of population that is of caucasian ',
                'racePctAsian': 'percentage of population that is of asian heritage',
                'racePctHisp': 'percentage of population that is of hispanic heritage',
                'agePct12t21': 'percentage of population that is 12-21 in age',
                'agePct12t29': 'percentage of population that is 12-29 in age',
                'agePct16t24': 'percentage of population that is 16-24 in age',

                'agePct65up': 'percentage of population that is 65 and over in age',
                'numbUrban': ' number of people living in areas classified as urban',
                'pctUrban': 'percentage of people living in areas classified as urban',
                'medIncome': 'median household income  ',
                'pctWWage': ' percentage of households with wage or salary income',
                'pctWFarmSelf': 'percentage of households with farm or self employment income',
                'pctWInvInc': 'percentage of households with investment / rent income',
                'pctWSocSec': 'percentage of households with social security income',
                'pctWPubAsst': ' percentage of households with public assistance income',
                
                'pctWRetire': 'percentage of population that is 65 and over in age',
                'medFamInc': ' number of people living in areas classified as urban',
                'perCapInc': 'percentage of people living in areas classified as urban',
                'whitePerCap': 'per capita income for caucasians', 
                'blackPerCap': 'per capita income for african americans', 
                'AsianPerCap': 'per capita income for people with asian heritage', 
                'OtherPerCap': 'per capita income for people with "other" heritage', 
                'HispPerCap': 'per capita income for people with hispanic heritage',  

                'NumUnderPov': 'number of people under the poverty level', 
                'PctPopUnderPov': 'percentage of people under the poverty level',
                'PctLess9thGrade': 'percentage of people 25 and over with less than a 9th grade education', 
                'PctNotHSGrad': 'percentage of people 25 and over that are not high school graduates' ,
                'PctBSorMore': 'percentage of people 25 and over with a bachelors degree or higher education' ,
                'PctUnemployed':' percentage of people 16 and over, in the labor force, and unemployed ',
                'PctEmploy': 'percentage of people 16 and over who are employed ',
                'PctEmplManu':' percentage of people 16 and over who are employed in manufacturing ',
                'PctEmplProfServ':' percentage of people 16 and over who are employed in professional services ',
                'PctOccupManu': 'percentage of people 16 and over who are employed in manufacturing' ,
                'PctOccupMgmtProf': 'percentage of people 16 and over who are employed in management or professional occupations ',
                'MalePctDivorce': 'percentage of males who are divorced ',
                'MalePctNevMarr':' percentage of males who have never married ',
                'FemalePctDiv': 'percentage of females who are divorced ',
                'TotalPctDiv': 'percentage of population who are divorced ',
                'PersPerFam': 'mean number of people per family ',
                'PctFam2Par': 'percentage of families (with kids) that are headed by two parents' ,
                'PctKids2Par': 'percentage of kids in family housing with two parents' ,
                'PctYoungKids2Par': 'percent of kids 4 and under in two parent households ',
                'PctTeen2Par':' percent of kids age 12-17 in two parent households ',
                'PctWorkMomYoungKids': 'percentage of moms of kids 6 and under in labor force ',
                'PctWorkMom': 'percentage of moms of kids under 18 in labor force ',
                'NumIlleg': 'number of kids born to never married ',
                'PctIlleg': 'percentage of kids born to never married ',
                'NumImmig': 'total number of people known to be foreign born ',
                'PctImmigRecent': 'percentage of _immigrants_ who immigated within last 3 years',
                'PctImmigRec5': 'percentage of _immigrants_ who immigated within last 5 years ',
                'PctImmigRec8': 'percentage of _immigrants_ who immigated within last 8 years ',
                'PctImmigRec10':' percentage of _immigrants_ who immigated within last 10 years ',
                'PctRecentImmig': 'percent of _population_ who have immigrated within the last 3 years ',
                'PctRecImmig5': 'percent of _population_ who have immigrated within the last 5 years ',
                'PctRecImmig8': 'percent of _population_ who have immigrated within the last 8 years ',
                'PctRecImmig10': 'percent of _population_ who have immigrated within the last 10 years ',
                'PctSpeakEnglOnly': 'percent of people who speak only English ',
                'PctNotSpeakEnglWell': 'percent of people who do not speak English well ',
                'PctLargHouseFam': 'percent of family households that are large ',
                'PctLargHouseOccup': 'percent of all occupied households that are large ',
                'PersPerOccupHous': 'mean persons per household ',
                'PersPerOwnOccHous': 'mean persons per owner occupied household ',
                'PersPerRentOccHous': 'mean persons per rental household ',
                'PctPersOwnOccup': 'percent of people in owner occupied households ',
                'PctPersDenseHous': 'percent of persons in dense housing ',
                'PctHousLess3BR': 'percent of housing units with less than 3 bedrooms ',
                'MedNumBR': 'median number of bedrooms ',
                'HousVacant': 'number of vacant households ',
                'PctHousOccup': 'percent of housing occupied ',
                'PctHousOwnOcc': 'percent of households owner occupied ',
                'PctVacantBoarded': 'percent of vacant housing that is boarded up ',
                'PctVacMore6Mos': 'percent of vacant housing that has been vacant more than 6 months',
                'MedYrHousBuilt': 'median year housing units built ',
                'PctHousNoPhone': 'percent of occupied housing units without phone ',
                'PctWOFullPlumb': 'percent of housing without complete plumbing facilities ',
                'OwnOccLowQuart': 'owner occupied housing - lower quartile value ',
                'OwnOccMedVal': 'owner occupied housing - median value ',
                'OwnOccHiQuart': 'owner occupied housing - upper quartile value ',
                'RentLowQ': 'rental housing - lower quartile rent ',
                'RentMedian': 'rental housing - median rent ',
                'RentHighQ': 'rental housing - upper quartile rent ',
                'MedRent': 'median gross rent ',
                'MedRentPctHousInc': 'median gross rent as a percentage of household income', 
                'MedOwnCostPctInc':' median owners cost as a percentage of household income - for owners with a mortgage ',
                'MedOwnCostPctIncNoMtg': 'median owners cost as a percentage of household income - for owners without a mortgage ',
                'NumInShelters': 'number of people in homeless shelters ',
                'NumStreet': 'number of homeless people counted in the street ',
                'PctForeignBorn': 'percent of people foreign born ',
                'PctBornSameState': 'percent of people born in the same state as currently living ',
                'PctSameHouse85': 'percent of people living in the same house as in 1985 ',
                'PctSameCity85': 'percent of people living in the same city as in 1985 ',
                'PctSameState85': 'percent of people living in the same state as in 1985 '          
               }
   return Data_dict[var]

with tab1:
   st.header("What this tool does:")
   st.markdown("This tool uses crime data collected from a variety of communities  across the US combined with census data to highlight " + 
   "potential links in community attributes and types of crime. This tool also displays general crime information for each state represented in the data and D.C. in" + 
   "different visualization methods.")
   st.header("What this tool is for:")
   st.markdown("Our web app can be used to inform users about the types of crimes in their communities in a digestible manner. For people in power" + 
   "potential links in community attributes and types of crime.")
   st.header("Who can use this tool:")
   st.markdown("The public can use this web app to gain insight about their communities. Non-government organizations can use this tool to see areas that impact crime rates. The government and politicians can use this tool to predict crime rates in their cities based on census statistics.")
   st.header("Additional Info:")
   st.markdown("Made by: Prachi Chandanshive, Abel Villanueva Perez, Nikhil Mandge, and Charlie Jubera.")
   st.markdown("Data sourced from: https://www.kaggle.com/datasets/michaelbryantds/crimedata/code.")
with tab2:
   col1, col2 = st.columns([1, 3])
   crime_df, crime_corr = load_crime_data()
   with col1:
    census_stats = ['population','householdsize','racepctblack','racePctWhite','racePctAsian','racePctHisp','agePct12t21','agePct12t29','agePct16t24','agePct65up','numbUrban','pctUrban','medIncome','pctWWage','pctWFarmSelf','pctWInvInc','pctWSocSec','pctWPubAsst','pctWRetire','medFamInc','perCapInc','whitePerCap','blackPerCap','indianPerCap','AsianPerCap','OtherPerCap','HispPerCap','NumUnderPov','PctPopUnderPov','PctLess9thGrade','PctNotHSGrad','PctBSorMore','PctUnemployed','PctEmploy','PctEmplManu','PctEmplProfServ','PctOccupManu','PctOccupMgmtProf','MalePctDivorce','MalePctNevMarr','FemalePctDiv','TotalPctDiv','PersPerFam','PctFam2Par','PctKids2Par','PctYoungKids2Par','PctTeen2Par','PctWorkMomYoungKids','PctWorkMom','NumKidsBornNeverMar','PctKidsBornNeverMar','NumImmig','PctImmigRecent','PctImmigRec5','PctImmigRec8','PctImmigRec10','PctRecentImmig','PctRecImmig5','PctRecImmig8','PctRecImmig10','PctSpeakEnglOnly','PctNotSpeakEnglWell','PctLargHouseFam','PctLargHouseOccup','PersPerOccupHous','PersPerOwnOccHous','PersPerRentOccHous','PctPersOwnOccup','PctPersDenseHous','PctHousLess3BR','MedNumBR','HousVacant','PctHousOccup','PctHousOwnOcc','PctVacantBoarded','PctVacMore6Mos','MedYrHousBuilt','PctHousNoPhone','PctWOFullPlumb','OwnOccLowQuart','OwnOccMedVal','OwnOccHiQuart','OwnOccQrange','RentLowQ','RentMedian','RentHighQ','RentQrange','MedRent','MedRentPctHousInc','MedOwnCostPctInc','MedOwnCostPctIncNoMtg','NumInShelters','NumStreet','PctForeignBorn','PctBornSameState','PctSameHouse85','PctSameCity85','PctSameState85']
    crimes = ['murders','murdPerPop','rapes','rapesPerPop','robberies','robbbPerPop','assaults','assaultPerPop','burglaries','burglPerPop','larcenies','larcPerPop','autoTheft','autoTheftPerPop','arsons','arsonsPerPop','ViolentCrimesPerPop','nonViolPerPop']
    
    crime_type = st.selectbox("What crime type would you like to get more info on?", crimes)
    census_selection = st.selectbox('What census statistic would you like to visualize your selected crimes with?', census_stats)
    st.write('Description of statistic:  ' + var_dict(census_selection))
    crime_selected_corr = crime_corr[['index', crime_type]].sort_values(by=crime_type, ascending=False)
    filtered_corr = crime_selected_corr[crime_selected_corr['index'].isin(census_stats)]['index']
    st.markdown("### Census Statistics with the Highest Correlation to your Selected Crime Type \n " + 
    '1. ' + filtered_corr.iloc[0] + "\n" +
    '2. ' + filtered_corr.iloc[1] + "\n" + 
    '3. ' + filtered_corr.iloc[2] + "\n" + 
    '4. ' + filtered_corr.iloc[3] + "\n" + 
    '5. ' + filtered_corr.iloc[4])
   crimes_chart = alt.Chart(crime_df).mark_point().encode(
    x=census_selection,
    y=crime_type,
   ).properties(
      width= 750,
      height = 500)
   with col2:
      st.write(crimes_chart + crimes_chart.transform_regression(census_selection,crime_type).mark_line(color='red'))

with tab3:
   
   state = st.selectbox("What state are you in?", crime_df['state'].unique())
   population = st.slider("What is population of your community?", min_value=10000, max_value=7500000)
   household_size = st.slider("What is the average household size?", min_value=0, max_value=6)

   a12to21 = st.slider("What percent of your community is aged 12 to 21?", min_value=0, max_value=100)
   a12t29 = st.slider("What percent of your community is aged 12 to 19?", min_value=0, max_value=100)
   a16t24 = st.slider("What percent of your community is aged 16 to 24?", min_value=0, max_value=100)

   a65up = st.slider("What percent of your community is aged older than 65?", min_value=0, max_value=100)
   income = st.slider("What is your communities median income?", min_value=5000, max_value=130000)
   PubAsst = st.slider("What percent of your community recieve public assistance?", min_value=0, max_value=100)

   HSGrad = st.slider("What percent of your community has not graduated highschool?", min_value=0, max_value=100)
   Unemployed = st.slider("What percent of your community is unemployed?", min_value=0, max_value=100)
   Employ = st.slider("What percent of your community is employed ?", min_value=0, max_value=100)

   divorce = st.slider("What percent of your community has been divorced?", min_value=0, max_value=100)
   personperfam = st.slider("What is the average number of people per family?", min_value=2, max_value=5)
   vacanthouse = st.slider("How many vacant houses do you have in your area?", min_value=0, max_value=175000)

   people_shelter = st.slider("How many people live in shelters ?", min_value=0, max_value=30000)
   people_street = st.slider("How many people live on the street?", min_value=0, max_value=10000)

   test_data = pd.DataFrame({'state': state,
   'population': population,
   'householdsize': household_size,
   'agePct12t21': a12to21,
   'agePct12t29': a12t29,
   'agePct16t24': a16t24,
   'agePct65up': a65up,
   'medIncome': income,
   'pctWPubAsst': PubAsst,
   'PctNotHSGrad': HSGrad,
   'PctUnemployed': Unemployed,
   'PctEmploy': Employ,
   'TotalPctDiv': divorce,
   'PersPerFam': personperfam,
   'HousVacant': vacanthouse,
   'NumInShelters': people_shelter,
   'NumStreet': people_street}, index=[0])

   st.markdown("### Non-violent Crimes per Population predicted = %0.2f"%non_v_pred_cache(test_data)[0])
   st.markdown("### Violent Crimes per Population predicted = %0.2f"%v_pred_cache(test_data)[0])

with tab4:
   st.markdown("## Crime By State")
   coro_type = st.selectbox("What stat would you like to see per state?", ('robbbPerPop','assaultPerPop','burglPerPop','larcPerPop','autoTheftPerPop','arsonsPerPop','ViolentCrimesPerPop','nonViolPerPop'))
    
    
   state_crime_df = crime_df.groupby('state').agg({'robbbPerPop': 'mean','assaultPerPop': 'mean','burglPerPop': 'mean','larcPerPop': 'mean','autoTheftPerPop': 'mean','arsonsPerPop': 'mean','ViolentCrimesPerPop': 'mean','nonViolPerPop': 'mean'})
   state_crime_df =state_crime_df.reset_index()
   state_ids = {'AL': 1, 'AK': 2, 'AR': 5, 'AZ':4, 'CA': 6, 'CO': 8,
             'CT': 9, 'DC': 11, 'FL': 12, 'GA': 13, 'IA': 19, 'DE':10,
             'ID': 16, 'IL': 17, 'IN': 18, 'KS': 20, 'KY': 21,
             'LA': 22, 'MA': 25, 'MD': 24, 'ME': 23, 'MI': 26,
             'MN': 27, 'MO': 30, 'MS': 28, 'NC': 37, 'ND': 38,
             'NH': 33, 'NJ': 34, 'NM': 35, 'NV': 32, 'NY': 36,
             'OH': 39, 'OK': 40, 'OR': 41, 'PA': 42, 'RI': 44,
             'SC': 45, 'SD': 46, 'TN': 47, 'TX': 48, 'UT': 49,
             'VA': 51, 'VT': 50, 'WA': 53, 'WI': 55, 'WV': 54, 'WY': 56}
   state_crime_df['id'] = state_crime_df['state'].map(state_ids)

   state_bar = alt.Chart(crime_df).mark_bar().encode(
   x='state:N',
    y=alt.Y(coro_type, aggregate='mean')
    ).properties(
        width=1000,
        height=300
    )

   states = alt.topo_feature(data.us_10m.url, feature="states")
   state_cloro = alt.Chart(states).mark_geoshape().encode(
        color=coro_type+":Q"
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(state_crime_df, 'id', [coro_type])
    ).project(
        type='albersUsa'
    ).properties(
        width=1000,
        height=500
    )

   st.write(state_cloro)

   st.write( state_bar )

   
