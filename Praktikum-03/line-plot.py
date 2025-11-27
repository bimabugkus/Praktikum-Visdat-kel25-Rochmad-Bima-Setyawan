import streamlit as st
import matplotlib.pyplot as plt

#Buat data sampel
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,36,40,45]

#layout streammlit
st.title("visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih tipe visualisasi", ("Singel Line Plot",
"Multiple Line Plot&Customizations", "Jenis Garis untuk Menunjukan Tren", "Subplot"))

#identitas kelompok
st.caption("Praktikum03 - Matplotlib Line Chart")
st.markdown("""
kelompok25:
  Rochmad Bima Setyawan (0110122152)
  Silvia Pitriani (0110222136)
  Pandu Linggar Kumara (0110221277)
""")

#singel Line plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A')
    ax.set_title('Penjualan Produk per bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

#Multiple Line Plot&Customizations
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', color='blue', linestyle="--", marker='o')
    ax.plot(months, product_B_sales, label='Product B', color='red', linestyle="-", marker='x')
    ax.set_title('Penjualan Produk per bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

#Data sampel tambahan
product_C_sales = [18,22,15,25,33,55,45,60,70,50,50,70]
product_D_sales = [7,12,10,17,20,22,24,32,27,38,42,47]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_C_sales, label='Product C', color='green', linestyle="-.")
    axs.plot(months, product_D_sales, label='Product D', color='purple', linestyle=":")
    axs.set_title('Penjualan Produk per bulan')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Penjualan')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

#subplot
def subplots():
    fig, axs = plt.subplot(2, 1, figsize=(10,8))

    #plot pertama untuk produk C
    axs[0].plot(months, product_C_sales, label='Product C', color='green', marker='d')
    axs[0].set_title('Penjualan Produk C per bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    #plot kedua untuk produk D
    axs[1].plot(months, product_D_sales, label='Product D', color='purple', marker='s')
    axs[1].set_title('Penjualan Produk D per bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)                  

#logika untuk menampilkan visualisasi sesuai menu
if option == "ingel Line Plot":
    line_plot()
elif option == "Multiple Line Plot&Customizations":
    customize_line_plot()
elif option == "Jenis Garis untuk Menunjukan Tren":
    line_plot()
elif option == "Subplot":
    subplot()