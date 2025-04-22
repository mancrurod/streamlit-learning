import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

data = pd.read_csv("data/pisos.csv")
centro = [data["lat"].mean(), data["lon"].mean()]

# Folium > Map > Marker > Layer > Icon --> Iremos instanciando el mapa y añadiendo los marcadores
lat = 40.402924
lon = -3.69730

m = folium.Map(location=(lat,lon), zoom_start=15)

# icon
icon = folium.Icon(icon="umbrella-beach", prefix="fa", color="blue")
marker = folium.Marker(location=(lat, lon),
                       icon=icon)
marker.add_to(m)

# pin

def create_marker(row):

    dict_color = {
        "Norte": "blue",
        "Centro": "black",
        "Este": "red",
        "Sur": "purple",
        "Oeste": "green"
    }

    icon = folium.Icon(icon="umbrella-beach", prefix="fa", color=dict_color[row["barrio"]])

    marker = folium.Marker(location=(row["lat"],row["lon"]),
                           icon=icon)
    marker.add_to(m)

for _, row in data.iterrows():
    create_marker(row)

st_folium(m, width=800, height=600)