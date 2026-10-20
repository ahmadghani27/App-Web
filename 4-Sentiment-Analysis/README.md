# 4. Sentiment Analysis

Analisis sentimen NLP dengan Streamlit, ada dua versi: Bahasa Inggris dan Bahasa Indonesia.

## Isi

| File | Bahasa | Cara kerja |
|---|---|---|
| [`English-Sentiment.py`](English-Sentiment.py) | Inggris | `TextBlob` menghitung `polarity` dan `subjectivity`, lalu `vaderSentiment` memberi skor tiap kata. Hasilnya ditampilkan sebagai DataFrame dan bar chart `altair`. |
| [`Indo-Sentiment.py`](Indo-Sentiment.py) | Indonesia | Model RoBERTa `w11wo/indonesian-roberta-base-sentiment-classifier` lewat `transformers`, di-cache dengan `st.cache_resource`. Selain label dan confidence, ada analisis kontribusi tiap kata dengan cara menghapus kata lalu membandingkan skornya. |

Keduanya punya alur yang sama: input teks di `st.form`, hasil analisis di dua kolom, tabel metrik, grafik Altair, dan menu di sidebar.

**Library:** `streamlit`, `pandas`, `altair`, `textblob`, `vaderSentiment`, `transformers`

## Dependensi

```bash
pip install streamlit pandas altair

# untuk versi Inggris
pip install textblob vaderSentiment

# untuk versi Indonesia (butuh PyTorch)
pip install transformers torch
```

## Menjalankan

```bash
cd 4-Sentiment-Analysis

# Bahasa Inggris
streamlit run English-Sentiment.py

# Bahasa Indonesia
streamlit run Indo-Sentiment.py
```

> **Catatan:** `Indo-Sentiment.py` mengunduh model RoBERTa (sekitar 400 MB) saat pertama dijalankan, jadi butuh koneksi internet.
>
> **Catatan:** di `English-Sentiment.py`, blok `About` (baris 50 sampai 51) salah indentasi sehingga berada di dalam `if choice == "Home"`. Pindahkan ke luar blok `if` agar menu About berfungsi.
