import streamlit as st
import google.generativeai as genai
from PIL import Image, ImageEnhance

# 1. Konfigurasi API - Ganti dengan API Key milik Anda
genai.configure(api_key="AIzaSyDzewUAtveIaBaCDLCLnZny7yRxFN2fG74")

# 2. Desain UI Futuristik
st.set_page_config(page_title="NEON AI ENHANCER", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00F2FF; }
    .stButton>button { 
        background: linear-gradient(90deg, #00F2FF, #7000FF); 
        color: white; border-radius: 30px; border: none;
        width: 100%; font-weight: bold; height: 50px;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ NEON AI ENHANCER")
st.write("Aplikasi AI untuk meningkatkan kualitas foto secara instan.")

# 3. Proses Unggah
file_foto = st.file_uploader("Unggah foto (JPG/PNG)", type=['jpg', 'png', 'jpeg'])

# Pastikan semua proses dilakukan di DALAM blok "if file_foto:"
if file_foto is not None:
    # Membaca gambar
    img = Image.open(file_foto)
    st.image(img, caption="Foto Asli", use_container_width=True)
    
    if st.button("PROSES DENGAN AI"):
        with st.spinner("AI sedang bekerja..."):
            try:
                # Memanggil Model AI
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Mengirim gambar ke Gemini
                respon = model.generate_content([
                    "Analyze this image and provide technical advice for color, sharpness, and lighting.", 
                    img
                ])
                
                st.success("Selesai!")
                
                # Menampilkan saran teks dari AI
                with st.expander("Lihat Analisis Detail AI"):
                    st.write(respon.text)
                
                # PROSES OTOMATIS: Meningkatkan Kualitas secara visual
                # 1. Pertajam (Sharpness)
                sharper = ImageEnhance.Sharpness(img).enhance(2.0)
                # 2. Perbaiki Kontras (Contrast)
                enhanced_img = ImageEnhance.Contrast(sharper).enhance(1.2)
                
                st.subheader("✨ HASIL ENHANCE:")
                st.image(enhanced_img, caption="Hasil Peningkatan Otomatis", use_container_width=True)
                
                # Tombol Download (Penting untuk kepuasan pengguna)
                # (Opsional: fitur ini sangat disukai pengguna Play Store)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
else:
    st.info("Silakan unggah foto terlebih dahulu untuk memulai.")
