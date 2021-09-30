# https://www.youtube.com/watch?v=RHzjE-WBaSk&t=218s
import streamlit as st

name = st.text_input("Enter your name:","")
job = st.text_area("What do you do?")
age = st.number_input("Enter a number value", min_value = 0, max_value = 100)

if name != "":
    st.markdown(f"""
        * Name: {name}
        * Job: {job}
        * Age: {age}
    """
    )

avail = st.checkbox("Are you available for work?")
st.write(avail)

threshold = st.slider("Pick a threshold:", min_value=1.0, max_value=100.0, value=50.0, step=.1)
st.write(threshold)

sel = st.selectbox("Pick", ("Item1", "Item2", "Item3"))
st.write(sel)


