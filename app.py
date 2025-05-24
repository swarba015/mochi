import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1x4mi-F7JHJSgFLCzaBYEj6rEtl62UCPkXpc_YX4NDXY/edit?gid=0#gid=0").sheet1


st.set_page_config(page_title = 'Moods', layout = 'centered') #configuring streamlit
st.title('moods')


st.header('Log Mood')

mood = st.selectbox("Mood", ["😊 Happy", "😠 Frustrated", "😕 Confused", "🎉 Celebrating"])
note = st.text_input("Optional note")


if st.button('Submit'):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([now, mood, note])
    st.success('Logged!')
   



st.header('Today Mood Summary')

try:
    df = pd.DataFrame(sheet.get_all_records())
    df.columns = [col.strip().lower() for col in df.columns]
    
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors='coerce')
    df = df.dropna(subset=["timestamp"])

    #st.subheader("Raw Sheet Data")
    #st.dataframe(df)  
    today = pd.Timestamp.now().normalize()
    df_today = df[df["timestamp"] >= today]

    if df_today.empty:
        st.info("No moods logged today.")
    else:
        mood_summary = df_today["mood"].value_counts().reset_index()
        mood_summary.columns = ["Mood", "Count"]
        fig = px.bar(mood_summary, x="Mood", y="Count", title="Mood Count Today", color="Mood", text="Count")
        st.plotly_chart(fig)

except Exception as e:
    st.error(f"Failed to load data: {e}")
