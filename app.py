import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Masukkan API Key Anda di sini
genai.configure(api_key="PASTE_KODE_API_GEMINI_ANDA_DISINI")

# 2. Desain Tampilan Futuristik
st.set_page_config(page_title="AI Photo Enhancer Pro", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00F2FF; }
    h1 { text-shadow: 0 0 10px #00F2FF; font-family: 'Courier New', monospace; }
    .stButton>button { 
        background: linear-gradient(90deg, #00F2FF, #7000FF); 
        color: white; border-radius: 30px; border: none;
        width: 100%; font-weight: bold; height: 50px;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ NEON AI ENHANCER")
st.write("---")

# 3. Fitur Unggah Foto
file_foto = st.file_uploader("Unggah foto yang ingin diperbaiki", type=['jpg', 'png', 'jpeg'])

if file_foto:
    img = Image.open(file_foto)
    st.image(img, caption="Foto Asli", use_container_width=True)
    
    if st.button("PROSES DENGAN AI"):
        with st.spinner("Menganalisis detail piksel..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            # Perintah khusus ke AI
            respon = model.generate_content(["Tolong berikan deskripsi teknis bagaimana cara meningkatkan kualitas foto ini secara drastis dalam hal saturasi, kontras, dan ketajaman.", img])
            
            st.success("Analisis Selesai!")
            st.subheader("Rekomendasi Perbaikan AI:")
            st.write(respon.text)
            st.info("Fitur auto-filter akan diterapkan pada versi Pro.")