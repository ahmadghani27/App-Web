import os
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

import nltk
nltk.download('stopwords')

from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# CONFIG & PAGE SETUP
st.set_page_config(
    page_title="Dashboard Analisis Sentimen dataset F1_Sepang_Circuit", layout="wide"
)

st.title("Dashboard Analisis Sentimen & Clustering (F1_Sepang_Circuit)")
st.caption(
    "Aplikasi berbasis Streamlit untuk analisis sentimen Twitter dan K-Means Topic Clustering."
)

# LOAD DATA & MODEL (CACHED)
DATA_PATH = "./tm5/data_scrap/F1_Sepang_Labeled.csv"
MODEL_PATH = "./tm5/model/model_F1_Sepang.joblib"

# STOPWORDS
stop_words = set(stopwords.words('english'))
additional = {
    'sepang', 'circuit', 'f1', 'formula1', 'formula', 'gp', 'grand', 'prix',
    'malaysia', 'malaysiangp', 'malaysian', 'bahrain', 'sic', 'malay',
    'amp', 'rt', 'via', 'tweet', 'twitter', 'https', 'http', 'com', 'www',
    'dm', 'link', 'pic', 'photo', 'video', 'f'
}
keep = {
    'no', 'nor', 'not', 'never', 'none', 'neither', 'cannot', 'cant'
}

final_stopwords = list((stop_words | additional) - keep)


@st.cache_data
def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    else:
        return pd.DataFrame(
            {
                "full_text": ["sample tweet 1", "sample tweet 2"],
                "sentiment": ["neutral", "negative"],
            }
        )

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None


df = load_data()
model = load_model()

# SIDEBAR NAVIGATION
menu = st.sidebar.radio(
    "Pilih Halaman:",
    [
        "Overview",
        "Uji Prediksi Model",
    ],
)

