import altair as alt
import streamlit as st
import pandas as pd


def get_crime_types():
    return ['murdPerPop', 'rapesPerPop', 'robbbPerPop',
              'assaultPerPop', 'burglPerPop', 'larcPerPop', 
              'autoTheftPerPop', 'arsonsPerPop', 'ViolentCrimesPerPop',
              'nonViolPerPop']

@st.cache
def return_crime_dataset():
    # get data   
    df_data = pd.read_csv('crimedata.csv')
    return df_data

# get data for visualization
crime_data = return_crime_dataset()

with st.sidebar:
    y_axis = st.selectbox(label = "Crime_Types", options = get_crime_types())
    # x_axis = st.selectbox(label = "y_axi", options = crime_data['state'])

    

# altair plot
ch_prime = alt.Chart(crime_data).mark_bar().encode(
           x = 'state',
           y = y_axis,
).properties(
    width=800,
    height=600
)

ch_scatter = alt.Chart(crime_data).mark_circle(size=60).encode(
           x = 'state',
           y = y_axis,
).properties(
    width=800,
    height=600
).interactive()


tab1, tab2, tab3 = st.tabs(["tab1", "tab2", "tab3"])

with tab1:
   tab11,tab12 = st.tabs(["tab11","tab12"])
   with tab11:
    st.header("Bar Chart")
    st.write(ch_prime)
   with tab12:
    st.header("Bar Chart")
    st.write(ch_prime)

with tab2:
   st.header("Scatter Chart")
   st.write(ch_scatter)

with tab3:
   st.header("Data")
   st.write(crime_data)



