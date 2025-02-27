import streamlit as st
from PIL import Image 


st.title("Hello word")

st.header("En este espacio comienzo a desarrollar mis apps de interfaces multimodales")
st.write("Facilmente puedo hacer backed y fortend")
image = Image.open("images.jpeg")

st.image(image, caption="Ay mi madre el bicho")

texto = st.text_input("El mejor jugador de la historia"," Un crack goles de cabeza, pierna derecha, pierna izquierda, alto, veloz, fuerte")
st.write("Esto es el fucking futbol",texto)

st.subheader("Ahora hay dos columnas")

col1,col2 = st.columns(2)

with col1:
  st.subheader("primera columna")
  st.write("Todo es mejor si programando estoy")
  respecto = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Buenisima")


