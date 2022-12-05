import altair as alt
import streamlit as st
import pandas as pd
from pycaret.regression import *


st.title("Crime in the United Sates")

tab1, tab2, tab3, tab4 = st.tabs(["Main", "Crime","Predict Crime", "State"])

@st.cache
def load_crime_data():
   crime_df = pd.read_csv("crimedata.csv")
   crime_corr = pd.read_csv("corr.csv", index_col=0)
   crime_corr = crime_corr.reset_index()
   return crime_df, crime_corr

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
   
   crime_df, crime_corr = load_crime_data()
   with st.sidebar:
    census_stats = ['population','householdsize','racepctblack','racePctWhite','racePctAsian','racePctHisp','agePct12t21','agePct12t29','agePct16t24','agePct65up','numbUrban','pctUrban','medIncome','pctWWage','pctWFarmSelf','pctWInvInc','pctWSocSec','pctWPubAsst','pctWRetire','medFamInc','perCapInc','whitePerCap','blackPerCap','indianPerCap','AsianPerCap','OtherPerCap','HispPerCap','NumUnderPov','PctPopUnderPov','PctLess9thGrade','PctNotHSGrad','PctBSorMore','PctUnemployed','PctEmploy','PctEmplManu','PctEmplProfServ','PctOccupManu','PctOccupMgmtProf','MalePctDivorce','MalePctNevMarr','FemalePctDiv','TotalPctDiv','PersPerFam','PctFam2Par','PctKids2Par','PctYoungKids2Par','PctTeen2Par','PctWorkMomYoungKids','PctWorkMom','NumKidsBornNeverMar','PctKidsBornNeverMar','NumImmig','PctImmigRecent','PctImmigRec5','PctImmigRec8','PctImmigRec10','PctRecentImmig','PctRecImmig5','PctRecImmig8','PctRecImmig10','PctSpeakEnglOnly','PctNotSpeakEnglWell','PctLargHouseFam','PctLargHouseOccup','PersPerOccupHous','PersPerOwnOccHous','PersPerRentOccHous','PctPersOwnOccup','PctPersDenseHous','PctHousLess3BR','MedNumBR','HousVacant','PctHousOccup','PctHousOwnOcc','PctVacantBoarded','PctVacMore6Mos','MedYrHousBuilt','PctHousNoPhone','PctWOFullPlumb','OwnOccLowQuart','OwnOccMedVal','OwnOccHiQuart','OwnOccQrange','RentLowQ','RentMedian','RentHighQ','RentQrange','MedRent','MedRentPctHousInc','MedOwnCostPctInc','MedOwnCostPctIncNoMtg','NumInShelters','NumStreet','PctForeignBorn','PctBornSameState','PctSameHouse85','PctSameCity85','PctSameState85']
    crimes = ['murders','murdPerPop','rapes','rapesPerPop','robberies','robbbPerPop','assaults','assaultPerPop','burglaries','burglPerPop','larcenies','larcPerPop','autoTheft','autoTheftPerPop','arsons','arsonsPerPop','ViolentCrimesPerPop','nonViolPerPop']
    
    crime_type = st.selectbox("What crime type would you like to get more info on?", crimes)
    census_selection = st.selectbox('What census statistic would you like to visualize your selected crimes with?', census_stats)
    crime_selected_corr = crime_corr[['index', crime_type]].sort_values(by=crime_type, ascending=False)
    filtered_corr = crime_selected_corr[crime_selected_corr['index'].isin(census_stats)]['index']
    st.markdown("### Census Statistics with the Highest Correlation to your Selected Crime Type \n " + 
    '1. ' + filtered_corr.iloc[0] + "\n" +
    '2. ' + filtered_corr.iloc[1] + "\n" + 
    '3. ' + filtered_corr.iloc[2] + "\n" + 
    '4. ' + filtered_corr.iloc[3] + "\n" + 
    '5. ' + filtered_corr.iloc[4])

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)