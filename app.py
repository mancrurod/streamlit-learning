import streamlit as st

st.set_page_config(page_title="Tasador", page_icon=":shark:")

st.title("🏠 Predicción de precios de pisos")

tab1, tab2 = st.tabs(["Resumen", "Contacto"])

with tab1:
    st.subheader("Resumen del proyecto")
    st.write("Este proyecto predice precio de pisos en Madriz (como siempre).")

with tab2:
    st.subheader("Contacto")
    st.write("Autor: Manué")
    st.write("Correo: pimpamarrobagemail.com")