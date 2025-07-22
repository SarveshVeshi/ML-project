# import streamlit as st
# import os
# from model.audio_model import predict_audio
# import tempfile

# st.set_page_config(page_title="🎙️ Voice Emotion & Gender Detection")

# st.title("🎤 Voice-Based Emotion and Gender Detector")
# st.markdown("Upload a `.wav` audio file to detect the speaker's **gender** and **emotion**.")

# uploaded_file = st.file_uploader("Upload your voice (.wav only)", type=["wav"])

# if uploaded_file:
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#         tmp_file.write(uploaded_file.read())
#         tmp_path = tmp_file.name

#     st.audio(uploaded_file, format="audio/wav")

#     with st.spinner("Analyzing..."):
#         gender, emotion = predict_audio(tmp_path)

#     st.success(f"**Gender**: {gender}")
#     st.success(f"**Emotion**: {emotion}")

#version 1.2 

# import streamlit as st
# import os
# from model.audio_model import predict_audio
# import tempfile

# # --------------- Page Setup ---------------
# st.set_page_config(
#     page_title="🎙️ Voice Emotion & Gender Detector",
#     page_icon="🎧",
#     layout="centered"
# )

# # --------------- Custom Styling ---------------
# st.markdown(
#     """
#     <style>
#     .main {
#         background: linear-gradient(to right, #eef2f3, #8e9eab);
#         padding: 2rem;
#         border-radius: 12px;
#         box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
#     }
#     .title {
#         text-align: center;
#         color: #333333;
#     }
#     .result-box {
#         background-color: #ffffffdd;
#         padding: 1.5rem;
#         margin-top: 2rem;
#         border-radius: 12px;
#         box-shadow: 0px 0px 15px rgba(0,0,0,0.05);
#         font-size: 1.2rem;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # --------------- App Header ---------------
# st.markdown("<h1 class='title'>🎤 Voice Emotion & Gender Detection</h1>", unsafe_allow_html=True)
# st.markdown("#### Upload a `.wav` file to analyze the speaker's **emotion** and **gender** using AI.")
# st.markdown("---")

# # --------------- File Upload ---------------
# uploaded_file = st.file_uploader("📁 Upload your voice file (.wav only)", type=["wav"])

# # --------------- If File is Uploaded ---------------
# if uploaded_file:
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#         tmp_file.write(uploaded_file.read())
#         tmp_path = tmp_file.name

#     st.audio(uploaded_file, format="audio/wav")

#     with st.spinner("🔍 Analyzing voice... please wait"):
#         gender, emotion = predict_audio(tmp_path)

#     # --------------- Display Result ---------------
#     st.markdown(f"""
#     <div class='result-box'>
#         <h4>👤 Gender Prediction: <span style='color:#3366cc'>{gender}</span></h4>
#         <h4>😊 Emotion Prediction: <span style='color:#cc3366'>{emotion}</span></h4>
#     </div>
#     """, unsafe_allow_html=True)

# # --------------- Footer ---------------
# st.markdown("---")
# st.caption("🚀 Built with ❤️ using Streamlit | @YourName")


#version 1.3

# import streamlit as st

# st.set_page_config(page_title="Voice AI", page_icon="🎧", layout="centered")

# st.title("🎧 Welcome to Voice Emotion & Gender Detector")
# st.markdown("""
# Welcome to your AI-powered voice analysis platform!  
# This site allows you to upload `.wav` audio files and detect the **emotion** and **gender** of the speaker using machine learning.

# ---

# 🎙️ Navigate to the sidebar to try it out.

# 💡 Features:
# - Upload your voice
# - Get real-time predictions
# - Learn how the model works
# """)
# st.image("https://images.unsplash.com/photo-1581090700227-1e8f15c3a16c", caption="AI Listening In...", use_container_width=True)

# version 1.4

# from streamlit_lottie import st_lottie
# import requests

# def load_lottie_url(url):
#     try:
#         r = requests.get(url)
#         if r.status_code != 200:
#             st.warning("⚠️ Could not fetch animation.")
#             return None
#         return r.json()
#     except Exception as e:
#         st.error(f"❌ Error loading animation: {e}")
#         return None

# lottie_ai = load_lottie_url("https://lottie.host/67aee6e1-1ce3-4e04-8044-4d92ef8d5e88/UioF2xzNUN.json")

# if lottie_ai:
#     st_lottie(lottie_ai, height=300, key="ai_lottie")
# else:
#     st.warning("Lottie animation failed to load. Check URL or connection.")

#     import requests
# from streamlit_lottie import st_lottie

