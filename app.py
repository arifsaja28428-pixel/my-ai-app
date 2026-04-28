import streamlit as st
import google.generativeai as genai
from PIL import Image, ImageEnhance
import streamlit.components.v1 as components

# 1. Konfigurasi API - Pastikan masukkan API Key Gemini Anda di sini
genai.configure(api_key="AIzaSyDzewUAtveIaBaCDLCLnZny7yRxFN2fG74")

# 2. Desain UI Futuristik (Cyberpunk Dark Mode)
st.set_page_config(page_title="NEON AI ENHANCER", layout="centered")

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
    .stExpander { background-color: #111; border: 1px solid #00F2FF; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ NEON AI ENHANCER")
st.write("Tingkatkan kualitas foto Anda dengan kekuatan kecerdasan buatan.")

# 3. Fitur Unggah Foto
file_foto = st.file_uploader("Pilih foto untuk ditingkatkan (JPG/PNG)", type=['jpg', 'png', 'jpeg'])

if file_foto is not None:
    img = Image.open(file_foto)
    st.image(img, caption="Foto Asli", use_container_width=True)
    
    if st.button("PROSES ENHANCE SEKARANG"):
        with st.spinner("AI sedang merekonstruksi detail..."):
            try:
                # Inisialisasi Model Gemini
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # Analisis AI
                respon = model.generate_content([
                    "Tolong berikan deskripsi teknis singkat untuk meningkatkan kualitas foto ini.", 
                    img
                ])
                
                # Eksekusi Perbaikan Visual (Sharpness & Contrast)
                # Menaikkan ketajaman (2.0) dan kontras (1.2)
                enhanced_img = ImageEnhance.Sharpness(img).enhance(2.0)
                enhanced_img = ImageEnhance.Contrast(enhanced_img).enhance(1.2)
                
                st.success("Selesai!")
                
                st.subheader("✨ HASIL ENHANCE:")
                st.image(enhanced_img, caption="Foto Berhasil Ditingkatkan", use_container_width=True)
                
                with st.expander("Lihat Detail Analisis AI"):
                    st.write(respon.text)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

# --- BAGIAN IKLAN ADMOB (PENEMPATAN DI BAWAH) ---
st.write("---")
st.caption("Sponsor")

# Menggunakan ID Publisher dan Unit ID yang Anda berikan
admob_code = """
<div align="center">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-app-pub-1564130561589966"
         crossorigin="anonymous"></script>
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-app-pub-1564130561589966"
         data-ad-slot="2855826294"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
</div>
"""

# Menampilkan iklan
components.html(admob_code, height=150)
