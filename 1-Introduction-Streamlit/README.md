# 1. Introduction Streamlit

Latihan dasar komponen UI Streamlit: title, write, markdown, columns, metric, form input, dan sidebar.

## Isi

| File | Isi |
|---|---|
| [`main.py`](main.py) | Router halaman manual. `st.sidebar.selectbox` dipetakan ke dictionary berisi fungsi tiap halaman: halaman utama, halaman error 404, dan halaman dari `home.py`. |
| [`home.py`](home.py) | Demo komponen UI: `st.title`, `st.write`, `st.markdown`, `st.columns`, `st.metric`, `st.warning`/`st.info`, `st.expander`, plus input dasar (`checkbox`, `button`, `text_input`, `radio`). Ada juga `st.image` yang membaca gambar lewat Pillow. |
| [`multiPage.py`](multiPage.py) | Stub halaman kosong, tidak terpakai oleh `main.py`. |

**Library:** `streamlit`, `Pillow`

## Dependensi

```bash
pip install streamlit pillow
```

## Menjalankan

```bash
cd 1-Introduction-Streamlit
streamlit run main.py
```

Pilih halaman lewat sidebar: **Halaman utama**, **Kontak**, atau **Test**.

> **Catatan:** `home.py` memuat gambar dari path absolut lokal (baris 23). Ganti path tersebut jika folder asal berpindah.
