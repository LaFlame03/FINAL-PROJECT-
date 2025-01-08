import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the provided text using Watson NLP's Emotion Predict function.
    """
    # URL and headers for Watson NLP API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input JSON
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        # Sending POST request to the API
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        # Return the "text" attribute of the response JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any exceptions during the request
        return {"error": str(e)}
