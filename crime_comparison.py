import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def write():
    df = pd.read_csv('./crimedata.csv', sep=r'\s*,\s*')
    st.header("Crimes in states visualization")
    
    #Cleaning data
    df['ViolentCrimesPerPop'] = pd.to_numeric(df['ViolentCrimesPerPop'], errors='coerce')
    df = df.dropna(subset=['ViolentCrimesPerPop'])
    df['ViolentCrimesPerPop'] = df['ViolentCrimesPerPop'].astype(int)
    
    def crime_classify_by_state():
        col = df['state'].unique()
        label = list(col)
        categories=['ViolentCrimesPerPop','nonViolPerPop']
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:\
        option = st.selectbox('What states do you want to check the violent vs non violent crimes?', label)
        data = df.groupby('state')[categories].mean().reset_index()
        sizes = data.loc[data['state'] == option].reset_index()
        sizesx=sizes[['ViolentCrimesPerPop','nonViolPerPop']]
        explode = (0, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizesx.iloc[0], explode=explode, labels=categories, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)
    
    def crime_by_state(col):
       
        state = df.groupby('state')[col].mean().reset_index()
        state.sort_values(by=col, ascending=False, inplace=True)
        plt.figure(figsize=(12,12))
        st.bar_chart(data=state, y=col, x='state')

    
    
        
    crime_classify_by_state()
    states_list=['murdPerPop','rapesPerPop','robbbPerPop','assaultPerPop','burglPerPop','larcPerPop','autoTheftPerPop','arsonsPerPop']
    option = st.multiselect('Select crimes for which  visualization can be created for all states?', states_list, default =states_list[0] )
    crime_by_state(option)
if __name__ == '__main__':
    write()
    