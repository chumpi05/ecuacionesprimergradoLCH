import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="🧮")

st.title("🧮 Práctica de Ecuaciones de Primer Grado")

# Generar un nuevo ejercicio
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(1, 10)
    st.session_state.x = random.randint(1, 10)
    st.session_state.c = st.session_state.a * st.session_state.x + st.session_state.b

def nuevo_ejercicio():
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(1, 10)
    st.session_state.x = random.randint(1, 10)
    st.session_state.c = st.session_state.a * st.session_state.x + st.session_state.b

# Mostrar la ecuación
st.latex(f"{st.session_state.a}x + {st.session_state.b} = {st.session_state.c}")

# Entrada del usuario
respuesta = st.number_input("✍️ Escribe el valor de x:", step=1)

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Verificar respuesta"):
        if respuesta == st.session_state.x:
            st.success("🎉 ¡Correcto!")
        else:
            st.error(f"❌ Incorrecto. La respuesta correcta es x = {st.session_state.x}")

with col2:
    if st.button("🔄 Nuevo ejercicio"):
        nuevo_ejercicio()
        st.rerun()
