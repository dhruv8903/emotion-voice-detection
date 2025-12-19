import streamlit as st
import requests
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile

st.title("🎙️ Emotion Detection from Voice")

DURATION = 4  # seconds
FS = 16000

API_URL = "https://xxxx.ngrok-free.app/predict"  # paste Colab ngrok URL

if st.button("Record Voice"):
    st.info("Recording... Speak now.")
    audio = sd.rec(int(DURATION * FS), samplerate=FS, channels=1)
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        wav.write(tmp.name, FS, audio)
        with open(tmp.name, "rb") as f:
            files = {"file": f}
            response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Emotion: **{result['emotion']}**")
        st.write(f"Confidence: {result['confidence']:.2f}")
    else:
        st.error("Prediction failed.")
