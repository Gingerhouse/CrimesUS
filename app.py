import altair as alt
import streamlit as st
import pandas as pd

@st.cache
def return_crime_dataset():
    # get data   
    df_data = pd.read_csv('crimedata.csv')
    return df_data

# get data for visualization
crime_data = return_crime_dataset()
print(crime_data)

# with st.sidebar:
#     pass
    # x_axis = st.selectbox(label = "x_axis", options = crime_data.columns)
    

# altair plot
ch_prime = alt.Chart(crime_data).mark_bar().encode(
           # x = 'Component_1:Q',
           # y = 'Component_2:Q',
           x = "state:Q",
           y = "assaults:Q",
        #    color=alt.condition(
        #         alt.datum.state>100,  # If the year is 1810 this test returns True,
        #         alt.value('orange'),     # which sets the bar orange.
        #         alt.value('steelblue')),
           tooltip = ['Class', 'Label', 'Score']
).properties(
    width=800,
    height=600
)


st.write(ch_prime)