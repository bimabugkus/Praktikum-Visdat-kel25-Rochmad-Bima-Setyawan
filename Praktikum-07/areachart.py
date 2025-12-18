import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# header
st.title("Praktikum 07 Visualisasi Data")
st.write("Kelompok 25")
st.markdown("""
-  Rochmad Bima Setyawan (0110122152)
-  Silvia Pitriani (0110222136)
-  Pandu Linggar Kumara (0110221277)
""")

# Data Penjualan Bulanan
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

shoes = [500, 600, 700, 800, 650, 700, 850, 900, 750, 800, 950, 1000]
sandals = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850]
socks = [200, 250, 300, 350, 300, 400, 450, 500, 600, 700, 750, 800]

# Fungsi untuk Membuat Area Chart
def plot_area_chart(selected_products):
    plt.figure(figsize=(10, 6))
    # Memilih produk yang akan divisualisasikan
    if 'Sepatu' in selected_products:
        plt.fill_between(months, shoes, color='blue', alpha=0.5, label='Sepatu')
    if 'Sandal' in selected_products:
        plt.fill_between(months, sandals, color='green', alpha=0.5, label='Sandal')
    if 'Kaos Kaki' in selected_products:
        plt.fill_between(months, socks, color='orange', alpha=0.5, label='Kaos Kaki')
    plt.title("Area Chart: Penjualan Bulanan")
    plt.xlabel("Bulan")
    plt.ylabel("Unit Terjual")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend()
    st.pyplot(plt)

# Aplikasi Streamlit
def main():
    st.title("Visualisasi Penjualan Bulanan")
    st.sidebar.title("Pengaturan Grafik")

    # Filter Produk
    st.sidebar.markdown("### Pilih Produk")
    products = ['Sepatu', 'Sandal', 'Kaos Kaki']
    selected_products = st.sidebar.multiselect(
        "Produk yang akan ditampilkan:",
        products,
        default=products
    )

    st.markdown("### Area Chart Penjualan")
    plot_area_chart(selected_products)

if __name__ == "__main__":
    main()
