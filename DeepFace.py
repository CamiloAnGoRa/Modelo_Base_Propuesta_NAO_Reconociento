from deepface import DeepFace
import cv2

# Análisis de emoción desde imagen
result = DeepFace.analyze(img, actions=['emotion'])
dominant_emotion = result['dominant_emotion']
emotion_scores = result['emotion']