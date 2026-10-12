import streamlit as st
import home

def main_page():
    st.markdown("# :green[Halaman Utama]")
    
def error_page():
    st.title("404 not found")
    st.error("Halaman sedang tidak dapat diakses")

page_list = {
    "Halaman utama": main_page,
    "Kontak": error_page,
    "Test": home.home
}

selecte_page = st.sidebar.selectbox("Pilih halaman", page_list.keys())
page_list[selecte_page]()