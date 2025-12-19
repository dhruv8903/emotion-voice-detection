import streamlit as st
import requests
import tempfile

st.set_page_config(page_title="Voice Emotion Detection", layout="centered")

st.title("🎙️ Voice Emotion Detection")
st.write("Upload a WAV file to predict emotion from speech.")

API_URL = "https://xxxx.ngrok-free.app/predict"  # your ngrok URL

uploaded_file = st.file_uploader(
    "Upload an audio file (.wav)",
    type=["wav"]
)

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    if st.button("Predict Emotion"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        with open(tmp_path, "rb") as f:
            files = {"file": f}
            response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Emotion: **{result['emotion']}**")
            st.write(f"Confidence: {result['confidence']:.2f}")
        else:
            st.error("Prediction failed. Check backend.")
