

import sys
import os

# # Add backend folder to system path
# # sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

# from predict import predict_gender_emotion

# def predict_audio(audio_path):
#     try:
#         gender, emotion = predict_gender_emotion(audio_path)
#         return gender, emotion
#     except Exception as e:
#         return "Error", str(e)

from predict import predict_gender_emotion

def predict_audio(audio_path):
    try:
        gender, emotion = predict_gender_emotion(audio_path)
        return gender, emotion
    except Exception as e:
        return "Error", str(e)

