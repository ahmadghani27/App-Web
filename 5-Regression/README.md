# 5. Regression

Prediksi kalori terbakar dari jumlah langkah harian dengan Simple Linear Regression.

## Isi

| File | Isi |
|---|---|
| [`regression.py`](regression.py) | Aplikasi Streamlit. Input `st.slider` untuk jumlah langkah, model di-load pakai `joblib`, hasil prediksi dihitung dengan `numpy`. Ada juga halaman penjelasan singkat soal regresi linier sederhana. |
| [`linear_regression_stepstocal.pkl`](linear_regression_stepstocal.pkl) | Model terlatih, dipakai langsung oleh aplikasi. |
| [`Linear Regression.ipynb`](Linear%20Regression.ipynb) | Notebook training dan eksplorasi model. |
| [`Dataset/Activity.csv`](Dataset/Activity.csv) | Dataset pelatihan. |
| [`salary.csv`](salary.csv) | Dataset contoh tambahan. |

**Library:** `streamlit`, `scikit-learn`, `joblib`, `numpy`, `pandas`

## Cara Kerja

Variabel bebas $X$ = jumlah langkah, variabel terikat $Y$ = kalori terbakar.

## Dependensi

```bash
pip install streamlit scikit-learn joblib numpy pandas

# untuk notebook
pip install jupyter matplotlib seaborn
```

## Menjalankan

```bash
cd 5-Regression
streamlit run regression.py
```

Atau buka notebook-nya:

```bash
jupyter notebook "Linear Regression.ipynb"
```

> **Catatan:** model di-load dengan path relatif `./linear_regression_stepstocal.pkl`, jadi perintah `streamlit run` harus dijalankan **dari dalam folder ini**.
