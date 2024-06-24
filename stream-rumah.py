import pickle
import streamlit as st

# Buka file dengan mode biner
try:
    with open('model_harga_rumah.sav', 'rb') as file:
        model_harga_rumah = pickle.load(file)
except UnicodeDecodeError as e:
    st.error("Error loading the model: " + str(e))

st.title('Aplikasi Prediksi Harga Rumah')

# Ambil input dari pengguna dan konversi ke tipe data numerik
bedrooms = st.text_input('Jumlah kamar tidur')
bathrooms = st.text_input('Jumlah kamar mandi')
sqft_living = st.text_input('Luas tanah')
grade = st.text_input('Grade')
yr_built = st.text_input('Tahun pembuatan')

predict = ''

if st.button('Prediksi Harga Rumah'):
    # Periksa apakah input tidak kosong dan merupakan angka
    if bedrooms and bathrooms and sqft_living and grade and yr_built:
        try:
            bedrooms = int(bedrooms)
            bathrooms = int(bathrooms)
            sqft_living = int(sqft_living)
            grade = int(grade)
            yr_built = int(yr_built)
            
            # Pastikan semua input sudah dalam bentuk numerik sebelum diprediksi
            predict = model_harga_rumah.predict([[bedrooms, bathrooms, sqft_living, grade, yr_built]])
            st.success(f'Prediksi Harga Rumah dalam US Dollar : {predict[0]}')
        except ValueError:
            st.error('Harap masukkan nilai numerik untuk semua input')
    else:
        st.warning('Harap lengkapi semua input sebelum melakukan prediksi')
