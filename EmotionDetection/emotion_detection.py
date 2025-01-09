import requests
import json

def emotion_detector(text_to_analyze):
    # Check if the input text is empty or contains only spaces
    if not text_to_analyze or not text_to_analyze.strip():
        # Return a dictionary with None for all emotions if input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Define the API URL
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Headers required by Watson NLP API
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Payload containing the text to analyze
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        # Sending the POST request
        response = requests.post(url, headers=headers, json=payload, timeout=30)

        if response.status_code == 200:
            # Convert response to JSON
            response_data = response.json()
            
            # Extracting emotions from the response
            emotions = response_data['emotion']['emotion']
            
            # Extracting the required emotions and their scores
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)
            
            # Find the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)
            
            # Return the formatted dictionary
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }

        else:
            return {"error": "Failed to fetch response from the API"}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
