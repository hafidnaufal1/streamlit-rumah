import pickle 
import streamlit as st

model_harga_rumah = pickle.load(open('model_harga_rumah.sav'))

st.title('Aplikasi Prediksi Harga Rumah')