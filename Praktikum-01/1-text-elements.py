import streamlit as streamlit

st.header("ini header")
st.subheader("ini sub header")
st.text("ini text biasa tanpa format")
st.markdown("**ini teks bold**dan*ini text italic*")
st.markdow("""
- ini baris 1
- ini mengunakan markdown multibaris
1.ini baris 2
2.ini mengubakan marksown multibaris
* ini baris 3
* ini mengubakan marksown multibaris
""")
st.caption("ini caption")
st.titel("ini judul")

# bagian2 menampilkan rumus latex
st.latex(r'''\cos^2\theta = 1-2\sin^2\theta ''')
# trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''')
# binominal

# bagian3
st.header("Displaying Code")
st.subheader("Python Code")

code = '''
def hello():
    print("Hello, Streamliti")
'''

st.code(code, language='python')

st.subheader("Java Code")
st.code("""
    public class GFD{
        public static void main(sting arg[]) {
            System.out.printIn("Hello World");
            }
        }
""", language='java')

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try{
    adddlert("Welcome gust!"); // kesalahan ketik (adddlaert)
    sengaja dibuat untuk menimbulkan error    
}
catch(err){
    document.getElementByid("demo").innerHTML
}
""")