import streamlit as st
from PIL import Image

def home():
    st.title("Test Title")
    st.write("Kalau ini test st.write")
    st.markdown("`Test warna pakai` :yellow[***MD***]")
    col1, col2, col3 = st.columns(3)
    col1.warning("Peringatan")
    col2.metric(label="stonk", value=101, delta=99)
    col3.info("[Streamlit docs](https://docs.streamlit.io).")
    st.caption("Caption Test")


    col11, col22, col33, col44 = st.columns(4)
    col11.checkbox("Setuju?")
    col22.button("**Klik**")
    col33.text_input(label="Input")
    col44.radio("Pilih", ["**A**", "*B*"])

    st.expander("Klik untuk ...  **detail tambahan**")
    st.sidebar.markdown("### Navbar")
    img = Image.open('D:\SEMESTER 5\Aplikasi_Web\m1\streamlit\gambar.png')
    st.image(img, caption='ini gamabar')