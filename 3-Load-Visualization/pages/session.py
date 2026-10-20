import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Session dan Callback",
    layout="wide"
)

st.title("Test Session State dan Callback")

df = pd.read_csv("./data/csv/sample-5mb.csv")
if "input_id" not in st.session_state:
    st.session_state.input_id = 1

if "last_search_id" not in st.session_state:
    st.session_state.last_search_id = None

if "selected_column" not in st.session_state:
    st.session_state.selected_column = "id"

if "result" not in st.session_state:
    st.session_state.result = pd.DataFrame()

def search_data():
    st.session_state.last_search_id = st.session_state.input_id
    st.session_state.result = df[
        df["id"] == st.session_state.input_id
    ]

def change_column():
    st.session_state.selected_column = (
        st.session_state.column_radio
    )

st.number_input(
    "Masukkan ID:",
    min_value=1,
    step=1,
    key="input_id"
)

st.button(
    "Cari Data",
    on_click=search_data
)

st.radio(
    "Tampilkan data:",
    ["id", "email", "age", "salary"],
    key="column_radio",
    on_change=change_column
)
if not st.session_state.result.empty:
    st.write(
        f"ID terakhir dicari: "
        f"**{st.session_state.last_search_id}**"
    )
    st.dataframe(
        st.session_state.result[
            [st.session_state.selected_column]
        ],
        use_container_width=True
    )

else:
    st.info("Silakan cari ID terlebih dahulu.")
