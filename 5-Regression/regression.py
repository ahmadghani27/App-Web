import streamlit as st
import sklearn
import joblib
import os
import numpy as np 

# Function untuk meload model
def load_prediction_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

def main():
    """Simple Linear Regression - Steps to Calories"""
    st.title("Prediksi Kalori Terbakar") 
    html_templ = """
    <div style="background-color:#4CAF50;padding:10px;border-radius:5px;">
    <h3 style="color:white;text-align:center;">Prediksi Pembakaran Kalori Menggunakan Regresi Linier</h3>
    </div>
    <br>
    """
    st.markdown(html_templ, unsafe_allow_html=True)
    activity = ["Prediksi Kalori", "Apa itu Regresi?"]
    choice = st.sidebar.selectbox("Menu", activity)

    #Prediksi Kalori
    if choice == 'Prediksi Kalori':
        st.subheader("Hitung Estimasi Pembakaran Kalori")
        # Step input slider (range: 500 to 35,000 steps)
        steps = st.slider("Berapa jumlah langkah harianmu?", min_value=500, max_value=35000, value=500, step=1)
        if st.button("Proses"):
            # Load model 
            regressor = load_prediction_model("./linear_regression_stepstocal.pkl")
            # Ubah input ke 2D array [[steps]]
            steps_reshaped = np.array(steps).reshape(-1, 1)
            # Buat predksi
            predicted_calories = regressor.predict(steps_reshaped)
            cal_value = float(np.ravel(predicted_calories)[0])
            st.success(f"Estimasi kalori yang terbakar untuk **{steps:,}** langkah adalah **{cal_value:,.2f} kcal**")

    # Penjelasan
    elif choice == 'Apa itu Regresi?':
        st.subheader("Tentang Regresi Linier Sederhana")
        st.write("""
        **Regresi Linier Sederhana** adalah metode statistik yang digunakan untuk memodelkan hubungan antara satu variabel bebas ($X$) dan satu variabel terikat ($Y$).
        
        Pada aplikasi ini:
        * **Variabel $X$ (Independent):** Jumlah Langkah (`Steps`)
        * **Variabel $Y$ (Dependent):** Kalori Terbakar (`Calories_Burned`)
        """)

if __name__ == '__main__':
    main()