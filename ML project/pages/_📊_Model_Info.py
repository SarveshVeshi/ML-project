#version 1.3
from utils import local_css
local_css("assets/style.css")

import streamlit as st
st.title("📊 Model Information")
st.markdown("""
### How It Works

- Uses **MFCC audio features** for voice signal processing.
- Trained on **RAVDESS**, **TESS**, and gender datasets.
- ML Models used:
  - 🎯 Emotion: `RandomForestClassifier`
  - 👤 Gender: `SVM` or similar

---  

📦 Accuracy:
- Gender Detection: ~95%
- Emotion Detection: ~85%
""")
