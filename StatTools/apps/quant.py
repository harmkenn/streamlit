# quant.py

import streamlit as st
import plotly_express as px
import pandas as pd

# title of the app
st.title("Python Stat Tools v1.0")
st.subtitle("by Ken Harmon")

# Add a sidebar
st.sidebar.subheader("Settings")

gs_URL = st.text_input("Public Google Sheet URL:") 
googleSheetId = gs_URL.split("spreadsheets/d/")[1].split("/edit")[0]
worksheetName = st.text_input("Sheet Name:","Sheet1")
URL = f'https://docs.google.com/spreadsheets/d/{googleSheetId}/gviz/tq?tqx=out:csv&sheet={worksheetName}'

@st.cache (ttl = 600)
def upload_gs(x):
    out = pd.read_csv(x)
    return out

df = upload_gs(URL)

global numeric_columns
global non_numeric_columns
try:
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")
    
# add a select widget to the side bar
chart_select = st.sidebar.selectbox(
    label="Select the chart type",
    options=['Histogram', 'Boxplot', "Dotplot","QQPlot"]
)

if chart_select == 'Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x = st.sidebar.selectbox('Feature', options=numeric_columns)
        bins = st.sidebar.slider("Number of Bins", min_value=1,
                                     max_value=40, value=7)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.histogram(x=x, data_frame=df, color=color_value, nbins=bins)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        y = st.sidebar.selectbox("Y axis", options=numeric_columns)
        x = st.sidebar.selectbox("X axis", options=non_numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.box(data_frame=df, y=y, x=x, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Dotplot':
    st.sidebar.subheader("Dotplot Settings")
    try:
        x = st.sidebar.selectbox('Feature', options=numeric_columns)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.do(x=x, data_frame=df, color=color_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

st.write(df)






