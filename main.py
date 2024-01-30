import streamlit as st
import plotly.express as px

st.title("Weather Forcast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                     ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2024-28-01", "2024-29-01", "2024-30-01"]
    temperature = [10, 11, 15]
    temperature = [days * i for i in temperature]
    return dates, temperature


d, t = get_data(days)

figure = px.line(x=d, y=t,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
