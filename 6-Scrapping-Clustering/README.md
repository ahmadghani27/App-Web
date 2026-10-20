# 6. Scrapping & Clustering

Dashboard analisis sentimen dan topic clustering dari data tweet tentang F1 Malaysian Grand Prix di Sirkuit Sepang.

## Isi

[`app.py`](app.py) satu-satunya file aplikasi, tapi isinya padat. Stopwords bahasa Inggris dari `nltk` digabung dengan kata khusus domain (sepang, f1, malaysian gp, dan sejenisnya), sementara negasi seperti `not` dan `never` sengaja tidak dibuang. Pembacaan data dan model dibungkus `st.cache_data` dan `st.cache_resource`.

Halaman **Overview** berisi:

- Jumlah data dan sampel tweet yang diwarnai per sentimen (`df.style.apply`)
- Distribusi sentimen berupa tabel persentase dan bar chart `matplotlib`
- WordCloud dan 12 kata paling sering muncul (`collections.Counter`)
- Clustering `KMeans` 6 cluster di atas matriks TF-IDF, direduksi jadi 2 dimensi pakai `PCA`, lalu digambar sebagai scatter plot beserta centroidnya
- Kata kunci utama tiap cluster

Halaman **Uji Prediksi Model**: input teks bebas di `st.text_area`, lalu model memberi label beserta probabilitas positive, neutral, dan negative.

| Folder | Isi |
|---|---|
| [`data_scrap/`](data_scrap/) | Progres data: hasil scrapping, versi bersih, versi berlabel sentimen (yang dipakai aplikasi), dan gabungannya. |
| [`model/`](model/) | `model_F1_Sepang.joblib`, model klasifikasi sentimen terlatih. |
| [`img/`](img/) | Screenshot pendukung. |

**Library:** `streamlit`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `nltk`, `wordcloud`, `scikit-learn`, `joblib`

## Dependensi

```bash
pip install streamlit pandas numpy matplotlib seaborn nltk wordcloud scikit-learn joblib
```

## Menjalankan

```bash
cd <folder induk>
streamlit run 6-Scrapping-Clustering/app.py
```

> **Penting:** `app.py` memakai path `./tm5/data_scrap/...` dan `./tm5/model/...` (baris 30 sampai 31), jadi folder ini perlu bernama **`tm5`** dan aplikasi dijalankan dari direktori induknya. Kalau nama folder tetap `6-Scrapping-Clustering`, ubah kedua path itu jadi `./6-Scrapping-Clustering/data_scrap/...` dan `./6-Scrapping-Clustering/model/...`.
>
> Aplikasi tetap jalan walau file tidak ditemukan. Ia akan memakai data dan model contoh, lalu menampilkan pesan error di halaman prediksi.
