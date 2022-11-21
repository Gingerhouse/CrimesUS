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


crime_data = return_crime_dataset()

with st.sidebar:
    add_radio = st.radio(
        "Choose Data Set Type By",
        ("State", "CommunityName")
    )

if add_radio == 'State':
    y_axis = st.selectbox(label="Crime_Types", options=get_crime_types())
    tab1, tab2, tab3 = st.tabs(["Bar Chart", "Scatter Chart", "Data"])
    
    ch_prime = alt.Chart(crime_data).mark_bar().encode(
        x='state',
        y=y_axis,
        tooltip=['state', 'population']
    ).properties(
        width=800,
        height=600
    )

    ch_scatter = alt.Chart(crime_data).mark_circle(size=60).encode(
        x='state',
        y=y_axis,
    ).properties(
        width=800,
        height=600
    ).interactive()

    with tab1:
        st.header("Bar Chart")
        st.write(ch_prime)

    with tab2:
        st.header("Scatter Chart")
        st.write(ch_scatter)

    with tab3:
        st.header("Data")
        st.write(crime_data)
else:
    # x_axis = st.selectbox(label="Crime_Types", options=crime_data[''])
    y_axis = st.selectbox(label="Crime_Types", options=get_crime_types())
    crime_data1 = crime_data.sort_values(by=y_axis, ascending=False)

    base = alt.Chart(crime_data1).mark_arc(innerRadius=50).encode(
    theta=alt.Theta(field=y_axis, type="quantitative"),
    color=alt.Color(field="communityName", type="nominal"),
        )
    # base = alt.Chart(crime_data).encode(
    # theta=alt.Theta(y_axis, stack=True),
    # radius=alt.Radius(y_axis, scale=alt.Scale(type="sqrt", zero=True, rangeMin=20)),
    # color="state",
    # )

    # c1 = base.mark_arc(innerRadius=20, stroke="#fff")

    # c2 = base.mark_text(radiusOffset=10).encode(text="values:Q")

    # c1 + c2
    st.write(base)
