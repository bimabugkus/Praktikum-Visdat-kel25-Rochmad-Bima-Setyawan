import streamlit as st
import pandas as pd
import numpy as np

st.title("Graphviz Chart")
st.write("Kelompok 25")
st.markdown("""
    - Rochmad Bima Setyawan (0110122152)
    - Pandu Linggar Kumara  (0110221277)
    - Silvia Pitriani       (0110222136)
""")
st.graphviz_chart("""
     digraph  {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
    }
""")