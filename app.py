import streamlit as st

# Title of the app
st.title("BharathKumarReddy Reegatipalli Portfolio")
st.header("Welocme Reegatipalli")
# Add links to the sidebar
st.sidebar.header("Explore Projects")
st.sidebar.markdown(
    """
    - [Google](https://www.google.com)
    - [OpenAI](https://www.openai.com)
    - [Streamlit Documentation](https://docs.streamlit.io)
    """
)

# Main content of the app
st.write("Welcome to the main content area of the app!")
st.write("You can use the sidebar to navigate to different pages or websites.")
