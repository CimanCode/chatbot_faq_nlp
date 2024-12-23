from django.http import JsonResponse
from django.shortcuts import render
import random
import json
import os
import pickle
from django.conf import settings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_PATH = os.path.join(settings.BASE_DIR, 'chatbot_rule_based/models/svm_chatbot_model_indonesia.pkl')
VECTORIZER_PATH = os.path.join(settings.BASE_DIR, 'chatbot_rule_based/models/tfidf_vectorizer.pkl')
LABEL_ENCODER_PATH = os.path.join(settings.BASE_DIR, 'chatbot_rule_based/models/label_encoder.pkl')
INTENTS_PATH = os.path.join(settings.BASE_DIR, 'chatbot_rule_based/models/intents_translated.json')

# Load model, vectorizer, dan intents
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

with open(VECTORIZER_PATH, 'rb') as file:
    vectorizer = pickle.load(file)

with open(LABEL_ENCODER_PATH, 'rb') as file:
    label_encoder = pickle.load(file)

with open(INTENTS_PATH, 'r') as file:
    intents = json.load(file)

def chatbot(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        user_question = request.POST.get("question", "").strip()

        if not user_question:
            return JsonResponse({"response": "Silakan masukkan pertanyaan."}, status=200)

        # Transform input pengguna menjadi vektor
        user_vector = vectorizer.transform([user_question])

        # Prediksi intent
        predicted_label = model.predict(user_vector)
        predicted_intent = predicted_label[0]

        # Cari respons berdasarkan intent
        for intent in intents["intents"]:
            if intent["tag"] == predicted_intent:
                response = random.choice(intent["responses"])
                break
        else:
            response = "Maaf, saya tidak mengerti pertanyaan Anda."

        return JsonResponse({"response": response}, status=200)

    return render(request, "chatbot/chat.html")
