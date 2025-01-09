import streamlit as st
import pandas as pd
import json
import requests

st.title('Weather Dashboard')
st.subheader('Hi! Welcome to my Wheather Dashboard :)')
Latitude=st.sidebar.number_input('Enter Latitude',value=0.0) 
Longitude=st.sidebar.number_input('Enter Longitude',value=0.0)
api_url= f'https://api.open-meteo.com/v1/forecast?latitude={Latitude}&longitude={Longitude}&current=temperature_2m,is_day,rain,wind_direction_10m&hourly=temperature_2m,relative_humidity_2m,rain,showers,wind_speed_80m,wind_direction_80m&timezone=auto'
resp=requests.get(api_url)
value=json.loads(resp.text)
st.image('https://miro.medium.com/v2/resize:fit:1400/1*ceM2qkdwPB8EqrZACxd87Q.jpeg')
# st.video('https://youtu.be/3hXSgRSIHMU?si=waPQCLnQY5tjIvOS')
st.sidebar.write('Click on the link below to find the longitude and latitude value or seach on google')
st.sidebar.write('https://www.latlong.net')
temp=value['current']['temperature_2m']
day_night=value['current']['is_day']
rain=value['current']['rain']
wind_direc=value['current']['wind_direction_10m']
def Day_Night():
    return 'Day' if day_night == 1 else 'night'  
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric('Day or Night',Day_Night())   
with col2:
    st.metric('Temperature(°C)',temp)
with col3:
    st.metric('Rain(mm)',rain)
with col4:
    st.metric('Wind Direction',wind_direc)  
selectbox_option=st.sidebar.selectbox(
    'Select data to visualize',
    ('Relative Humidity','Showers','Wind Speed')
)   
xy=pd.DataFrame(value['hourly']['relative_humidity_2m'],
                                               value['hourly']['time'])
bc=pd.DataFrame(value['hourly']['showers'],
                                               value['hourly']['time'])
ad=pd.DataFrame(value['hourly']['wind_speed_80m'],
                                               value['hourly']['time'])
if selectbox_option == 'Relative Humidity':
    st.line_chart(xy)
elif selectbox_option == 'Showers':
    st.line_chart(bc)
else: 
    st.line_chart(ad)


