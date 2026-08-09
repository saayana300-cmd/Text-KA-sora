import streamlit as st
import pandas as pd

st.set_page_config(page_title="Riset Produk Viral", layout="centered")

st.title("🔥 Tracker Produk Viral")
st.markdown("Dashboard riset real-time untuk Shopee & TikTok.")

data = {
    "Kategori": ["Kuliner", "Fashion", "Home", "Beauty"],
    "Produk Terpanas": ["Mochi Bites & Snack Jepang", "Ando Reborn & Baggy Jeans", "Pisau Keramik & Blender Mini", "Eyelashes Magnet & Serum Vit C"],
    "Platform": ["TikTok Shop", "Shopee/TikTok", "Shopee", "TikTok Shop"],
    "Status": ["🔥 Viral", "🔥 Viral", "📈 Stabil", "📈 Stabil"]
}

df = pd.DataFrame(data)
st.table(df)

st.divider()
st.subheader("🔍 Catatan Riset Saya")
user_input = st.text_input("Produk viral apa yang Anda temukan hari ini?")
if st.button("Simpan Produk"):
    if user_input:
        st.success(f"Produk '{user_input}' telah dicatat untuk riset selanjutnya!")

st.info("💡 Tips: Update terus data ini lewat GitHub jika menemukan tren produk baru!")
