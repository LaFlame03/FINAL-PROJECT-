from flask import Flask, request, jsonify
from emotion_detector import emotion_detector 
app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    # Get the statement from the POST request body (JSON)
    user_input = request.json.get("statement")
    response = emotion_detector(user_input)
    
    if response["dominant_emotion"] is None:
        # If dominant_emotion is None, return an error response with 400 status
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400  # HTTP status code 400 for bad request
    
    # If valid, return the emotion scores along with the dominant emotion
    formatted_response = {
        "anger": response["anger"],
        "disgust": response["disgust"],
        "fear": response["fear"],
        "joy": response["joy"],
        "sadness": response["sadness"],
        "dominant_emotion": response["dominant_emotion"]
    }
    
    # Return the JSON response with emotion scores and dominant emotion
    return jsonify(formatted_response)

if __name__ == "__main__":
    # Running the Flask app on localhost, port 5000
    app.run(debug=True, host="0.0.0.0", port=5000)
