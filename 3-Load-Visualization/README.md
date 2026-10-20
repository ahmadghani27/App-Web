# 3. Load & Visualization

Latihan membaca data CSV dan menampilkannya: caching, progress bar, session state, peta, dan grafik.

## Isi

[`main.py`](main.py) cuma jadi halaman indeks. Materi utamanya ada di folder [`pages/`](pages/):

| Halaman | Materi |
|---|---|
| [`cache.py`](pages/cache.py) | `st.cache_data(persist=True)` mempercepat pembacaan CSV 5 MB, plus `time.perf_counter()` untuk mengukur lama eksekusi. |
| [`progress_bar.py`](pages/progress_bar.py) | `st.progress` dan `time.sleep` sebagai simulasi proses loading. |
| [`session.py`](pages/session.py) | `st.session_state` menyimpan input dan hasil pencarian antar rerun. Callback dipasang lewat `on_click` pada `st.button` dan `on_change` pada `st.radio`. |
| [`uber.py`](pages/uber.py) | Dataset Uber NYC dari URL publik. Histogram per jam pakai `np.histogram` dan `st.bar_chart`, sebaran lokasi di `st.map` yang difilter `st.slider`. |
| [`volcano.py`](pages/volcano.py) | Data gunung berapi Indonesia. Ketinggian dan koordinat diambil dari teks pakai regex, lalu ditampilkan sebagai metric, bar chart, dan `st.map`. Filter pakai `st.pills`. |

Data ada di [`data/csv/`](data/csv/): `sample-5mb.csv` dan `sample-simple.csv` untuk halaman cache dan session, `indonesia_volcanoes.csv` untuk halaman volcano.

**Library:** `streamlit`, `pandas`, `numpy`

## Dependensi

```bash
pip install streamlit pandas numpy
```

## Menjalankan

```bash
cd 3-Load-Visualization
streamlit run main.py
```

Buka halaman lewat sidebar: cache, progress bar, session, uber, volcano.

> **Catatan:** `uber.py` mengunduh dataset dari S3, jadi butuh koneksi internet saat pertama dibuka.
