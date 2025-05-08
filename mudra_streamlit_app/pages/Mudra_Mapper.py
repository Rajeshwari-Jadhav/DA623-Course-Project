import streamlit as st
import json
import re
import os
from PIL import Image

# --- Load mudra dictionary ---
with open("mudra_word_mapping.json", "r", encoding="utf-8") as f:
    mudra_dict = json.load(f)

# --- Mudra search function ---
def find_mudras_by_query(query):
    query = query.strip().lower()
    results = []
    for mudra, entries in mudra_dict.items():
        for entry in entries:
            word_match = query in entry["word"].lower()
            trans_match = any(query in t.lower() for t in entry["translations"])
            if word_match or trans_match:
                results.append({
                    "mudra": mudra,
                    "word": entry["word"],
                    "translations": entry["translations"]
                })
    return results

# --- Shloka matching function ---
def get_mudras_for_shloka(shloka_text):
    words = re.findall(r'\b\w+\b', shloka_text.lower())
    matched_mudras = {}
    for word in words:
        for mudra, entries in mudra_dict.items():
            for entry in entries:
                if word in entry["word"].lower() or any(word in t.lower() for t in entry["translations"]):
                    if mudra not in matched_mudras:
                        matched_mudras[mudra] = []
                    matched_mudras[mudra].append({
                        "word": entry["word"],
                        "translation": entry["translations"]
                    })
    return matched_mudras

# --- UI ---
st.set_page_config(page_title="Mudra Mapper")
st.title("📖 Mudra Mapper")

option = st.radio("Choose a mode:", ["Search by Word/Meaning", "Search by Shloka"])

if option == "Search by Word/Meaning":
    query = st.text_input("🔍 Enter word or meaning (e.g., 'wind', 'vayo'):")
    if st.button("Search") and query:
        results = find_mudras_by_query(query)
        if results:
            st.markdown(f"### 🔍 Results for: *{query}*")
            for res in results:
                st.markdown(f"**🌸 Mudra:** {res['mudra']}")
                st.markdown(f"**Word:** {res['word']}")
                st.markdown(f"**Meanings:** {', '.join(res['translations'])}")
                img_path = os.path.join("All_Mudras", f"{res['mudra'].lower()}.jpg")
                if os.path.exists(img_path):
                    st.image(Image.open(img_path), caption=res['mudra'], use_container_width=True)
                st.markdown("---")
        else:
            st.error("❌ No mudras found.")

elif option == "Search by Shloka":
    shloka_text = st.text_area("📜 Paste your shloka or verse below:", height=120)
    if st.button("Find Mudras") and shloka_text:
        matched_mudras = get_mudras_for_shloka(shloka_text)
        if matched_mudras:
            st.markdown("###🪷 Mudras matching this shloka:")
            for mudra, matches in matched_mudras.items():
                st.markdown(f"**🌸 Mudra:** {mudra}")
                for m in matches:
                    st.markdown(f"↳ Word: *{m['word']}*, Meanings: {', '.join(m['translation'])}")
                img_path = os.path.join("All_Mudras", f"{mudra.lower()}.jpg")
                if os.path.exists(img_path):
                    st.image(Image.open(img_path), caption=mudra, use_container_width=True)
                st.markdown("---")
        else:
            st.error("❌ No matching mudras found for the shloka.")
