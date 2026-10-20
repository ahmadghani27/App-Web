# 2. Multipage

Demo fitur **native multipage** Streamlit: satu file Python per halaman di dalam folder `pages/`, otomatis muncul di sidebar.

## Isi

| File | Isi |
|---|---|
| [`multiPage.py`](multiPage.py) | Halaman utama. Isinya cuma `st.title` dan `st.markdown`. |
| [`pages/about.py`](pages/about.py) | Halaman About, masih template judul. |
| [`pages/feature.py`](pages/feature.py) | Halaman Fitur, masih template judul. |
| [`pages/katalog.py`](pages/katalog.py) | Halaman Katalog, masih template judul. |

Tidak ada router di sini. Tiap file di dalam `pages/` otomatis jadi satu entri navigasi di sidebar.

**Library:** `streamlit`

## Dependensi

```bash
pip install streamlit
```

## Menjalankan

```bash
cd 2-Multipage
streamlit run multiPage.py
```

Semua halaman tampil di sidebar kiri. Isi tiap halaman masih berupa template buat diisi nanti.
