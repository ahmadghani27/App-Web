# App Web (Aplikasi Web)

 **Repositori ini adalah ruang latihan dan eksperimen** dalam mempelajari pengembangan aplikasi web berbasis Streamlit. Jadi, seluruh kode di sini adalah adalah hasil praktik bukan untuk lingkungan produksi (production-ready).


---

## Daftar Materi

| Folder | Materi |
|---|---|
| [**1. Introduction Streamlit**](1-Introduction-Streamlit/) | Pengena0lan Streamlit: komponen UI dasar (`title`, `write`, `markdown`, `columns`, `metric`, input form) dan navigasi halaman manual pakai `selectbox`. |
| [**2. Multipage**](2-Multipage/) | Fitur native multipage Streamlit. Satu file Python per halaman di folder `pages/`, otomatis masuk sidebar. |
| [**3. Load & Visualization**](3-Load-Visualization/) | Membaca data CSV, caching (`st.cache_data`), progress bar, `session_state` + callback, hingga visualisasi peta dan grafik. |
| [**4. Sentiment Analysis**](4-Sentiment-Analysis/) | Analisis sentimen NLP dalam dua bahasa: Inggris (`TextBlob` + `VADER`) dan Indonesia (RoBERTa via `transformers`). |
| [**5. Regression**](5-Regression/) | Simple Linear Regression dengan scikit-learn: prediksi kalori terbakar dari jumlah langkah harian, lengkap dengan notebook training. |
| [**6. Scrapping & Clustering**](6-Scrapping-Clustering/) | Project akhir: dashboard sentimen tweet F1 Sepang dengan TF-IDF, K-Means clustering, PCA, dan WordCloud. |


---

## Setup

Semua latihan memakai Python 3.12 dan `.venv` sebagai virtual environment.

### 1. Buat virtual environment

Dari folder root repositori ini:

**PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**CMD**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

Kalau PowerShell menolak menjalankan script aktifasi karena execution policy, jalankan ini sekali saja:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Cek Python di dalam venv:

```bash
python --version
```

### 2. Install dependensi

```bash
pip install -r requirements.txt
```

Isi [`requirements.txt`](requirements.txt) sudah mencakup semua library yang dipakai di folder 1 sampai 6, termasuk `torch` untuk model RoBERTa di folder 4.

### 3. Jalankan aplikasi

Setiap folder punya aplikasi Streamlit sendiri. Masuk dulu ke foldernya, baru jalankan:

```bash
cd 1-Introduction-Streamlit
streamlit run main.py
```

Contoh lain:

```bash
cd 6-Scrapping-Clustering
streamlit run ../6-Scrapping-Clustering/app.py
```

Tiap folder punya `README.md` sendiri yang menjelaskan isi, dependensi, dan cara menjalankannya lebih rinci. Lihat langsung di masing-masing folder.

---

## Catatan

Beberapa folder punya hal yang perlu diperhatikan sebelum dijalankan, misalnya path file dan ukuran model. Detailnya ada di `README.md` tiap folder.
