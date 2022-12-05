import altair as alt
import streamlit as st
import pandas as pd
from pycaret.regression import *


st.title("Crime in the United Sates")

tab1, tab2, tab3, tab4 = st.tabs(["Main", "Crime","Predict Crime", "State"])

@st.cache
def return_lr_dataset():
    # get data   
    df_data = pd.read_csv("crimedata.csv")

    # model   
    data_setup = setup(data = df_data, target = 'Class', 
                       silent=True, verbose=False)

    # train logistic regression model
    lr = create_model('lr', verbose=False)

    # predictions & data preparation for visualization
    pred_pca = predict_model(lr, verbose=False)
    pred_pca['Error'] = pred_pca['Class'] != pred_pca['Label']

    return pred_pca

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
   

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)