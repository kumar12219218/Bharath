import streamlit as st

# Title of the app
st.title("BharathKumarReddy Reegatipalli Portfolio")
st.header("Welocme Reegatipalli")
# Add links to the sidebar
st.sidebar.header("Explore Projects")
st.sidebar.markdown(
    """
    - [Text to Text](https://text-to-text-description.streamlit.app/)
    - [Image to Text](https://image-to-text-description.streamlit.app/)
    - [Leetcode Profile](https://leetcode.com/u/BharathKumarReddy_Reegatipalli/)
    """
)

# Main content of the app
st.write("Welcome to the main content area of the app!")
st.write("You can use the sidebar to navigate to different pages or websites.")
