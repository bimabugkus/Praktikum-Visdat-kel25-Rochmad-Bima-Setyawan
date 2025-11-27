import streamlit as st
import pandas as pd
import numpy as np

st.title("Map Chart")
st.write("Kelompok 25")
st.markdown("""
    - Rochmad Bima Setyawan (0110122152)
    - Pandu Linggar Kumara  (0110221277)
    - Silvia Pitriani       (0110222136)
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10, 10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)
st.map(df)