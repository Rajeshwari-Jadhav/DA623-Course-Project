import streamlit as st
import numpy as np
from PIL import Image,ImageOps
import tensorflow as tf  # or import torch and load your model differently
import cv2
import matplotlib.pyplot as plt

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("mudra_cnn_model_MobileNetV2.h5")  # <-- replace with your model
    return model

model = load_model()

# Define your mudra class labels (update as per your model)
MUDRA_CLASSES = [
    'Alapadma', 'Arala', 'Ardhachandra', 'Ardhapathaka', 'Bhramara', 'Chandrakala', 'Chatura',
    'Hamsapaksha', 'Hamsasya', 'Kangula', 'Kapittha', 'Kartarimukha', 'Katakamukha', 'Mayura',
    'Mrigashirsha', 'Mukula', 'Mushti', 'Padmakosha', 'Pathaka', 'Samdamsha', 'Sarpashirsha', 
    'Shikhara', 'Shukatunda', 'Simhamukha', 'Suchi', 'Tamrachuda', 'Tripathaka', 'Trishula'
]

# Preprocessing function
def preprocess_image(img):
    image = ImageOps.fit(img, (224, 224),  Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    image = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
    img_reshape = image[np.newaxis,...]
    return img_reshape

st.title('🌸 Mudra Classifier 🌸</div>')
# Choose input method
option = st.radio("📷 Choose input method:", ["Upload Image", "Capture from Camera"])

image = None

if option == "Upload Image":
    uploaded_file = st.file_uploader("📁 Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')

elif option == "Capture from Camera":
    captured_image = st.camera_input("📸 Capture image")
    if captured_image is not None:
        image = Image.open(captured_image).convert('RGB')

# Display and predict
if image is not None:
    st.markdown('<div class="container">', unsafe_allow_html=True)

    st.image(image, caption="Input Image", use_container_width=True)
    st.write("Processing...")

    processed_img = preprocess_image(image)
   
    prediction = model.predict(processed_img)
    pred_class = MUDRA_CLASSES[np.argmax(prediction)]
    confidence = np.max(prediction)
    st.success(f"🧿 Predicted Mudra: **{pred_class}** (Confidence: {confidence:.5f})")