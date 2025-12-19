# Frontend – Voice Emotion Detection

This frontend is built using Streamlit.
It records audio input from the user, sends it to a FastAPI
backend hosted temporarily on Google Colab via Ngrok,
and displays the predicted emotion and confidence score.

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Start the app:
   streamlit run app.py

3. Ensure the Colab backend is running and update
   the API_URL in app.py with the Ngrok link.
