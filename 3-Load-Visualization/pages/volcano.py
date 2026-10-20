import streamlit as st
import pandas as pd

st.set_page_config(page_title="Volcanoes in Indonesia", layout="wide")

PATH = "./data/csv/indonesia_volcanoes.csv"


@st.cache_data(show_spinner=True)
def load_data(path):
    p = st.progress(0, "Memuat data")
    df = pd.read_csv(path)
    p.progress(50, "Memproses data")

    df["tinggi"] = pd.to_numeric(
        df["tinggi_meter"].str.extract(r"([\d.]+)")[0],
        errors="coerce"
    )

    c = df["geolokasi"].str.extract(
        r"([\d.]+)°([NS])\s+([\d.]+)°([EW])"
    )
    # 5.82°N 95.28°E
    # 5.82, N, 95.28, E

    df["lat"] = pd.to_numeric(c[0], errors="coerce")
    df["lon"] = pd.to_numeric(c[2], errors="coerce")

    df.loc[c[1] == "S", "lat"] *= -1
    df.loc[c[3] == "W", "lon"] *= -1

    df = df.dropna(subset=["lat", "lon"])

    p.progress(100, "Selesai")
    return df


def change_volcano():
    st.session_state.selected = st.session_state.volcano


df = load_data(PATH)

if "selected" not in st.session_state:
    st.session_state.selected = df.iloc[0]["nama"]

st.title("Gunung Berapi di Indonesia")
st.caption("Eksplorasi data gunung berapi berdasarkan bentuk, ketinggian, letusan terakhir, dan lokasi.")

st.subheader("Filter bentuk gunung")
bentuk = st.pills(
    "Pilih bentuk gunung",
    df["bentuk"].unique(),
    default=df["bentuk"].unique(),
    selection_mode="multi",
    label_visibility="collapsed"
)

data = df[df["bentuk"].isin(bentuk)]

a, b, c, d = st.columns(4)
a.metric("Total Gunung", len(data))
b.metric("Tertinggi", f"{data.tinggi.max():,.0f} m" if len(data) else "-")
c.metric("Rata-rata", f"{data.tinggi.mean():,.0f} m" if len(data) else "-")
d.metric("Jenis Bentuk", data.bentuk.nunique())

left, right = st.columns(2)

with left:
    st.subheader("Jumlah Berdasarkan Bentuk")
    st.bar_chart(data.bentuk.value_counts())

with right:
    st.subheader("Ketinggian Gunung")
    st.bar_chart(data.set_index("nama").tinggi.sort_values())

st.subheader("Persebaran Gunung")

if len(data):
    st.map(data[["lat", "lon"]], height=400)
else:
    st.warning("Tidak ada data yang sesuai.")

if len(data):
    st.subheader("Detail Gunung")

    names = data.nama.tolist()
    if st.session_state.selected not in names:
        st.session_state.selected = names[0]

    st.selectbox(
        "Pilih gunung",
        names,
        key="volcano",
        index=names.index(st.session_state.selected),
        on_change=change_volcano
    )

    v = data[data.nama == st.session_state.selected].iloc[0]

    x, y = st.columns([1, 2])

    with x:
        st.metric("Ketinggian", f"{v.tinggi:,.0f} m")
        st.write(f"Nama: {v.nama}")
        st.write(f"Bentuk: {v.bentuk}")
        st.write(f"Letusan terakhir: {v.estimasi_letusan_terakhir}")
        st.write(f"Geolokasi: {v.geolokasi}")

    with y:
        st.map(
            pd.DataFrame({"lat": [v.lat], "lon": [v.lon]}),
            zoom=8,
            height=300
        )
