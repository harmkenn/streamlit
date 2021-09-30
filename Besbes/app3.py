# https://www.youtube.com/watch?v=hQnMV_bF84I
import streamlit as st

name = st.sidebar.text_input("Enter your name:","")
job = st.sidebar.text_area("What do you do?")
age = st.sidebar.number_input("Enter your age", min_value = 0, max_value = 100)
avail = st.sidebar.checkbox("Are you available for work?")
threshold = st.sidebar.slider("Pick a threshold:", min_value=1.0, max_value=100.0, value=50.0, step=.1)
sel = st.sidebar.selectbox("Pick", ("Item1", "Item2", "Item3"))

if name != "":
    st.markdown(f"""
        * Name: {name}
        * Job: {job}
        * Age: {age}
    """
    )

columns = st.columns((2,1))
with columns[0]:
    st.markdown(f"Name: {name}")
    st.markdown(f"Job: {job}")
    st.markdown(f"Age: {age}")

with columns[1]:
    st.markdown(f"Available for work: {avail}")
    
st.markdown("---")

container = st.container()

with container: 
    st.markdown("This is stuff in a container")

expander = st.expander("Expand")

with expander:
    st.info("The is information")
