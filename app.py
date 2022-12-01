import streamlit as st
import crime_comparison
import intro_home



PAGES = {
    "Home": intro_home,
    "Crime in states": crime_comparison
}


def main():
    """Main function of the App"""
    st.set_page_config(layout='wide')
    st.sidebar.title("Select which visualization you would like to see:")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        page.write()


if __name__ == "__main__":
    main()