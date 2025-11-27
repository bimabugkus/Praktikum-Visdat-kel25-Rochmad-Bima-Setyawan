import streamlit as st

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0, 10)
st.sidebar.selectbox("Pilih Visualisasi", ["Bar", "Line", "Area"])  # menampilkan dropdown di sidebar untuk memilih jenis visualisasi

# Konten utama
st.title("Contoh Aplikasi Streamlit dengan Sidebar")
st.write("Gunakan sidebar di sebelah kiri untuk berinteraksi dengan aplikasi.")
