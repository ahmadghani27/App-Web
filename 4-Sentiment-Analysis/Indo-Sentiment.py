import streamlit as st
import pandas as pd
import altair as alt
from transformers import pipeline
# Nama model yang digunakan
MODEL_NAME = "w11wo/indonesian-roberta-base-sentiment-classifier"

# Memuat model dengan caching
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model=MODEL_NAME)

# Mengubah hasil analisis menjadi DataFrame
def convert_to_df(result):
    # kolom "metric" berisi nama metrik, kolom "value" berisi nilai metrik
    return pd.DataFrame({
        "metric": ["label", "confidence"],
        "value": [str(result["label"]), float(result["score"])]
    })


# Menganalisis sentimen per token untuk mengetahui pengaruh tiap kata terhadap kalimat sentimen keseluruhan
def analyze_token_sentiment(text, classifier):
    # Tokenisasi tiap teks jadi kata2
    tokens = text.split()
    
    if len(tokens) <= 1:
        return pd.DataFrame(columns=["token", "sentiment", "impact"])

    # Untuk menyimpan hasil analisis sentimen
    original_result = classifier(text)[0]
    original_score = original_result["score"]
    modified_texts = []
    
    # Membuat teks modifikasi dengan menghapus satu token tiap iterasi untuk melihat pengarunya terhadap sentimen keseluruhan
    for i in range(len(tokens)):
        remaining = tokens[:i] + tokens[i + 1:]
        modified_texts.append(" ".join(remaining))
    batch_results = classifier(modified_texts)

    # Membandingkan skor sentimen asli dengan skor sentimen setelah token dihapus
    results = []
    for token, result in zip(tokens, batch_results):
        score_change = original_score - result["score"]
        # Terdapat dua kemungkinan
        if abs(score_change) > 0.05:
            sentiment = "Berpengaruh"
        else:
            sentiment = "Netral"
        
        # Hasilnya akan disimpan ke dictionary yang berisi token/kata, sentimennya, dan skor impact
        results.append({
            "token": token,
            "sentiment": sentiment,
            "impact": round(score_change, 4)
        })
                       
    # Ditampilkan menggunakan fungsi dataframe
    return pd.DataFrame(results)


# Fungsi utama untuk tampilan dan proses
def main():
    st.title("Sentiment Analysis NLP App")
    st.subheader("RoBERTa - Bahasa Indonesia")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

        classifier = load_model()

        with st.form("nlpForm"):
            raw_text = st.text_area("Masukkan Teks Bahasa Indonesia")
            submit_button = st.form_submit_button(label="Analyze")

            col1, col2 = st.columns(2)

            if submit_button and raw_text.strip():

                with col1:
                    st.info("Results")

                    result = classifier(raw_text)[0]
                    label = result["label"]
                    score = result["score"]

                    st.write({"sentiment": label, "confidence": score})

                    label_lower = label.lower()
                    if label_lower == "positive":
                        st.success("Positif")
                    elif label_lower == "negative":
                        st.error("Negatif")
                    else:
                        st.info("Netral")

                    result_df = convert_to_df({"label": label, "score": score})
                    st.dataframe(result_df)

                    conf_df = result_df[result_df["metric"] == "confidence"].copy()
                    chart = alt.Chart(conf_df).mark_bar().encode(
                        x=alt.X("metric", title=""),
                        y=alt.Y("value", scale=alt.Scale(domain=[0, 1]), title="Confidence"),
                        color=alt.value("#4CAF50" if label_lower == "positive"
                                        else "#F44336" if label_lower == "negative"
                                        else "#9E9E9E")
                    )
                    st.altair_chart(chart, use_container_width=True)

                with col2:
                    st.info("Token Sentiment")

                    token_results = analyze_token_sentiment(raw_text, classifier)

                    if token_results.empty:
                        st.warning("Teks terlalu pendek untuk dianalisis per token.")
                    else:
                        st.dataframe(token_results)

            elif submit_button:
                st.warning("Masukkan teks terlebih dahulu.")

    else:
        st.subheader("About")
        st.write("Aplikasi analisis sentimen Bahasa Indonesia menggunakan RoBERTa.")


if __name__ == "__main__":
    main()