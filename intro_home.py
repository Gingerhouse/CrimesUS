import streamlit as st

def write():
    st.markdown("# Crimes in US")
    st.markdown("## Project group 13")
    st.markdown("""This is a dataset of 2018 US communities, demographics of each community, 
    and their crime rates. The dataset has 146 variables where the first four columns are community/location, 
    the middle features are demographic information about each community such as population, age, race, income, 
    and the final columns are types of crimes and overall crime rates.""")
    with st.container():
        image_col, text_col = st.columns((1,2))
        with image_col:
            st.image("./images/crime1.jpeg")
        with text_col:
            st.subheader("A Multi-page Interactive Dashboard with Streamlit and Plotly")
            st.write("""Visualization of crimes in USA communities and factors influencing it
            """)
        
    with st.container():
        image_col, text_col = st.columns((1,2))
        with image_col:
            st.image("https://cdn-images-1.medium.com/max/906/1*hjhCIWGgLzOznTFwDyeIeA.png")
        with text_col:
            st.subheader("Regression of dataset")
            st.write("""This is a dataset of 2018 US communities, demographics of each community, 
    and their crime rates. The dataset has 146 variables where the first four columns are community/location, 
    the middle features are demographic information about each community such as population, age, race, income, 
    and the final columns are types of crimes and overall crime rates.
            """)
            

if __name__ == '__main__':
    write()