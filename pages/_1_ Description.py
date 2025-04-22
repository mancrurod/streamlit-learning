import streamlit as st

st.title("Descripción de los datos")
st.markdown(
    """
    Este conjunto de datos simula las características de pisos en una ciudad.

    - **metros_cuadrados**: tamaño del piso en metros cuadrados (int)
    - **habitaciones**: número de habitaciones (int)
    - **baños**: número de baños (int)
    - **garaje**: si tiene (1) o no (0) garaje (booleano)
    - **antigüedad**: antigüedad del piso en años (int)
    - **precio**: precio del piso en euros (float)
    - etc.
    """
)