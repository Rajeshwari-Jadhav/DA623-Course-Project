# 🌸 Bharatanatyam Mudra Recognition & Mapping App

This is a two-page **Streamlit web application** designed to recognize and map **Bharatanatyam mudras (hand gestures)** using computer vision and text-based search. It leverages a CNN classifier for gesture recognition and a custom mapping tool to link mudras with meanings and shlokas.

## 🌟 Application Pages

### 1. **Mudra Image Classifier**

* Upload or capture an image of a **Bharatanatyam mudra**.
* The app uses a trained **CNN-based classifier** to predict the corresponding mudra.
* Built using:
  * A **Custom CNN model** (from scratch)
  * A **Pre-trained MobileNetV2 model** (for improved accuracy and performance)

### 2. **Mudra Mapper**

* Search mudras by **Sanskrit word** or **Semantic Meaning**.
* Paste a **Sanskrit Shloka** to retrieve relevant mudras.
* Displays:
  * **Matching Mudra Names**
  * **Descriptions of the Mudras**
  * **Reference Images**

---

## 🗂 Repository Contents

* `"mudra_streamlit_app\app.py"`
  Contains the main Streamlit application and supporting scripts.

* `"mudra_streamlit_app\mudra_word_mapping.json"`
  Mapping of mudras to their Sanskrit terms and semantic meanings.

* `"mudra_streamlit_app\requirements"`
  List of dependencies needed to run the app.

* `notebooks/`
  * `DA626-Project-CNN.ipynb`: Basic CNN for mudra classification
  * `DA626-Project-CNN-MobileNetV2.ipynb`: Transfer learning using MobileNetV2
  * `Mudra-Mapping.ipynb`: Logic for text-based mudra retrieval

---

## 🧪 Dataset

The mudra image dataset used for training was sourced from [Kaggle](https://www.kaggle.com/datasets/mayamohan2212/bharatnatyam-asamyuta-hasta-mudras) and contains labeled images of various **Bharatanatyam Asamyukta Hasta Mudras**.

---

## 🚀 Installation & Usage

1. **Clone the repository**

   ```bash
   git clone https://github.com/Rajeshwari-Jadhav/DA623-Course-Project.git
   cd DA623-Course-Project
   ```

2. **Install dependencies**

   ```bash
   cd mudra_streamlit_app
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run "app.py".py
   ```

---

## 🧠 Model Overview

* **CNN from Scratch**: Simple architecture designed for foundational classification.
* **MobileNetV2**: Pre-trained network fine-tuned on the mudra dataset for superior performance.

Trained models can be accessed from https://drive.google.com/file/d/1U9PT0YLmSsrUsi2Wzc4ckwz-mkq1RTor/view?usp=sharing