import streamlit as st
from PIL import Image 

set_mod=""
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
  if respecto:
    st.write("Buenisima")

with col2:
  st.subheader("Segunda columna")
  modo = st.radio("Tu que prefieres backed o fronted",("backend","fronted","ninguna"))
  if modo == "backend":
    st.write("Eres de los mios siuuuuuu")
  if modo == "fronted":
    st.write("Eres una mierda gasss")
  if modo == "ninguna":
    st.write("Que estas haciendo aqui entonces")

st.subheader("uso de botones")
in_mod = st.selectbox(
  "selección de la modalidad",
  ("Audío","Visual","Haptico"),
)
if in_mod == "Audio":
  set_mod= "reproducion audio"
elif in_mod == "Visual":
  set_mod = "Reproducir video"
elif in_mod == "Haptico":
  set_mod = "Activar vibracion"
  
st.write("la accion es:",set_mod)
    
   


