# https://www.youtube.com/watch?v=wDysPcF0Hbc
import streamlit as st
import pandas as pd
st.title("My Streamlit App")
st.header("A Machine Learning app")
st.subheader("Built by Ken Harmon")
st.markdown("This is the description")
st.markdown("Out of the box, a typical web app created using Streamlit is a one page app. In this video, I will be showing you how you can make a multi-page web app in Streamlit. How useful is a multiple page web app? Well, there are many uses for it such as separating the contents of the app into self-contained and organized topics.")
st.markdown("*This is italics*")
st.markdown("**This is Bold**")
st.markdown("* This is a bullet")
st.info("This is information")
st.warning("This is a Warning")
st.error("This is an Error")

iris_data = pd.read_csv("./data/iris.csv")

st.write(iris_data)








