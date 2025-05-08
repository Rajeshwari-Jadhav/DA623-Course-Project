import streamlit as st
st.set_page_config(page_title="Mudra Classifier", layout="centered")



# Streamlit UI
st.title("🌸 Mudra Classifier 🌸")
st.write("Upload or capture an image to identify the Bharatanatyam mudra.")
st.markdown("""
Use the sidebar to:
- Classify an image into a mudra using the **Mudra Classifier**
- Explore Sanskrit word and meaning mappings using the **Mudra Mapper**
""")

