import streamlit as st
import random
import time

st.set_page_config(page_title="🤖 Mancuerna vs Barra", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4500;'>🤖 Mancuerna vs Barra</h1>", unsafe_allow_html=True)
st.markdown("### Dos robots entran al ring... ¡solo uno gana el derecho a entrenar hoy! 🥊")

# Imagen de introducción
st.image("pelea.gif", use_container_width=True)

# Iniciar batalla
if st.button("🔥 Iniciar pelea"):
    st.markdown("### ⏳ ¡Batalla en curso!")
    with st.spinner("⚔️ Los robots están peleando..."):
        time.sleep(2.5)

    ganador = random.choice(["Mancuerna", "Barra"])
    st.markdown("### ✨ ¡Resultado!")

    if ganador == "Mancuerna":
        st.image("mancuerna_gana.png", caption="💪 ¡Mancuerna gana!", use_container_width=True)
        st.success("🏆 Hoy toca entrenar con **MANCUERNA**")
    else:
        st.image("Barra gana.png", caption="🏋️‍♂️ ¡Barra gana!", use_container_width=True)
        st.success("🏆 Hoy toca entrenar con **BARRA**")

    st.balloons()

# 🔁 Botón para volver a empezar
if st.button("🔁 Jugar otra vez"):
    st.rerun()

