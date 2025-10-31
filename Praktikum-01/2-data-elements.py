

st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    colummns=('col_no %d' % i for i in range(10))
)

st.dataframe(sf)

st.subheader("Highlight Minuman Value di DataFrame")

st.dataframe(df.style.highlight_min(axis=0))

st.subheader("Tabel statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    colummns=('col_no %d' % i for i in range(10))
)

st.table(df)

st.subheader("Metrics")
st.Metrics(label="temperature", value="31 c". delta="1,2 c")

col1, col2, col3 = st.columns(3)

col1.metric("curah hujan","100 cm","10cm")
col2.metric(label="Populasi", value="123 Miliar", delta"1 miliar", delta_color="inverse")
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off")

st.matric(label="speed", value=None, delta=0)

st.matric("Trees", "91456", "-1132649")