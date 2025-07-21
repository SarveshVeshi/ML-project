import streamlit as st
import os
from model.audio_model import predict_audio
import tempfile

st.set_page_config(page_title="🎙️ Voice Emotion & Gender Detection")

st.title("🎤 Voice-Based Emotion and Gender Detector")
st.markdown("Upload a `.wav` audio file to detect the speaker's **gender** and **emotion**.")

uploaded_file = st.file_uploader("Upload your voice (.wav only)", type=["wav"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.audio(uploaded_file, format="audio/wav")

    with st.spinner("Analyzing..."):
        gender, emotion = predict_audio(tmp_path)

    st.success(f"**Gender**: {gender}")
    st.success(f"**Emotion**: {emotion}")
