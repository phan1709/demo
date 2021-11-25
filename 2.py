import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from ipywidgets import widgets
df = pd.read_excel (r'F:\THD\Demo\demo.xlsx', sheet_name='Nhân sự CT')
print(df)
import streamlit as st
#Mainpage
st.set_page_config(page_title="Phan Tuan Anh",page_icon=":imp:",layout="wide")
#Sidebar
st.sidebar.header("Hiệu suất NS")
Ban = st.sidebar.multiselect("Ban",
                       options=df['Ban'].unique(),
                       default=df['Ban'].unique())
NS = st.sidebar.multiselect("NS",
                       options=df['NS'].unique(),
                       default=df['NS'].unique())
Loại =  st.sidebar.multiselect("Loại NS",
                       options=df['Loại'].unique(),
                       default=df['Loại'].unique())
Status = st.sidebar.multiselect("Status",
                       options=df['Status'].unique(),
                       default=df['Status'].unique())
df_selection = df.query(
    "Ban == @Ban & NS ==@NS & Loại ==@Loại & Status == @Status"
)
st.dataframe(df_selection)
# ---- MAINPAGE ----
st.title(":bar_chart: Hiệu suất NS")
st.markdown("##")
#chart
pio.templates.default = "presentation"
abc_bar = px.bar(data_frame=df, x= 'NS', y= 'HS',color="NS",color_discrete_sequence=px.colors.qualitative.G10)
#linechart

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
#plot!!
st.plotly_chart(abc_bar, use_container_width=True)
