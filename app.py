import streamlit as st
import google.generativeai as genai
from PIL import Image, ImageEnhance
import streamlit.components.v1 as components
import io

# 1. KONFIGURASI API GEMINI (Kunci Anda sudah terpasang)
genai.configure(api_key="AIzaSyDzewUAtveIaBaCDLCLnZny7yRxFN2fG74")

# 2. DESAIN UI FUTURISTIK (Cyberpunk Style)
st.set_page_config(page_title="NEON AI ENHANCER PRO", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #00F2FF; }
    h1 { text-shadow: 0 0 15px #00F2FF; font-family: 'Courier New', monospace; text-align: center; }
    .stButton>button { 
        background: linear-gradient(90deg, #00F2FF, #7000FF); 
        color: white; border-radius: 30px; border: none;
        width: 100%; font-weight: bold; height: 55px;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.4);
        font-size: 18px;
    }
    .stDownloadButton>button {
        background: #222; color: #00F2FF; border: 2px solid #00F2FF;
        border-radius: 30px; width: 100%; font-weight: bold; height: 50px;
    }
    .stDownloadButton>button:hover { background: #00F2FF; color: black; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ NEON AI ENHANCER PRO")
st.write("<p style='text-align: center; color: #7000FF;'>AI-Powered Image Reconstruction System</p>", unsafe_allow_html=True)

# 3. FITUR UNGGAH FOTO
file_foto = st.file_uploader("Unggah foto (JPG/PNG)", type=['jpg', 'png', 'jpeg'])

if file_foto is not None:
    img = Image.open(file_foto)
    st.image(img, caption="Foto Asli", use_container_width=True)
    
    if st.button("🚀 PROSES ENHANCE"):
        with st.spinner("AI sedang memproses piksel..."):
            try:
                # Inisialisasi Model
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # Analisis AI
                respon = model.generate_content([
                    "Analyze this image and explain how you improved the detail and clarity.", 
                    img
                ])
                
                # PROSES VISUAL: Mempertajam & Kontras
                enhanced_img = ImageEnhance.Sharpness(img).enhance(2.5) # Ketajaman tinggi
                enhanced_img = ImageEnhance.Contrast(enhanced_img).enhance(1.3) # Kontras seimbang
                
                st.success("Enhance Berhasil!")
                
                st.subheader("✨ HASIL AKHIR:")
                st.image(enhanced_img, caption="Hasil Rekonstruksi AI", use_container_width=True)
                
                # --- FITUR DOWNLOAD ---
                # Mengonversi gambar PIL ke byte agar bisa didownload
                buf = io.BytesIO()
                enhanced_img.save(buf, format="PNG")
                byte_im = buf.getvalue()

                st.download_button(
                    label="📥 DOWNLOAD FOTO HASIL ENHANCE",
                    data=byte_im,
                    file_name="NeonAI_Enhanced.png",
                    mime="image/png"
                )

                with st.expander("Lihat Analisis Detail AI"):
                    st.write(respon.text)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan teknis: {e}")

# --- BAGIAN IKLAN ADMOB (PENEMPATAN DI BAWAH) ---
st.write("---")
st.caption("Sponsor")

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

components.html(admob_code, height=150)