# # ✅ Safe loader with error handling
# def load_lottie_url(url):
#     try:
#         response = requests.get(url)
#         if response.status_code != 200:
#             st.error(f"❌ Failed to fetch Lottie. Status code: {response.status_code}")
#             return None
#         return response.json()
#     except Exception as e:
#         st.error(f"❌ Error loading animation: {e}")
#         return None


#version 1.5

# Background animation / gradient
# st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
#         background-attachment: fixed;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
#         background-attachment: fixed;
#     }
#     </style>
# """, unsafe_allow_html=True)


# version 1.5

# import streamlit as st

# # Inject custom CSS
# st.markdown("""
#     <style>
#     /* App background gradient */
#     .stApp {
#         background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
#         background-attachment: fixed;
#         color: #333333;
#         font-family: 'Segoe UI', sans-serif;
#     }

#     /* Headers */
#     h1, h2, h3 {
#         color: #222831;
#     }

#     /* Sidebar */
#     section[data-testid="stSidebar"] {
#         background-color: #ffffff;
#         border-right: 2px solid #eeeeee;
#     }

#     /* Markdown text */
#     .markdown-text-container {
#         font-size: 18px;
#         line-height: 1.6;
#     }
#     </style>
# """, unsafe_allow_html=True)




# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Inject custom CSS
# local_css("assets/style.css")


# import streamlit as st
# from streamlit_lottie import st_lottie
# import requests

# st.set_page_config(page_title="Voice AI", page_icon="🎧", layout="centered")

# st.title("🎧 Welcome to Voice Emotion & Gender Detector")

# # ------------------------
# # ✅ Lottie Loading Function
# # ------------------------
# def load_lottie_url(url):
#     try:
#         response = requests.get(url)
#         if response.status_code != 200:
#             st.error(f"❌ Failed to fetch Lottie. Status code: {response.status_code}")
#             return None
#         return response.json()
#     except Exception as e:
#         st.error(f"❌ Error loading animation: {e}")
#         return None

# # ------------------------
# # ✅ Load and Display Animation
# # ------------------------
# # lottie_ai = load_lottie_url("https://lottie.host/67aee6e1-1ce3-4e04-8044-4d92ef8d5e88/UioF2xzNUN.json")
# lottie_ai = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")


# if lottie_ai:
#     st_lottie(lottie_ai, height=300, key="ai_lottie")
# else:
#     st.warning("Animation couldn't be loaded.")

# # ------------------------
# # ✅ UI Text and Layout
# # ------------------------
# st.markdown("""
# Welcome to your AI-powered voice analysis platform!  
# This site allows you to upload `.wav` audio files and detect the **emotion** and **gender** of the speaker using machine learning.

# ---

# 🎙️ Navigate to the sidebar to try it out.

# 💡 Features:
# - Upload your voice
# - Get real-time predictions
# - Learn how the model works
# """)

# st.image("https://images.unsplash.com/photo-1581090700227-1e8f15c3a16c", caption="AI Listening In...", use_container_width=True)



#version 1.6
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ✅ Page config
st.set_page_config(page_title="Voice AI", page_icon="🎧", layout="centered")

# -------------------------------
# ✅ Inject Minimal CSS Inline
# -------------------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        background-attachment: fixed;
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 { color: #222831; }
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #eeeeee;
    }
    .markdown-text-container {
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Optionally load more CSS from a local file
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Custom CSS file not found.")

local_css("assets/style.css")  # You can skip this if file is unnecessary

# -------------------------------
# ✅ Cache the Lottie JSON fetch
# -------------------------------
@st.cache_data
def load_lottie_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        st.error(f"❌ Lottie load error: {e}")
    return None

# -------------------------------
# ✅ Load Lottie Animation
# -------------------------------
lottie_ai = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")
st.title("🎧 Welcome to Voice Emotion & Gender Detector")

if lottie_ai:
    st_lottie(lottie_ai, height=300, key="ai_lottie")

# -------------------------------
# ✅ App Description
# -------------------------------
st.markdown("""
Welcome to your AI-powered voice analysis platform!  
This site allows you to upload `.wav` audio files and detect the **emotion** and **gender** of the speaker using machine learning.

---

🎙️ Navigate to the sidebar to try it out.

💡 Features:
- Upload your voice
- Get real-time predictions
- Learn how the model works
""")

# -------------------------------
# ✅ Cache External Image
# -------------------------------
@st.cache_data
def get_image_url():
    return "https://images.unsplash.com/photo-1581090700227-1e8f15c3a16c"

st.image(get_image_url(), caption="AI Listening In...", use_container_width=True)