if menu == "Overview":
    st.header("Overview Dataset X (F1_Sepang_Circuit)")
    st.write(f"Total Data Terkumpul: **{len(df)}** baris")
    
    st.markdown("---")

    st.subheader("Sampel Data")
    def color_sentiment(row):

        if row['sentiment'] == 'positive':
            color = 'background-color: rgba(76, 175, 80, 0.25)' 
        elif row['sentiment'] == 'negative':
            color = 'background-color: rgba(244, 67, 54, 0.25)' 
        else:
            color = 'background-color: rgba(158, 158, 158, 0.20)'
        
        return [color] * len(row)

    styled_df = df.style.apply(color_sentiment, axis=1)

    st.dataframe(styled_df, use_container_width=True, height=400)
    
    st.markdown("---")

    st.header("Distribusi Sentimen (RoBERTa Auto-Labeling)")
    st.markdown("Model : '''cardiffnlp/twitter-roberta-base-sentiment-latest'''")

    if "sentiment" in df.columns:
        sentiment_counts = df["sentiment"].value_counts()
        colors = ["red", "green", "blue"]

        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Ringkasan Angka")
            st.dataframe(
                pd.DataFrame(
                    {
                        "Jumlah": sentiment_counts,
                        "Persentase (%)": (
                            sentiment_counts / len(df) * 100
                        ).round(2),
                    }
                )
            )

        with col2:
            fig, ax = plt.subplots(figsize=(8, 2))
    
            palette = ['red', 'green', 'blue']
            colors = palette[:len(sentiment_counts)]

            bars = ax.bar(sentiment_counts.index, sentiment_counts.values, color=colors)

            ax.set_xlabel('Sentiment')
            ax.set_ylabel('Count')
            ax.set_title('Sentiment Distribution')
            ax.set_xticks(range(len(sentiment_counts)))
            ax.set_xticklabels(sentiment_counts.index, rotation=0)

            for bar in bars:
                height = bar.get_height()
                if height > 0:
                    ax.text(
                        bar.get_x() + bar.get_width() / 2,
                        height / 2,
                        str(int(height)),
                        fontsize=12,
                        fontweight='bold',
                        color='white',
                        ha='center',
                        va='center'
                    )

            st.pyplot(fig)
        
        st.markdown("---")
        
        # wordcloud
        st.subheader("WordCloud Kata Utama")

        data_text = " ".join(df["full_text"].fillna("").astype(str).tolist())

        wc = WordCloud(
            stopwords=final_stopwords,
            width=1000,
            height=400,
            background_color="white",
        ).generate(data_text)

        fig_wc, ax_wc = plt.subplots(figsize=(10, 4))
        ax_wc.imshow(wc, interpolation="bilinear")
        ax_wc.axis("off")
        st.pyplot(fig_wc)

        st.markdown("---")

        # top 12 kata
        st.subheader("12 Kata yang Sering Muncul")

        text = " ".join(df["full_text"].fillna("").astype(str).tolist())
        words = [
            word
            for word in text.split()
            if word.lower() not in final_stopwords
        ]

        word_counts = Counter(words)
        top_words = word_counts.most_common(12)

        if top_words:
            words_list, counts = zip(*top_words)

            colors_bar = plt.cm.Paired(range(len(words_list)))

            fig_bar, ax_bar = plt.subplots(figsize=(10, 4))
            bars = ax_bar.bar(words_list, counts, color=colors_bar)

            ax_bar.set_ylabel("Frekuensi")
            ax_bar.set_title("12 Kata yang Sering Muncul")
            ax_bar.set_xticks(range(len(words_list)))
            ax_bar.set_xticklabels(words_list, rotation=45)

            for bar, num in zip(bars, counts):
                ax_bar.text(
                    bar.get_x() + bar.get_width() / 2,
                    num + 1,
                    str(num),
                    fontsize=12,
                    color="black",
                    ha="center",
                )

            st.pyplot(fig_bar)    
        else:
            st.warning("Kolom 'sentiment' tidak ditemukan di CSV.")
            
    st.markdown("---")
        
    st.header("Visualisasi Clustering K-Means Data Riil (Centroid 0–6)")

    if not df.empty and "full_text" in df.columns:
        texts = df["full_text"].fillna("").astype(str).tolist()
        
        vectorizer = TfidfVectorizer(
            stop_words=final_stopwords,
            max_df=0.85,
            min_df=2,
            ngram_range=(1, 2),
            sublinear_tf=True
        )
        X = vectorizer.fit_transform(texts)

        kmeans = KMeans(n_clusters=6, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)
        centroids = kmeans.cluster_centers_

        pca = PCA(n_components=2, random_state=42)
        reduced_features = pca.fit_transform(X.toarray())
        reduced_centroids = pca.transform(centroids)

        # 4. Visualisasi Plot
        fig, ax = plt.subplots(figsize=(10, 4))

        ax.scatter(
            reduced_features[:, 0],
            reduced_features[:, 1],
            c=labels,
            cmap="tab10",
            alpha=0.5,
        )

        for i, (x, y) in enumerate(reduced_centroids):
            ax.text(
                x,
                y,
                str(i+1),  
                color="white",
                fontsize=10,
                fontweight="light",
                ha="center",
                va="center",
                bbox=dict(
                    boxstyle="circle,pad=0.1", fc="black", alpha=0.3
                ),
            )

        ax.set_title("Visualisasi Clustering KMeans Data F1 Sepang")
        ax.set_xlabel("PCA Component 1")
        ax.set_ylabel("PCA Component 2")

        st.pyplot(fig)
        
        st.markdown("---")

        st.subheader("Kata Kunci Utama tiap Cluster")
        order_centroids = centroids.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()

        for row in range(3):
            col1, col2 = st.columns(2)
            
            idx_left = row * 2
            top_terms_left = [terms[ind] for ind in order_centroids[idx_left, :20]]
            with col1:
                with st.container(border=True):
                    st.markdown(f"### Cluster {idx_left + 1}")
                    st.write(", ".join(top_terms_left))

            idx_right = row * 2 + 1
            top_terms_right = [terms[ind] for ind in order_centroids[idx_right, :20]]
            with col2:
                with st.container(border=True):
                    st.markdown(f"### Cluster {idx_right + 1}")
                    st.write(", ".join(top_terms_right))
    else:
        st.error("Kolom 'full_text' tidak ditemukan dalam file CSV Anda.")

elif menu == "Uji Prediksi Model":
    st.header("Live Text Sentiment Prediction")

    if model is None:
        st.error(f"File model tidak ditemukan di `{MODEL_PATH}`.")
    else:
        user_input = st.text_area(
            "Masukkan teks tweet untuk diuji sentimennya:",
            "Max Verstappen got pole position at Sepang Circuit!",
        )

        if st.button("Prediksi Sentimen"):
            if user_input.strip() != "":
                prediction = model.predict([user_input])[0]

                if str(prediction).lower() == "positive":
                    st.success(f"Hasil Prediksi: **{str(prediction).upper()}**")
                elif str(prediction).lower() == "negative":
                    st.error(f"Hasil Prediksi: **{str(prediction).upper()}** ")
                else:
                    st.info(f"Hasil Prediksi: **{str(prediction).upper()}** ")

                classes = list(model.classes_) 
                probs = model.predict_proba([user_input])[0]  

                prob_dict = {str(cls).lower(): prob for cls, prob in zip(classes, probs)}

                pos_score = prob_dict.get("positive", 0.0) * 100
                neu_score = prob_dict.get("neutral", 0.0) * 100
                neg_score = prob_dict.get("negative", 0.0) * 100

                st.write("") 

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.caption("Positive")
                    st.subheader(f"{pos_score:.1f}%")

                with col2:
                    st.caption("Neutral")
                    st.subheader(f"{neu_score:.1f}%")

                with col3:
                    st.caption("Negative")
                    st.subheader(f"{neg_score:.1f}%")

            else:
                st.warning("Mohon masukkan teks terlebih dahulu.")