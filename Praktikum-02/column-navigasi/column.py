import streamlit as st

st.title("Columns Chart")
st.write("Kelompok 25")
st.markdown("""
    - Rochmad Bima Setyawan (0110122152)
    - Pandu Linggar Kumara  (0110221277)
    - Silvia Pitriani       (0110222136)
""")

col1, col2 = st.columns(2)

col1.write("ini adalah kolom pertama")
col1.image("../../Praktikum-01/files/avocado.csv")
col2.write("ini adalah kolom kedua")