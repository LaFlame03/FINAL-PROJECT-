from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def emotionDetector():
    if request.method == 'POST':
        # Get the text input from the form
        user_input = request.form['user_input']
        
        # Get the emotion analysis from the emotion_detector function
        response = emotion_detector(user_input)
        
        # Extract the emotions and the dominant emotion
        anger_score = response.get('anger')
        disgust_score = response.get('disgust')
        fear_score = response.get('fear')
        joy_score = response.get('joy')
        sadness_score = response.get('sadness')
        dominant_emotion = response.get('dominant_emotion')
        
        # Prepare the output for the user
        output = f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
        
        return render_template('index.html', output=output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

