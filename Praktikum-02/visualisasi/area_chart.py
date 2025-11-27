import streamlit as st
import pandas as pd
import numpy as np

st.title("Area Chart")
st.write("Kelompok 25")
st.markdown("""
    - Rochmad Bima Setyawan (0110122152)
    - Pandu Linggar Kumara  (0110221277)
    - Silvia Pitriani       (0110222136)
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)
st.area_chart(df)