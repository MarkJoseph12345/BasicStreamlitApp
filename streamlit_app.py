import streamlit as st
from PIL import Image

st.set_page_config(page_title="Basic Streamlit App", page_icon="🧑‍🚀")

tab1, tab2, tab3, = st.tabs(["Home", "About Me", "Links"])

with tab1:
    st.header("Home")
    st.write("Basic Streamlit App Act 1")
    st.markdown(
        """
        Welcome to my website, it doesn't have much for now but i will fill it in the future with stuff and projects and redesign.
        """
    )

with tab2:
    st.header("About Me")
    st.markdown(
        """
        Hi I'm Mark Joseph Piodos, an IT Student in CIT-U.
        
        I live in Tuyom, Carcar City, Cebu.
        
        I like space and amazing sceneries like it.
        
        Languages I've learned or have basic knowledge:
        - **C++**
        - **Kotlin**
        - **Python**
        - **Java**
        - **JavaScript**
        - **TypeScript**
        """
    )
    image = Image.open("images/astro.jpg")
    st.image(image, caption='Astro', use_column_width=True)

with tab3:
    st.header("Links")
    st.markdown(
    """
    - <a href="https://github.com/MarkJoseph12345">
        <img src="https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg" style="height: 30px; vertical-align: middle;" />
      Github
      </a> 
    - <a href="https://www.kaggle.com/markjosephpiodos">
        <img src="https://www.kaggle.com/static/images/site-logo.svg" style="height: 20px; vertical-align: middle;" />
      </a> 
    """,
    unsafe_allow_html=True
)