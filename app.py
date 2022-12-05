import altair as alt
import streamlit as st
import pandas as pd


st.title("Crime in the United Sates")

tab1, tab2, tab3 = st.tabs(["Main", "Crime", "State"])

with tab1:
   st.header("What this tool does:")
   st.markdown("This tool uses crime data collected from a variety of communinties across the US combined with census data to highlight " + 
   "potential links in community attributes and types of crime. This tool also displays general crime information for each state represented in the data and D.C. in" + 
   "different forms of visualization methods.")
   st.header("What this tool is for:")
   st.markdown("Our web app can be used to inform users about the types of crimes in their communities in a digestible manner. For people in power" + 
   "potential links in community attributes and types of crime.")
   st.header("Who can use this tool:")
   st.header("Additional Info:")
   st.markdown("Made by: Prachi Chandanshive, Abel Villanueva Perez, Nikhil Mandge, and Charlie Jubera.")
   st.markdown("Data sourced from: https://www.kaggle.com/datasets/michaelbryantds/crimedata/code.")
with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)