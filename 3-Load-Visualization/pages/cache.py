import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Caching dengan Streamlit",
    layout="wide"
)

st.title("Test pencarian Data dengan Cache")

@st.cache_data(persist=True,show_spinner="Membaca file CSV...")
def load_data(path: str) -> pd.DataFrame:
    print("Membaca CSV...")
    return pd.read_csv(path)

@st.cache_data
def search_by_id(df: pd.DataFrame, id_value):
    print(f"Mencari ID: {id_value}")
    time.sleep(2)
    
    result = df[df["id"] == id_value]
    
    return result

df = load_data("./data/csv/sample-5mb.csv")

st.write(f"Jumlah data: {len(df)}")
id_input = st.number_input(
    "Masukkan ID yang ingin dicari",
    min_value=1,
    step=1
)

if st.button("Cari Data"):
    start_time = time.perf_counter()

    result = search_by_id(df, id_input)

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    st.write(f"**{execution_time:.2f} ms**")
    result = search_by_id(df, id_input)

    if result.empty:
        st.warning(f"Data dengan ID {id_input} tidak ditemukan.")
    else:
        st.success(f"Data dengan ID {id_input} ditemukan!")
        st.dataframe(result)